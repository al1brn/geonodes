"""Script exécuté dans Blender pour lancer pytest."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pytest

# Les arguments après "--" dans la commande Blender sont passés à pytest
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
args = argv if argv else ["tests/", "-v"]

sys.exit(pytest.main(args + ["-p", "no:pytest-blender"]))
