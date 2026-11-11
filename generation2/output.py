"""Render an environment directly against its handwritten socket classes."""
import ast
import io
import tokenize
import textwrap
from datetime import datetime

ENVIRONMENTS = {'GeometryNodeTree': 'geonodes', 'ShaderNodeTree': 'shadernodes'}
GEOMETRIES = {'Mesh', 'Curve', 'Cloud', 'Instances', 'GreasePencil', 'Volume'}
POINT_DOMAINS = {'Vertex', 'SplinePoint', 'CloudPoint'}


def specialize_source(source, tree_type):
    """Resolve environment branches by editing their source spans only."""
    while True:
        tree = ast.parse(source)
        branch = None
        for node in ast.walk(tree):
            if not isinstance(node, ast.If):
                continue
            test = node.test
            if (isinstance(test, ast.Compare) and len(test.ops) == 1
                    and isinstance(test.ops[0], (ast.Eq, ast.NotEq))
                    and isinstance(test.left, ast.Attribute) and test.left.attr == 'bl_idname'
                    and isinstance(test.comparators[0], ast.Constant)
                    and test.comparators[0].value in ENVIRONMENTS):
                branch = node
                match = tree_type == test.comparators[0].value
                if isinstance(test.ops[0], ast.NotEq):
                    match = not match
                break
        if branch is None:
            return source

        lines = source.splitlines(keepends=True)
        tokens = list(tokenize.generate_tokens(io.StringIO(source).readline))
        # Locate an else/elif at this branch's indentation, ignoring nested ones.
        alternative = next((token for token in tokens
                            if token.type == tokenize.NAME and token.string in ('else', 'elif')
                            and token.start[1] == branch.col_offset
                            and branch.body[-1].end_lineno < token.start[0] <= branch.end_lineno), None)
        selected = branch.body if match else branch.orelse
        prefix = ' ' * branch.col_offset
        if not selected:
            replacement = prefix + 'pass\n'
        elif not match and alternative.string == 'elif':
            # Keep the remaining conditional, including its original formatting.
            replacement = ''.join(lines[alternative.start[0] - 1:branch.end_lineno])
            replacement = replacement.replace(prefix + 'elif', prefix + 'if', 1)
        else:
            header = branch.lineno if match else alternative.start[0]
            first = selected[0]
            end = alternative.start[0] - 1 if match and alternative else branch.end_lineno
            if first.lineno == header:
                # A one-line suite: keep its statements and trailing comment.
                replacement = prefix + lines[header - 1][first.col_offset:]
            else:
                header_end = next(token.end[0] for token in tokens
                                  if token.type == tokenize.NEWLINE and token.start[0] >= header)
                # Do not change indentation inside multiline string values.
                string_lines = {row for token in tokens if token.type == tokenize.STRING
                                for row in range(token.start[0] + 1, token.end[0] + 1)}
                shift = first.col_offset - branch.col_offset
                replacement = ''.join(
                    line if row in string_lines or not line.strip() else line[shift:]
                    for row, line in enumerate(lines[header_end:end], header_end + 1))
        # An elif belonging to an outer, unrelated if must remain an elif.
        if lines[branch.lineno - 1].lstrip().startswith('elif '):
            replacement_tokens = tokenize.generate_tokens(io.StringIO(replacement).readline)
            string_lines = {row for token in replacement_tokens if token.type == tokenize.STRING
                            for row in range(token.start[0] + 1, token.end[0] + 1)}
            replacement = prefix + 'else:\n' + ''.join(
                '    ' + line if line.strip() and row not in string_lines else line
                for row, line in enumerate(replacement.splitlines(keepends=True), 1))
        lines[branch.lineno - 1:branch.end_lineno] = [replacement]
        source = ''.join(lines)


def render_modules(core_path, tree_type, sources, cross_refs=None):
    """Return destination path -> source, validating the complete environment."""

    environment = ENVIRONMENTS[tree_type]
    targets = {}
    handwritten = {}
    folders = [core_path / 'root', core_path / environment / 'sockets']
    if environment == 'geonodes':
        folders.append(core_path / environment / 'domains')

    # Loop on folders
    for folder in folders:
        # Loop on python files in the folder, not in sub folders
        for path in folder.glob('*.py'):
            # Parse the content
            for node in ast.parse(path.read_text()).body:
                # Interested only in ClassDef
                if not isinstance(node, ast.ClassDef):
                    continue

                # Stores the existing methods into handwritten dict
                handwritten.setdefault(node.name, set()).update(
                    method.name for method in node.body if isinstance(method, ast.FunctionDef))

                # Stores (class_name, module path)
                if folder.name == 'sockets':
                    targets[node.name.lower() + '.py'] = (node.name, f'{environment}.sockets.{path.stem}')
                elif folder.name == 'domains' and path.stem not in ('domain', 'attribute'):
                    targets['dom_' + node.name.lower() + '.py'] = (node.name, f'geonodes.domains.{path.stem}')

    static_name, static_class = 'static_nd.py', 'ND'
    targets[static_name] = (static_class, None)
    unknown = sources.keys() - targets.keys() - {'gnmath.py', 'type_aliases.py'}

    if unknown:
        from pprint import pprint
        print("sources.keys():")
        print(list(sources.keys()))
        #pprint(sources)
        print()
        print("targets:")
        pprint(targets)
        print()

        raise ValueError(f"The following destination files don't exist for '{environment}'. Make sure to create them in  '{environment}/sockets' folder: {sorted(unknown)}")
    
    alias_source = '\n'.join(sources.get('type_aliases.py', ['from typing import Literal\n']))
    alias_names = [node.targets[0].id for node in ast.parse(alias_source).body
                   if isinstance(node, ast.Assign)]
    alias_imports = ''.join(f'from .type_aliases import {name}\n' for name in alias_names)

    header = (f'# Generated {datetime.now():%Y-%m-%d %H:%M:%S}\n'
              'from __future__ import annotations\n')
    header += alias_imports
    header += ('from ...common.sockettype import SocketType\n'
              'from ...root.socket import Socket\n'
              'from ...root.node import Node, ColorRamp, NodeCurves\n'
              'from ...common import utils\n'
              'from ...common.scripterror import NodeError\n'
              'from typing import TYPE_CHECKING, Literal, Union, Sequence\n\n'
              'if TYPE_CHECKING:\n')
    header += ''.join(f'    class {name}: ...\n' for name, base in targets.values() if base)
    modules = {'type_aliases.py': alias_source}
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
