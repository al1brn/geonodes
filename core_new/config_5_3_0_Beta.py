# GeoNodes configuration
# Blender (5, 3, 0)
# Generated 2026-11-14 07:00:02


blender_version = (5, 3, 0)

__all__ = ['blender_version', 'TREE_TYPES', 'CLASS_NAMES', 'GEOMETRY_CLASSES', 'DOMAIN_CLASSES', 'ATTRIBUTE_CLASSES', 'DATA_TYPE_HOMONYMS', 'AUTO_INPUT_TYPE_NODES', 'SOCKET_SHAPES', 'SOCKETS', 'SOCKET_SUBTYPES', 'SOCKET_IDS', 'NODE_INFO', 'NODE_NAMES', 'ONE_ITEMS_NODES', 'BUILTIN_GROUPS']

#--------------------------------------------------------------------------------
# Trees
#--------------------------------------------------------------------------------

TREE_TYPES = ('GeometryNodeTree', 'ShaderNodeTree')

#--------------------------------------------------------------------------------
# Classes lists
#--------------------------------------------------------------------------------

CLASS_NAMES = {
   'BOOLEAN'    : 'Boolean',
   'BUNDLE'     : 'Bundle',
   'CLOSURE'    : 'Closure',
   'COLLECTION' : 'Collection',
   'CUSTOM'     : 'Input',
   'FONT'       : 'Font',
   'GEOMETRY'   : 'Geometry',
   'IMAGE'      : 'Image',
   'INT'        : 'Integer',
   'MATERIAL'   : 'Material',
   'MATRIX'     : 'Matrix',
   'MENU'       : 'Menu',
   'OBJECT'     : 'Object',
   'RGBA'       : 'Color',
   'ROTATION'   : 'Rotation',
   'SHADER'     : 'Shader',
   'SOUND'      : 'Sound',
   'STRING'     : 'String',
   'VALUE'      : 'Float',
   'VECTOR'     : 'Vector',
}



GEOMETRY_CLASSES = ['Geometry', 'Mesh', 'Curve', 'Cloud', 'Instances', 'Volume', 'GreasePencil']
DOMAIN_CLASSES = ['Domain', 'Point', 'Vertex', 'CloudPoint', 'SplinePoint', 'Face', 'Edge', 'Corner', 'Spline', 'Layer', 'Instance']
ATTRIBUTE_CLASSES = ['Boolean', 'Integer', 'Float', 'Vector', 'Color', 'Matrix', 'Rotation']

SOCKET_SHAPES = {'Auto': 'AUTO', 'Dynamic': 'DYNAMIC', 'Field': 'FIELD', 'Grid': 'GRID', 'List': 'LIST', 'Single': 'SINGLE'}

#--------------------------------------------------------------------------------
# Sockets
#--------------------------------------------------------------------------------

DATA_TYPE_HOMONYMS = {
   'INT8'         : 'INT',
   'INTEGER'      : 'INT',
   'FLOAT2'       : 'VECTOR',
   'FLOAT_VECTOR' : 'VECTOR',
   'VECTOR_FLOAT' : 'VECTOR',
   'TRANSFORM'    : 'MATRIX',
   'FLOAT4X4'     : 'MATRIX',
   'BYTE_COLOR'   : 'RGBA',
   'FLOAT_COLOR'  : 'RGBA',
   'COLOR'        : 'RGBA',
   'FLOAT'        : 'VALUE',
   'QUATERNION'   : 'ROTATION',
   'FLOAT4'       : 'VECTOR',
}

