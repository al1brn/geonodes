"""
This file is part of the geonodes distribution (https://github.com/al1brn/geonodes).
Copyright (c) 2025 Alain Bernard.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

$ DOC hidden

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : constants
------------------
- declare global constants

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"
# Set / unset to debug somewhere in the package
GLOBAL_DEBUG = False

# ====================================================================================================
# Import from last generated module
# ====================================================================================================

#from .config_5_0_0 import *
#from .config_5_1_0 import *
#from .config_5_2_0_LTS import *
from .config_5_3_0_Beta import *

# ====================================================================================================
# OPTIONS
# ====================================================================================================

SWITCH_JUMP = True

# ====================================================================================================
# Constants
# ====================================================================================================

EMPTY_SOCKET = 'EMPTY_SOCKET'

# ====================================================================================================
# SOCKET_SHAPES
# ====================================================================================================

SOCKET_SHAPES = {
    'Auto'      : 'AUTO',
    'Dynamic'   : 'DYNAMIC',
    'Field'     : 'FIELD',
    'Grid'      : 'GRID',
    'List'      : 'LIST',
    'Single'    : 'SINGLE',
}

# ====================================================================================================
# Array type combination
# ====================================================================================================

ARRAY_TYPES = {
    'VECTOR'  : {'shape': (3,),  'combine': 'Combine XYZ',    'init': 'Vector',   'param': 'vector'},
    'ROTATION': {'shape': (3,),  'combine': 'Combine XYZ',    'init': 'Rotation', 'param': 'rotation'},
    'RGBA'    : {'shape': (4,),  'combine': 'Combine Color',  'init': 'Color',    'param': 'color'},
    'MATRIX'  : {'shape': (16,), 'combine': 'Combine Matrix', 'init': None},
}

TOOL_ONLY = (
    '3D Cursor',
    'Mouse Position',
    'Viewport Transform',
    'Active Element',
    'Selection',
    'Set Selection',
    'Face Set',
    'Set Face Set',
)

MODIFIER_ONLY = (
    'Simulation Input',
    'Viewer',
)

PAIRED_NODES = {
    'GeometryNodeRepeatOutput'                  : 'GeometryNodeRepeatInput',
    'GeometryNodeSimulationOutput'              : 'GeometryNodeSimulationInput',
    'GeometryNodeForeachGeometryElementOutput'  : 'GeometryNodeForeachGeometryElementInput',
    'NodeClosureOutput'                         : 'NodeClosureInput',
}

# ====================================================================================================
# Ignored Sockets
# ====================================================================================================

# Some sockets are not available for all tree

IGNORED_SOCKETS = {
    'ShaderNodeCombineColor' : ('alpha',), # Shader combinaison doesn't support Alpha
}

