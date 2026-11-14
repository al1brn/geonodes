"""Load the renderer with the real configuration, without importing Blender."""
import ast
from pathlib import Path
import runpy
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]


def load_output():
    config = SimpleNamespace(**runpy.run_path(str(ROOT / 'config.py')))
    tree = ast.parse((ROOT / 'output.py').read_text())
    tree.body = [node for node in tree.body
                 if not (isinstance(node, ast.ImportFrom) and node.level)]
    namespace = {'config': config, '__file__': str(ROOT / 'output.py')}
    exec(compile(tree, 'output.py', 'exec'), namespace)
    return namespace
