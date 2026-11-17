# geonodes — Linux test runner
#
#   make setup                     create .venv with bpy + pytest
#   make test                      run the whole test suite
#   make test T=tests/integration/test_colors.py
#   make test T="tests/integration -k blink"
#   make face                      run the grease pencil face demo test
#
# Tests run inside the `bpy` Python module (no Blender binary needed).
# To use a Blender binary instead:  make test BLENDER=/usr/bin/blender

PY      ?= .venv/bin/python
BPY_VER ?= 5.2.4
T       ?= tests/
BLENDER ?=

.PHONY: setup test face drawing nodes kaomoji kaomoji-svg clean-venv bpy-version

setup:
	uv venv --python 3.13 .venv
	uv pip install --python $(PY) bpy==$(BPY_VER) pytest

bpy-version:
	@$(PY) -c "import bpy; print(bpy.app.version_string)"

ifeq ($(BLENDER),)
test:
	$(PY) run_blender_tests.py -- $(T) -v
else
test:
	$(BLENDER) --background --python run_blender_tests.py -- $(T) -v
endif

nodes:
	$(MAKE) test T=tests/integration/test_drawing_nodes.py

kaomoji:
	$(MAKE) test T="tests/unit/test_kaomojilang.py tests/integration/test_kaomojilang_grease.py"

# make kaomoji-svg [KL=kaomojilang/examples/example.kmj] [OUT=out/kaomoji]
KL  ?= kaomojilang/examples/example.kmj
OUT ?= out/kaomoji
kaomoji-svg:
	cd .. && geonodes/$(PY) -m geonodes.kaomojilang geonodes/$(KL) --svg geonodes/$(OUT)

drawing:
	$(MAKE) test T="tests/unit tests/integration/test_drawing_grease.py tests/integration/test_drawing_nodes.py"

face:
	$(MAKE) test T=tests/integration/test_face.py

clean-venv:
	rm -rf .venv
