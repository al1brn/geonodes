""" Kernel constants

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : kernel/constants
-------------------------
- constants common to generation and api

updates
-------
- creation : 2026/11/14
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"

# Tree types and module names
TREE_TYPES = ('GeometryNodeTree', 'ShaderNodeTree')
TREE_MODULES = {'GeometryNodeTree': 'geonodes', 'ShaderNodeTree': 'shadernodes'}

# Socket types -> class names
CLASS_NAMES = {
 'BOOLEAN'      : 'Boolean',
 'BUNDLE'       : 'Bundle',
 'CLOSURE'      : 'Closure',
 'COLLECTION'   : 'Collection',
 'CUSTOM'       : 'Input',
 'FONT'         : 'Font',
 'GEOMETRY'     : 'Geometry',
 'IMAGE'        : 'Image',
 'INT'          : 'Integer',
 #'INT_VECTOR'   : 'IntVector',
 'MATERIAL'     : 'Material',
 'MATRIX'       : 'Matrix',
 'MENU'         : 'Menu',
 'OBJECT'       : 'Object',
 'RGBA'         : 'Color',
 'ROTATION'     : 'Rotation',
 'SHADER'       : 'Shader',
 'SOUND'        : 'Sound',
 'STRING'       : 'String',
 'VALUE'        : 'Float',
 'VECTOR'       : 'Vector'
}

# Geometry and domain classes
GEOMETRY_CLASSES  = ['Geometry', 'Mesh', 'Curve', 'Cloud', 'Instances', 'Volume', 'GreasePencil']
DOMAIN_CLASSES = ['Domain', 'Point', 'Vertex', 'CloudPoint', 'SplinePoint', 'Face', 'Edge', 'Corner', 'Spline', 'Layer', 'Instance']
POINT_DOMAIN_CLASSES = ('Vertex', 'SplinePoint', 'CloudPoint')

# Attribute classes
ATTRIBUTE_CLASSES = ['Boolean', 'Integer', 'Float', 'Vector', 'Color', 'Matrix', 'Rotation']

# data_types, input_type, socket_type to standard socket_types
DATA_TYPE_HOMONYMS = {
    'INT8'          : 'INT',
    'INTEGER'       : 'INT',
    'FLOAT2'        : 'VECTOR',
    'FLOAT_VECTOR'  : 'VECTOR',
    'VECTOR_FLOAT'  : 'VECTOR',
    'TRANSFORM'     : 'MATRIX',
    'FLOAT4X4'      : 'MATRIX',
    'BYTE_COLOR'    : 'RGBA',
    'FLOAT_COLOR'   : 'RGBA',
    'COLOR'         : 'RGBA',
    'FLOAT'         : 'VALUE',
    'QUATERNION'    : 'ROTATION',
    'FLOAT4'        : 'VECTOR',
}

# Correspondance between blender type and python type plus default value
PYTHON_TYPES = {
    'Boolean'  : ('bool', False),
    'Integer'  : ('int', 0),
    'Float'    : ('float', 0.),
    'Vector'   : ('tuple', (0, 0, 0)),
    'Color'    : ('tuple', (1, 1, 1)),
    'Matrix'   : ('tuple', ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))),
    'Rotation' : ('tuple', (0, 0, 0)),
    'String'   : ('str', '""'),
}

SOCKET_SHAPES = {
    'Auto'      : 'AUTO',
    'Dynamic'   : 'DYNAMIC',
    'Field'     : 'FIELD',
    'Grid'      : 'GRID',
    'List'      : 'LIST',
    'Single'    : 'SINGLE',
}