SOCKET_IDS = {
   'NodeSocketFloat'                 : 'NodeSocketFloat',
   'Float'                           : 'NodeSocketFloat',
   'VALUE'                           : 'NodeSocketFloat',
   'NodeSocketFloatPixel'            : 'NodeSocketFloat',
   'NodeSocketFloatPercentage'       : 'NodeSocketFloat',
   'NodeSocketFloatFactor'           : 'NodeSocketFloat',
   'NodeSocketFloatMass'             : 'NodeSocketFloat',
   'NodeSocketFloatAngle'            : 'NodeSocketFloat',
   'NodeSocketFloatTime'             : 'NodeSocketFloat',
   'NodeSocketFloatTimeAbsolute'     : 'NodeSocketFloat',
   'NodeSocketFloatDistance'         : 'NodeSocketFloat',
   'NodeSocketFloatWavelength'       : 'NodeSocketFloat',
   'NodeSocketFloatColorTemperature' : 'NodeSocketFloat',
   'NodeSocketFloatFrequency'        : 'NodeSocketFloat',
   'NodeSocketInt'                   : 'NodeSocketInt',
   'Integer'                         : 'NodeSocketInt',
   'INT'                             : 'NodeSocketInt',
   'NodeSocketIntPixel'              : 'NodeSocketInt',
   'NodeSocketIntPercentage'         : 'NodeSocketInt',
   'NodeSocketIntFactor'             : 'NodeSocketInt',
   'NodeSocketBool'                  : 'NodeSocketBool',
   'Boolean'                         : 'NodeSocketBool',
   'BOOLEAN'                         : 'NodeSocketBool',
   'NodeSocketVector'                : 'NodeSocketVector',
   'Vector'                          : 'NodeSocketVector',
   'VECTOR'                          : 'NodeSocketVector',
   'NodeSocketVectorPixel'           : 'NodeSocketVector',
   'NodeSocketVectorPercentage'      : 'NodeSocketVector',
   'NodeSocketVectorFactor'          : 'NodeSocketVector',
   'NodeSocketVectorTranslation'     : 'NodeSocketVector',
   'NodeSocketVectorDirection'       : 'NodeSocketVector',
   'NodeSocketVectorVelocity'        : 'NodeSocketVector',
   'NodeSocketVectorAcceleration'    : 'NodeSocketVector',
   'NodeSocketVectorEuler'           : 'NodeSocketVector',
   'NodeSocketVectorXYZ'             : 'NodeSocketVector',
   'NodeSocketColor'                 : 'NodeSocketColor',
   'Color'                           : 'NodeSocketColor',
   'RGBA'                            : 'NodeSocketColor',
   'NodeSocketRotation'              : 'NodeSocketRotation',
   'Rotation'                        : 'NodeSocketRotation',
   'ROTATION'                        : 'NodeSocketRotation',
   'NodeSocketMatrix'                : 'NodeSocketMatrix',
   'Matrix'                          : 'NodeSocketMatrix',
   'MATRIX'                          : 'NodeSocketMatrix',
   'NodeSocketString'                : 'NodeSocketString',
   'String'                          : 'NodeSocketString',
   'STRING'                          : 'NodeSocketString',
   'NodeSocketStringFilePath'        : 'NodeSocketString',
   'NodeSocketMenu'                  : 'NodeSocketMenu',
   'Menu'                            : 'NodeSocketMenu',
   'MENU'                            : 'NodeSocketMenu',
   'NodeSocketGeometry'              : 'NodeSocketGeometry',
   'Geometry'                        : 'NodeSocketGeometry',
   'GEOMETRY'                        : 'NodeSocketGeometry',
   'NodeSocketObject'                : 'NodeSocketObject',
   'Object'                          : 'NodeSocketObject',
   'OBJECT'                          : 'NodeSocketObject',
   'NodeSocketCollection'            : 'NodeSocketCollection',
   'Collection'                      : 'NodeSocketCollection',
   'COLLECTION'                      : 'NodeSocketCollection',
   'NodeSocketImage'                 : 'NodeSocketImage',
   'Image'                           : 'NodeSocketImage',
   'IMAGE'                           : 'NodeSocketImage',
   'NodeSocketMaterial'              : 'NodeSocketMaterial',
   'Material'                        : 'NodeSocketMaterial',
   'MATERIAL'                        : 'NodeSocketMaterial',
   'NodeSocketFont'                  : 'NodeSocketFont',
   'Font'                            : 'NodeSocketFont',
   'FONT'                            : 'NodeSocketFont',
   'NodeSocketSound'                 : 'NodeSocketSound',
   'Sound'                           : 'NodeSocketSound',
   'SOUND'                           : 'NodeSocketSound',
   'NodeSocketBundle'                : 'NodeSocketBundle',
   'Bundle'                          : 'NodeSocketBundle',
   'BUNDLE'                          : 'NodeSocketBundle',
   'NodeSocketClosure'               : 'NodeSocketClosure',
   'Closure'                         : 'NodeSocketClosure',
   'CLOSURE'                         : 'NodeSocketClosure',
   'NodeSocketVirtual'               : 'NodeSocketVirtual',
   'CUSTOM'                          : 'NodeSocketVirtual',
   'Input'                           : 'NodeSocketVirtual',
   'Mesh'                            : 'NodeSocketGeometry',
   'Curve'                           : 'NodeSocketGeometry',
   'Cloud'                           : 'NodeSocketGeometry',
   'Instances'                       : 'NodeSocketGeometry',
   'Volume'                          : 'NodeSocketGeometry',
   'GreasePencil'                    : 'NodeSocketGeometry',
   'Domain'                          : 'NodeSocketGeometry',
   'Point'                           : 'NodeSocketGeometry',
   'Vertex'                          : 'NodeSocketGeometry',
   'CloudPoint'                      : 'NodeSocketGeometry',
   'SplinePoint'                     : 'NodeSocketGeometry',
   'Face'                            : 'NodeSocketGeometry',
   'Edge'                            : 'NodeSocketGeometry',
   'Corner'                          : 'NodeSocketGeometry',
   'Spline'                          : 'NodeSocketGeometry',
   'Layer'                           : 'NodeSocketGeometry',
   'Instance'                        : 'NodeSocketGeometry',
