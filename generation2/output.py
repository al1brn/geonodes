"""Render an environment directly against its handwritten socket classes."""
import ast
import textwrap
from datetime import datetime

ENVIRONMENTS = {'GeometryNodeTree': 'geonodes', 'ShaderNodeTree': 'shadernodes'}
GEOMETRIES = {'Mesh', 'Curve', 'Cloud', 'Instances', 'GreasePencil', 'Volume'}
POINT_DOMAINS = {'Vertex', 'SplinePoint', 'CloudPoint'}


class SpecializeContext(ast.NodeTransformer):
    def __init__(self, tree_type):
        self.tree_type = tree_type

    def visit_If(self, node):
        self.generic_visit(node)
        test = node.test
        if (isinstance(test, ast.Compare) and len(test.ops) == 1
                and isinstance(test.ops[0], (ast.Eq, ast.NotEq))
                and isinstance(test.left, ast.Attribute) and test.left.attr == 'bl_idname'
                and isinstance(test.comparators[0], ast.Constant)
                and test.comparators[0].value in ENVIRONMENTS):
            match = self.tree_type == test.comparators[0].value
            if isinstance(test.ops[0], ast.NotEq):
                match = not match
            return node.body if match else node.orelse
        return node


def specialize_source(source, tree_type):
    """Resolve context switches before emitting code for one environment."""
    tree = SpecializeContext(tree_type).visit(ast.parse(source))
    return ast.unparse(ast.fix_missing_locations(tree)) + '\n'


def render_modules(core_path, tree_type, sources, cross_refs=None):
    """Return destination path -> source, validating the complete environment."""
    environment = ENVIRONMENTS[tree_type]
    targets = {}
    handwritten = {}
    folders = [core_path / 'root', core_path / environment / 'sockets']
    if environment == 'geonodes':
        folders.append(core_path / environment / 'domains')
    for folder in folders:
        for path in folder.glob('*.py'):
            for node in ast.parse(path.read_text()).body:
                if not isinstance(node, ast.ClassDef):
                    continue
                handwritten.setdefault(node.name, set()).update(
                    method.name for method in node.body if isinstance(method, ast.FunctionDef))
                if folder.name == 'sockets':
                    targets[node.name.lower() + '.py'] = (node.name, f'{environment}.sockets.{path.stem}')
                elif folder.name == 'domains' and path.stem not in ('domain', 'attribute'):
                    targets['dom_' + node.name.lower() + '.py'] = (node.name, f'geonodes.domains.{path.stem}')
    static_name, static_class = 'static_nd.py', 'ND'
    targets[static_name] = (static_class, None)
    unknown = sources.keys() - targets.keys() - {'gnmath.py'}
    if unknown:
        raise ValueError(f'Unknown destinations in {environment}: {sorted(unknown)}')
    header = (f'# Generated {datetime.now():%Y-%m-%d %H:%M:%S}\n'
              'from __future__ import annotations\n'
              'from ...common.sockettype import SocketType\n'
              'from ...root.socket import Socket\n'
              'from ...root.node import Node, ColorRamp, NodeCurves\n'
              'from ...common import utils\n'
              'from ...common.scripterror import NodeError\n'
              'from typing import TYPE_CHECKING, Literal, Union, Sequence\n\n'
              'if TYPE_CHECKING:\n')
    header += ''.join(f'    class {name}: ...\n' for name, base in targets.values() if base)
    modules = {}
    exports = []
    for filename in [*targets, 'gnmath.py']:
        code = header + '\n'
        methods = sources.get(filename, [])
        if filename == 'gnmath.py':
            code += '\n'.join(methods)
        else:
            class_name, base = targets[filename]
            if base:
                code += f'from ...{base} import {class_name} as Base{class_name}\n'
                bases = 'Base' + class_name
                if class_name in GEOMETRIES and not filename.startswith('dom_'):
                    code += 'from .geometry import Geometry\n'
                    bases += ', Geometry'
                elif class_name in POINT_DOMAINS and filename.startswith('dom_'):
                    code += 'from .dom_point import Point\n'
                    bases += ', Point'
                code += f'\nclass {class_name}({bases}):\n    __slots__ = ()\n\n'
                # Preserve shared/intermediate handwritten behavior instead of
                # masking it with the historical automatically emitted wrappers.
                methods = [method for method in methods if ast.parse(textwrap.dedent(method)).body[0].name
                           not in handwritten.get(class_name, ())]
                exports.append((filename[:-3], class_name))
            else:
                code += f'\nclass {class_name}:\n'
            code += '\n'.join(methods) if methods else '    pass\n'
            if not base:
                code += f'\n{class_name.lower()} = {class_name}()\n'
        # Specialization also handles copied source_code methods.
        code = specialize_source(code, tree_type)
        modules[filename] = '# Generated by generation2 for ' + tree_type + '\n' + code
    modules['__init__.py'] = ''.join(f'from .{module} import {name}\n' for module, name in exports)
    modules['__init__.py'] += 'from . import gnmath\n'
    modules['__init__.py'] += f'from .{static_name[:-3]} import {static_class.lower()}\n'
    modules['cross_reference.py'] = 'CROSS_REF = ' + repr(cross_refs or {}) + '\n'
    result = {}
    for filename, source in modules.items():
        path = core_path / environment / 'generated' / filename
        compile(source, str(path), 'exec')
        result[path] = source
    return result
