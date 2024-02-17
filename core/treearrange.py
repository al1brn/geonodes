#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 07:40:10 2022

@author: alain
"""

from pprint import pprint

from mathutils import Vector, Color
import bpy


NODE_DIMS = {
   'FunctionNodeAlignEulerToVector'          : {'dimensions': (280, 468), 'param_count': 0,},
   'FunctionNodeBooleanMath'                 : {'dimensions': (280, 254), 'param_count': 1,
           'name'    : 'operation',
           'changes' : {
                'NOT'                : (280, 214),},},
   'FunctionNodeCombineColor'                : {'dimensions': (280, 342), 'param_count': 0,},
   'FunctionNodeCompare'                     : {'dimensions': (280, 308), 'param_count': 2,
           'names'   : ['data_type', 'operation'],
           'changes' : {
                ('FLOAT',  'LESS_THAN',     ) : (280, 308),
                ('FLOAT',  'LESS_EQUAL',    ) : (280, 308),
                ('FLOAT',  'GREATER_THAN',  ) : (280, 308),
                ('FLOAT',  'GREATER_EQUAL', ) : (280, 308),
                ('FLOAT',  'EQUAL',         ) : (280, 348),
                ('FLOAT',  'NOT_EQUAL',     ) : (280, 348),
                ('INT',    'LESS_THAN',     ) : (280, 308),
                ('INT',    'LESS_EQUAL',    ) : (280, 308),
                ('INT',    'GREATER_THAN',  ) : (280, 308),
                ('INT',    'GREATER_EQUAL', ) : (280, 308),
                ('INT',    'EQUAL',         ) : (280, 308),
                ('INT',    'NOT_EQUAL',     ) : (280, 308),
                ('VECTOR', 'LESS_THAN',     ) : (280, 642),
                ('VECTOR', 'LESS_EQUAL',    ) : (280, 642),
                ('VECTOR', 'GREATER_THAN',  ) : (280, 642),
                ('VECTOR', 'GREATER_EQUAL', ) : (280, 642),
                ('VECTOR', 'EQUAL',         ) : (280, 682),
                ('VECTOR', 'NOT_EQUAL',     ) : (280, 682),
                ('STRING', 'EQUAL',         ) : (280, 308),
                ('STRING', 'NOT_EQUAL',     ) : (280, 308),
                ('RGBA',   'EQUAL',         ) : (280, 348),
                ('RGBA',   'NOT_EQUAL',     ) : (280, 348),
                ('RGBA',   'BRIGHTER',      ) : (280, 308),
                ('RGBA',   'DARKER',        ) : (280, 308),
                ('FLOAT',  'BRIGHTER',      ) : (280, 348),
                ('INT',    'BRIGHTER',      ) : (280, 308),
                ('VECTOR', 'BRIGHTER',      ) : (280, 682),
                ('STRING', 'BRIGHTER',      ) : (280, 308),
                ('FLOAT',  'DARKER',        ) : (280, 348),
                ('INT',    'DARKER',        ) : (280, 308),
                ('VECTOR', 'DARKER',        ) : (280, 682),
                ('STRING', 'DARKER',        ) : (280, 308),},},
   'FunctionNodeFloatToInt'                  : {'dimensions': (280, 210), 'param_count': 0,},
   'FunctionNodeInputBool'                   : {'dimensions': (280, 160), 'param_count': 0,},
   'FunctionNodeInputColor'                  : {'dimensions': (280, 370), 'param_count': 0,},
   'FunctionNodeInputInt'                    : {'dimensions': (280, 160), 'param_count': 0,},
   'FunctionNodeInputSpecialCharacters'      : {'dimensions': (280, 144), 'param_count': 0,},
   'FunctionNodeInputString'                 : {'dimensions': (280, 160), 'param_count': 0,},
   'FunctionNodeInputVector'                 : {'dimensions': (280, 240), 'param_count': 0,},
   'FunctionNodeRandomValue'                 : {'dimensions': (280, 346), 'param_count': 1,
           'name'    : 'data_type',
           'changes' : {
                'FLOAT_VECTOR'       : (280, 586),
                'BOOLEAN'            : (280, 298),},},
   'FunctionNodeReplaceString'               : {'dimensions': (280, 238), 'param_count': 0,},
   'FunctionNodeRotateEuler'                 : {'dimensions': (280, 428), 'param_count': 0,},
   'FunctionNodeSeparateColor'               : {'dimensions': (280, 342), 'param_count': 0,},
   'FunctionNodeSliceString'                 : {'dimensions': (280, 238), 'param_count': 0,},
   'FunctionNodeStringLength'                : {'dimensions': (280, 150), 'param_count': 0,},
   'FunctionNodeValueToString'               : {'dimensions': (280, 194), 'param_count': 0,},
   'GeometryNodeAccumulateField'             : {'dimensions': (280, 396), 'param_count': 1,
           'name'    : 'data_type',
           'changes' : {
                'INT'                : (280, 392),
                'FLOAT_VECTOR'       : (280, 516),},},
   'GeometryNodeAttributeDomainSize'         : {'dimensions': (280, 346), 'param_count': 1,
           'name'    : 'component',
           'changes' : {
                'POINTCLOUD'         : (280, 214),
                'CURVE'              : (280, 258),
                'INSTANCES'          : (280, 210),},},
   'GeometryNodeAttributeStatistic'          : {'dimensions': (280, 664), 'param_count': 1,
           'name'    : 'data_type',
           'changes' : {
                'FLOAT_VECTOR'       : (280, 656),},},
   'GeometryNodeBlurAttribute'               : {'dimensions': (280, 302), 'param_count': 1,
           'name'    : 'data_type',
           'changes' : {
                'FLOAT_COLOR'        : (280, 298),},},
   'GeometryNodeBoundBox'                    : {'dimensions': (280, 238), 'param_count': 0,},
   'GeometryNodeCaptureAttribute'            : {'dimensions': (280, 356), 'param_count': 1,
           'name'    : 'data_type',
           'changes' : {
                'INT'                : (280, 348),
                'FLOAT_VECTOR'       : (280, 476),},},
   'GeometryNodeCollectionInfo'              : {'dimensions': (280, 298), 'param_count': 0,},
   'GeometryNodeConvexHull'                  : {'dimensions': (280, 150), 'param_count': 0,},
   'GeometryNodeCornersOfFace'               : {'dimensions': (280, 282), 'param_count': 0,},
   'GeometryNodeCornersOfVertex'             : {'dimensions': (280, 282), 'param_count': 0,},
   'GeometryNodeCurveArc'                    : {'dimensions': (280, 434), 'param_count': 1,
           'name'    : 'mode',
           'changes' : {
                'POINTS'             : (280, 966),},},
   'GeometryNodeCurveEndpointSelection'      : {'dimensions': (280, 194), 'param_count': 0,},
   'GeometryNodeCurveHandleTypeSelection'    : {'dimensions': (280, 210), 'param_count': 0,},
   'GeometryNodeCurveLength'                 : {'dimensions': (280, 150), 'param_count': 0,},
   'GeometryNodeCurveOfPoint'                : {'dimensions': (280, 194), 'param_count': 0,},
   'GeometryNodeCurvePrimitiveBezierSegment' : {'dimensions': (280, 866), 'param_count': 0,},
   'GeometryNodeCurvePrimitiveCircle'        : {'dimensions': (280, 258), 'param_count': 1,
           'name'    : 'mode',
           'changes' : {
                'POINTS'             : (280, 750),},},
   'GeometryNodeCurvePrimitiveLine'          : {'dimensions': (280, 498), 'param_count': 1,
           'name'    : 'mode',
           'changes' : {
                'DIRECTION'          : (280, 538),},},
   'GeometryNodeCurvePrimitiveQuadrilateral' : {'dimensions': (280, 258), 'param_count': 1,
           'name'    : 'mode',
           'changes' : {
                'PARALLELOGRAM'      : (280, 302),
                'TRAPEZOID'          : (280, 346),
                'KITE'               : (280, 302),
                'POINTS'             : (280, 822),},},
   'GeometryNodeCurveQuadraticBezier'        : {'dimensions': (280, 642), 'param_count': 0,},
   'GeometryNodeCurveSetHandles'             : {'dimensions': (280, 304), 'param_count': 0,},
   'GeometryNodeCurveSpiral'                 : {'dimensions': (280, 370), 'param_count': 0,},
   'GeometryNodeCurveSplineType'             : {'dimensions': (280, 254), 'param_count': 0,},
   'GeometryNodeCurveStar'                   : {'dimensions': (280, 326), 'param_count': 0,},
   'GeometryNodeCurveToMesh'                 : {'dimensions': (280, 238), 'param_count': 0,},
   'GeometryNodeCurveToPoints'               : {'dimensions': (280, 390), 'param_count': 1,
           'name'    : 'mode',
           'changes' : {
                'EVALUATED'          : (280, 346),
                'LENGTH'             : (280, 386),},},
   'GeometryNodeDeformCurvesOnSurface'       : {'dimensions': (340, 150), 'param_count': 0,},
   'GeometryNodeDeleteGeometry'              : {'dimensions': (280, 304), 'param_count': 1,
           'name'    : 'domain',
           'changes' : {
                'CURVE'              : (280, 254),
                'INSTANCE'           : (280, 254),},},
   'GeometryNodeDistributePointsInVolume'    : {'dimensions': (340, 302), 'param_count': 1,
           'name'    : 'mode',
           'changes' : {
                'DENSITY_GRID'       : (340, 418),},},
   'GeometryNodeDistributePointsOnFaces'     : {'dimensions': (340, 430), 'param_count': 1,
           'name'    : 'distribute_method',
           'changes' : {
                'POISSON'            : (340, 518),},},
   'GeometryNodeDualMesh'                    : {'dimensions': (280, 194), 'param_count': 0,},
   'GeometryNodeDuplicateElements'           : {'dimensions': (280, 342), 'param_count': 0,},
   'GeometryNodeEdgePathsToCurves'           : {'dimensions': (280, 238), 'param_count': 0,},
   'GeometryNodeEdgePathsToSelection'        : {'dimensions': (300, 194), 'param_count': 0,},
   'GeometryNodeEdgesOfCorner'               : {'dimensions': (280, 194), 'param_count': 0,},
   'GeometryNodeEdgesOfVertex'               : {'dimensions': (280, 282), 'param_count': 0,},
   'GeometryNodeEdgesToFaceGroups'           : {'dimensions': (280, 150), 'param_count': 0,},
   'GeometryNodeExtrudeMesh'                 : {'dimensions': (280, 474), 'param_count': 1,
           'name'    : 'mode',
           'changes' : {
                'VERTICES'           : (280, 434),
                'EDGES'              : (280, 434),},},
   'GeometryNodeFaceOfCorner'                : {'dimensions': (280, 194), 'param_count': 0,},
   'GeometryNodeFieldAtIndex'                : {'dimensions': (280, 312), 'param_count': 1,
           'name'    : 'data_type',
           'changes' : {
                'BOOLEAN'            : (280, 304),},},
   'GeometryNodeFieldOnDomain'               : {'dimensions': (280, 268), 'param_count': 1,
           'name'    : 'data_type',
           'changes' : {
                'FLOAT_VECTOR'       : (280, 388),
                'BOOLEAN'            : (280, 260),},},
   'GeometryNodeFillCurve'                   : {'dimensions': (280, 210), 'param_count': 0,},
   'GeometryNodeFilletCurve'                 : {'dimensions': (280, 298), 'param_count': 1,
           'name'    : 'mode',
           'changes' : {
                'POLY'               : (280, 342),},},
   'GeometryNodeFlipFaces'                   : {'dimensions': (280, 194), 'param_count': 0,},
   'GeometryNodeGeometryToInstance'          : {'dimensions': (320, 150), 'param_count': 0,},
   'GeometryNodeGroup'                       : {'dimensions': (280, 100), 'param_count': 0,},
   'GeometryNodeImageInfo'                   : {'dimensions': (480, 370), 'param_count': 0,},
   'GeometryNodeImageTexture'                : {'dimensions': (480, 392), 'param_count': 0,},
   'GeometryNodeIndexOfNearest'              : {'dimensions': (280, 238), 'param_count': 0,},
   'GeometryNodeInputCurveHandlePositions'   : {'dimensions': (300, 194), 'param_count': 0,},
   'GeometryNodeInputCurveTilt'              : {'dimensions': (280, 100), 'param_count': 0,},
   'GeometryNodeInputID'                     : {'dimensions': (280, 100), 'param_count': 0,},
   'GeometryNodeInputImage'                  : {'dimensions': (480, 160), 'param_count': 0,},
   'GeometryNodeInputIndex'                  : {'dimensions': (280, 100), 'param_count': 0,},
   'GeometryNodeInputInstanceRotation'       : {'dimensions': (280, 100), 'param_count': 0,},
   'GeometryNodeInputInstanceScale'          : {'dimensions': (280, 100), 'param_count': 0,},
   'GeometryNodeInputMaterial'               : {'dimensions': (280, 160), 'param_count': 0,},
   'GeometryNodeInputMaterialIndex'          : {'dimensions': (280, 100), 'param_count': 0,},
   'GeometryNodeInputMeshEdgeAngle'          : {'dimensions': (280, 144), 'param_count': 0,},
   'GeometryNodeInputMeshEdgeNeighbors'      : {'dimensions': (280, 100), 'param_count': 0,},
   'GeometryNodeInputMeshEdgeVertices'       : {'dimensions': (280, 232), 'param_count': 0,},
   'GeometryNodeInputMeshFaceArea'           : {'dimensions': (280, 100), 'param_count': 0,},
   'GeometryNodeInputMeshFaceIsPlanar'       : {'dimensions': (280, 150), 'param_count': 0,},
   'GeometryNodeInputMeshFaceNeighbors'      : {'dimensions': (300, 144), 'param_count': 0,},
   'GeometryNodeInputMeshIsland'             : {'dimensions': (280, 144), 'param_count': 0,},
   'GeometryNodeInputMeshVertexNeighbors'    : {'dimensions': (280, 144), 'param_count': 0,},
   'GeometryNodeInputNamedAttribute'         : {'dimensions': (280, 254), 'param_count': 0,},
   'GeometryNodeInputNormal'                 : {'dimensions': (280, 100), 'param_count': 0,},
   'GeometryNodeInputPosition'               : {'dimensions': (280, 100), 'param_count': 0,},
   'GeometryNodeInputRadius'                 : {'dimensions': (280, 100), 'param_count': 0,},
   'GeometryNodeInputSceneTime'              : {'dimensions': (280, 144), 'param_count': 0,},
   'GeometryNodeInputShadeSmooth'            : {'dimensions': (280, 100), 'param_count': 0,},
   'GeometryNodeInputShortestEdgePaths'      : {'dimensions': (280, 238), 'param_count': 0,},
   'GeometryNodeInputSignedDistance'         : {'dimensions': (280, 100), 'param_count': 0,},
   'GeometryNodeInputSplineCyclic'           : {'dimensions': (280, 100), 'param_count': 0,},
   'GeometryNodeInputSplineResolution'       : {'dimensions': (280, 100), 'param_count': 0,},
   'GeometryNodeInputTangent'                : {'dimensions': (280, 100), 'param_count': 0,},
   'GeometryNodeInstanceOnPoints'            : {'dimensions': (280, 654), 'param_count': 0,},
   'GeometryNodeInstancesToPoints'           : {'dimensions': (280, 282), 'param_count': 0,},
   'GeometryNodeInterpolateCurves'           : {'dimensions': (280, 502), 'param_count': 0,},
   'GeometryNodeIsViewport'                  : {'dimensions': (280, 100), 'param_count': 0,},
   'GeometryNodeJoinGeometry'                : {'dimensions': (280, 150), 'param_count': 0,},
   'GeometryNodeMaterialSelection'           : {'dimensions': (280, 150), 'param_count': 0,},
   'GeometryNodeMeanFilterSDFVolume'         : {'dimensions': (320, 238), 'param_count': 0,},
   'GeometryNodeMergeByDistance'             : {'dimensions': (280, 298), 'param_count': 0,},
   'GeometryNodeMeshBoolean'                 : {'dimensions': (280, 386), 'param_count': 1,
           'name'    : 'operation',
           'changes' : {
                'INTERSECT'          : (280, 342),
                'UNION'              : (280, 342),},},
   'GeometryNodeMeshCircle'                  : {'dimensions': (280, 254), 'param_count': 0,},
   'GeometryNodeMeshCone'                    : {'dimensions': (280, 606), 'param_count': 1,
           'name'    : 'fill_type',
           'changes' : {
                'NONE'               : (280, 562),},},
   'GeometryNodeMeshCube'                    : {'dimensions': (280, 446), 'param_count': 0,},
   'GeometryNodeMeshCylinder'                : {'dimensions': (280, 562), 'param_count': 1,
           'name'    : 'fill_type',
           'changes' : {
                'NONE'               : (280, 518),},},
   'GeometryNodeMeshFaceSetBoundaries'       : {'dimensions': (300, 150), 'param_count': 0,},
   'GeometryNodeMeshGrid'                    : {'dimensions': (280, 326), 'param_count': 0,},
   'GeometryNodeMeshIcoSphere'               : {'dimensions': (280, 238), 'param_count': 0,},
   'GeometryNodeMeshLine'                    : {'dimensions': (280, 538), 'param_count': 1,
           'name'    : 'mode',
           'changes' : {
                'END_POINTS'         : (280, 588),},},
   'GeometryNodeMeshToCurve'                 : {'dimensions': (280, 194), 'param_count': 0,},
   'GeometryNodeMeshToPoints'                : {'dimensions': (280, 342), 'param_count': 0,},
   'GeometryNodeMeshToSDFVolume'             : {'dimensions': (360, 298), 'param_count': 0,},
   'GeometryNodeMeshToVolume'                : {'dimensions': (400, 430), 'param_count': 0,},
   'GeometryNodeMeshUVSphere'                : {'dimensions': (280, 282), 'param_count': 0,},
   'GeometryNodeObjectInfo'                  : {'dimensions': (280, 386), 'param_count': 0,},
   'GeometryNodeOffsetCornerInFace'          : {'dimensions': (280, 194), 'param_count': 0,},
   'GeometryNodeOffsetPointInCurve'          : {'dimensions': (280, 238), 'param_count': 0,},
   'GeometryNodeOffsetSDFVolume'             : {'dimensions': (280, 194), 'param_count': 0,},
   'GeometryNodePoints'                      : {'dimensions': (280, 358), 'param_count': 0,},
   'GeometryNodePointsOfCurve'               : {'dimensions': (280, 282), 'param_count': 0,},
   'GeometryNodePointsToSDFVolume'           : {'dimensions': (340, 298), 'param_count': 0,},
   'GeometryNodePointsToVertices'            : {'dimensions': (280, 194), 'param_count': 0,},
   'GeometryNodePointsToVolume'              : {'dimensions': (340, 342), 'param_count': 0,},
   'GeometryNodeProximity'                   : {'dimensions': (280, 298), 'param_count': 0,},
   'GeometryNodeRaycast'                     : {'dimensions': (300, 736), 'param_count': 1,
           'name'    : 'data_type',
           'changes' : {
                'INT'                : (300, 732),},},
   'GeometryNodeRealizeInstances'            : {'dimensions': (280, 150), 'param_count': 0,},
   'GeometryNodeRemoveAttribute'             : {'dimensions': (340, 194), 'param_count': 0,},
   'GeometryNodeReplaceMaterial'             : {'dimensions': (280, 238), 'param_count': 0,},
   'GeometryNodeResampleCurve'               : {'dimensions': (280, 302), 'param_count': 1,
           'name'    : 'mode',
           'changes' : {
                'EVALUATED'          : (280, 258),
                'LENGTH'             : (280, 298),},},
   'GeometryNodeReverseCurve'                : {'dimensions': (280, 194), 'param_count': 0,},
   'GeometryNodeRotateInstances'             : {'dimensions': (280, 566), 'param_count': 0,},
   'GeometryNodeSDFVolumeSphere'             : {'dimensions': (360, 238), 'param_count': 0,},
   'GeometryNodeSampleCurve'                 : {'dimensions': (280, 574), 'param_count': 0,},
   'GeometryNodeSampleIndex'                 : {'dimensions': (280, 402), 'param_count': 1,
           'name'    : 'data_type',
           'changes' : {
                'BOOLEAN'            : (280, 398),},},
   'GeometryNodeSampleNearest'               : {'dimensions': (280, 254), 'param_count': 0,},
   'GeometryNodeSampleNearestSurface'        : {'dimensions': (300, 302), 'param_count': 1,
           'name'    : 'data_type',
           'changes' : {
                'BOOLEAN'            : (300, 298),},},
   'GeometryNodeSampleUVSurface'             : {'dimensions': (280, 506), 'param_count': 0,},
   'GeometryNodeSampleVolume'                : {'dimensions': (280, 352), 'param_count': 1,
           'name'    : 'grid_type',
           'changes' : {
                'INT'                : (280, 348),},},
   'GeometryNodeScaleElements'               : {'dimensions': (280, 396), 'param_count': 1,
           'name'    : 'scale_mode',
           'changes' : {
                'SINGLE_AXIS'        : (280, 556),},},
   'GeometryNodeScaleInstances'              : {'dimensions': (280, 566), 'param_count': 0,},
   'GeometryNodeSelfObject'                  : {'dimensions': (280, 100), 'param_count': 0,},
   'GeometryNodeSeparateComponents'          : {'dimensions': (280, 326), 'param_count': 0,},
   'GeometryNodeSeparateGeometry'            : {'dimensions': (280, 298), 'param_count': 0,},
   'GeometryNodeSetCurveHandlePositions'     : {'dimensions': (280, 462), 'param_count': 0,},
   'GeometryNodeSetCurveNormal'              : {'dimensions': (280, 254), 'param_count': 0,},
   'GeometryNodeSetCurveRadius'              : {'dimensions': (280, 238), 'param_count': 0,},
   'GeometryNodeSetCurveTilt'                : {'dimensions': (280, 238), 'param_count': 0,},
   'GeometryNodeSetID'                       : {'dimensions': (280, 238), 'param_count': 0,},
   'GeometryNodeSetMaterial'                 : {'dimensions': (280, 238), 'param_count': 0,},
   'GeometryNodeSetMaterialIndex'            : {'dimensions': (280, 238), 'param_count': 0,},
   'GeometryNodeSetPointRadius'              : {'dimensions': (280, 238), 'param_count': 0,},
   'GeometryNodeSetPosition'                 : {'dimensions': (280, 402), 'param_count': 0,},
   'GeometryNodeSetShadeSmooth'              : {'dimensions': (280, 238), 'param_count': 0,},
   'GeometryNodeSetSplineCyclic'             : {'dimensions': (280, 238), 'param_count': 0,},
   'GeometryNodeSetSplineResolution'         : {'dimensions': (280, 238), 'param_count': 0,},
   'GeometryNodeSimulationInput'             : {'dimensions': (280,  80), 'param_count': 0,},
   'GeometryNodeSimulationOutput'            : {'dimensions': (280, 238), 'param_count': 0,},
   'GeometryNodeSplineLength'                : {'dimensions': (280, 144), 'param_count': 0,},
   'GeometryNodeSplineParameter'             : {'dimensions': (280, 188), 'param_count': 0,},
   'GeometryNodeSplitEdges'                  : {'dimensions': (280, 194), 'param_count': 0,},
   'GeometryNodeStoreNamedAttribute'         : {'dimensions': (280, 396), 'param_count': 1,
           'name'    : 'data_type',
           'changes' : {
                'INT'                : (280, 392),
                'FLOAT_VECTOR'       : (280, 516),
                'FLOAT2'             : (280, 516),},},
   'GeometryNodeStringJoin'                  : {'dimensions': (280, 194), 'param_count': 0,},
   'GeometryNodeStringToCurves'              : {'dimensions': (380, 722), 'param_count': 1,
           'name'    : 'overflow',
           'changes' : {
                'SCALE_TO_FIT'       : (380, 762),
                'TRUNCATE'           : (380, 806),},},
   'GeometryNodeSubdivideCurve'              : {'dimensions': (280, 194), 'param_count': 0,},
   'GeometryNodeSubdivideMesh'               : {'dimensions': (280, 194), 'param_count': 0,},
   'GeometryNodeSubdivisionSurface'          : {'dimensions': (300, 392), 'param_count': 0,},
   'GeometryNodeSwitch'                      : {'dimensions': (280, 306), 'param_count': 1,
           'name'    : 'input_type',
           'changes' : {
                'VECTOR'             : (280, 546),
                'IMAGE'              : (280, 298),},},
   'GeometryNodeTransform'                   : {'dimensions': (280, 642), 'param_count': 0,},
   'GeometryNodeTranslateInstances'          : {'dimensions': (280, 402), 'param_count': 0,},
   'GeometryNodeTriangulate'                 : {'dimensions': (280, 348), 'param_count': 0,},
   'GeometryNodeTrimCurve'                   : {'dimensions': (280, 346), 'param_count': 1,
           'name'    : 'mode',
           'changes' : {
                'LENGTH'             : (280, 342),},},
   'GeometryNodeUVPackIslands'               : {'dimensions': (280, 282), 'param_count': 0,},
   'GeometryNodeUVUnwrap'                    : {'dimensions': (280, 342), 'param_count': 0,},
   'GeometryNodeVertexOfCorner'              : {'dimensions': (280, 150), 'param_count': 0,},
   'GeometryNodeViewer'                      : {'dimensions': (280, 198), 'param_count': 1,
           'name'    : 'data_type',
           'changes' : {
                'BOOLEAN'            : (280, 194),},},
   'GeometryNodeVolumeCube'                  : {'dimensions': (280, 654), 'param_count': 0,},
   'GeometryNodeVolumeToMesh'                : {'dimensions': (340, 298), 'param_count': 1,
           'name'    : 'resolution_mode',
           'changes' : {
                'VOXEL_AMOUNT'       : (340, 342),
                'VOXEL_SIZE'         : (340, 342),},},
   'NodeFrame'                               : {'dimensions': (300, 200), 'param_count': 0,},
   'NodeGroupInput'                          : {'dimensions': (280, 672), 'param_count': 0,},
   'NodeGroupOutput'                         : {'dimensions': (280, 144), 'param_count': 0,},
   'NodeReroute'                             : {'dimensions': ( 16,  16), 'param_count': 0,},
   'ShaderNodeClamp'                         : {'dimensions': (280, 298), 'param_count': 0,},
   'ShaderNodeCombineRGB'                    : {'dimensions': (280, 238), 'param_count': 0,},
   'ShaderNodeCombineXYZ'                    : {'dimensions': (280, 238), 'param_count': 0,},
   'ShaderNodeFloatCurve'                    : {'dimensions': (480, 584), 'param_count': 0,},
   'ShaderNodeMapRange'                      : {'dimensions': (280, 494), 'param_count': 2,
           'names'   : ['data_type', 'interpolation_type'],
           'changes' : {
                ('FLOAT',        'LINEAR',       ) : (280, 494),
                ('FLOAT',        'STEPPED',      ) : (280, 538),
                ('FLOAT',        'SMOOTHSTEP',   ) : (280, 444),
                ('FLOAT',        'SMOOTHERSTEP', ) : (280, 444),
                ('FLOAT_VECTOR', 'LINEAR',       ) : (280, 970),
                ('FLOAT_VECTOR', 'STEPPED',      ) : (280, 1130),
                ('FLOAT_VECTOR', 'SMOOTHSTEP',   ) : (280, 920),
                ('FLOAT_VECTOR', 'SMOOTHERSTEP', ) : (280, 920),},},
   'ShaderNodeMath'                          : {'dimensions': (280, 308), 'param_count': 1,
           'name'    : 'operation',
           'changes' : {
                'MULTIPLY_ADD'       : (280, 348),
                'SQRT'               : (280, 264),
                'INVERSE_SQRT'       : (280, 264),
                'ABSOLUTE'           : (280, 264),
                'EXPONENT'           : (280, 264),
                'SIGN'               : (280, 264),
                'COMPARE'            : (280, 348),
                'SMOOTH_MIN'         : (280, 348),
                'SMOOTH_MAX'         : (280, 348),
                'ROUND'              : (280, 264),
                'FLOOR'              : (280, 264),
                'CEIL'               : (280, 264),
                'TRUNC'              : (280, 264),
                'FRACT'              : (280, 264),
                'WRAP'               : (280, 348),
                'SINE'               : (280, 264),
                'COSINE'             : (280, 264),
                'TANGENT'            : (280, 264),
                'ARCSINE'            : (280, 264),
                'ARCCOSINE'          : (280, 264),
                'ARCTANGENT'         : (280, 264),
                'SINH'               : (280, 264),
                'COSH'               : (280, 264),
                'TANH'               : (280, 264),
                'RADIANS'            : (280, 264),
                'DEGREES'            : (280, 264),},},
   'ShaderNodeMix'                           : {'dimensions': (280, 356), 'param_count': 1,
           'name'    : 'data_type',
           'changes' : {
                'VECTOR'             : (280, 646),
                'RGBA'               : (280, 448),},},
   'ShaderNodeMixRGB'                        : {'dimensions': (280, 342), 'param_count': 0,},
   'ShaderNodeRGBCurve'                      : {'dimensions': (480, 584), 'param_count': 0,},
   'ShaderNodeSeparateRGB'                   : {'dimensions': (280, 238), 'param_count': 0,},
   'ShaderNodeSeparateXYZ'                   : {'dimensions': (280, 358), 'param_count': 0,},
   'ShaderNodeTexBrick'                      : {'dimensions': (300, 780), 'param_count': 0,},
   'ShaderNodeTexChecker'                    : {'dimensions': (280, 326), 'param_count': 0,},
   'ShaderNodeTexGradient'                   : {'dimensions': (280, 254), 'param_count': 0,},
   'ShaderNodeTexMagic'                      : {'dimensions': (280, 342), 'param_count': 0,},
   'ShaderNodeTexMusgrave'                   : {'dimensions': (300, 440), 'param_count': 2,
           'names'   : ['musgrave_dimensions', 'musgrave_type'],
           'changes' : {
                ('1D', 'MULTIFRACTAL',        ) : (300, 440),
                ('1D', 'RIDGED_MULTIFRACTAL', ) : (300, 524),
                ('1D', 'HYBRID_MULTIFRACTAL', ) : (300, 524),
                ('1D', 'FBM',                 ) : (300, 440),
                ('1D', 'HETERO_TERRAIN',      ) : (300, 484),
                ('2D', 'MULTIFRACTAL',        ) : (300, 440),
                ('2D', 'RIDGED_MULTIFRACTAL', ) : (300, 524),
                ('2D', 'HYBRID_MULTIFRACTAL', ) : (300, 524),
                ('2D', 'FBM',                 ) : (300, 440),
                ('2D', 'HETERO_TERRAIN',      ) : (300, 484),
                ('3D', 'MULTIFRACTAL',        ) : (300, 440),
                ('3D', 'RIDGED_MULTIFRACTAL', ) : (300, 524),
                ('3D', 'HYBRID_MULTIFRACTAL', ) : (300, 524),
                ('3D', 'FBM',                 ) : (300, 440),
                ('3D', 'HETERO_TERRAIN',      ) : (300, 484),
                ('4D', 'MULTIFRACTAL',        ) : (300, 484),
                ('4D', 'RIDGED_MULTIFRACTAL', ) : (300, 568),
                ('4D', 'HYBRID_MULTIFRACTAL', ) : (300, 568),
                ('4D', 'FBM',                 ) : (300, 484),
                ('4D', 'HETERO_TERRAIN',      ) : (300, 528),},},
   'ShaderNodeTexNoise'                      : {'dimensions': (280, 430), 'param_count': 1,
           'name'    : 'noise_dimensions',
           'changes' : {
                '4D'                 : (280, 474),},},
   'ShaderNodeTexVoronoi'                    : {'dimensions': (280, 490), 'param_count': 3,
           'names'   : ['distance', 'feature', 'voronoi_dimensions'],
           'changes' : {
                ('EUCLIDEAN', 'F1',               '1D', ) : (280, 440),
                ('EUCLIDEAN', 'F1',               '2D', ) : (280, 490),
                ('EUCLIDEAN', 'F1',               '3D', ) : (280, 490),
                ('EUCLIDEAN', 'F1',               '4D', ) : (280, 578),
                ('EUCLIDEAN', 'F2',               '1D', ) : (280, 440),
                ('EUCLIDEAN', 'F2',               '2D', ) : (280, 490),
                ('EUCLIDEAN', 'F2',               '3D', ) : (280, 490),
                ('EUCLIDEAN', 'F2',               '4D', ) : (280, 578),
                ('EUCLIDEAN', 'SMOOTH_F1',        '1D', ) : (280, 484),
                ('EUCLIDEAN', 'SMOOTH_F1',        '2D', ) : (280, 534),
                ('EUCLIDEAN', 'SMOOTH_F1',        '3D', ) : (280, 534),
                ('EUCLIDEAN', 'SMOOTH_F1',        '4D', ) : (280, 622),
                ('EUCLIDEAN', 'DISTANCE_TO_EDGE', '1D', ) : (280, 352),
                ('EUCLIDEAN', 'DISTANCE_TO_EDGE', '2D', ) : (280, 352),
                ('EUCLIDEAN', 'DISTANCE_TO_EDGE', '3D', ) : (280, 352),
                ('EUCLIDEAN', 'DISTANCE_TO_EDGE', '4D', ) : (280, 396),
                ('EUCLIDEAN', 'N_SPHERE_RADIUS',  '1D', ) : (280, 348),
                ('EUCLIDEAN', 'N_SPHERE_RADIUS',  '2D', ) : (280, 348),
                ('EUCLIDEAN', 'N_SPHERE_RADIUS',  '3D', ) : (280, 348),
                ('EUCLIDEAN', 'N_SPHERE_RADIUS',  '4D', ) : (280, 392),
                ('MANHATTAN', 'F1',               '1D', ) : (280, 440),
                ('MANHATTAN', 'F1',               '2D', ) : (280, 490),
                ('MANHATTAN', 'F1',               '3D', ) : (280, 490),
                ('MANHATTAN', 'F1',               '4D', ) : (280, 578),
                ('MANHATTAN', 'F2',               '1D', ) : (280, 440),
                ('MANHATTAN', 'F2',               '2D', ) : (280, 490),
                ('MANHATTAN', 'F2',               '3D', ) : (280, 490),
                ('MANHATTAN', 'F2',               '4D', ) : (280, 578),
                ('MANHATTAN', 'SMOOTH_F1',        '1D', ) : (280, 484),
                ('MANHATTAN', 'SMOOTH_F1',        '2D', ) : (280, 534),
                ('MANHATTAN', 'SMOOTH_F1',        '3D', ) : (280, 534),
                ('MANHATTAN', 'SMOOTH_F1',        '4D', ) : (280, 622),
                ('MANHATTAN', 'DISTANCE_TO_EDGE', '1D', ) : (280, 352),
                ('MANHATTAN', 'DISTANCE_TO_EDGE', '2D', ) : (280, 352),
                ('MANHATTAN', 'DISTANCE_TO_EDGE', '3D', ) : (280, 352),
                ('MANHATTAN', 'DISTANCE_TO_EDGE', '4D', ) : (280, 396),
                ('MANHATTAN', 'N_SPHERE_RADIUS',  '1D', ) : (280, 348),
                ('MANHATTAN', 'N_SPHERE_RADIUS',  '2D', ) : (280, 348),
                ('MANHATTAN', 'N_SPHERE_RADIUS',  '3D', ) : (280, 348),
                ('MANHATTAN', 'N_SPHERE_RADIUS',  '4D', ) : (280, 392),
                ('CHEBYCHEV', 'F1',               '1D', ) : (280, 440),
                ('CHEBYCHEV', 'F1',               '2D', ) : (280, 490),
                ('CHEBYCHEV', 'F1',               '3D', ) : (280, 490),
                ('CHEBYCHEV', 'F1',               '4D', ) : (280, 578),
                ('CHEBYCHEV', 'F2',               '1D', ) : (280, 440),
                ('CHEBYCHEV', 'F2',               '2D', ) : (280, 490),
                ('CHEBYCHEV', 'F2',               '3D', ) : (280, 490),
                ('CHEBYCHEV', 'F2',               '4D', ) : (280, 578),
                ('CHEBYCHEV', 'SMOOTH_F1',        '1D', ) : (280, 484),
                ('CHEBYCHEV', 'SMOOTH_F1',        '2D', ) : (280, 534),
                ('CHEBYCHEV', 'SMOOTH_F1',        '3D', ) : (280, 534),
                ('CHEBYCHEV', 'SMOOTH_F1',        '4D', ) : (280, 622),
                ('CHEBYCHEV', 'DISTANCE_TO_EDGE', '1D', ) : (280, 352),
                ('CHEBYCHEV', 'DISTANCE_TO_EDGE', '2D', ) : (280, 352),
                ('CHEBYCHEV', 'DISTANCE_TO_EDGE', '3D', ) : (280, 352),
                ('CHEBYCHEV', 'DISTANCE_TO_EDGE', '4D', ) : (280, 396),
                ('CHEBYCHEV', 'N_SPHERE_RADIUS',  '1D', ) : (280, 348),
                ('CHEBYCHEV', 'N_SPHERE_RADIUS',  '2D', ) : (280, 348),
                ('CHEBYCHEV', 'N_SPHERE_RADIUS',  '3D', ) : (280, 348),
                ('CHEBYCHEV', 'N_SPHERE_RADIUS',  '4D', ) : (280, 392),
                ('MINKOWSKI', 'F1',               '1D', ) : (280, 440),
                ('MINKOWSKI', 'F1',               '2D', ) : (280, 534),
                ('MINKOWSKI', 'F1',               '3D', ) : (280, 534),
                ('MINKOWSKI', 'F1',               '4D', ) : (280, 622),
                ('MINKOWSKI', 'F2',               '1D', ) : (280, 440),
                ('MINKOWSKI', 'F2',               '2D', ) : (280, 534),
                ('MINKOWSKI', 'F2',               '3D', ) : (280, 534),
                ('MINKOWSKI', 'F2',               '4D', ) : (280, 622),
                ('MINKOWSKI', 'SMOOTH_F1',        '1D', ) : (280, 484),
                ('MINKOWSKI', 'SMOOTH_F1',        '2D', ) : (280, 578),
                ('MINKOWSKI', 'SMOOTH_F1',        '3D', ) : (280, 578),
                ('MINKOWSKI', 'SMOOTH_F1',        '4D', ) : (280, 666),
                ('MINKOWSKI', 'DISTANCE_TO_EDGE', '1D', ) : (280, 352),
                ('MINKOWSKI', 'DISTANCE_TO_EDGE', '2D', ) : (280, 352),
                ('MINKOWSKI', 'DISTANCE_TO_EDGE', '3D', ) : (280, 352),
                ('MINKOWSKI', 'DISTANCE_TO_EDGE', '4D', ) : (280, 396),
                ('MINKOWSKI', 'N_SPHERE_RADIUS',  '1D', ) : (280, 348),
                ('MINKOWSKI', 'N_SPHERE_RADIUS',  '2D', ) : (280, 348),
                ('MINKOWSKI', 'N_SPHERE_RADIUS',  '3D', ) : (280, 348),
                ('MINKOWSKI', 'N_SPHERE_RADIUS',  '4D', ) : (280, 392),},},
   'ShaderNodeTexWave'                       : {'dimensions': (300, 618), 'param_count': 0,},
   'ShaderNodeTexWhiteNoise'                 : {'dimensions': (280, 258), 'param_count': 1,
           'name'    : 'noise_dimensions',
           'changes' : {
                '1D'                 : (280, 254),
                '4D'                 : (280, 298),},},
   'ShaderNodeValToRGB'                      : {'dimensions': (480, 424), 'param_count': 0,},
   'ShaderNodeValue'                         : {'dimensions': (280, 160), 'param_count': 0,},
   'ShaderNodeVectorCurve'                   : {'dimensions': (480, 704), 'param_count': 0,},
   'ShaderNodeVectorMath'                    : {'dimensions': (280, 502), 'param_count': 1,
           'name'    : 'operation',
           'changes' : {
                'MULTIPLY_ADD'       : (280, 666),
                'REFRACT'            : (280, 542),
                'FACEFORWARD'        : (280, 666),
                'DOT_PRODUCT'        : (280, 498),
                'DISTANCE'           : (280, 498),
                'LENGTH'             : (280, 334),
                'SCALE'              : (280, 378),
                'NORMALIZE'          : (280, 338),
                'ABSOLUTE'           : (280, 338),
                'FLOOR'              : (280, 338),
                'CEIL'               : (280, 338),
                'FRACTION'           : (280, 338),
                'WRAP'               : (280, 666),
                'SINE'               : (280, 338),
                'COSINE'             : (280, 338),
                'TANGENT'            : (280, 338),},},
   'ShaderNodeVectorRotate'                  : {'dimensions': (280, 636), 'param_count': 1,
           'name'    : 'rotation_type',
           'changes' : {
                'X_AXIS'             : (280, 472),
                'Y_AXIS'             : (280, 472),
                'Z_AXIS'             : (280, 472),
                'EULER_XYZ'          : (280, 588),},},   
}


for blid in ['GeometryNodeSimulationInput', 'GeometryNodeSimulationOutput']:
    dim = list(NODE_DIMS[blid]['dimensions'])
    dim[0] += 50
    dim[1] += 300
    NODE_DIMS[blid]['dimensions'] = list(dim)



# ====================================================================================================
# Build the node dimensions by trying all the parameter configurations
#
# Must be run with an open "Geometry Nodes Editor"

def gen_node_dims():
    
    print('-'*80)
    print("Nodes dimensions dictionary builder.")
    print()
    print("The dictionary is used by the arrange algorithm to have the true nodes dimensions.")
    print("This function calls a UI redraw and requires that a 'Geometry Nodes Editor' be open")
    print("with the default 'Geometry Nodes' geometry.")
    print()

    STD_ATTRS = [
       '__doc__', '__module__', '__slots__', 'bl_description', 'bl_height_default', 'bl_height_max',
       'bl_height_min', 'bl_icon', 'bl_idname', 'bl_label', 'bl_rna', 'bl_static_type',
       'bl_width_default', 'bl_width_max', 'bl_width_min', 'color', 'dimensions', 'draw_buttons',
       'draw_buttons_ext', 'height', 'hide', 'input_template', 'inputs', 'internal_links',
       'is_registered_node_type', 'label', 'location', 'mute', 'name', 'output_template', 'outputs',
       'parent', 'poll', 'poll_instance', 'rna_type', 'select', 'show_options', 'show_preview',
       'show_texture', 'socket_value_update', 'type', 'update', 'use_clamp', 'use_custom_color',
       'width', 'width_hidden']
       
    tree_name = "Geometry Nodes"
    tree = bpy.data.node_groups[tree_name]
    tree.nodes.clear()

    # ----------------------------------------------------------------------------------------------------
    # Get all the possible values of an enum param

    def get_node_enums(node, param_name):
        
        value  = getattr(node, param_name)
        values = None
        if isinstance(value, str):
            try:
                setattr(node, param_name, "TOTO")
            except TypeError as e:
                values = eval(str(e)[54:])
                
        return values

    # ----------------------------------------------------------------------------------------------------
    # Set all the possible values of a node parameter et check if the dimensions change
    # Return the values for which the dimensions differ from default

    def get_changed_dims(node, param_name, values):
        
        default  = getattr(node, param_name)
        def_dims = tuple(node.dimensions)
        
        changes = {}
        
        for value in values:

            setattr(node, param_name, value)
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            
            dims = tuple(node.dimensions)
            if dims != def_dims:
                changes[value] = dims

        setattr(node, param_name, value)
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
                
        return changes

    # ----------------------------------------------------------------------------------------------------
    # Get all the combinations

    def get_combination_dims(node, param_names):
        
        inds = {name: index for index, name in enumerate(param_names)}
        
        combs = {}
        for param_name in param_names:
            
            default = getattr(node, param_name)
            values  = get_node_enums(node, param_name)
            
            rems   = [pname for pname in param_names if pname != param_name]
            worder = [param_name]
            worder.extend(rems)
            
            for value in values:
                setattr(node, param_name, value)
                
                if rems:
                    sub = get_combination_dims(node, rems)
                    for k, v in sub.items():
                        
                        ukey = (value,) + k
                        okey = [None] * len(param_names)
                        for pname, pv in zip(worder, ukey):
                            okey[inds[pname]] = pv
                            
                        key = tuple(okey)
                        if not key in combs:
                            combs[key] = v
                        
                        #combs[(value,) + k] = v
                    
                else:
                    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
                    combs[(value,)] = tuple(node.dimensions)
                    
            setattr(node, param_name, default)
            
        return combs

    # ----------------------------------------------------------------------------------------------------
    # Get the attributes and default dimensions
    #
    # nodes is a dict indexed by bl_idname
    # the values are a dict with a list two entries:
    # 'dimensions' (w, h) : the default dimensions of the node
    # 'changes'    dict (key: attr_name, value: (w, h))
        
    nodes = {}
    count = 0

    for tp in dir(bpy.types):
        
        try:
            node = tree.nodes.new(type=tp)
        except:
            continue
        
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
        nodes[node.bl_idname] = {'dimensions': tuple(node.dimensions)}
        
        params = {}
        for attr in dir(node):
            
            if attr in STD_ATTRS:
                continue
            
            value  = getattr(node, attr)
            values = None
            if isinstance(value, str):
                try:
                    setattr(node, attr, "TOTO")
                except TypeError as e:
                    values = eval(str(e)[54:])
                    
            # ----- Store the dimensions if changed
            
            if values is not None:
                ch_dims = get_changed_dims(node, attr, values)
                if ch_dims:
                    params[attr] = ch_dims

        nodes[node.bl_idname]['param_count'] = len(params)
        
        if len(params) == 1:
            name = list(params.keys())[0]
            nodes[node.bl_idname]['name']    = name
            nodes[node.bl_idname]['changes'] = params[name]
            
        elif len(params) > 1:
            param_names = list(params.keys())
            combs = get_combination_dims(node, param_names)

            nodes[node.bl_idname]['names']   = param_names
            nodes[node.bl_idname]['changes'] = combs
            
        tree.nodes.remove(node)
        
    # ----------------------------------------------------------------------------------------------------
    # Customized pretty print

    for blid, ndims in nodes.items():
        
        def sdim(d):
            try:
                return f"({int(d[0]):3d}, {int(d[1]):3d})"
            except:
                return "???" + str(d) + "???"
            
        sblid  = f"'{blid}'"
        pcount = ndims['param_count'] 
        s = f"   {sblid:42s}: " + "{" + f"'dimensions': {sdim(ndims['dimensions'])}, 'param_count': {pcount},"
        
        if pcount == 1:
            name    = ndims['name']
            changes = ndims['changes']

            s += f"\n{' ':10s} 'name'    : '{name}',"  
            s += f"\n{' ':10s} 'changes' : " + "{"
            for k, v in changes.items():
                sk = f"'{k}'"
                s += f"\n{' ':15s} {sk:20s} : {sdim(v)},"
            s += "}," 
            
        elif pcount > 1:
            names   = ndims['names']
            changes = ndims['changes']

            s += f"\n{' ':10s} 'names'   : {names},"  
            s += f"\n{' ':10s} 'changes' : " + "{"
            
            lname = [0] * len(names)
            for k in changes:
                for i, name in enumerate(k):
                    lname[i] = max(lname[i], len(name))
            sks = []
            for k in changes:
                sk = "("
                for i, name in enumerate(k):
                    sk += f"'{name}',{' '*(lname[i]-len(name)+1)}"
                sks.append(sk + ")")

            for sk, v in zip(sks, changes.values()):
                #s += f"\n{' ':15s} {str(k):50s} : {sdim(v)},"
                s += f"\n{' ':15s} {sk} : {sdim(v)},"
            s += "}," 
        
        s += "},"
        
        print(s)
        
# ====================================================================================================
# Custom group dimensions

def group_dim(node):
    
    dims = NODE_DIMS.get(node.bl_idname)
    if dims is None:
        #print(f"WARNING geonodes arrange: the node '{node.bl_idname}' is not referenced in NODE_DIMS")
        return [200, 200]
    
    nd = list(dims['dimensions'])
    
    # ----- Output sockets
    
    h = 116 + 44*len(node.outputs) if node.outputs else 100
        
    # Input sockets
    
    if node.inputs:

        h += 6
        
        for sock in node.inputs:
            h += 44
            if sock.bl_idname[:16] == 'NodeSocketVector' and not bool(sock.links):
                h += 120
                
    if node.bl_idname == 'GeometryNodeGroup':
        nd[0] = 474
        
    nd[1] = h
            
    return [nd[0]/2, nd[1]/2]
    

# ====================================================================================================
# Frame dimensions

def frame_dim(tree, frame):
    
    first_node = True
    for node in tree.nodes:
        if node.parent != frame:
            continue
        
        ndim = node_dim(node)
        
        w0 = 2*node.location[0]
        w1 = 2*node.location[0] + ndim[0]
        h0 = 2*node.location[1] - ndim[1]
        h1 = 2*node.location[1]

        if first_node:
            W0, W1, H0, H1 = w0, w1, h0, h1
            first_node = False
            
        else:
            W0 = min(W0, w0)
            W1 = max(W1, w1)
            H0 = min(H0, h0)
            H1 = max(H1, h1)
            
    return ((W1 - W0) + 120, (H1 - H0) + 120)

# ====================================================================================================
# Node dimensions

def node_dim(node, tree=None):
    
    if node.bl_idname in ['GeometryNodeGroup', 'NodeGroupInput', 'NodeGroupOutput']:
        return group_dim(node)
    
    if node.bl_idname == 'FRAME':
        return frame_dim(tree, frame)
    
    # ----- General case
    
    ddims = NODE_DIMS.get(node.bl_idname)
    if ddims is None:
        #print(f"WARNING geonodes arrange: the node '{node.bl_idname}' is not referenced in NODE_DIMS")
        return [200, 200]

    nd    = list(ddims['dimensions'])
    
    pcount = ddims['param_count']
    
    # ----- One changing attribute
    
    if pcount == 1:
        name = ddims['name']
        value = getattr(node, name)
        ch_nd = ddims['changes'].get(value)
        if ch_nd is not None:
            nd = list(ch_nd)

    # -----More than one changing attribute
    
    elif pcount > 1:
        
        names = ddims['names']
        key = ()
        for name in ddims['names']:
            key += (getattr(node, name),)
            
        if key not in ddims['changes']:
            pprint(ddims)
            raise RuntimeError(f"node_dim Error: node '{node.name}', key {key} not found.")
        
        nd = list(ddims['changes'][key])
        
    # ----- Plugged vectors lower the height
    
    if not node.bl_idname in ['NodeReroute']:
        for sock in node.inputs:
            if sock.enabled and (not sock.hide_value) and bool(sock.links) and sock.bl_idname[:16] == 'NodeSocketVector':
                nd[1] -= 120
                
    
    if node.bl_idname == 'NodeFrame':
        return [nd[0]*2, nd[1]*2]
    else:
        return [nd[0]/2, nd[1]/2]

    return nd    
        
# ====================================================================================================
# Delete the frames

def delete_frames(tree):
    nodes = list(tree.nodes)
    for node in nodes:
        if node.bl_idname == 'NodeFrame':
            tree.nodes.remove(node)
            
# ====================================================================================================
# Delete the reroute

def delete_reroute(tree):
    
    # ----- A reroute node is one to many
    # One reroute gives a list of to_sockets
    # The from_socket and the to_sockets can also be reroute nodes
    # Recursive call will allow to manage that 
    
    def get_from_socket(reroute):
        
        if not reroute.inputs[0].links:
            return None
        
        link = reroute.inputs[0].links[0]
        from_node = link.from_node
        if from_node.bl_idname == 'NodeReroute':
            return get_from_socket(from_node)
        else:
            return link.from_socket
                
    def get_to_sockets(reroute):
        
        to_sockets = []
        if not reroute.outputs[0].links:
            return to_sockets
        
        for link in reroute.outputs[0].links:
            if link.to_node.bl_idname == 'NodeReroute':
                to_sockets.extend(get_to_sockets(link.to_node))
            else:
                to_sockets.append(link.to_socket)
        
        return to_sockets

    links = []
    dels  = []
    count = 0
    
    reroutes = [node for node in tree.nodes if node.bl_idname == 'NodeReroute']
    
    for node in tree.nodes:
        if node.bl_idname == 'NodeReroute':
            dels.append(node)
            
            from_socket = get_from_socket(node)
            if from_socket is None:
                continue
            
            for to_socket in get_to_sockets(node):
                links.append((from_socket, to_socket))

            count += 1
            
    for node in dels:
        tree.nodes.remove(node)
        
    for from_socket, to_socket in links:
        tree.links.new(from_socket, to_socket)
            
    print(f"Removed: {count} reroute nodes.")
    
    
# ====================================================================================================
# Create reroute nodes as entry and exit points in frames

def is_in_frame(node, frame):
    nd = node
    for _ in range(10):
        if nd.parent is None:
            return False
        
        if nd.parent == frame:
            return True
        
        nd = nd.parent
        
    return False # Should never append


def frame_inputs(tree):
    
    for frame in tree.nodes:
        
        if frame.bl_idname != 'NodeFrame':
            continue
        
        # ----- All the nodes within the frames
        
        nodes = [node for node in tree.nodes if is_in_frame(node, frame)]
        if not nodes:
            continue
        
        # ----- All the links in the frame
        
        links = [link for link in tree.links if not is_in_frame(link.from_node, frame) and is_in_frame(link.to_node, frame)]
        
        # ----- Reroute the links
        
        reroutes = {}
        for link in links:
            from_socket = link.from_socket
            to_sockets = reroutes.get(from_socket)
            if to_sockets is None:
                to_sockets = []
                reroutes[from_socket] = to_sockets
                
            to_sockets.append(link.to_socket)
            
        # ----- Delete the links
        
        for link in links:
            tree.links.remove(link)
            
        # ----- Create the reroutes
        
        x_sepa  = 30
        y_sepa  = 50
        
        x = -frame.dimensions[0]/2 - x_sepa
        y = -frame.dimensions[1]/2 + y_sepa
        
        
        for from_socket, to_sockets in reroutes.items():
            
            node = tree.nodes.new(type='NodeReroute')
            node.parent = frame
            node.label = f"[{from_socket.node.label}].{from_socket.name}"
            
            tree.links.new(from_socket, node.inputs[0])
            
            for to_socket in to_sockets:
                tree.links.new(node.outputs[0], to_socket)

            node.location = (x, y)
            y += y_sepa
            
def frame_outputs(tree):
    
    for frame in tree.nodes:
        
        if frame.bl_idname != 'NodeFrame':
            continue
        
        # ----- All the nodes within the frames
        
        nodes = [node for node in tree.nodes if is_in_frame(node, frame)]
        if not nodes:
            continue
        
        # ----- All the links in the frame
        
        links = [link for link in tree.links if is_in_frame(link.from_node, frame) and not is_in_frame(link.to_node, frame)]
        
        # ----- Reroute the links
        
        reroutes = {}
        for link in links:
            from_socket = link.from_socket
            to_sockets = reroutes.get(from_socket)
            if to_sockets is None:
                to_sockets = []
                reroutes[from_socket] = to_sockets
                
            to_sockets.append(link.to_socket)
            
        # ----- Delete the links
        
        for link in links:
            tree.links.remove(link)
            
        # ----- Create the reroutes
        
        x_sepa  = 30
        y_sepa  = 50
        
        x = 2*x_sepa
        y = y_sepa
        
        for from_socket, to_sockets in reroutes.items():
            
            node = tree.nodes.new(type='NodeReroute')
            node.parent = frame
            node.label = f"[{from_socket.node.label}].{from_socket.name}"
            
            tree.links.new(from_socket, node.inputs[0])
            
            for to_socket in to_sockets:
                tree.links.new(node.outputs[0], to_socket)

            node.location = (x, y)
            y -= y_sepa            
            
# ====================================================================================================
# Delete single nodes

def delete_single_nodes(tree):
    
    nodes = []
    for node in tree.nodes:

        if node.bl_idname in ['NodeFrame']:
            continue
        
        single = True
        
        for socket in node.inputs:
            if len(socket.links):
                single = False
                break
            
        for socket in node.outputs:
            if len(socket.links):
                single = False
                break
            
        if single:
            nodes.append(node)
        
    for node in nodes:
        if node.bl_idname in ['NodeGroupInput']:
            tree.nodes.remove(node)
        #node.use_custom_color = True
        #node.color = Color((1, 0, 0))

        
    return len(nodes)

# ====================================================================================================
# Hierachical boxes

class Box:
    
    BOXES = []
    
    def __init__(self, tree, node):
        
        super().__init__()
        
        self.index = len(Box.BOXES)
        Box.BOXES.append(self)
        
        self.tree     = tree
        self.node     = node
        self.frame    = None
        
        self.is_tree  = False
        self.is_frame = False
        
        # ----- Dimensions
        
        self._dims   = [0, 0]
        self._margin = [0, 0]
        
        self.single_left = None
        
        if self.node is not None:
            
            if self.node.bl_idname == 'NodeFrame':
                pass
            
            elif self.node.bl_idname == 'NodeReroute':
                self._dims   = [ 0, -30]
                self._margin = [ 0, -15]
                
            else:
                self._dims = node_dim(node, self.tree)
                
            # ----- Single left
        
            self.single_left = True
            for socket in node.inputs:
                if len(socket.links):
                    self.single_left = False
                    break
                
            if self.single_left:
                count = 0
                for socket in node.outputs:
                    if len(socket.links):
                        count += len(socket.links)
                        fed_node = socket.links[0].to_node
                    
            self.single_left = self.single_left and (count == 1)
            if node.bl_idname in ['NodeGroupInput', 'GeometryNodeSimulationInput']:
                self.single_left = False
            
            # ----- Ensure single left is in the same frame
            
            if self.single_left:
                self.node.parent = fed_node.parent
        
        # ----- Links
        
        self.in_siblings = {}
        
        # ----- Location
        
        self.located = False
        
        self.row = 0
        self.col = 0
        self.infinite_loop = False
        
    # ---------------------------------------------------------------------------
    # str
    
    @property
    def name(self):
        return f"{self.index} " + self.node.name
    
        return f"{self.index} " + (self.tree.name if self.node is None else self.node.name)
    
    @property
    def slinks(self):
        return f"\n   ins:  {[Box.BOXES[b].name for b in self.in_siblings]}"
    
    def __str__(self):
        return f"<Box '{self.name}'>"

    def __repr__(self):
        return f"<Box {self.name}" + self.slinks + "\n>"

       
    # ---------------------------------------------------------------------------
    # Access to the box of a node
    
    def node_box(self, node):
        for i, nd in enumerate(self.tree.nodes):
            if nd == node:
                return Box.BOXES[i]
        raise RuntimeError(f"Algo error: node '{node}' strangely boxed.")
        
    # ---------------------------------------------------------------------------
    # Boxes from indices
    
    @staticmethod
    def from_index(index):
        if isinstance(index, int):
            return Box.BOXES[index]
        else:
            return [Box.from_index(i) for i in index]

    # ---------------------------------------------------------------------------
    # Top frame
    
    @property
    def top(self):
        return self.frame.top

    # ---------------------------------------------------------------------------
    # Hierarchical depth
        
    @property
    def depth(self):
        return self.frame.depth + 1
        
    # ---------------------------------------------------------------------------
    # Location
    #
    # Margin mechanism is used by frames
    
    @property
    def margin(self):
        return Vector(self._margin)
    
    @property
    def location(self):
        return list(self.node.location + self.margin)
    
    @location.setter
    def location(self, value):
        self.node.location = Vector(value) - self.margin
    
    @property
    def x(self):
        return self.location[0]
    
    @x.setter
    def x(self, value):
        self.location = (value, self.y)
        
    @property
    def y(self):
        return self.location[1]
    
    @y.setter
    def y(self, value):
        self.location = (self.x, value)
        
    # ---------------------------------------------------------------------------
    # Width and height
    
    @property
    def dims(self):
        return self._dims
        
    @property
    def w(self):
        return self.dims[0]
        
    @property
    def h(self):
        return self.dims[1]
        
    # ---------------------------------------------------------------------------
    # Sort the in_siblings links
    # Used by frames
    
    def sorted_in_siblings(self):
        return list(self.in_siblings.values())

    # ---------------------------------------------------------------------------
    # Sibling test
    
    def is_sibling(self, other):
        
        if self.node is None or other.node is None:
            return False
        
        if self.node.parent is None:
            return other.node.parent is None
        
        elif other.node.parent is None:
            return False
        
        else:
            return self.node.parent == other.node.parent
        
    # ---------------------------------------------------------------------------
    # Sibling ancestor
    # Return self or one ancestor so that the parent is the one passed in param
    
    def common_ancestor(self, other):
        
        if self == other:
            raise RuntimeError("common_ancestor: This is a stupid request!")
        
        box0 = self
        box1 = other
        
        depth0 = box0.depth
        depth1 = box1.depth
        depth  = depth0
        
        if depth0 > depth1:
            for _ in range(depth0 - depth1):
                box0 = box0.frame
            depth = depth1
                
        elif depth1 > depth0:
            for _ in range(depth1 - depth0):
                box1 = box1.frame
            depth = depth0
                
        # ----- Same depth now
        
        if box0 == box1:
            raise RuntimeError("common_ancestor: No common ancestor when one is the ancestor of the other")
        
        for _ in range(depth):
            
            if box0.frame is None or box1.frame is None:
                raise RuntimeError("common_ancestor: I can't believe this could happen!")
            
            if box0.is_sibling(box1):
                return box0.frame, box0, box1
            
            box0 = box0.frame
            box1 = box1.frame
            
        raise RuntimeError("common_ancestor: Normally tjhs should never happen")
    
    # ---------------------------------------------------------------------------
    # Compute the columns
    
    def update_column(self, col):
        
        if self.infinite_loop:
            return
        
        if self.col is None or col > self.col:
            
            self.col = col
            
            self.infinite_loop = True
            
            for box in Box.from_index(list(self.in_siblings.keys())):
                box.update_column(self.col + 1)
                    
            self.infinite_loop = False
            
        # ----- Put the feeding single left nodes in the same column
        
        for b in self.in_siblings:
            box = Box.BOXES[b]
            if box.single_left:
                box.col = self.col
        
        
            
    # ---------------------------------------------------------------------------
    # Is a reroute node
    
    @property
    def is_reroute(self):
        return False if self.node is None else self.node.bl_idname == 'NodeReroute'
    
    @property
    def is_input_reroute(self):
        
        if self.frame is None:
            return False
        
        if self.node.bl_idname != 'NodeReroute':
            return False
        
        return len(self.in_siblings) == 0

    @property    
    def is_output_reroute(self):
        
        if self.frame is None:
            return False
        
        if self.node.bl_idname != 'NodeReroute':
            return False
        
        return len(self.in_siblings) != 0
            
            
# ====================================================================================================
# A link between two boxes

class BoxLink(list):
    def __init__(self, top, link, nodes=None):
        
        super().__init__()
        
        self.append(link)
        
        self.top = top
        
        if nodes is None:
            nodes = list(top.tree.nodes)
            
        self.key = (nodes.index(link.from_node), nodes.index(link.to_node))
        
        self.box_from = Box.BOXES[self.key[0]]
        self.box_to   = Box.BOXES[self.key[1]]
        
        self.frame, self.sib_from, self.sib_to = self.box_from.common_ancestor(self.box_to)
        
        # ----- orders
        
        for i, sock in enumerate(link.to_node.inputs):
            if sock == link.to_socket:
                self.box_to_socket_index = i
                break
            
        for i, sock in enumerate(link.from_node.outputs):
            if sock == link.from_socket:
                self.box_from_socket_index = i
                break
            
    def __str__(self):
        return f"<BoxLink {self.key}, {len(self)} link(s), siblings=({self.sib_from.index}, {self.sib_to.index})"
    
        
        
# ====================================================================================================
# A frame

class Frame(Box):
    
    def __init__(self, tree, node):
        
        super().__init__(tree, node)
        self.sized  = False
        
        self.boxes = []
        
        self.is_tree  = node is None
        self.is_frame = True
        
        self.cols = None
        
    # ===========================================================================
    # Some debug utilities
    
    def track_box(self, x0, y0, x1, y1, parent=True):

        rr0 = self.tree.nodes.new("NodeReroute")
        if parent:
            rr0.parent = self.node
        rr0.location = (x0, y0)
        
        rr1 = self.tree.nodes.new("NodeReroute")
        if parent:
            rr1.parent = self.node
        rr1.location = (x1, y1)
        
        self.tree.links.new(rr0.outputs[0], rr1.inputs[0])
        
    def track_boxes(self):
        
        for box in self.boxes:
            
            if box.node.bl_idname == 'NodeReroute':
                continue
            
            self.track_box(box.x, box.y, box.x + box.w, box.y - box.h)
    
    def track_inner_frame(self):
        
        x0, y0, x1, y1 = self.inner_box
        self.track_box(x0, y0, x1, y1)
        
        rr = self.tree.nodes.new("NodeReroute")
        rr.parent = self.node
        rr.location = (0, 0)
        
    def track_frame(self):
        
        self.track_box(self.x, self.y, self.x + self.w, self.y - self.h, parent=False)
        
    # ===========================================================================
    # str
        
    @property
    def name(self):
        return self.tree.name if self.node is None else self.node.label
    
    def __str__(self):
        return f"<Tree {self.name}>" if self.node is None else f"<Frame {self.name}>"

    def __repr__(self):
        
        s = str(self) + self.slinks + "\n"
        for child in self.boxes:
            sc = repr(child).split("\n")
            s += "\n   " + "\n   ".join(sc)
            
        return s
    
    # ---------------------------------------------------------------------------
    # Sort the in_siblings links
    
    def sorted_in_siblings(self):
        links = sorted(self.in_siblings.values(), key = lambda bl: -bl.box_to.y)
        return links
    
    # ---------------------------------------------------------------------------
    # The frame is drawn as a rectangle around its boxes (plus a certain margin)
    # The frame origin can be outside the drawn rectangle
    # In the algorithm, we need to locate a frame in the same way we locate a node:
    # - location at the top left corner
    #
    # The inner_box return the coordinates of the box including
    # exactly the child boxes: x0, y0, x1, y1
    #
    # The inner box is used to compute:
    # - the frame dimensions : (x1 - x0, y1 - y0)
    # - the offset location  : (x0, y0) (plus the margin)
    
    @property
    def inner_box(self):

        if self.boxes:
            
            x0 = None
            for box in self.boxes:
                
                if x0 is None:
                    x0 = box.x
                    y0 = box.y
                    x1 = box.x + box.w
                    y1 = box.y + box.h
                else:
                    x0 = min(x0, box.x)
                    y0 = max(y0, box.y)
                    x1 = max(x1, box.x + box.w)
                    y1 = min(y1, box.y - box.h)
                    
            return x0, y0, x1, y1
            
        else:
            return 0, 0, 0, 0
        
    # ---------------------------------------------------------------------------
    # Frame margin
    
    @property
    def margin(self):
        if self.sized:
            return self._margin
        
        x0, y0, _, _ = self.inner_box
        
        return Vector((x0 - 30, -y0 + 30))

    # ---------------------------------------------------------------------------
    # Frame dimensions

    @property
    def dims(self):
        
        if self.sized:
            return self._dims
        
        x0, y0, x1, y1 = self.inner_box
        
        return (x1 - x0 + 60, y0 - y1 + 60)
        
        
        if self.boxes:
            
            first_node = True
            for box in self.boxes:
                
                w0 = 2*box.x
                w1 = 2*box.x + box.w
                h0 = 2*box.y - box.h
                h1 = 2*box.y
        
                if first_node:
                    W0, W1, H0, H1 = w0, w1, h0, h1
                    first_node = False
                    
                else:
                    W0 = min(W0, w0)
                    W1 = max(W1, w1)
                    H0 = min(H0, h0)
                    H1 = max(H1, h1)
                    
            return [(W1 - W0)/2 + 120, (H1 - H0)/2 + 120]
            
        else:
            
            return [120, 120]
    
    # ---------------------------------------------------------------------------
    # Top frame
    
    @property
    def top(self):
        return self if self.node is None else self.frame.top

    # ---------------------------------------------------------------------------
    # Hierarchical depth
        
    @property
    def depth(self):
        return 0 if self.node is None else self.frame.depth + 1
    
    # ---------------------------------------------------------------------------
    # All children
    # Return children ids
    
    @property
    def all_children(self):
        children = []
        for child in self.boxes:
            children.append(child.index)
            if child.is_frame:
                children += child.all_children
            
        return children
    
    # ---------------------------------------------------------------------------
    # Build the frame
    
    def build(self):
        
        for box in Box.BOXES:
            
            # ----- Get the nodes belonging to the frame
            
            if box == self or box.node is None:
                continue
            
            if (self.node is None and box.node.parent is None) or (self.node is not None and box.node.parent == self.node):
                box.frame = self
                self.boxes.append(box)
                
    # ---------------------------------------------------------------------------
    # The full tree
    
    @classmethod
    def Tree(cls, tree, reroutes=False):
        
        Box.BOXES = []
        
        # ---- Insert reroutes
        
        if reroutes:
            frame_inputs(tree)
            frame_outputs(tree)
        
        # ---- Build the boxes such as their index is the same as teir nodes index
        
        frames = []
        for node in tree.nodes:
            if node.bl_idname == 'NodeFrame':
                frames.append(Frame(tree, node))
            else:
                Box(tree, node)
                
        top = Frame(tree, None)
        frames.append(top)
                
        # ----- Build the frames
        
        for frame in frames:
            frame.build()

        # ----- Transform the tree links in links between boxes
        
        top.blinks = {}
        nodes = list(tree.nodes)
        
        for link in tree.links:
            blink = BoxLink(top, link, nodes=nodes)
            
            if blink.key in top.blinks:
                top.blinks[blink.key].append(link)
                
            else:
                top.blinks[blink.key] = blink
                
                blink.sib_to.in_siblings[blink.sib_from.index] = blink
            
        return top
    
    # ---------------------------------------------------------------------------
    # Compute the columns
    
    def compute_columns(self):
        
        debug = False
        
        # ---------------------------------------------------------------------------
        # Compute sub frames and reset col property
        
        for child in self.boxes:
            if child.is_frame:
                child.compute_columns()
                
            child.col = None
            
        # ---------------------------------------------------------------------------
        # 1) Compute the column index of the children
        # 2) Capture the list of in an out reroute nodes
        
        in_rrs  = []
        out_rrs = []
            
        for child in self.boxes:
            
            child.update_column(0)
            
            if child.is_input_reroute:
                in_rrs.append(child)
                
            elif child.is_output_reroute:
                out_rrs.append(child)
                
        if not self.boxes:
            return
                
        # ---------------------------------------------------------------------------
        # How many columns do we have ?
        # We put the input reroutes as first column
        
        max_col = max([box.col for box in self.boxes])
        
        # Put the input reroutes as the leftmost column
        
        for rr in in_rrs:
            rr.col = max_col

        # ---------------------------------------------------------------------------
        # Create the columns
        
        ncols = max_col + 1
        self.cols = [Column(index) for index in range(ncols)]
        for i in range(ncols-1):
            self.cols[i].prev_col = self.cols[i+1]
        
        for box in self.boxes:
            self.cols[box.col].append(box)
            
        # ----- Make sure the single left boxes are just below the node they feed
        
        """
        for col in self.cols:
            fed_nodes = []
            sl_nodes  = []
            for box in col:
                if box.single_left:
                    sl_nodes.append(box)
                else:
                    fed_nodes.append(box)
                    
            index = 0
            for box in fed_nodes:
                col[index] = box
                index += 1
                
                for b in box.in_siblings:
                    f_box = Box.BOXES[b]
                    if f_box.single_left:
                        col[index] = f_box
                        index += 1
                        
            if index != len(col):
                print('-'*30)
                print("COL")
                print(col)
                print('-'*30)
                print("FED NODES")
                print(fed_nodes)
                print('-'*30)
                print("SL NODES")
                print(sl_nodes)
                print('-')
                
                raise Exception(f"Algo error: {index} != {len(col)}")
        """
            
        # ----- Columns x location
            
        x = 0
        for col in reversed(self.cols):
            col.x = x
            x += Column.X_SEPA + col.width
        
        # Reset the y setup position of the boxes
        # x location is initialized since it won't change for not frames
        
        for box in self.boxes:
            box.located = False
            box.x = self.cols[box.col].x

        # ---------------------------------------------------------------------------
        # The boxes are vertically ordered by following the links from right to left
        # for all the boxes in right most column
        
        # ----- Order the boxes by growing col
        
        new_feedings = self.cols[0]

        # ---- Loop while there is boxes to locate
        
        bug = True
        for wd in range(1000): # No break exit will raise an error
        
            if not new_feedings:
                bug = False
                break
        
            feedings = new_feedings
            new_feedings = []
            
            # ----- Loop on the boxes
            
            for i_box, box in enumerate(feedings):
                
                # ----- Already located
                
                if box.located:
                    continue
                
                # ----- Columns before the box's one are not yet initialized
                # We'll do this box later
                
                if sum([c.no_located_box for c in self.cols[:box.col]]) != 0:
                    new_feedings.append(box)
                    continue
                
                # ----- The owning column
                
                col = self.cols[box.col]
                
                # ----- y is min of left columns
                
                y = min([col.next_y for col in self.cols[col.col_index:]])
                    
                # ----- Locate the box in the column
                
                col.locate_box(box, y)
                
                # ----- The feeding nodes
                
                box_links = box.sorted_in_siblings()
                for box_link in box_links:
                    fb = box_link.sib_from
                    if not fb.located and fb not in new_feedings:
                        
                        # ------ If single left feeder, put it right below
                        
                        if fb.single_left:
                            col.locate_box(fb, box.y - box.h - Column.Y_SEPA/4)
                            
                        # ----- else put it in the new feedings list
                        
                        else:
                            new_feedings.append(fb)
                    
                        
        if bug:
            raise RuntimeError("Algorithm error")
            
        # ---------------------------------------------------------------------------
        # Relocate the in/out reroutes
        
        self.cols[-1].relocate_reroutes()
        self.cols[0].relocate_reroutes()

            
# ====================================================================================================
# A Column of boxes

class Column(list):
    
    X_SEPA = 60
    Y_SEPA = 60
    
    def __init__(self, index, x=0, y=0):
        super().__init__()
        
        self.col_index = index
        self.x = x
        self.y = y
        
        self.prev_col = None
    
    @property
    def width(self):
        if self:
            return max([box.w for box in self])
        else:
            return 10
    
    @property
    def height(self):
        return Column.Y_SEPA * (len(self) - 1) + sum([box.h for box in self])
    
    # ----------------------------------------------------------------------------------------------------
    # Return index and box from either index or box
    
    def index_box(self, box):
        
        if isinstance(box, Box):
            try:
                i_box = self.index(box)
                
            except ValueError as e:
                return None, None

        else:
            i_box = box
            box   = self[i_box]
            
        return i_box, box
    
    # ----------------------------------------------------------------------------------------------------
    # Move a box in the list
            
    def move(self, box, index):
        
        i_box, box = self.index_box(box)
        
        if i_box == index:
            return
        
        dy = box.h + Column.Y_SEPA
        for b in self[i_box:]:
            b.y += dy
        del self[i_box]
        
        box.y = self[index].y
        
        dy = box.h + Column.Y_SEPA
        for b in self[index:]:
            b.y -= dy
        self.insert(index, box)
        
    # ----------------------------------------------------------------------------------------------------
    # Height with only located boxes
    
    @property
    def next_y(self):
        y = 0
        for box in self:
            if box.located:
                y = box.y - box.h - Column.Y_SEPA
            else:
                break
            
        return y
    
    # ----------------------------------------------------------------------------------------------------
    # Located boxes count
    
    @property
    def located_count(self):
        n = 0
        for box in self:
            if box.located:
                n += 1
            else:
                return n

    # ----------------------------------------------------------------------------------------------------
    # return 1 if no located boxes
    
    @property
    def no_located_box(self):
        return 1 if self.located_count == 0 else 0
            
    # ----------------------------------------------------------------------------------------------------
    # Locate a box
    
    def locate_box(self, box, y):
        
        i_box, box = self.index_box(box)
        
        self.move(i_box, self.located_count)
        
        box.y = y
        box.located = True

    # ----------------------------------------------------------------------------------------------------
    # Relocate input reroutes    
        
    def relocate_reroutes(self):
        
        # ----- Get all the reroute nodes in the list
        
        irrs = []
        for i, box in enumerate(self):
            if box.is_reroute:
                irrs.append(i)
                
        if not irrs:
            return

        # ----- Move them as first nodes of the column
        
        for i, index in enumerate(irrs):
            self.move(index, i)
            
# ====================================================================================================
# Arrange a tree

def arrange(tree, reroutes=True, delete_single=False):
    
    if isinstance(tree, str):
        tree = bpy.data.node_groups[name]
    
    # Some cleaning
    
    if delete_single:
        delete_single_nodes(tree)
    
    top = Frame.Tree(tree, reroutes=reroutes)
    if top is None:
        return
    
    top.compute_columns()
            
        

        