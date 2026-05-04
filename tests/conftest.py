"""
pytest configuration — tests run inside Blender's Python interpreter.
Launch with: ./run_tests.sh
"""
import sys
import os

# Make geonodes importable as a package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
