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
__version__ = "5.0.0"

# Set / unset to debug somewhere in the package
GLOBAL_DEBUG = False

# ====================================================================================================
# Import from last generated module
# ====================================================================================================

from .config_5_0_0 import *

# ====================================================================================================
# Constants
# ====================================================================================================

EMPTY_SOCKET = 'EMPTY_SOCKET'

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

# ====================================================================================================
# Nodes with dynamic input items
# ====================================================================================================

NODE_WITH_IN_ITEMS = {
    'NodeCombineBundle' 			: 'bundle_items',
    'GeometryNodeCaptureAttribute' 	: 'capture_items',
    'GeometryNodeIndexSwitch'       : 'index_switch_items',
    'GeometryNodeMenuSwitch'        : 'enum_items',
    'NodeClosureOutput'             : 'output_items',
    'FunctionNodeFormatString' 		: 'format_items',
}

# ====================================================================================================
# Nodes with dynamic inputs accepting dynamic inputs
# ====================================================================================================

AUTO_INPUT_TYPE_NODES = [
    'GeometryNodeMenuSwitch',
    'GeometryNodeIndexSwitch',
    'GeometryNodeSwitch',    
]

# ====================================================================================================
# Paired nodes
# ====================================================================================================

PAIRED_NODES = {
	'GeometryNodeRepeatOutput' 					: 'GeometryNodeRepeatInput',
	'GeometryNodeSimulationOutput' 				: 'GeometryNodeSimulationInput',
	'GeometryNodeForeachGeometryElementOutput' 	: 'GeometryNodeForeachGeometryElementInput',
	'NodeClosureOutput'							: 'NodeClosureInput',
}

# ====================================================================================================
# Ignored Sockets
# ====================================================================================================

# Some sockets are anot available for all tree

IGNORED_SOCKETS = {
    'ShaderNodeCombineColor' : ('alpha',), # Shader combinaison doesn't support Alpha
}

# ====================================================================================================
# Nodes enum params transco
# Blender version: (4, 3, 0)

# ----------------------------------------------------------------------------------------------------
# Node specific transco

SPEC_ENUM_PARAMS = {
    'Boolean Math': {
        'Equal'                   : 'XNOR',
        'Not Equal'               : 'XOR',
        'Subtract'                : 'NIMPLY',
    },
    'Compare': {
        'Less Equal'              : 'LESS_EQUAL',
        'Greater Equal'           : 'GREATER_EQUAL',
    },
    ('Math', 'Vector Math', 'Integer Math'): {
        'Add'                     : 'ADD',
        'Sub'                     : 'SUBTRACT',
        'Mult'                    : 'MULTIPLY',
        'Div'                     : 'DIVIDE',
        'Abs'                     : 'ABSOLUTE',
        'Min'                     : 'MINIMUM',
        'Max'                     : 'MAXIMUM',
        'Sign'                    : 'SIGN',
        'Mod'                     : 'MODULO',
        'GCD'                     : 'GCD',
        'LCM'                     : 'LCM',

        'Log'                     : 'LOGARITHM',
        'Exp'                     : 'EXPONENT',
        'Smooth Min'              : 'SMOOTH_MIN',             # ['Math']
        'Smooth Max'              : 'SMOOTH_MAX',             # ['Math']
         #'Trunc'                   : 'TRUNC',                  # ['Math'] # Homonym with 'Float to Integer' and 'String to Curve''
        'Fract'                   : 'FRACT',                  # ['Math']
        'Sin'                     : 'SINE',                   # ['Math', 'Vector Math']
        'Cos'                     : 'COSINE',                 # ['Math', 'Vector Math']
        'Tan'                     : 'TANGENT',                # ['Math', 'Vector Math']
        'Asin'                    : 'ARCSINE',                # ['Math']
        'Acos'                    : 'ARCCOSINE',              # ['Math']
        'Atan'                    : 'ARCTANGENT',             # ['Math']
        'Atan2'                   : 'ARCTAN2',                # ['Math']
        'Sinh'                    : 'SINH',                   # ['Math']
        'Cosh'                    : 'COSH',                   # ['Math']
        'Tanh'                    : 'TANH',                   # ['Math']
        'Radians'                 : 'RADIANS',                # ['Math']
        'Degrees'                 : 'DEGREES',                # ['Math']

        'Cross'                   : 'CROSS_PRODUCT',          # ['Vector Math']
        'Dot'                     : 'DOT_PRODUCT',            # ['Vector Math']

    },
    'Delete Geometry': {
        'Only Edges and Faces'    : 'EDGE_FACE',
        'Only Faces'              : 'ONLY_FACE',
    },
    'Distribute Points in Volume': {
        'Random'                  : 'DENSITY_RANDOM',
        'Grid'                    : 'DENSITY_GRID',
    },
    'Distribute Points in Grid' : {
        'Random'                  : 'DENSITY_RANDOM',
        'Grid'                    : 'DENSITY_GRID',
    },
    'Distribute Points on Faces' : {
        'Poisson Disk'            : 'POISSON',
    },
    ('Mesh Circle', 'Cone', 'Cylinder'): {
        'Triangles'               : 'TRIANGLE_FAN',
    },
    ('Mesh to Volume', 'Points to Volume', 'Volume to Mesh'): {
        'Amount'                  : 'VOXEL_AMOUNT',
        'Size'                    : 'VOXEL_SIZE',
    },
    'Subdivision Surface': {
        'All'                     : 'SMOOTH_ALL',
    },
    'Map Range': {
        'Stepped Linear'          : 'STEPPED',
    },
    'Image Texture': {
        'Linear'                  : 'Linear',
    },
    'Wave Texture': {
        'Sine'                    : 'SIN',
        'Triangles'               : 'TRI',
    },
}


