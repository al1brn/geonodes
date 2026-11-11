# Generated file. Do not edit.
from typing import Literal

T_DATA_TYPE_1 = Literal['FLOAT', 'INT', 'FLOAT_VECTOR', 'TRANSFORM']
T_DOMAIN_1 = Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']
T_DOMAIN_2 = Literal['POINT', 'EDGE', 'FACE', 'LAYER']
T_DATA_TYPE_2 = Literal['FLOAT', 'INT', 'VECTOR']
T_AXIS_1 = Literal['X', 'Y', 'Z']
T_PIVOT_AXIS_1 = Literal['AUTO', 'X', 'Y', 'Z']
T_MODE_1 = Literal['POINTS', 'RADIUS']
T_DATA_TYPE_3 = Literal['FLOAT', 'FLOAT_VECTOR']
T_OPERATION_1 = Literal['AND', 'OR', 'XOR', 'NOT', 'SHIFT', 'ROTATE']
T_DATA_TYPE_4 = Literal['FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR']
T_TRANSFORM_SPACE_1 = Literal['ORIGINAL', 'RELATIVE']
T_OPERATION_2 = Literal['AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY']
T_MODE_2 = Literal['POSITION', 'OFFSET']
T_CLAMP_TYPE_1 = Literal['MINMAX', 'RANGE']
T_DATA_TYPE_5 = Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR']
T_MODE_3 = Literal['RGB', 'HSV', 'HSL']
T_DATA_TYPE_6 = Literal[
    'FLOAT',
    'INT',
    'BOOLEAN',
    'VECTOR',
    'RGBA',
    'ROTATION',
    'MATRIX',
    'STRING',
    'MENU',
    'OBJECT',
    'IMAGE',
    'GEOMETRY',
    'COLLECTION',
    'MATERIAL',
    'BUNDLE',
    'CLOSURE',
    'FONT',
    'SOUND',
]
T_DATA_TYPE_7 = Literal[
    'FLOAT',
    'INT',
    'VECTOR',
    'RGBA',
    'STRING',
    'OBJECT',
    'IMAGE',
    'COLLECTION',
    'MATERIAL',
    'FONT',
    'SOUND',
]
T_OPERATION_3 = Literal[
    'LESS_THAN',
    'LESS_EQUAL',
    'GREATER_THAN',
    'GREATER_EQUAL',
    'EQUAL',
    'NOT_EQUAL',
]
T_MODE_4 = Literal['ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION']
T_FILL_TYPE_1 = Literal['NONE', 'NGON', 'TRIANGLE_FAN']
T_MODE_5 = Literal['POINTS', 'DIRECTION']
T_MODE_6 = Literal['EVALUATED', 'COUNT', 'LENGTH']
T_MODE_7 = Literal['ALL', 'EDGE_FACE', 'ONLY_FACE']
T_DOMAIN_3 = Literal['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE', 'LAYER']
T_COLOR_ID_1 = Literal['PRIMARY', 'SECONDARY', 'X', 'Y', 'Z']
T_MODE_8 = Literal['DENSITY_RANDOM', 'DENSITY_GRID']
T_DISTRIBUTE_METHOD_1 = Literal['RANDOM', 'POISSON']
T_COMPONENT_1 = Literal['MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES', 'GREASEPENCIL']
T_DOMAIN_4 = Literal['POINT', 'EDGE', 'FACE', 'SPLINE', 'LAYER', 'INSTANCE']
T_DATA_TYPE_8 = Literal[
    'FLOAT',
    'INT',
    'BOOLEAN',
    'FLOAT_VECTOR',
    'FLOAT_COLOR',
    'QUATERNION',
    'FLOAT4X4',
]
T_MODE_9 = Literal['VERTICES', 'EDGES', 'FACES']
T_DATA_TYPE_9 = Literal['FLOAT', 'INT', 'FLOAT_VECTOR']
T_ROUNDING_MODE_1 = Literal['ROUND', 'FLOOR', 'CEILING', 'TRUNCATE']
T_GABOR_TYPE_1 = Literal['2D', '3D']
T_TARGET_ELEMENT_1 = Literal['POINTS', 'EDGES', 'FACES']
T_GRADIENT_TYPE_1 = Literal[
    'LINEAR',
    'QUADRATIC',
    'EASING',
    'DIAGONAL',
    'SPHERICAL',
    'QUADRATIC_SPHERE',
    'RADIAL',
]
T_HANDLE_TYPE_1 = Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN']
T_DATA_TYPE_10 = Literal['FLOAT', 'INT', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING']
T_INTERPOLATION_1 = Literal['Linear', 'Closest', 'Cubic']
T_EXTENSION_1 = Literal['REPEAT', 'EXTEND', 'CLIP', 'MIRROR']
T_OPERATION_4 = Literal[
    'ADD',
    'SUBTRACT',
    'MULTIPLY',
    'DIVIDE',
    'MULTIPLY_ADD',
    'ABSOLUTE',
    'NEGATE',
    'POWER',
    'MINIMUM',
    'MAXIMUM',
    'SIGN',
    'DIVIDE_ROUND',
    'DIVIDE_FLOOR',
    'DIVIDE_CEIL',
    'FLOORED_MODULO',
    'MODULO',
    'GCD',
    'LCM',
]
T_DRAW_STYLE_1 = Literal['ARROW', 'CROSS', 'BOX']
T_INTERPOLATION_TYPE_1 = Literal['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP']
T_OPERATION_5 = Literal[
    'ADD',
    'SUBTRACT',
    'MULTIPLY',
    'DIVIDE',
    'MULTIPLY_ADD',
    'POWER',
    'LOGARITHM',
    'SQRT',
    'INVERSE_SQRT',
    'ABSOLUTE',
    'EXPONENT',
    'MINIMUM',
    'MAXIMUM',
    'LESS_THAN',
    'GREATER_THAN',
    'SIGN',
    'COMPARE',
    'SMOOTH_MIN',
    'SMOOTH_MAX',
    'ROUND',
    'FLOOR',
    'CEIL',
    'TRUNC',
    'FRACT',
    'MODULO',
    'FLOORED_MODULO',
    'WRAP',
    'SNAP',
    'PINGPONG',
    'SINE',
    'COSINE',
    'TANGENT',
    'ARCSINE',
    'ARCCOSINE',
    'ARCTANGENT',
    'ARCTAN2',
    'SINH',
    'COSH',
    'TANH',
    'RADIANS',
    'DEGREES',
]
T_MODE_10 = Literal['MERGE_BY_NAME', 'MERGE_BY_ID']
T_OPERATION_6 = Literal['INTERSECT', 'UNION', 'DIFFERENCE']
T_SOLVER_1 = Literal['EXACT', 'FLOAT', 'MANIFOLD']
T_MODE_11 = Literal['OFFSET', 'END_POINTS']
T_COUNT_MODE_1 = Literal['TOTAL', 'RESOLUTION']
T_MODE_12 = Literal['EDGES', 'FACES']
T_MODE_13 = Literal['VERTICES', 'EDGES', 'FACES', 'CORNERS']
T_DATA_TYPE_11 = Literal['FLOAT', 'VECTOR', 'RGBA', 'ROTATION']
T_FACTOR_MODE_1 = Literal['UNIFORM', 'NON_UNIFORM']
T_BLEND_TYPE_1 = Literal[
    'MIX',
    'DARKEN',
    'MULTIPLY',
    'BURN',
    'LIGHTEN',
    'SCREEN',
    'DODGE',
    'ADD',
    'OVERLAY',
    'SOFT_LIGHT',
    'LINEAR_LIGHT',
    'DIFFERENCE',
    'EXCLUSION',
    'SUBTRACT',
    'DIVIDE',
    'HUE',
    'SATURATION',
    'COLOR',
    'VALUE',
]
T_NOISE_DIMENSIONS_1 = Literal['1D', '2D', '3D', '4D']
T_NOISE_TYPE_1 = Literal[
    'MULTIFRACTAL',
    'RIDGED_MULTIFRACTAL',
    'HYBRID_MULTIFRACTAL',
    'FBM',
    'HETERO_TERRAIN',
]
T_MODE_14 = Literal['RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS']
T_DATA_TYPE_12 = Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR']
T_ROTATION_SPACE_1 = Literal['GLOBAL', 'LOCAL']
T_MODE_15 = Literal['FACTOR', 'LENGTH']
T_DOMAIN_5 = Literal['POINT', 'EDGE', 'FACE', 'CORNER']
T_DOMAIN_6 = Literal['FACE', 'EDGE']
T_MODE_16 = Literal['STROKE', 'FILL', 'BOTH']
T_MODE_17 = Literal['LEFT', 'RIGHT']
T_MODE_18 = Literal['SHARPNESS', 'FREE', 'TANGENT_SPACE']
T_DOMAIN_7 = Literal['POINT', 'FACE', 'CORNER']
T_DOMAIN_8 = Literal['POINT', 'EDGE', 'FACE', 'CURVE']
T_SELECTION_TYPE_1 = Literal['BOOLEAN', 'FLOAT']
T_SPLINE_TYPE_1 = Literal['CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS']
T_DOMAIN_9 = Literal['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE']
T_DATA_TYPE_13 = Literal[
    'FLOAT',
    'INT',
    'BOOLEAN',
    'FLOAT_VECTOR',
    'FLOAT_COLOR',
    'QUATERNION',
    'FLOAT4X4',
    'INT8',
    'FLOAT2',
    'FLOAT4',
    'BYTE_COLOR',
]
T_DATA_TYPE_14 = Literal['BOOLEAN', 'FLOAT', 'INT', 'VECTOR_FLOAT']
T_DATA_TYPE_15 = Literal['FLOAT', 'INT']
T_OPERATION_7 = Literal[
    'ADD',
    'SUBTRACT',
    'MULTIPLY',
    'DIVIDE',
    'MULTIPLY_ADD',
    'CROSS_PRODUCT',
    'PROJECT',
    'REFLECT',
    'REFRACT',
    'FACEFORWARD',
    'DOT_PRODUCT',
    'DISTANCE',
    'LENGTH',
    'SCALE',
    'NORMALIZE',
    'ABSOLUTE',
    'POWER',
    'SIGN',
    'MINIMUM',
    'MAXIMUM',
    'ROUND',
    'FLOOR',
    'CEIL',
    'FRACTION',
    'MODULO',
    'WRAP',
    'SNAP',
    'SINE',
    'COSINE',
    'TANGENT',
]
T_ROTATION_TYPE_1 = Literal['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ']
T_DOMAIN_10 = Literal['AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']
T_DISTANCE_1 = Literal['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI']
T_FEATURE_1 = Literal['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS']
T_WARNING_TYPE_1 = Literal['ERROR', 'WARNING', 'INFO']
T_WAVE_TYPE_1 = Literal['BANDS', 'RINGS']
T_BANDS_DIRECTION_1 = Literal['X', 'Y', 'Z', 'DIAGONAL']
T_RINGS_DIRECTION_1 = Literal['X', 'Y', 'Z', 'SPHERICAL']
T_WAVE_PROFILE_1 = Literal['SIN', 'SAW', 'TRI']
