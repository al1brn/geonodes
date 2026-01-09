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


# ----------------------------------------------------------------------------------------------------
# Node specific transco
#
# Generated by node_explore.build_user_enum_params

ENUM_PARAMS = {
    'X'                       : 'X',                      # ['Align Rotation to Vector', 'Align Rotation to Vector', 'Axes to Rotation', 'Axes to Rotation', 'Dial Gizmo', 'Linear Gizmo', 'Wave Texture', 'Wave Texture']
    'Y'                       : 'Y',                      # ['Align Rotation to Vector', 'Align Rotation to Vector', 'Axes to Rotation', 'Axes to Rotation', 'Dial Gizmo', 'Linear Gizmo', 'Wave Texture', 'Wave Texture']
    'Z'                       : 'Z',                      # ['Align Rotation to Vector', 'Align Rotation to Vector', 'Axes to Rotation', 'Axes to Rotation', 'Dial Gizmo', 'Linear Gizmo', 'Wave Texture', 'Wave Texture']
    'Auto'                    : 'AUTO',                   # ['Align Rotation to Vector', 'Handle Type Selection', 'Set Handle Type']
    'And'                     : 'AND',                    # ['Boolean Math']
    'Or'                      : 'OR',                     # ['Boolean Math']
    'Not'                     : 'NOT',                    # ['Boolean Math']
    'Nand'                    : 'NAND',                   # ['Boolean Math']
    'Nor'                     : 'NOR',                    # ['Boolean Math']
    'Xnor'                    : 'XNOR',                   # ['Boolean Math']
    'Xor'                     : 'XOR',                    # ['Boolean Math']
    'Imply'                   : 'IMPLY',                  # ['Boolean Math']
    'Nimply'                  : 'NIMPLY',                 # ['Boolean Math']
    'RGB'                     : 'RGB',                    # ['Combine Color', 'Separate Color']
    'HSV'                     : 'HSV',                    # ['Combine Color', 'Separate Color']
    'HSL'                     : 'HSL',                    # ['Combine Color', 'Separate Color']
    'Element'                 : 'ELEMENT',                # ['Compare']
    'Length'                  : 'LENGTH',                 # ['Compare', 'Curve to Points', 'Resample Curve', 'Sample Curve', 'Trim Curve', 'Vector Math']
    'Average'                 : 'AVERAGE',                # ['Compare']
    'Dot Product'             : 'DOT_PRODUCT',            # ['Compare', 'Vector Math']
    'Direction'               : 'DIRECTION',              # ['Compare', 'Curve Line']
    'Less Than'               : 'LESS_THAN',              # ['Compare', 'Math']
    'Less Than or Equal'      : 'LESS_EQUAL',             # ['Compare']
    'Greater Than'            : 'GREATER_THAN',           # ['Compare', 'Math']
    'Greater Than or Equal'   : 'GREATER_EQUAL',          # ['Compare']
    'Equal'                   : 'EQUAL',                  # ['Compare']
    'Not Equal'               : 'NOT_EQUAL',              # ['Compare']
    'Round'                   : 'ROUND',                  # ['Float to Integer', 'Math']
    'Floor'                   : 'FLOOR',                  # ['Float to Integer', 'Math', 'Vector Math']
    'Ceiling'                 : 'CEILING',                # ['Float to Integer']
    'Truncate'                : 'TRUNCATE',               # ['Float to Integer', 'String to Curves']
    'Add'                     : 'ADD',                    # ['Integer Math', 'Math', 'Mix', 'Vector Math']
    'Subtract'                : 'SUBTRACT',               # ['Integer Math', 'Math', 'Mix', 'Vector Math']
    'Multiply'                : 'MULTIPLY',               # ['Integer Math', 'Math', 'Mix', 'Vector Math']
    'Divide'                  : 'DIVIDE',                 # ['Integer Math', 'Math', 'Mix', 'Vector Math']
    'Multiply Add'            : 'MULTIPLY_ADD',           # ['Integer Math', 'Math', 'Vector Math']
    'Absolute'                : 'ABSOLUTE',               # ['Integer Math', 'Math', 'Vector Math']
    'Negate'                  : 'NEGATE',                 # ['Integer Math']
    'Power'                   : 'POWER',                  # ['Integer Math', 'Math']
    'Minimum'                 : 'MINIMUM',                # ['Integer Math', 'Math', 'Vector Math']
    'Maximum'                 : 'MAXIMUM',                # ['Integer Math', 'Math', 'Vector Math']
    'Sign'                    : 'SIGN',                   # ['Integer Math', 'Math']
    'Divide Round'            : 'DIVIDE_ROUND',           # ['Integer Math']
    'Divide Floor'            : 'DIVIDE_FLOOR',           # ['Integer Math']
    'Divide Ceil'             : 'DIVIDE_CEIL',            # ['Integer Math']
    'Floored Modulo'          : 'FLOORED_MODULO',         # ['Integer Math', 'Math']
    'Modulo'                  : 'MODULO',                 # ['Integer Math', 'Math', 'Vector Math']
    'Greatest Common Divisor' : 'GCD',                    # ['Integer Math']
    'Least Common Multiple'   : 'LCM',                    # ['Integer Math']
    'Global'                  : 'GLOBAL',                 # ['Rotate Rotation']
    'Local'                   : 'LOCAL',                  # ['Rotate Rotation']
    'Mesh'                    : 'MESH',                   # ['Domain Size']
    'Point Cloud'             : 'POINTCLOUD',             # ['Domain Size']
    'Curve'                   : 'CURVE',                  # ['Domain Size']
    'Instances'               : 'INSTANCES',              # ['Domain Size']
    'Grease Pencil'           : 'GREASEPENCIL',           # ['Domain Size']
    'Original'                : 'ORIGINAL',               # ['Collection Info', 'Object Info']
    'Relative'                : 'RELATIVE',               # ['Collection Info', 'Object Info']
    'Points'                  : 'POINTS',                 # ['Arc', 'Curve Circle', 'Curve Line', 'Quadrilateral', 'Geometry Proximity']
    'Radius'                  : 'RADIUS',                 # ['Arc', 'Curve Circle']
    'Free'                    : 'FREE',                   # ['Handle Type Selection', 'Set Handle Type', 'Set Curve Normal']
    'Vector'                  : 'VECTOR',                 # ['Handle Type Selection', 'Set Handle Type', 'Switch']
    'Align'                   : 'ALIGN',                  # ['Handle Type Selection', 'Set Handle Type']
    'Position'                : 'POSITION',               # ['Bézier Segment']
    'Offset'                  : 'OFFSET',                 # ['Bézier Segment', 'Mesh Line']
    'Rectangle'               : 'RECTANGLE',              # ['Quadrilateral']
    'Parallelogram'           : 'PARALLELOGRAM',          # ['Quadrilateral']
    'Trapezoid'               : 'TRAPEZOID',              # ['Quadrilateral']
    'Kite'                    : 'KITE',                   # ['Quadrilateral']
    'Catmull Rom'             : 'CATMULL_ROM',            # ['Set Spline Type']
    'Poly'                    : 'POLY',                   # ['Set Spline Type', 'Fillet Curve']
    'Bezier'                  : 'BEZIER',                 # ['Set Spline Type', 'Fillet Curve']
    'NURBS'                   : 'NURBS',                  # ['Set Spline Type']
    'Evaluated'               : 'EVALUATED',              # ['Curve to Points', 'Resample Curve']
    'Count'                   : 'COUNT',                  # ['Curve to Points', 'Resample Curve']
    'All'                     : 'ALL',                    # ['Delete Geometry', 'Merge by Distance', 'Subdivision Surface']
    'Edge_Face'               : 'EDGE_FACE',              # ['Delete Geometry']
    'Only_Face'               : 'ONLY_FACE',              # ['Delete Geometry']
    'Density_Random'          : 'DENSITY_RANDOM',         # ['Distribute Points in Grid', 'Distribute Points in Volume']
    'Density_Grid'            : 'DENSITY_GRID',           # ['Distribute Points in Grid', 'Distribute Points in Volume']
    'Random'                  : 'RANDOM',                 # ['Distribute Points on Faces']
    'Poisson'                 : 'POISSON',                # ['Distribute Points on Faces']
    'Vertices'                : 'VERTICES',               # ['Extrude Mesh', 'Mesh to Points']
    'Edges'                   : 'EDGES',                  # ['Extrude Mesh', 'Mesh to Points', 'Geometry Proximity']
    'Faces'                   : 'FACES',                  # ['Extrude Mesh', 'Mesh to Points', 'Geometry Proximity']
    'Triangles'               : 'TRIANGLES',              # ['Fill Curve']
    'N-gons'                  : 'NGONS',                  # ['Fill Curve']
    'Primary'                 : 'PRIMARY',                # ['Dial Gizmo', 'Linear Gizmo']
    'Secondary'               : 'SECONDARY',              # ['Dial Gizmo', 'Linear Gizmo']
    'Arrow'                   : 'ARROW',                  # ['Linear Gizmo']
    'Cross'                   : 'CROSS',                  # ['Linear Gizmo']
    'Box'                     : 'BOX',                    # ['Linear Gizmo']
    'Repeat'                  : 'REPEAT',                 # ['Image Texture']
    'Extend'                  : 'EXTEND',                 # ['Image Texture']
    'Clip'                    : 'CLIP',                   # ['Image Texture', 'Triangulate']
    'Mirror'                  : 'MIRROR',                 # ['Image Texture']
    'Linear'                  : 'LINEAR',                 # ['Map Range', 'Gradient Texture']
    'Closest'                 : 'Closest',                # ['Image Texture']
    'Cubic'                   : 'Cubic',                  # ['Image Texture']
    'Connected'               : 'CONNECTED',              # ['Merge by Distance']
    'By Name'                 : 'MERGE_BY_NAME',          # ['Merge Layers']
    'By Group ID'             : 'MERGE_BY_ID',            # ['Merge Layers']
    'Intersect'               : 'INTERSECT',              # ['Mesh Boolean', 'SDF Grid Boolean']
    'Union'                   : 'UNION',                  # ['Mesh Boolean', 'SDF Grid Boolean']
    'Difference'              : 'DIFFERENCE',             # ['Mesh Boolean', 'SDF Grid Boolean', 'Mix']
    'Exact'                   : 'EXACT',                  # ['Mesh Boolean', 'Remove Named Attribute']
    'Float'                   : 'FLOAT',                  # ['Mesh Boolean', 'Switch', 'Set Selection']
    'None'                    : 'NONE',                   # ['Mesh Circle', 'Cone', 'Cylinder', 'Subdivision Surface']
    'N-Gon'                   : 'NGON',                   # ['Mesh Circle', 'Cone', 'Cylinder']
    'Triangle_Fan'            : 'TRIANGLE_FAN',           # ['Mesh Circle', 'Cone', 'Cylinder']
    'Total'                   : 'TOTAL',                  # ['Mesh Line']
    'Resolution'              : 'RESOLUTION',             # ['Mesh Line']
    'End Points'              : 'END_POINTS',             # ['Mesh Line']
    'Corners'                 : 'CORNERS',                # ['Mesh to Points']
    'Voxel_Amount'            : 'VOXEL_AMOUNT',           # ['Mesh to Volume', 'Points to Volume', 'Volume to Mesh']
    'Voxel_Size'              : 'VOXEL_SIZE',             # ['Mesh to Volume', 'Points to Volume', 'Volume to Mesh']
    'Interpolated'            : 'INTERPOLATED',           # ['Raycast']
    'Nearest'                 : 'NEAREST',                # ['Raycast', 'Sample Grid']
    'Wildcard'                : 'WILDCARD',               # ['Remove Named Attribute']
    'Factor'                  : 'FACTOR',                 # ['Sample Curve', 'Trim Curve']
    'Trilinear'               : 'TRILINEAR',              # ['Sample Grid']
    'Triquadratic'            : 'TRIQUADRATIC',           # ['Sample Grid']
    'Uniform'                 : 'UNIFORM',                # ['Scale Elements', 'Mix']
    'Single Axis'             : 'SINGLE_AXIS',            # ['Scale Elements']
    'Left'                    : 'LEFT',                   # ['Set Handle Positions', 'String to Curves']
    'Right'                   : 'RIGHT',                  # ['Set Handle Positions', 'String to Curves']
    'Minimum Twist'           : 'MINIMUM_TWIST',          # ['Set Curve Normal']
    'Z Up'                    : 'Z_UP',                   # ['Set Curve Normal']
    'Center'                  : 'CENTER',                 # ['String to Curves']
    'Justify'                 : 'JUSTIFY',                # ['String to Curves']
    'Flush'                   : 'FLUSH',                  # ['String to Curves']
    'Top'                     : 'TOP',                    # ['String to Curves']
    'Top Baseline'            : 'TOP_BASELINE',           # ['String to Curves']
    'Middle'                  : 'MIDDLE',                 # ['String to Curves']
    'Bottom Baseline'         : 'BOTTOM_BASELINE',        # ['String to Curves']
    'Bottom'                  : 'BOTTOM',                 # ['String to Curves']
    'Overflow'                : 'OVERFLOW',               # ['String to Curves']
    'Scale To Fit'            : 'SCALE_TO_FIT',           # ['String to Curves']
    'Midpoint'                : 'MIDPOINT',               # ['String to Curves']
    'Top Left'                : 'TOP_LEFT',               # ['String to Curves']
    'Top Center'              : 'TOP_CENTER',             # ['String to Curves']
    'Top Right'               : 'TOP_RIGHT',              # ['String to Curves']
    'Bottom Left'             : 'BOTTOM_LEFT',            # ['String to Curves']
    'Bottom Center'           : 'BOTTOM_CENTER',          # ['String to Curves']
    'Bottom Right'            : 'BOTTOM_RIGHT',           # ['String to Curves']
    'Keep Corners'                   : 'PRESERVE_CORNERS',                       # ['Subdivision Surface', 'Subdivision Surface']
    'Keep Corners Junctions'         : 'PRESERVE_CORNERS_AND_JUNCTIONS',         # ['Subdivision Surface']
    'Keep Corners Junctions Concave' : 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', # ['Subdivision Surface']
    'Keep Boundaries'                : 'PRESERVE_BOUNDARIES',                    # ['Subdivision Surface']
    'Smooth_All'                     : 'SMOOTH_ALL',                             # ['Subdivision Surface']
    'Boolean'                 : 'BOOLEAN',                # ['Set Selection']
    'Matrix'                  : 'MATRIX',                 # ['Transform Geometry']
    'Components'              : 'COMPONENTS',             # ['Transform Geometry']
    'Beauty'                  : 'BEAUTY',                 # ['Triangulate', 'Triangulate']
    'Fixed'                   : 'FIXED',                  # ['Triangulate']
    'Fixed Alternate'         : 'FIXED_ALTERNATE',        # ['Triangulate']
    'Shortest Diagonal'       : 'SHORTEST_DIAGONAL',      # ['Triangulate']
    'Longest Diagonal'        : 'LONGEST_DIAGONAL',       # ['Triangulate']
    'Angle Based'             : 'ANGLE_BASED',            # ['UV Unwrap']
    'Conformal'               : 'CONFORMAL',              # ['UV Unwrap']
    'Grid'                    : 'GRID',                   # ['Volume to Mesh']
    'Min Max'                 : 'MINMAX',                 # ['Clamp']
    'Range'                   : 'RANGE',                  # ['Clamp']
    'Stepped Linear'          : 'STEPPED',                # ['Map Range']
    'Smooth Step'             : 'SMOOTHSTEP',             # ['Map Range']
    'Smoother Step'           : 'SMOOTHERSTEP',           # ['Map Range']
    'Logarithm'               : 'LOGARITHM',              # ['Math']
    'Square Root'             : 'SQRT',                   # ['Math']
    'Inverse Square Root'     : 'INVERSE_SQRT',           # ['Math']
    'Exponent'                : 'EXPONENT',               # ['Math']
    'Compare'                 : 'COMPARE',                # ['Math']
    'Smooth Mininimum'        : 'SMOOTH_MIN',             # ['Math']
    'Smooth Maximum'          : 'SMOOTH_MAX',             # ['Math']
    'Ceil'                    : 'CEIL',                   # ['Math', 'Vector Math']
    'Trunc'                   : 'TRUNC',                  # ['Math']
    'Fraction'                : 'FRACT',                  # ['Math']
    'Wrap'                    : 'WRAP',                   # ['Math', 'Vector Math']
    'Snap'                    : 'SNAP',                   # ['Math', 'Vector Math']
    'Ping-Pong'               : 'PINGPONG',               # ['Math']
    'Sine'                    : 'SINE',                   # ['Math', 'Vector Math']
    'Cosine'                  : 'COSINE',                 # ['Math', 'Vector Math']
    'Tangent'                 : 'TANGENT',                # ['Math', 'Vector Math']
    'Arcsine'                 : 'ARCSINE',                # ['Math']
    'Arccosine'               : 'ARCCOSINE',              # ['Math']
    'Arctangent'              : 'ARCTANGENT',             # ['Math']
    'Arctan2'                 : 'ARCTAN2',                # ['Math']
    'Hyperbolic Sine'         : 'SINH',                   # ['Math']
    'Hyperbolic Cosine'       : 'COSH',                   # ['Math']
    'Hyperbolic Tangent'      : 'TANH',                   # ['Math']
    'To Radians'              : 'RADIANS',                # ['Math']
    'To Degrees'              : 'DEGREES',                # ['Math']
    'Mix'                     : 'MIX',                    # ['Mix']
    'Darken'                  : 'DARKEN',                 # ['Mix']
    'Color Burn'              : 'BURN',                   # ['Mix']
    'Lighten'                 : 'LIGHTEN',                # ['Mix']
    'Screen'                  : 'SCREEN',                 # ['Mix']
    'Color Dodge'             : 'DODGE',                  # ['Mix']
    'Overlay'                 : 'OVERLAY',                # ['Mix']
    'Soft Light'              : 'SOFT_LIGHT',             # ['Mix']
    'Linear Light'            : 'LINEAR_LIGHT',           # ['Mix']
    'Exclusion'               : 'EXCLUSION',              # ['Mix']
    'Hue'                     : 'HUE',                    # ['Mix']
    'Saturation'              : 'SATURATION',             # ['Mix']
    'Color'                   : 'COLOR',                  # ['Mix']
    'Value'                   : 'VALUE',                  # ['Mix']
    'Non-Uniform'             : 'NON_UNIFORM',            # ['Mix']
    '2D'                      : '2D',                     # ['Gabor Texture', 'Noise Texture', 'Voronoi Texture', 'White Noise Texture']
    '3D'                      : '3D',                     # ['Gabor Texture', 'Noise Texture', 'Voronoi Texture', 'White Noise Texture']
    'Quadratic'               : 'QUADRATIC',              # ['Gradient Texture']
    'Easing'                  : 'EASING',                 # ['Gradient Texture']
    'Diagonal'                : 'DIAGONAL',               # ['Gradient Texture', 'Wave Texture']
    'Spherical'               : 'SPHERICAL',              # ['Gradient Texture', 'Wave Texture']
    'Quadratic Sphere'        : 'QUADRATIC_SPHERE',       # ['Gradient Texture']
    'Radial'                  : 'RADIAL',                 # ['Gradient Texture']
    '1D'                      : '1D',                     # ['Noise Texture', 'Voronoi Texture', 'White Noise Texture']
    '4D'                      : '4D',                     # ['Noise Texture', 'Voronoi Texture', 'White Noise Texture']
    'Multifractal'            : 'MULTIFRACTAL',           # ['Noise Texture']
    'Ridged Multifractal'     : 'RIDGED_MULTIFRACTAL',    # ['Noise Texture']
    'Hybrid Multifractal'     : 'HYBRID_MULTIFRACTAL',    # ['Noise Texture']
    'fBM'                     : 'FBM',                    # ['Noise Texture']
    'Hetero Terrain'          : 'HETERO_TERRAIN',         # ['Noise Texture']
    'Euclidean'               : 'EUCLIDEAN',              # ['Voronoi Texture']
    'Manhattan'               : 'MANHATTAN',              # ['Voronoi Texture']
    'Chebychev'               : 'CHEBYCHEV',              # ['Voronoi Texture']
    'Minkowski'               : 'MINKOWSKI',              # ['Voronoi Texture']
    'F1'                      : 'F1',                     # ['Voronoi Texture']
    'F2'                      : 'F2',                     # ['Voronoi Texture']
    'Smooth F1'               : 'SMOOTH_F1',              # ['Voronoi Texture']
    'Distance to Edge'        : 'DISTANCE_TO_EDGE',       # ['Voronoi Texture']
    'N-Sphere Radius'         : 'N_SPHERE_RADIUS',        # ['Voronoi Texture']
    'Sin'                     : 'SIN',                    # ['Wave Texture']
    'Saw'                     : 'SAW',                    # ['Wave Texture']
    'Tri'                     : 'TRI',                    # ['Wave Texture']
    'Bands'                   : 'BANDS',                  # ['Wave Texture']
    'Rings'                   : 'RINGS',                  # ['Wave Texture']
    'Cross Product'           : 'CROSS_PRODUCT',          # ['Vector Math']
    'Project'                 : 'PROJECT',                # ['Vector Math']
    'Reflect'                 : 'REFLECT',                # ['Vector Math']
    'Refract'                 : 'REFRACT',                # ['Vector Math']
    'Faceforward'             : 'FACEFORWARD',            # ['Vector Math']
    'Distance'                : 'DISTANCE',               # ['Vector Math']
    'Scale'                   : 'SCALE',                  # ['Vector Math']
    'Normalize'               : 'NORMALIZE',              # ['Vector Math']
    'Fraction'                : 'FRACTION',               # ['Vector Math']
    'Axis Angle'              : 'AXIS_ANGLE',             # ['Vector Rotate']
    'X Axis'                  : 'X_AXIS',                 # ['Vector Rotate']
    'Y Axis'                  : 'Y_AXIS',                 # ['Vector Rotate']
    'Z Axis'                  : 'Z_AXIS',                 # ['Vector Rotate']
    'Euler XYZ'               : 'EULER_XYZ',              # ['Vector Rotate']

    # Shader

    'Geometry'                : 'GEOMETRY',               # ['Attribute']
    'Object'                  : 'OBJECT',                 # ['Attribute', 'Displacement', 'Normal Map', 'Point Density', 'Vector Displacement', 'Vector Transform', 'Vector Transform']
    'Instancer'               : 'INSTANCER',              # ['Attribute']
    'View Layer'              : 'VIEW_LAYER',             # ['Attribute']
    'Beckmann'                : 'BECKMANN',               # ['Glossy BSDF', 'Glass BSDF', 'Metallic BSDF', 'Refraction BSDF']
    'GGX'                     : 'GGX',                    # ['Glossy BSDF', 'Glass BSDF', 'Metallic BSDF', 'Principled BSDF', 'Refraction BSDF']
    'Ashikhmin-Shirley'       : 'ASHIKHMIN_SHIRLEY',      # ['Glossy BSDF']
    'Multiscatter GGX'        : 'MULTI_GGX',              # ['Glossy BSDF', 'Glass BSDF', 'Metallic BSDF', 'Principled BSDF']
    'Reflection'              : 'Reflection',             # ['Hair BSDF']
    'Transmission'            : 'Transmission',           # ['Hair BSDF']
    'Chiang'                  : 'CHIANG',                 # ['Principled Hair BSDF']
    'Huang'                   : 'HUANG',                  # ['Principled Hair BSDF']
    'Absorption'              : 'ABSORPTION',             # ['Principled Hair BSDF']
    'Melanin'                 : 'MELANIN',                # ['Principled Hair BSDF']
    'Physical Conductor'      : 'PHYSICAL_CONDUCTOR',     # ['Metallic BSDF']
    'F82'                     : 'F82',                    # ['Metallic BSDF']
    'Burley'                  : 'BURLEY',                 # ['Principled BSDF', 'Subsurface Scattering']
    'Random Walk'             : 'RANDOM_WALK',            # ['Principled BSDF', 'Subsurface Scattering']
    'Random Walk (Skin)'      : 'RANDOM_WALK_SKIN',       # ['Principled BSDF', 'Subsurface Scattering']
    'Ashikhmin'               : 'ASHIKHMIN',              # ['Sheen BSDF']
    'Microfiber'              : 'MICROFIBER',             # ['Sheen BSDF']
    'Diffuse'                 : 'DIFFUSE',                # ['Toon BSDF']
    'Glossy'                  : 'GLOSSY',                 # ['Toon BSDF']
    'World'                   : 'WORLD',                  # ['Displacement', 'Normal Map', 'Vector Displacement', 'Vector Transform', 'Vector Transform']
    'Point'                   : 'POINT',                  # ['Mapping', 'Vector Transform']
    'Texture'                 : 'TEXTURE',                # ['Mapping']
    'Normal'                  : 'NORMAL',                 # ['Mapping', 'Vector Transform']
    'Blender Object'          : 'BLENDER_OBJECT',         # ['Normal Map']
    'Blender World'           : 'BLENDER_WORLD',          # ['Normal Map']
    'EEVEE'                   : 'EEVEE',                  # ['Light Output', 'Line Style Output', 'Material Output', 'World Output']
    'Cycles'                  : 'CYCLES',                 # ['Light Output', 'Line Style Output', 'Material Output', 'World Output']
    'Internal'                : 'INTERNAL',               # ['Script', 'IES Texture']
    'External'                : 'EXTERNAL',               # ['Script', 'IES Texture']
    'UU Map'                  : 'UV_MAP',                 # ['Tangent']
    'Smart'                   : 'Smart',                  # ['Environment Texture', 'Image Texture']
    'Equirectangular'         : 'EQUIRECTANGULAR',        # ['Environment Texture']
    'Mirror Ball'             : 'MIRROR_BALL',            # ['Environment Texture']
    'Flat'                    : 'FLAT',                   # ['Image Texture']
    'Sphere'                  : 'SPHERE',                 # ['Image Texture']
    'Tube'                    : 'TUBE',                   # ['Image Texture']
    'Particle_Age'            : 'PARTICLE_AGE',           # ['Point Density']
    'Particle_Speed'          : 'PARTICLE_SPEED',         # ['Point Density']
    'Particle Velocity'       : 'PARTICLE_VELOCITY',      # ['Point Density']
    'Particle System'         : 'PARTICLE_SYSTEM',        # ['Point Density']
    'Object Vertices'         : 'OBJECT',                 # ['Point Density']
    'Object Space'            : 'OBJECT',                 # ['Point Density']
    'World Space'             : 'World',                  # ['Point Density']
    'Vertex Color'            : 'VERTEX_COLOR',           # ['Point Density']
    'Vertex Weight'           : 'VERTEX_WEIGHT',          # ['Point Density']
    'Vertex Normal'           : 'VERTEX_NORMAL',          # ['Point Density']
    'Preetham'                : 'PREETHAM',               # ['Sky Texture']
    'Hosek / Wilkie'          : 'HOSEK_WILKIE',           # ['Sky Texture']
    'Nishita'                 : 'NISHITA',                # ['Sky Texture']
    'Camera'                  : 'CAMERA',                 # ['Vector Transform', 'Vector Transform']
    'Henyey§Greenstein'       : 'HENYEY_GREENSTEIN',      # ['Volume Scatter']
    'Fournier§Forand'         : 'FOURNIER_FORAND',        # ['Volume Scatter']
    'Draine'                  : 'DRAINE',                 # ['Volume Scatter']
    'Rayleigh'                : 'RAYLEIGH',               # ['Volume Scatter']
    'Mie'                     : 'MIE',                    # ['Volume Scatter']

}
