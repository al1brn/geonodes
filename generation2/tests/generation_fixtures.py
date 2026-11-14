"""Load the orchestration classes without Blender for focused unit tests."""
import ast
from pathlib import Path
import runpy
from types import SimpleNamespace as NS
from unittest.mock import Mock

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT.parent / 'core_new'
writer = runpy.run_path(str(ROOT / 'sourcewriter.py'))
calls = runpy.run_path(str(ROOT / 'node_call.py'))
output = runpy.run_path(str(ROOT / 'tests/output_fixtures.py'))['load_output']()
namespace = dict(__file__=str(ROOT / 'generate.py'), Path=Path,
                 NodeCall=calls['NodeCall'], NodeCalls=calls['NodeCalls'],
                 TypeAliases=runpy.run_path(str(ROOT / 'typealiases.py'))['TypeAliases'],
                 SourceWriter=writer['SourceWriter'], R0=writer['R0'],
                 config=output['config'], render_modules=output['render_modules'],
                 core_module=NS(utils=NS(snake_case=lambda s: s.lower())),
                 gen_config=NS(SOCKETS={'loaded': True}, build=Mock()))

class WithoutImports(ast.NodeTransformer):
    def visit_Import(self, node):
        return None
    def visit_ImportFrom(self, node):
        return None

for filename, class_name in (('node_implementation.py', 'NodeImplementation'), ('tree_class.py', 'TreeClass')):
    tree = ast.parse((ROOT / filename).read_text())
    owner = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == class_name)
    module = WithoutImports().visit(ast.Module(body=[owner], type_ignores=[]))
    exec(compile(module, filename, 'exec'), namespace)
module = ast.parse((ROOT / 'generate.py').read_text())
module = WithoutImports().visit(module)
exec(compile(module, 'generate.py', 'exec'), namespace)
