#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 10:57:41 2022

@author: alain
"""


import os
from pprint import pprint, pformat
import inspect
import bpy

from .gen_load import Socket, Sockets, Node, SOCKET_TYPES

from . import nodesimpl as nimp



_0_ = " "*0
_1_ = " "*4
_2_ = " "*8
_3_ = " "*12

NODE_ATTRS = ['__doc__', '__module__', '__slots__',
    'bl_description', 'bl_height_default', 'bl_height_max', 'bl_height_min', 'bl_icon',
    'bl_idname', 'bl_label', 'bl_rna', 'bl_static_type', 'bl_width_default',
    'bl_width_max', 'bl_width_min',
    'color', 'dimensions', 'draw_buttons', 'draw_buttons_ext', 'height', 'hide',
    'input_template', 'inputs', 'internal_links', 'is_registered_node_type',
    'label', 'location', 'mute', 'name', 'output_template',
    'outputs', 'parent', 'poll', 'poll_instance', 'rna_type', 'select', 'show_options',
    'show_preview', 'show_texture', 'socket_value_update', 'type', 'update',
    'use_custom_color', 'width', 'width_hidden',
    'color_mapping', 'texture_mapping',
    ]
    
WRAPPED = {
    
# ----- Special nodes which are not implemented through functions or methods

'NodeGroupInput'                          : (''          , 'Special'   , ''                            ,  None       ),
'NodeGroupOutput'                         : (''          , 'Special'   , ''                            ,  None       ),
'NodeFrame'                               : (''          , 'Special'   , ''                            ,  None       ),
'NodeReroute'                             : (''          , 'Special'   , ''                            ,  None       ),

'GeometryNodeObjectInfo'                  : ('Object'    , 'Prop'      , 'info'                        ,  None       ),
'GeometryNodeInputSceneTime'              : (''          , 'Special'   , ''                            ,  None       ),
'GeometryNodeViewer'                      : (''          , 'Special'   , ''                            ,  None       ),
'FunctionNodeInputSpecialCharacters'      : ('String'    , 'Method'    , 'Special'                     ,  'String'   ),


# Manually implemented to pass the collection as a str argument
#'GeometryNodeCollectionInfo'              : ('Geometry'  , 'Method'    , 'FromCollection'              , 'Geometry'  ),
#'GeometryNodeInputMaterial'               : ('Material'  , 'Method'     , 'material'                    , 'Material'  ),

# -----------------------------------------------------------------------------------------------------------------------------
# ------------------------- Functions

'FunctionNodeAlignEulerToVector'          : (''          , 'Function'  , 'align_euler_to_vector'       , 'Vector'    ),
'FunctionNodeBooleanMath'                 : (''          , 'Function'  , 'boolean_math'                , 'Boolean'   ),
'FunctionNodeCompare'                     : (''          , 'Function'  , 'compare'                     ,  None       ),
'FunctionNodeRandomValue'                 : (''          , 'Function'  , 'random_value'                , 'Value'     ),
'FunctionNodeRotateEuler'                 : (''          , 'Function'  , 'rotate_euler'                , 'Vector'    ),
'GeometryNodeAccumulateField'             : (''          , 'Function'  , 'accumulate_field'            ,  None       ),
'GeometryNodeAttributeTransfer'           : (''          , 'Function'  , 'atribute_transfer'           , 'NODE'      ),
'GeometryNodeCurveArc'                    : (''          , 'Function'  , 'curve_arc'                   , 'Curve'     ),
'GeometryNodeFieldAtIndex'                : (''          , 'Function'  , 'field_at_index'              ,  None      ),
'GeometryNodeProximity'                   : (''          , 'Function'  , 'proximity'                   , 'Float'     ),
'GeometryNodeRaycast'                     : (''          , 'Function'  , 'raycast'                     ,  None       ),
'GeometryNodeStringJoin'                  : (''          , 'Function'  , 'join_strings'                , 'String'    ),
'GeometryNodeSwitch'                      : (''          , 'Function'  , 'switch'                      , 'Geometry'  ),
'ShaderNodeClamp'                         : (''          , 'Function'  , 'clamp'                       , 'Float'     ),
'ShaderNodeCombineRGB'                    : (''          , 'Function'  , 'combine_rgb'                 , 'Color'     ),
'ShaderNodeCombineXYZ'                    : (''          , 'Function'  , 'combine_xyz'                 , 'Vector'    ),
'ShaderNodeMapRange'                      : (''          , 'Function'  , 'map_range'                   ,  None       ),
'ShaderNodeMath'                          : (''          , 'Function'  , 'math'                        , 'Float'     ),
'ShaderNodeMixRGB'                        : (''          , 'Function'  , 'mixRGB'                      , 'Color'     ),
'ShaderNodeValToRGB'                      : (''          , 'Function'  , 'color_ramp'                  , 'Color'     ),
'ShaderNodeVectorMath'                    : (''          , 'Function'  , 'vector_math'                 ,  None       ),

'GeometryNodeMeshBoolean'                 : (''          , 'Function'  , 'boolean'                     , 'Mesh'      ),

# -----------------------------------------------------------------------------------------------------------------------------
# ------------------------- Basic data

# ----- Data creation are manually implemented with Input

'ShaderNodeValue'                         : ('Float'     , 'Special'   , ''                            ,  None   ),
'FunctionNodeInputBool'                   : ('Boolean'   , 'Special'   , ''                            ,  None   ),
'FunctionNodeInputInt'                    : ('Integer'   , 'Special'   , ''                            ,  None   ),
'FunctionNodeInputString'                 : ('String'    , 'Special'   , ''                            ,  None   ),
'FunctionNodeInputVector'                 : ('Vector'    , 'Special'   , ''                            ,  None   ),
'FunctionNodeInputColor'                  : ('Color'     , 'Special'   , ''                            ,  None   ),

# ----- Float
 
'FunctionNodeFloatToInt'                  : ('Float'     , 'Method'    , 'to_integer'                  , 'Integer'   ),
'FunctionNodeValueToString'               : ('Float'     , 'Method'    , 'to_string'                   , 'String'    ),
'ShaderNodeFloatCurve'                    : ('Float'     , 'Method'    , 'curve'                       , 'Float'     ),

# ----- Vector

'ShaderNodeSeparateXYZ'                   : ('Vector'    , 'PropSet'   , 'separate'                    ,  None       ),
'ShaderNodeVectorCurve'                   : ('Vector'    , 'Stack'     , 'curves'                      , 'Vector'    ),
'ShaderNodeVectorRotate'                  : ('Vector'    , 'Stack'     , 'rotate'                      , 'Vector'    ),

# ----- Color

'ShaderNodeSeparateRGB'                   : ('Color'     , 'Prop'      , 'separate'                    ,  None       ),
'ShaderNodeRGBCurve'                      : ('Color'     , 'Stack'     , 'curves'                      , 'Color'     ),

# ----- String

'FunctionNodeReplaceString'               : ('String'    , 'Stack'     , 'replace'                     , 'String'    ),
'FunctionNodeSliceString'                 : ('String'    , 'Stack'     , 'slice'                       , 'String'    ),

'FunctionNodeStringLength'                : ('String'    , 'Method'    , 'length'                      , 'Integer'   ),
'GeometryNodeStringToCurves'              : ('String'    , 'Method'    , 'to_curves'                   , 'Curve'     ),

# -----------------------------------------------------------------------------------------------------------------------------
# ------------------------- Geometry

# ----- Attributes

'GeometryNodeInputID'                     : ('Geometry'  , 'Attribute' , 'ID'                          , None    ),
'GeometryNodeInputIndex'                  : ('Geometry'  , 'Attribute' , 'index'                       , None    ),
'GeometryNodeInputMaterialIndex'          : ('Geometry'  , 'Attribute' , 'material_index'              , None    ),
'GeometryNodeInputNormal'                 : ('Geometry'  , 'Attribute' , 'normal'                      , None    ),
'GeometryNodeInputPosition'               : ('Geometry'  , 'Attribute' , 'position'                    , None    ),
'GeometryNodeInputShadeSmooth'            : ('Geometry'  , 'Attribute' , 'shade_smooth'                , None    ),
'GeometryNodeInputTangent'                : ('Geometry'  , 'Attribute' , 'tangent'                     , None    ),
'GeometryNodeIsViewport'                  : ('Geometry'  , 'Attribute' , 'is_viewport'                 , ['POINT']),


# ----- Prperties

'GeometryNodeBoundBox'                    : ('Geometry'  , 'Prop'      , 'bound_box'                   ,  ('box', 'box_min', 'box_max')),
'GeometryNodeSeparateComponents'          : ('Geometry'  , 'Prop'      , 'components'                  ,  ('mesh_component', 'points_component', 'curve_component', 'volume_component', 'instances_component')),

# ----- Stack methods

'GeometryNodeDeleteGeometry'              : ('Geometry'  , 'Stack'     , 'delete_geometry'             , 'Geometry'  ),
'GeometryNodeMergeByDistance'             : ('Geometry'  , 'Stack'     , 'merge_by_distance'           , 'Geometry'  ),
'GeometryNodeRealizeInstances'            : ('Geometry'  , 'Stack'     , 'realize_instances'           , 'Geometry'  ),
'GeometryNodeReplaceMaterial'             : ('Geometry'  , 'Stack'     , 'replace_material'            , 'Geometry'  ),
'GeometryNodeScaleElements'               : ('Geometry'  , 'Stack'     , 'scale_elements'              , 'Geometry'  ),
'GeometryNodeSetID'                       : ('Geometry'  , 'Stack'     , 'set_ID'                      , 'Geometry'  ),
'GeometryNodeSetMaterial'                 : ('Geometry'  , 'Stack'     , 'set_material'                , 'Geometry'  ),
'GeometryNodeSetMaterialIndex'            : ('Geometry'  , 'Stack'     , 'set_material_index'          , 'Geometry'  ),
'GeometryNodeSetPosition'                 : ('Geometry'  , 'Stack'     , 'set_position'                , 'Geometry'  ),
'GeometryNodeSetShadeSmooth'              : ('Geometry'  , 'Stack'     , 'set_shade_smooth'            , 'Geometry'  ),
'GeometryNodeTransform'                   : ('Geometry'  , 'Stack'     , 'transform'                   , 'Geometry'  ),

# ----- Methods

'GeometryNodeAttributeDomainSize'         : ('Geometry'  , 'Method'    , 'attribute_domain_size'       , 'Integer'   ),
'GeometryNodeAttributeRemove'             : ('Geometry'  , 'Method'    , 'attribute_remove'            , 'Geometry'  ),
'GeometryNodeAttributeStatistic'          : ('Geometry'  , 'Method'    , 'attribute_statistic'         , 'Float'     ),
'GeometryNodeSeparateGeometry'            : ('Geometry'  , 'Method'    , 'components'                  ,  None ),
'GeometryNodeCaptureAttribute'            : ('Geometry'  , 'Method'    , 'capture_attribute'           ,  None       ),
'GeometryNodeConvexHull'                  : ('Geometry'  , 'Method'    , 'convex_hull'                 , 'Geometry'  ),
'GeometryNodeGeometryToInstance'          : ('Geometry'  , 'Method'    , 'to_instance'                 , 'Instances' ),
'GeometryNodeJoinGeometry'                : ('Geometry'  , 'Method'    , 'join'                        , 'Geometry'  ),

# -----------------------------------------------------------------------------------------------------------------------------
# ------------------------- Curve

# ----- Constructors

'GeometryNodeCurvePrimitiveBezierSegment' : ('Curve'     , 'Method'    , 'BezierSegment'               , 'Curve'     ),
'GeometryNodeCurvePrimitiveCircle'        : ('Curve'     , 'Method'    , 'Circle'                      , 'Curve'     ),
'GeometryNodeCurvePrimitiveLine'          : ('Curve'     , 'Method'    , 'Line'                        , 'Curve'     ),
'GeometryNodeCurvePrimitiveQuadrilateral' : ('Curve'     , 'Method'    , 'Quadrilateral'               , 'Curve'     ),
'GeometryNodeCurveQuadraticBezier'        : ('Curve'     , 'Method'    , 'QuadraticBezier'             , 'Curve'     ),
'GeometryNodeCurveStar'                   : ('Curve'     , 'Method'    , 'Star'                        , 'Curve'     ),
'GeometryNodeCurveSpiral'                 : ('Curve'     , 'Method'    , 'Spiral'                      , 'Curve'     ),

# ----- Attributes

'GeometryNodeCurveEndpointSelection'      : ('Curve'     , 'Attribute' , 'endpoint_selection'          , ['CURVE']   ),
'GeometryNodeCurveHandleTypeSelection'    : ('Curve'     , 'Attribute' , 'handle_type_selection'       , ['CURVE']   ),
'GeometryNodeInputCurveTilt'              : ('Curve'     , 'Attribute' , 'tilt'                        , ['CURVE']   ),
'GeometryNodeInputRadius'                 : ('Curve'     , 'Attribute' , 'radius'                      , ['CURVE']   ),
'GeometryNodeInputCurveHandlePositions'   : ('Curve'     , 'Attribute' , 'handle_positions'            , ['CURVE']   ),

# ----- Stack methods

'GeometryNodeCurveSetHandles'             : ('Curve'     , 'Stack'     , 'set_handles'                 , 'Curve'     ),
'GeometryNodeCurveSplineType'             : ('Curve'     , 'Stack'     , 'set_spline_type'             , 'Curve'     ),
'GeometryNodeFillCurve'                   : ('Curve'     , 'Stack'     , 'fill'                        , 'Mesh'      ),
'GeometryNodeFilletCurve'                 : ('Curve'     , 'Stack'     , 'fillet'                      , 'Curve'     ),
'GeometryNodeResampleCurve'               : ('Curve'     , 'Stack'     , 'resample'                    , 'Curve'     ),
'GeometryNodeReverseCurve'                : ('Curve'     , 'Stack'     , 'reverse'                     , 'Curve'     ),
'GeometryNodeSetCurveHandlePositions'     : ('Curve'     , 'Stack'     , 'set_handle_positions'        , 'Curve'     ),
'GeometryNodeSetCurveRadius'              : ('Curve'     , 'Stack'     , 'set_radius'                  , 'Curve'     ),
'GeometryNodeSetCurveTilt'                : ('Curve'     , 'Stack'     , 'set_tilt'                    , 'Curve'     ),
'GeometryNodeSubdivideCurve'              : ('Curve'     , 'Stack'     , 'subdivide'                   , 'Curve'     ),
'GeometryNodeTrimCurve'                   : ('Curve'     , 'Stack'     , 'trim'                        , 'Curve'     ),

# ----- Methods

'GeometryNodeCurveToMesh'                 : ('Curve'     , 'Method'    , 'to_mesh'                     , 'Mesh'      ),
'GeometryNodeCurveToPoints'               : ('Curve'     , 'Method'    , 'to_points'                   , 'Points'    ),
'GeometryNodeSampleCurve'                 : ('Curve'     , 'Method'    , 'sample'                      ,  None       ),
'GeometryNodeCurveLength'                 : ('Curve'     , 'Prop'      , 'length'                      , 'Float'     ),

# -----------------------------------------------------------------------------------------------------------------------------
# ------------------------- Spline

# ----- Attributes

'GeometryNodeInputSplineCyclic'           : ('Spline'    , 'Attribute' , 'cyclic'                      , ['CURVE']   ),
'GeometryNodeInputSplineResolution'       : ('Spline'    , 'Attribute' , 'resolution'                  , ['CURVE']   ),
'GeometryNodeSplineLength'                : ('Spline'    , 'Attribute' , 'length'                      , ['CURVE']   ),
'GeometryNodeSplineParameter'             : ('Spline'    , 'Attribute' , 'parameter'                   , ['CURVE']   ),

# ----- Stack methods

'GeometryNodeSetSplineCyclic'             : ('Spline'    , 'Stack'     , 'set_cyclic'                  , 'Spline'    ),
'GeometryNodeSetSplineResolution'         : ('Spline'    , 'Stack'     , 'set_resolution'              , 'Spline'    ),

# -----------------------------------------------------------------------------------------------------------------------------
# ------------------------- Mesh

# ----- Constructors

'GeometryNodeMeshCircle'                  : ('Mesh'      , 'Method'    , 'Circle'                      , 'Mesh'      ),
'GeometryNodeMeshCone'                    : ('Mesh'      , 'Method'    , 'Cone'                        , 'Mesh'      ),
'GeometryNodeMeshCube'                    : ('Mesh'      , 'Method'    , 'Cube'                        , 'Mesh'      ),
'GeometryNodeMeshCylinder'                : ('Mesh'      , 'Method'    , 'Cylinder'                    , 'Mesh'      ),
'GeometryNodeMeshGrid'                    : ('Mesh'      , 'Method'    , 'Grid'                        , 'Mesh'      ),
'GeometryNodeMeshIcoSphere'               : ('Mesh'      , 'Method'    , 'IcoSphere'                   , 'Mesh'      ),
'GeometryNodeMeshLine'                    : ('Mesh'      , 'Method'    , 'Line'                        , 'Mesh'      ),
'GeometryNodeMeshToCurve'                 : ('Mesh'      , 'Method'    , 'to_curve'                    , 'Curve'     ),
'GeometryNodeMeshToPoints'                : ('Mesh'      , 'Method'    , 'to_points'                   , 'Points'    ),
'GeometryNodeMeshUVSphere'                : ('Mesh'      , 'Method'    , 'UVSphere'                    , 'Mesh'      ),

# ----- Attributes

'GeometryNodeInputMeshEdgeNeighbors'      : ('Mesh'      , 'Attribute' , 'edge_neighbors'              , ['EDGE']    ),
'GeometryNodeInputMeshFaceArea'           : ('Mesh'      , 'Attribute' , 'face_area'                   , ["FACE"]    ),
'GeometryNodeInputMeshEdgeAngle'          : ('Mesh'      , 'Attribute' , 'edge_angle'                  , ['EDGE']    ),
'GeometryNodeInputMeshEdgeVertices'       : ('Mesh'      , 'Attribute' , 'edge_vertices'               , ['EDGE']    ),
'GeometryNodeInputMeshFaceNeighbors'      : ('Mesh'      , 'Attribute' , 'face_neighbors'              , ['FACE']    ),
'GeometryNodeInputMeshIsland'             : ('Mesh'      , 'Attribute' , 'island'                      , ['FACE']    ),
'GeometryNodeInputMeshVertexNeighbors'    : ('Mesh'      , 'Attribute' , 'vertex_neighbors'            , ['POINT']   ),

# ----- Mesh stack methods

'GeometryNodeSplitEdges'                  : ('Mesh'      , 'Stack'     , 'split_edges'                 , 'Mesh'      ),
'GeometryNodeSubdivideMesh'               : ('Mesh'      , 'Stack'     , 'subdivide'                   , 'Mesh'      ),
'GeometryNodeSubdivisionSurface'          : ('Mesh'      , 'Stack'     , 'subdivision_surface'         , 'Mesh'      ),
'GeometryNodeTriangulate'                 : ('Mesh'      , 'Stack'     , 'triangulate'                 , 'Mesh'      ),
'GeometryNodeDualMesh'                    : ('Mesh'      , 'Stack'     , 'dual'                        , 'Mesh'      ),
'GeometryNodeExtrudeMesh'                 : ('Mesh'      , 'Stack'     , 'extrude'                     , 'Mesh'      ),
'GeometryNodeFlipFaces'                   : ('Mesh'      , 'Stack'     , 'flip_faces'                  , 'Mesh'      ),

# -----------------------------------------------------------------------------------------------------------------------------
# ------------------------- Points

# ----- Constructors

'GeometryNodeDistributePointsOnFaces'     : ('Mesh'      , 'Method'    , 'DistributePointsOnFaces',      'Points'    ),

# ----- Stack methods

'GeometryNodeSetPointRadius'              : ('Points'    , 'Stack'     , 'set_radius'                  , 'Points'    ),

# ----- Methods

'GeometryNodeInstanceOnPoints'            : ('Points'    , 'Method'    , 'instance_on_points'          , 'Instances' ),
'GeometryNodePointsToVertices'            : ('Points'    , 'Method'    , 'to_vertices'                 , 'Mesh'      ),
'GeometryNodePointsToVolume'              : ('Points'    , 'Method'    , 'to_volume'                   , 'Volume'    ),

# -----------------------------------------------------------------------------------------------------------------------------
# ------------------------- Instances

# ----- Stack methods

'GeometryNodeRotateInstances'             : ('Instances' , 'Stack'     , 'rotate'                      , 'Instances' ),
'GeometryNodeScaleInstances'              : ('Instances' , 'Stack'     , 'scale'                       , 'Instances' ),
'GeometryNodeTranslateInstances'          : ('Instances' , 'Stack'     , 'translate'                   , 'Instances' ),

# ----- Methods

'GeometryNodeInstancesToPoints'           : ('Instances' , 'Method'    , 'to_points'                   , 'Points'    ),

# -----------------------------------------------------------------------------------------------------------------------------
# ------------------------- Material

'GeometryNodeMaterialSelection'           : ('Material'  , 'Method'    , 'selection'                   , 'Boolean'   ),


# -----------------------------------------------------------------------------------------------------------------------------
# ------------------------- Texture

# ----- Constructors

'ShaderNodeTexBrick'                      : ('Texture'   , 'Method'    , 'Brick'                       , 'Texture'   ),
'ShaderNodeTexChecker'                    : ('Texture'   , 'Method'    , 'Checker'                     , 'Texture'   ),
'ShaderNodeTexGradient'                   : ('Texture'   , 'Method'    , 'Gradient'                    , 'Texture'   ),
'ShaderNodeTexMagic'                      : ('Texture'   , 'Method'    , 'Magic'                       , 'Texture'   ),
'ShaderNodeTexMusgrave'                   : ('Texture'   , 'Method'    , 'Musgrave'                    , 'Texture'   ),
'ShaderNodeTexNoise'                      : ('Texture'   , 'Method'    , 'Noise'                       , 'Texture'   ),
'ShaderNodeTexVoronoi'                    : ('Texture'   , 'Method'    , 'Voronoi'                     , 'Texture'   ),
'ShaderNodeTexWave'                       : ('Texture'   , 'Method'    , 'Wave'                        , 'Texture'   ),
'ShaderNodeTexWhiteNoise'                 : ('Texture'   , 'Method'    , 'WhiteNoise'                  , 'Texture'   ),
'GeometryNodeImageTexture'                : ('Texture'   , 'Method'    , 'Image'                       , 'Texture'   ),

# -----------------------------------------------------------------------------------------------------------------------------
# ------------------------- Volume

# ----- Methods

'GeometryNodeVolumeToMesh'                : ('Volume'    , 'Method'    , 'to_mesh'                     , 'Mesh'      ),

}


VARIATIONS = {
   'FunctionNodeBooleanMath' : {
      'param'  : 'operation',
      'class'  : 'Boolean',
      'comment' : "Boolean math",
      'values' : {
         'AND'                : ('b_and'               , 'b_and'        , ('__mul__', '__rmul__') ),
         'OR'                 : ('b_or'                , 'b_or'         , ('__add__', '__radd__') ),
         'NOT'                : ('b_not'               , 'b_not'        , '__invert__'),
         'NAND'               : ('nand'                , 'nand'         , ''          ),
         'NOR'                : ('nor'                 , 'nor'          , ''          ),
         'XNOR'               : ('xnor'                , 'xnor'         , ''          ),
         'XOR'                : ('xor'                 , 'xor'          , ''          ),
         'IMPLY'              : ('imply'               , 'imply'        , ''          ),
         'NIMPLY'             : ('nimply'              , 'nimply'       , ''          ),
    }},
   'FunctionNodeRandomValue' : {
      'param'  : 'data_type',
      'class'  : 'DATA_TYPE',
      'comment' : "Generate random values",
      'values' : {
         'FLOAT'              : ('random_float'        , 'Random'       , ''          ),
         'INT'                : ('random_integer'      , 'Random'       , ''          ),
         'FLOAT_VECTOR'       : ('random_vector'       , 'Random'       , ''          ),
         'BOOLEAN'            : ('random_boolean'      , 'Random'       , ''          ),
    }},
   'GeometryNodeSwitch' : {
      'param'  : 'input_type',
      'class'  : 'DATA_TYPE',
      'comment' : "Switch values",
      'decorator': 'static',
      'values' : {
         'FLOAT'              : ('switch_float'        , 'switch'       , ''          ),
         'INT'                : ('switch_integer'      , 'switch'       , ''          ),
         'BOOLEAN'            : ('switch_boolean'      , 'switch'       , ''          ),
         'VECTOR'             : ('switch_vector'       , 'switch'       , ''          ),
         'STRING'             : ('switch_string'       , 'switch'       , ''          ),
         'RGBA'               : ('switch_color'        , 'switch'       , ''          ),
         'OBJECT'             : ('switch_object'       , 'switch'       , ''          ),
         'IMAGE'              : ('switch_image'        , 'switch'       , ''          ),
         'GEOMETRY'           : ('switch_geometry'     , 'switch'       , ''          ),
         'COLLECTION'         : ('switch_collection'   , 'switch'       , ''          ),
         'TEXTURE'            : ('switch_texture'      , 'switch'       , ''          ),
         'MATERIAL'           : ('switch_material'     , 'switch'       , ''          ),
    }},
   'GeometryNodeViewer' : {
      'param'  : 'data_type',
      'class'  : 'DATA_TYPE',
      'comment' : "To output node viewer",
      'values' : {
         'FLOAT'              : ('float_viewer'        , 'to_viewer'    , ''          ),
         'INT'                : ('integer_viewer'      , 'to_viewer'    , ''          ),
         'FLOAT_VECTOR'       : ('vector_viewer'       , 'to_viewer'    , ''          ),
         'FLOAT_COLOR'        : ('color_viewer'        , 'to_viewer'    , ''          ),
         'BOOLEAN'            : ('boolean_viewer'      , 'to_viewer'    , ''          ),
    }},
   'ShaderNodeMath' : {
      'param'  : 'operation',
      'class'  : ('Integer', 'Float'),
      'comment': "Math operations and functions",
      'values' : {
         'ADD'                : ('add'                 , 'add'          , ('__add__', '__radd__')   ),
         'SUBTRACT'           : ('substract'           , 'substract'    , ('__sub__', '__rsub__')   ),
         'MULTIPLY'           : ('multiply'            , 'multiply'     , ('__mul__', '__rmul__')   ),
         'DIVIDE'             : ('divide'              , 'divide'       , ('__truediv__', '__rtruediv__')),
         'MULTIPLY_ADD'       : ('multiply_add'        , 'multiply_add' , ''          ),
         'POWER'              : ('pow'                 , 'pow'          , ('__pow__', '__rpow__')   ),
         'LOGARITHM'          : ('log'                 , 'log'          , ''          ),
         'SQRT'               : ('sqrt'                , 'sqrt'         , ''          ),
         'INVERSE_SQRT'       : ('inverse_sqrt'        , 'inverse_sqrt' , ''          ),
         'ABSOLUTE'           : ('abs'                 , 'abs'          , '__abs__'   ),
         'EXPONENT'           : ('exp'                 , 'exp'          , ''          ),
         'MINIMUM'            : ('min'                 , 'min'          , ''          ),
         'MAXIMUM'            : ('max'                 , 'max'          , ''          ),
         'LESS_THAN'          : ('less_than'           , 'less_than'    , ''          ),
         'GREATER_THAN'       : ('greater_than'        , 'greater_than' , ''          ),
         'SIGN'               : ('sign'                , 'sign'         , ''          ),
         'COMPARE'            : ('compare'             , 'compare'      , ''          ),
         'SMOOTH_MIN'         : ('smooth_min'          , 'smooth_min'   , ''          ),
         'SMOOTH_MAX'         : ('smooth_max'          , 'smooth_max'   , ''          ),
         'ROUND'              : ('round'               , 'round'        , '__round__' ),
         'FLOOR'              : ('floor'               , 'floor'        , '__floor__' ),
         'CEIL'               : ('ceil'                , 'ceil'         , '__ceil__'  ),
         'TRUNC'              : ('trunc'               , 'trunc'        , ''          ),
         'FRACT'              : ('fract'               , 'fract'        , ''          ),
         'MODULO'             : ('modulo'              , 'modulo'       , '__mod__'   ),
         'WRAP'               : ('wrap'                , 'wrap'         , ''          ),
         'SNAP'               : ('snap'                , 'snap'         , ''          ),
         'PINGPONG'           : ('pingpong'            , 'pingpong'     , ''          ),
         'SINE'               : ('sin'                 , 'sin'          , ''          ),
         'COSINE'             : ('cos'                 , 'cos'          , ''          ),
         'TANGENT'            : ('tan'                 , 'tan'          , ''          ),
         'ARCSINE'            : ('arcsin'              , 'arcsin'       , ''          ),
         'ARCCOSINE'          : ('arccos'              , 'arccos'       , ''          ),
         'ARCTANGENT'         : ('arctan'              , 'arctan'       , ''          ),
         'ARCTAN2'            : ('arctan2'             , 'arctan2'      , ''          ),
         'SINH'               : ('sinh'                , 'sinh'         , ''          ),
         'COSH'               : ('cosh'                , 'cosh'         , ''          ),
         'TANH'               : ('tanh'                , 'tanh'         , ''          ),
         'RADIANS'            : ('radians'             , 'radians'      , ''          ),
         'DEGREES'            : ('degrees'             , 'degrees'      , ''          ),
    }},
   'ShaderNodeVectorMath' : {
      'param'  : 'operation',
      'class'  : 'Vector',
      'comment': "Vector math operations and functions",
      'values' : {
         'ADD'                : ('vector_add'          , 'add'          , ('__add__', '__radd__')  ),
         'SUBTRACT'           : ('vector_subtract'     , 'subtract'     , ('__sub__', '__rsub__')  ),
         'MULTIPLY'           : ('vector_multiply'     , 'multiply'     , ('__mul__', '__rmul__')  ),
         'DIVIDE'             : ('vector_divide'       , 'divide'       , ('__truediv__', '__rtruediv__')),
         'MULTIPLY_ADD'       : ('vector_multiply_add' , 'multiply_add' , ''          ),
         'CROSS_PRODUCT'      : ('cross'               , 'cross'        , ''          ),
         'PROJECT'            : ('project'             , 'project'      , ''          ),
         'REFLECT'            : ('reflect'             , 'reflect'      , ''          ),
         'REFRACT'            : ('refract'             , 'refract'      , ''          ),
         'FACEFORWARD'        : ('faceforward'         , 'faceforward'  , ''          ),
         'DOT_PRODUCT'        : ('dot'                 , 'dot'          , ''          ),
         'DISTANCE'           : ('distance'            , 'distance'     , ''          ),
         'LENGTH'             : ('length'              , 'length'       , ''          ),
         'SCALE'              : ('scale'               , 'scale'        , ''          ),
         'NORMALIZE'          : ('normalize'           , 'normalize'    , ''          ),
         'ABSOLUTE'           : ('absolute'            , 'absolute'     , ''          ),
         'MINIMUM'            : ('vector_min'          , 'min'          , ''          ),
         'MAXIMUM'            : ('vector_max'          , 'max'          , ''          ),
         'FLOOR'              : ('vector_floor'        , 'floor'        , '__floor__' ),
         'CEIL'               : ('vector_ceil'         , 'ceil'         , '__ceil__'  ),
         'FRACTION'           : ('vector_fraction'     , 'fraction'     , ''          ),
         'MODULO'             : ('vector_modulo'       , 'modulo'       , '__mod__'   ),
         'WRAP'               : ('wrap'                , 'wrap'         , ''          ),
         'SNAP'               : ('snap'                , 'snap'         , ''          ),
         'SINE'               : ('vector_sin'          , 'sin'          , ''          ),
         'COSINE'             : ('vector_cos'          , 'cos'          , ''          ),
         'TANGENT'            : ('vector_tan'          , 'tan'          , ''          ),
    }},
   'GeometryNodeMeshBoolean' : {
      'param'  : 'operation',
      'class'  : 'VALUE',
      'comment': "Geometry combination",
      'values' : {
         'INTERSECT'          : ('intersect'           , 'intersect'    , '__mul__'   ),
         'UNION'              : ('union'               , 'union'        , '__add__'   ),
         'DIFFERENCE'         : ('difference'          , 'difference'   , '__sub__'   ),
    }},
}

MATH_OP_CLASSES = {
    'ADD'           : 'SAME',
    'SUBTRACT'      : 'SAME',
    'MULTIPLY'      : 'SAME',
    'DIVIDE'        : 'Float',
    'MULTIPLY_ADD'  : 'SAME',
    'POWER'         : 'SAME',
    'LOGARITHM'     : 'Float',
    'SQRT'          : 'Float',
    'INVERSE_SQRT'  : 'Float',
    'ABSOLUTE'      : 'SAME',
    'EXPONENT'      : 'Float',
    'MINIMUM'       : 'SAME',
    'MAXIMUM'       : 'SAME',
    'LESS_THAN'     : 'Boolean',
    'GREATER_THAN'  : 'Boolean',
    'SIGN'          : 'Integer',
    'COMPARE'       : 'Integer',
    'SMOOTH_MIN'    : 'SAME',
    'SMOOTH_MAX'    : 'SAME',
    'ROUND'         : 'Integer',
    'FLOOR'         : 'Integer',
    'CEIL'          : 'Integer',
    'TRUNC'         : 'Integer',
    'FRACT'         : 'Float',
    'MODULO'        : 'SAME',
    'WRAP'          : 'SAME',
    'SNAP'          : 'SAME',
    'PINGPONG'      : 'SAME',
    'SINE'          : 'Float',
    'COSINE'        : 'Float',
    'TANGENT'       : 'Float',
    'ARCSINE'       : 'Float',
    'ARCCOSINE'     : 'Float',
    'ARCTANGENT'    : 'Float',
    'ARCTAN2'       : 'Float',
    'SINH'          : 'Float',
    'COSH'          : 'Float',
    'TANH'          : 'Float',
    'RADIANS'       : 'Float',
    'DEGREES'       : 'Float',    
}


CLASSES = {'Float'      : ('NodeSocketFloat',     'NodeValue'       , 'bcls.Float'      ),
           'Integer'    : ('NodeSocketInt',       'NodeInputInt'    , 'bcls.Integer'    ),
           'Boolean'    : ('NodeSocketBool',      'NodeInputBool'   , 'bcls.Boolean'    ),
           'String'     : ('NodeSocketString',    'NodeInputString' , 'bcls.String'     ),
           'Vector'     : ('NodeSocketVector',    'NodeInputVector' , 'bcls.Vector'     ),
           'Color'      : ('NodeSocketColor',     'NodeInputColor'  , 'bcls.Color'      ),
           'Geometry'   : ('NodeSocketGeometry',   None,              'bcls.Geometry'   ),
           'Curve'      : ('NodeSocketGeometry',   None,              'Geometry'        ),
           'Spline'     : ('NodeSocketGeometry',   None,              'Curve'           ),
           'Mesh'       : ('NodeSocketGeometry',   None,              'Geometry'        ),
           'Points'     : ('NodeSocketGeometry',   None,              'Mesh'            ),
           'Instances'  : ('NodeSocketGeometry',   None,              'Mesh'            ),
           'Volume'     : ('NodeSocketGeometry',   None,              'Geometry'        ),
           'Collection' : ('NodeSocketCollection', None,              'bcls.Collection' ),
           'Object'     : ('NodeSocketObject',     None,              'bcls.Object' ),
           'Image'      : ('NodeSocketImage',      None,              'bcls.Image' ),
           'Material'   : ('NodeSocketMaterial',   None,              'bcls.Material' ),
           'Texture'    : ('NodeSocketTexture',    None,              'bcls.Texture' ),
           }

DATA_TYPES_CLASS = {
    'FLOAT'         : 'Float',
    'INT'           : 'Integer',  
    'BOOLEAN'       : 'Boolean',        
    'VECTOR'        : 'Vector',       
    'FLOAT_VECTOR'  : 'Vector',       
    'STRING'        : 'String',       
    'RGBA'          : 'Color',       
    'FLOAT_COLOR'   : 'Color',       
    'OBJECT'        : 'Object',        
    'IMAGE'         : 'Image',       
    'GEOMETRY'      : 'Geometry',      
    'COLLECTION'    : 'Collection',      
    'TEXTURE'       : 'Texture',      
    'MATERIAL'      : 'Material',        
}

# ====================================================================================================
# Get the variations available for a class

def get_class_variations(class_name):
    variations = {}
    for blid, spec in VARIATIONS.items():
        class_ = spec['class']

        if class_ == class_name:
            variations[blid] = spec
            
        elif isinstance(class_, tuple):
            if class_name in class_:
                variations[blid] = spec
            
        elif class_ == 'DATA_TYPE':
            extract = {}
            for data_type, val in spec['values'].items():
                if DATA_TYPES_CLASS[data_type] == class_name:
                    extract[data_type] = val
                    
            if extract:
                variations[blid] = {
                    'param'    : spec['param'],
                    'class'    : class_name,
                    'decorator': spec.get('decorator'),
                    'values'   : extract,
                    }
                
    return variations


# ====================================================================================================
# Templates 

# ----------------------------------------------------------------------------------------------------
# Read source code from a template

def get_code_template(func, rename=None, replace={}):
    s = inspect.getsource(func)
    if rename is not None:
        s = s.replace(f"def {func.__name__}", f"def {rename}")
    for k, v in replace.items():
        s = s.replace(k, v)
    return s.split("\n")


def is_vector(arg):
    return isinstance(arg, Vector) or (isinstance(arg, (tuple, list)) and len(arg) == 3)








# ----------------------------------------------------------------------------------------------------
# Template for class initialization

def CLASS_INIT(self, _VALUE_, socket=None, input_name=None):
               
    if input_name is None:
        if isinstance(value, nodes.Node):
            super().__init__(value, socket)
        else:
            super().__init__(nodes._NODE_(value), 0)
    else:
        ns = nodes.Tree.current().new_input_CLASS(value=value, name=input_name)
        super().__init__(ns.node, ns.socket)
        
        
# ====================================================================================================

def debug(fpath):
    
    # ====================================================================================================
    # Load all the possible geometry nodes
               
    nodes = bpy.data.node_groups["Dev"].nodes
    nodes.clear()

    all_nodes = {}

    for tp in dir(bpy.types):
        
        if tp.find('Legacy') >= 0:
            continue
        
        if tp in ['NodeFrame', 'NodeReroute', 'NodeGroupInput', 'NodeGroupOutput']:
            pass
            continue
        
        try:
            bnode = nodes.new(tp)
        except:
            continue
           
        node = Node(bnode)
        all_nodes[tp] = node
        
    # ====================================================================================================
    # Create the nodes module

    with open(fpath + "nodes.py", 'w') as f:
        
        #cur_path = os.path.dirname(os.path.realpath(__file__))
        #with open(cur_path + "/gen_root.py", "r") as ft:
        #    s = ft.read()
        
        #f.write(s.replace('_CR_', "\\n"))
        
        f.write("from .basenode import Socket, SocketIn, Sockets, Node, Attribute\n\n")
        
        for node in all_nodes.values():
            
            spec = WRAPPED.get(node.bnode.bl_idname)
            if spec is None:
                is_attribute = False
            else:
                is_attribute = spec[1] == 'Attribute'
            
            for line in node.gen_node_class(is_attribute):
                f.write(line)      
                
    # ====================================================================================================
    # Debug
    
    with open(fpath + "classes.py", 'w') as f:
        
        # ----------------------------------------------------------------------------------------------------
        # Imports
        
        f.write("from geonodes import baseclasses as bcls\n")
        f.write("from geonodes import nodes\n\n")
        f.write("import logging\n")
        f.write("logger = logging.Logger('geonodes')\n\n")
        
        # ----------------------------------------------------------------------------------------------------
        # Utility: argument is a vector
        
        f.write(f"# {'-'*100}\n# Argument is a vector\n\n")
        f.write("def is_vector(arg):\n")
        f.write("    return isinstance(arg, Vector) or (isinstance(arg, (tuple, list)) and len(arg) == 3)\n\n")
        
        # ----------------------------------------------------------------------------------------------------
        # Sockets
        
        f.write(f"# {'-'*100}\n# Sockets outputs\n\n")
        f.write("class Sockets(bcls.Sockets):\n")
        f.write("    pass\n\n")

        # ----------------------------------------------------------------------------------------------------
        # Classes
        
        nimp.GEN_NODES = []
        
        for i, dgen in enumerate(nimp.DATA_CLASSES):
            
            for line in dgen(all_nodes).gen_class():
                f.write(line)
                
        print('-'*80)
        print("Data classes created, unused nodes are:")
        print()
        for blid, node in all_nodes.items():
            if not blid in nimp.GEN_NODES:
                print(f"{node.node_name:20s}:{blid}")
        print()
            
    
    
        
        
    
# ====================================================================================================
# Generate all the files

def create_files(fpath):
    
    return debug(fpath)
    
    # ====================================================================================================
    # Load all the possible geometry nodes
               
    nodes = bpy.data.node_groups["Dev"].nodes
    nodes.clear()

    all_nodes = {}

    for tp in dir(bpy.types):
        
        if tp.find('Legacy') >= 0:
            continue
        
        if tp in ['NodeFrame', 'NodeReroute', 'NodeGroupInput', 'NodeGroupOutput']:
            pass
            continue
        
        try:
            bnode = nodes.new(tp)
        except:
            continue
           
        node = Node(bnode)
        all_nodes[tp] = node
        
    # ====================================================================================================
    # Create the nodes module

    with open(fpath + "nodes.py", 'w') as f:
        
        #cur_path = os.path.dirname(os.path.realpath(__file__))
        #with open(cur_path + "/gen_root.py", "r") as ft:
        #    s = ft.read()
        
        #f.write(s.replace('_CR_', "\\n"))
        
        f.write("from .basenode import Socket, SocketIn, Sockets, Node, Attribute\n\n")
        
        for node in all_nodes.values():
            
            spec = WRAPPED.get(node.bnode.bl_idname)
            if spec is None:
                is_attribute = False
            else:
                is_attribute = spec[1] == 'Attribute'
            
            for line in node.gen_node_class(is_attribute):
                f.write(line)

    # ====================================================================================================
    # Create the data module
        
    with open(fpath + "classes.py", 'w') as f:
        
        #f.write("from geonodes import tree\n")
        f.write("from geonodes import baseclasses as bcls\n")
        f.write("from geonodes import nodes\n\n")
        
        # ----------------------------------------------------------------------------------------------------
        # Utilities
        
        f.write("def is_vector(arg):\n")
        f.write(_1_ + "return isinstance(arg, Vector) or (isinstance(arg, (tuple, list)) and len(arg) == 3)\n\n")
        
        
        # ----------------------------------------------------------------------------------------------------
        # Functions
        
        f.write(f"# {'='*120}\n# Functions\n\n")
        
        for blid, spec in WRAPPED.items():
            if spec[0] != "":
                continue
            
            if spec[1] != "Function":
                continue

            if blid in VARIATIONS:
                continue
            
            node = all_nodes[blid]
            for line in node.gen_function('FUNCTION', func_name=spec[2], return_class = spec[3]):
                f.write(line)
                
        # ----------------------------------------------------------------------------------------------------
        # Variations

        for blid, spec in WRAPPED.items():
            if spec[0] != "":
                continue
            
            if spec[1] != "Function":
                continue
            
            if blid not in VARIATIONS:
                continue
            
            
            node = all_nodes[blid]
            f.write(f"# {'-'*120}\n")
            f.write(f"# {VARIATIONS[blid]['comment']}\n\n")

            if blid in VARIATIONS:
                param_name = VARIATIONS[blid]['param']
                values     = VARIATIONS[blid]['values'] 
                for value, var_spec in values.items():
                    for line in node.gen_function('FUNCTION', func_name=var_spec[0], variation={param_name: value}, return_class = spec[3]):
                        f.write(line)
                
                        
        # ----------------------------------------------------------------------------------------------------
        # Data classes
        
        f.write(f"# {'='*120}\n# Data classes\n\n")
        
        for class_name, class_spec in CLASSES.items():
            
            f.write(f"# {'-'*120}\n")
            f.write(f"# class {class_name}\n\n")
            
            f.write(f"class {class_name}(")
            if class_spec[2] is None:
                f.write("):\n\n")
            else:
                f.write(f"{class_spec[2]}):\n\n")
                
            # ---------------------------------------------------------------------------
            # Constructor if exist
            
            #node_init = class_spec[1]
            #if node_init is not None:
            #    f.write( "    @classmethod\n")
            #    f.write( "    def Input(cls, value=None):\n")
            #    f.write(f"        return cls(nodes.{node_init}(value), 0)\n\n")
                
            # ---------------------------------------------------------------------------
            # Methods associated to the class
        
            for blid, spec in WRAPPED.items():
                if spec[0] != class_name:
                    continue
                
                # ---------------------------------------------------------------------------
                # Method or stack method
                
                if spec[1] in ['Method', 'Stack']:
                    
                    ftype = spec[1].upper()
                    
                    if spec[1] == 'Field':
                        set_props = ["node.field_of = self.node"]
                    else:
                        set_props = []
                        
                    node = all_nodes[blid]
                    for line in node.gen_function(ftype, func_name=spec[2], return_class = spec[3]):
                        f.write(line)

                # ---------------------------------------------------------------------------
                # Property
                        
                elif spec[1] in ['Prop', 'PropSet']:

                    node = all_nodes[blid]
                    for line in node.gen_node_as_property(spec[2], names = spec[3], settable=spec[1] == 'PropSet'):
                        f.write(line)
                        
                # ---------------------------------------------------------------------------
                # Field
                        
                elif spec[1] == 'Attribute':
                    
                    node = all_nodes[blid]
                    for line in node.gen_attribute(spec[2], domains=spec[3]):
                        f.write(line)
                        
                # ---------------------------------------------------------------------------
                # Initializer
                # Code is generated here
                
                elif spec[1] == 'Init':
                    replace = {
                        '_VALUE_' : f"value={spec[3][0]}",
                        '_NODE_'  : spec[3][1],
                        'CLASS'   : class_name.lower(),
                        }
                    
                    for line in get_code_template(CLASS_INIT, rename="__init__", replace=replace):
                        f.write("    " + line + "\n")
                    f.write("\n")
                        
            
            # ---------------------------------------------------------------------------
            # Variations
            
            variations = get_class_variations(class_name)
            
            for blid, spec in variations.items():
            
                node = all_nodes[blid]
                
                param_name = spec['param']
                values     = spec['values'] 
                decorator  = spec.get('decorator')
                
                for value, var_spec in values.items():
                    
                    variation = {param_name: value}

                    return_class = None
                    if blid == 'ShaderNodeMath':
                        return_class = MATH_OP_CLASSES[value]
                        if return_class == 'SAME':
                            return_class = class_name
                        
                    # ----- The base method
                    
                    if decorator is None:
                        ftype = 'METHOD'
                    else:
                        if decorator == 'static':
                            ftype = 'STATIC'
                            
                    
                    for line in node.gen_function(ftype, func_name=var_spec[1], variation=variation, return_class=return_class):
                        f.write(line)

                    # ----- The operator : add --> __add__, __add__
                        
                    ops = var_spec[2]
                    if ops != "":
                        if not isinstance(ops, tuple):
                            ops = [ops]
                            
                        for op in ops:
                            for line in node.gen_function('METHOD', func_name=op, variation=variation, return_class=return_class):
                                f.write(line)
                                
            # ---------------------------------------------------------------------------
            # Some hacks
            
            if class_name in ['Integer', 'Float', 'Vector']:
                f.write("    def __neg__(self):\n")
                f.write("        return self.multiply(-1)\n\n")
                
            if class_name in ['Boolean']:
                f.write("    def __neg__(self):\n")
                f.write("        return self.b_not()\n\n")
                
        # ----------------------------------------------------------------------------------------------------
        # ClassServer initialization
        
        if False:
        
            f.write(f"# {'='*120}\n# Tree classes initialization\n\n")
                    
            #f.write(f"nodes.Tree.initialize_classes(globals())\n\n")
            f.write("nodes.Tree.CLASSES = {\n")
            for class_name in CLASSES:
                s = f"'{class_name}'"
                f.write(f"    {s:15s} : {class_name},\n")
            f.write("}\n\n\n")
                
        

                                
                        
                
                
                        
                
                    

                


        
        
        


