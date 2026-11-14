"""Load the real argument preparation without importing Blender."""
import ast
from copy import deepcopy
import keyword
from pathlib import Path
import runpy
from types import MethodType, SimpleNamespace as NS

ROOT = Path(__file__).resolve().parents[1]
NodeArgument = runpy.run_path(str(ROOT / 'node_argument.py'))['NodeArgument']
param_tree = ast.parse((ROOT / 'node_param.py').read_text())
param_tree.body = [node for node in param_tree.body if not isinstance(node, ast.Import)]
namespace = {}
exec(compile(param_tree, '<NodeParam>', 'exec'), namespace)
NodeParam = namespace['NodeParam']
info_tree = ast.parse((ROOT / 'node_info.py').read_text())
owner = next(node for node in info_tree.body if isinstance(node, ast.ClassDef) and node.name == 'NodeInfo')
method = next(node for node in owner.body if isinstance(node, ast.FunctionDef) and node.name == 'get_node_arguments')

def snake_case(value):
    value = value.lower().replace(' ', '_')
    return value + '_' if keyword.iskeyword(value) else value

namespace = dict(NodeArgument=NodeArgument, NodeParam=NodeParam,
                 core_module=NS(utils=NS(snake_case=snake_case)))
exec(compile(ast.Module(body=[method], type_ignores=[]), '<get_node_arguments>', 'exec'), namespace)


def attach_arguments(node):
    """Add actual preparation to a minimal node/introspection test double."""
    snapshots = deepcopy(node.default_params)
    existing = vars(node.bnode) if getattr(node, 'bnode', None) is not None else {}
    node.bnode = NS(**(existing | {name: info['value'] for name, info in snapshots.items()}))
    node.snapshot_params = lambda: {
        name: {**info, 'value': getattr(node.bnode, name)} for name, info in snapshots.items()}
    def set_params(**parameters):
        for name, value in parameters.items():
            if name in snapshots:
                setattr(node.bnode, name, value)
    node.set_params = set_params
    node.get_node_arguments = MethodType(namespace['get_node_arguments'], node)
    return node
