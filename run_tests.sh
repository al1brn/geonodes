#!/usr/bin/env bash
# Lance les tests geonodes dans le Python de Blender
# Usage : ./run_tests.sh [dossier_ou_fichier]
#   ./run_tests.sh
#   ./run_tests.sh tests/integration/test_colors.py -k test_str_to_color_hex

BLENDER=/Applications/Blender.app/Contents/MacOS/Blender
SCRIPT="$(cd "$(dirname "$0")" && pwd)/run_blender_tests.py"
TARGET="${1:-tests/}"

cd "$(dirname "$0")"
"$BLENDER" --background --python "$SCRIPT" -- "$@"
