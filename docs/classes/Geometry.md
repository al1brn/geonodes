# class Geometry (Socket)

<sub>go to [index](/docs/index.md)</sub>

Socket
------
 - Type : GEOMETRY
 - bl_idname : NodeSocketGeometry

Methods
-------
 - [bounding_box](#bounding_box) : BoundingBox, geometry=self
 - [capture_attribute](#capture_attribute) : CaptureAttribute, geometry=self
 - [capture_boolean](#capture_boolean) : CaptureAttribute, geometry=self, data_type='BOOLEAN'
 - [capture_color](#capture_color) : CaptureAttribute, geometry=self, data_type='FLOAT_COLOR'
 - [capture_float](#capture_float) : CaptureAttribute, geometry=self, data_type='FLOAT'
 - [capture_int](#capture_int) : CaptureAttribute, geometry=self, data_type='INT'
 - [capture_quaternion](#capture_quaternion) : CaptureAttribute, geometry=self, data_type='QUATERNION'
 - [capture_vector](#capture_vector) : CaptureAttribute, geometry=self, data_type='FLOAT_VECTOR'
 - [convex_hull](#convex_hull) : ConvexHull, geometry=self
 - [curve_length](#curve_length) : CurveLength, curve=self, return socket
 - [curve_to_mesh](#curve_to_mesh) : CurveToMesh, curve=self
 - [curve_to_points](#curve_to_points) : CurveToPoints, curve=self
 - [deform_curves_on_surface](#deform_curves_on_surface) : DeformCurvesOnSurface, curves=self
 - [delete_geometry](#delete_geometry) : DeleteGeometry, geometry=self
 - [difference](#difference) : MeshBoolean, mesh_1=self, mesh_2=args
 - [distribute_points_in_volume](#distribute_points_in_volume) : DistributePointsInVolume, volume=self
 - [distribute_points_on_faces](#distribute_points_on_faces) : DistributePointsOnFaces, mesh=self
 - [domain_size](#domain_size) : DomainSize, geometry=self, return node
 - [dual_mesh](#dual_mesh) : DualMesh, mesh=self
 - [duplicate_elements](#duplicate_elements) : DuplicateElements, geometry=self
 - [edge_paths_to_curves](#edge_paths_to_curves) : EdgePathsToCurves, mesh=self
 - [extrude_mesh](#extrude_mesh) : ExtrudeMesh, mesh=self
 - [fill_curve](#fill_curve) : FillCurve, curve=self
 - [fillet_curve](#fillet_curve) : FilletCurve, curve=self
 - [flip_faces](#flip_faces) : FlipFaces, mesh=self
 - [geometry_to_instance](#geometry_to_instance) : GeometryToInstance, geometry=self
 - [instance_on_points](#instance_on_points) : InstanceOnPoints, points=self
 - [instances_to_points](#instances_to_points) : InstancesToPoints, instances=self
 - [interpolate_curves](#interpolate_curves) : InterpolateCurves, guide_curves=self
 - [intersect](#intersect) : MeshBoolean, mesh=geometry + args
 - [join_geometry](#join_geometry) : JoinGeometry, geometry=self
 - [mean_filter_sdf_volume](#mean_filter_sdf_volume) : MeanFilterSDFVolume, volume=self
 - [merge_by_distance](#merge_by_distance) : MergeByDistance, geometry=self
 - [mesh_boolean](#mesh_boolean) : MeshBoolean, mesh_1=self
 - [mesh_to_curve](#mesh_to_curve) : MeshToCurve, mesh=self
 - [mesh_to_points](#mesh_to_points) : MeshToPoints, mesh=self
 - [mesh_to_sdf_volume](#mesh_to_sdf_volume) : MeshToSDFVolume, mesh=self
 - [mesh_to_volume](#mesh_to_volume) : MeshToVolume, mesh=self
 - [offset_sdf_volume](#offset_sdf_volume) : OffsetSDFVolume, volume=self
 - [points_to_curves](#points_to_curves) : PointsToCurves, points=self
 - [points_to_sdf_volume](#points_to_sdf_volume) : PointsToSDFVolume, points=self
 - [points_to_vertices](#points_to_vertices) : PointsToVertices, points=self
 - [points_to_volume](#points_to_volume) : PointsToVolume, points=self
 - [realize_instances](#realize_instances) : RealizeInstances, geometry=self
 - [remove_named_attribute](#remove_named_attribute) : RemoveNamedAttribute, geometry=self
 - [repeat_output](#repeat_output) : RepeatOutput, geometry=self
 - [replace_material](#replace_material) : ReplaceMaterial, geometry=self
 - [resample_curve](#resample_curve) : ResampleCurve, curve=self
 - [reverse_curve](#reverse_curve) : ReverseCurve, curve=self
 - [rotate_instances](#rotate_instances) : RotateInstances, instances=self
 - [sample_index_boolean](#sample_index_boolean) : SampleIndex, value=self, data_type='BOOLEAN'
 - [sample_index_color](#sample_index_color) : SampleIndex, value=self, data_type='FLOAT_COLOR'
 - [sample_index_float](#sample_index_float) : SampleIndex, value=self, data_type='FLOAT'
 - [sample_index_int](#sample_index_int) : SampleIndex, value=self, data_type='INT'
 - [sample_index_quaternion](#sample_index_quaternion) : SampleIndex, value=self, data_type='QUATERNION'
 - [sample_index_vector](#sample_index_vector) : SampleIndex, value=self, data_type='FLOAT_VECTOR'
 - [scale_elements](#scale_elements) : ScaleElements, geometry=self
 - [scale_instances](#scale_instances) : ScaleInstances, instances=self
 - [separate_components](#separate_components) : SeparateComponents, geometry=self
 - [separate_geometry](#separate_geometry) : SeparateGeometry, geometry=self
 - [set_curve_normal](#set_curve_normal) : SetCurveNormal, curve=self
 - [set_curve_radius](#set_curve_radius) : SetCurveRadius, curve=self
 - [set_curve_tilt](#set_curve_tilt) : SetCurveTilt, curve=self
 - [set_face_set](#set_face_set) : SetFaceSet, mesh=self
 - [set_handle_positions](#set_handle_positions) : SetHandlePositions, curve=self
 - [set_handle_type](#set_handle_type) : SetHandleType, curve=self
 - [set_id](#set_id) : SetID, geometry=self
 - [set_material](#set_material) : SetMaterial, geometry=self
 - [set_material_index](#set_material_index) : SetMaterialIndex, geometry=self
 - [set_point_radius](#set_point_radius) : SetPointRadius, points=self
 - [set_position](#set_position) : SetPosition, geometry=self
 - [set_selection](#set_selection) : SetSelection, geometry=self
 - [set_shade_smooth](#set_shade_smooth) : SetShadeSmooth, geometry=self
 - [set_spline_cyclic](#set_spline_cyclic) : SetSplineCyclic, geometry=self
 - [set_spline_resolution](#set_spline_resolution) : SetSplineResolution, geometry=self
 - [set_spline_type](#set_spline_type) : SetSplineType, curve=self
 - [simulation_output](#simulation_output) : SimulationOutput, geometry=self
 - [split_edges](#split_edges) : SplitEdges, mesh=self
 - [store_named_attribute](#store_named_attribute) : StoreNamedAttribute, geometry=self
 - [store_named_boolean](#store_named_boolean) : StoreNamedAttribute, geometry=self, data_type='BOOLEAN'
 - [store_named_byte_color](#store_named_byte_color) : StoreNamedAttribute, geometry=self, data_type='BYTE_COLOR'
 - [store_named_float](#store_named_float) : StoreNamedAttribute, geometry=self, data_type='FLOAT'
 - [store_named_float2](#store_named_float2) : StoreNamedAttribute, geometry=self, data_type='FLOAT2'
 - [store_named_float_color](#store_named_float_color) : StoreNamedAttribute, geometry=self, data_type='FLOAT_COLOR'
 - [store_named_int](#store_named_int) : StoreNamedAttribute, geometry=self, data_type='INT'
 - [store_named_quaternion](#store_named_quaternion) : StoreNamedAttribute, geometry=self, data_type='QUATERNION'
 - [store_named_vector](#store_named_vector) : StoreNamedAttribute, geometry=self, data_type='FLOAT_VECTOR'
 - [subdivide_curve](#subdivide_curve) : SubdivideCurve, curve=self
 - [subdivide_mesh](#subdivide_mesh) : SubdivideMesh, mesh=self
 - [subdivision_surface](#subdivision_surface) : SubdivisionSurface, mesh=self
 - [switch](#switch) : Switch, false=self, input_type='GEOMETRY'
 - [transform_geometry](#transform_geometry) : TransformGeometry, geometry=self
 - [translate_instances](#translate_instances) : TranslateInstances, instances=self
 - [triangulate](#triangulate) : Triangulate, mesh=self
 - [trim_curve](#trim_curve) : TrimCurve, curve=self
 - [union](#union) : MeshBoolean, mesh=geometry + args
 - [volume_to_mesh](#volume_to_mesh) : VolumeToMesh, volume=self

Properties
----------
 - [ID](#id)
 - [curve_radius](#curve_radius) : Curve radius property
 - [curve_tilt](#curve_tilt)
 - [edge_neighbors](#edge_neighbors)
 - [edge_shade_smooth](#edge_shade_smooth) : SetShadeSmooth(domain='EDGE')
 - [face_area](#face_area)
 - [face_shade_smooth](#face_shade_smooth) : SetShadeSmooth(domain='FACE')
 - [index](#index)
 - [offset](#offset) : SetPosition(offset=value)
 - [point_radius](#point_radius) : Point radius property
 - [position](#position) : SetPosition(position=value)
 - [spline_cyclic](#spline_cyclic)
 - [spline_resolution](#spline_resolution)
 - [tangent](#tangent)

## Methods

### bounding_box

BoundingBox, geometry=self

Node
----
 - class_name : [BoundingBox](/docs/classes/BoundingBox.md)
 - bl_idname : GeometryNodeBoundBox

### capture_attribute

CaptureAttribute, geometry=self

Node
----
 - class_name : [CaptureAttribute](/docs/classes/CaptureAttribute.md)
 - bl_idname : GeometryNodeCaptureAttribute

### capture_boolean

CaptureAttribute, geometry=self, data_type='BOOLEAN'

Node
----
 - class_name : [CaptureAttribute](/docs/classes/CaptureAttribute.md)
 - bl_idname : GeometryNodeCaptureAttribute

### capture_color

CaptureAttribute, geometry=self, data_type='FLOAT_COLOR'

Node
----
 - class_name : [CaptureAttribute](/docs/classes/CaptureAttribute.md)
 - bl_idname : GeometryNodeCaptureAttribute

### capture_float

CaptureAttribute, geometry=self, data_type='FLOAT'

Node
----
 - class_name : [CaptureAttribute](/docs/classes/CaptureAttribute.md)
 - bl_idname : GeometryNodeCaptureAttribute

### capture_int

CaptureAttribute, geometry=self, data_type='INT'

Node
----
 - class_name : [CaptureAttribute](/docs/classes/CaptureAttribute.md)
 - bl_idname : GeometryNodeCaptureAttribute

### capture_quaternion

CaptureAttribute, geometry=self, data_type='QUATERNION'

Node
----
 - class_name : [CaptureAttribute](/docs/classes/CaptureAttribute.md)
 - bl_idname : GeometryNodeCaptureAttribute

### capture_vector

CaptureAttribute, geometry=self, data_type='FLOAT_VECTOR'

Node
----
 - class_name : [CaptureAttribute](/docs/classes/CaptureAttribute.md)
 - bl_idname : GeometryNodeCaptureAttribute

### convex_hull

ConvexHull, geometry=self

Node
----
 - class_name : [ConvexHull](/docs/classes/ConvexHull.md)
 - bl_idname : GeometryNodeConvexHull

### curve_length

CurveLength, curve=self, return socket

Node
----
 - class_name : [CurveLength](/docs/classes/CurveLength.md)
 - bl_idname : GeometryNodeCurveLength

### curve_to_mesh

CurveToMesh, curve=self

Node
----
 - class_name : [CurveToMesh](/docs/classes/CurveToMesh.md)
 - bl_idname : GeometryNodeCurveToMesh

### curve_to_points

CurveToPoints, curve=self

Node
----
 - class_name : [CurveToPoints](/docs/classes/CurveToPoints.md)
 - bl_idname : GeometryNodeCurveToPoints

### deform_curves_on_surface

DeformCurvesOnSurface, curves=self

Node
----
 - class_name : [DeformCurvesOnSurface](/docs/classes/DeformCurvesOnSurface.md)
 - bl_idname : GeometryNodeDeformCurvesOnSurface

### delete_geometry

DeleteGeometry, geometry=self

Node
----
 - class_name : [DeleteGeometry](/docs/classes/DeleteGeometry.md)
 - bl_idname : GeometryNodeDeleteGeometry

### difference

MeshBoolean, mesh_1=self, mesh_2=args

Node
----
 - class_name : [MeshBoolean](/docs/classes/MeshBoolean.md)
 - bl_idname : GeometryNodeMeshBoolean

### distribute_points_in_volume

DistributePointsInVolume, volume=self

Node
----
 - class_name : [DistributePointsInVolume](/docs/classes/DistributePointsInVolume.md)
 - bl_idname : GeometryNodeDistributePointsInVolume

### distribute_points_on_faces

DistributePointsOnFaces, mesh=self

Node
----
 - class_name : [DistributePointsOnFaces](/docs/classes/DistributePointsOnFaces.md)
 - bl_idname : GeometryNodeDistributePointsOnFaces

### domain_size

DomainSize, geometry=self, return node

Node
----
 - class_name : [DomainSize](/docs/classes/DomainSize.md)
 - bl_idname : GeometryNodeAttributeDomainSize

### dual_mesh

DualMesh, mesh=self

Node
----
 - class_name : [DualMesh](/docs/classes/DualMesh.md)
 - bl_idname : GeometryNodeDualMesh

### duplicate_elements

DuplicateElements, geometry=self

Node
----
 - class_name : [DuplicateElements](/docs/classes/DuplicateElements.md)
 - bl_idname : GeometryNodeDuplicateElements

### edge_paths_to_curves

EdgePathsToCurves, mesh=self

Node
----
 - class_name : [EdgePathsToCurves](/docs/classes/EdgePathsToCurves.md)
 - bl_idname : GeometryNodeEdgePathsToCurves

### extrude_mesh

ExtrudeMesh, mesh=self

Node
----
 - class_name : [ExtrudeMesh](/docs/classes/ExtrudeMesh.md)
 - bl_idname : GeometryNodeExtrudeMesh

### fill_curve

FillCurve, curve=self

Node
----
 - class_name : [FillCurve](/docs/classes/FillCurve.md)
 - bl_idname : GeometryNodeFillCurve

### fillet_curve

FilletCurve, curve=self

Node
----
 - class_name : [FilletCurve](/docs/classes/FilletCurve.md)
 - bl_idname : GeometryNodeFilletCurve

### flip_faces

FlipFaces, mesh=self

Node
----
 - class_name : [FlipFaces](/docs/classes/FlipFaces.md)
 - bl_idname : GeometryNodeFlipFaces

### geometry_to_instance

GeometryToInstance, geometry=self

Node
----
 - class_name : [GeometryToInstance](/docs/classes/GeometryToInstance.md)
 - bl_idname : GeometryNodeGeometryToInstance

### instance_on_points

InstanceOnPoints, points=self

Node
----
 - class_name : [InstanceOnPoints](/docs/classes/InstanceOnPoints.md)
 - bl_idname : GeometryNodeInstanceOnPoints

### instances_to_points

InstancesToPoints, instances=self

Node
----
 - class_name : [InstancesToPoints](/docs/classes/InstancesToPoints.md)
 - bl_idname : GeometryNodeInstancesToPoints

### interpolate_curves

InterpolateCurves, guide_curves=self

Node
----
 - class_name : [InterpolateCurves](/docs/classes/InterpolateCurves.md)
 - bl_idname : GeometryNodeInterpolateCurves

### intersect

MeshBoolean, mesh=geometry + args

Node
----
 - class_name : [MeshBoolean](/docs/classes/MeshBoolean.md)
 - bl_idname : GeometryNodeMeshBoolean

### join_geometry

JoinGeometry, geometry=self

Node
----
 - class_name : [JoinGeometry](/docs/classes/JoinGeometry.md)
 - bl_idname : GeometryNodeJoinGeometry

### mean_filter_sdf_volume

MeanFilterSDFVolume, volume=self

Node
----
 - class_name : [MeanFilterSDFVolume](/docs/classes/MeanFilterSDFVolume.md)
 - bl_idname : GeometryNodeMeanFilterSDFVolume

### merge_by_distance

MergeByDistance, geometry=self

Node
----
 - class_name : [MergeByDistance](/docs/classes/MergeByDistance.md)
 - bl_idname : GeometryNodeMergeByDistance

### mesh_boolean

MeshBoolean, mesh_1=self

Node
----
 - class_name : [MeshBoolean](/docs/classes/MeshBoolean.md)
 - bl_idname : GeometryNodeMeshBoolean

### mesh_to_curve

MeshToCurve, mesh=self

Node
----
 - class_name : [MeshToCurve](/docs/classes/MeshToCurve.md)
 - bl_idname : GeometryNodeMeshToCurve

### mesh_to_points

MeshToPoints, mesh=self

Node
----
 - class_name : [MeshToPoints](/docs/classes/MeshToPoints.md)
 - bl_idname : GeometryNodeMeshToPoints

### mesh_to_sdf_volume

MeshToSDFVolume, mesh=self

Node
----
 - class_name : [MeshToSDFVolume](/docs/classes/MeshToSDFVolume.md)
 - bl_idname : GeometryNodeMeshToSDFVolume

### mesh_to_volume

MeshToVolume, mesh=self

Node
----
 - class_name : [MeshToVolume](/docs/classes/MeshToVolume.md)
 - bl_idname : GeometryNodeMeshToVolume

### offset_sdf_volume

OffsetSDFVolume, volume=self

Node
----
 - class_name : [OffsetSDFVolume](/docs/classes/OffsetSDFVolume.md)
 - bl_idname : GeometryNodeOffsetSDFVolume

### points_to_curves

PointsToCurves, points=self

Node
----
 - class_name : [PointsToCurves](/docs/classes/PointsToCurves.md)
 - bl_idname : GeometryNodePointsToCurves

### points_to_sdf_volume

PointsToSDFVolume, points=self

Node
----
 - class_name : [PointsToSDFVolume](/docs/classes/PointsToSDFVolume.md)
 - bl_idname : GeometryNodePointsToSDFVolume

### points_to_vertices

PointsToVertices, points=self

Node
----
 - class_name : [PointsToVertices](/docs/classes/PointsToVertices.md)
 - bl_idname : GeometryNodePointsToVertices

### points_to_volume

PointsToVolume, points=self

Node
----
 - class_name : [PointsToVolume](/docs/classes/PointsToVolume.md)
 - bl_idname : GeometryNodePointsToVolume

### realize_instances

RealizeInstances, geometry=self

Node
----
 - class_name : [RealizeInstances](/docs/classes/RealizeInstances.md)
 - bl_idname : GeometryNodeRealizeInstances

### remove_named_attribute

RemoveNamedAttribute, geometry=self

Node
----
 - class_name : [RemoveNamedAttribute](/docs/classes/RemoveNamedAttribute.md)
 - bl_idname : GeometryNodeRemoveAttribute

### repeat_output

RepeatOutput, geometry=self

Node
----
 - class_name : [RepeatOutput](/docs/classes/RepeatOutput.md)
 - bl_idname : GeometryNodeRepeatOutput

### replace_material

ReplaceMaterial, geometry=self

Node
----
 - class_name : [ReplaceMaterial](/docs/classes/ReplaceMaterial.md)
 - bl_idname : GeometryNodeReplaceMaterial

### resample_curve

ResampleCurve, curve=self

Node
----
 - class_name : [ResampleCurve](/docs/classes/ResampleCurve.md)
 - bl_idname : GeometryNodeResampleCurve

### reverse_curve

ReverseCurve, curve=self

Node
----
 - class_name : [ReverseCurve](/docs/classes/ReverseCurve.md)
 - bl_idname : GeometryNodeReverseCurve

### rotate_instances

RotateInstances, instances=self

Node
----
 - class_name : [RotateInstances](/docs/classes/RotateInstances.md)
 - bl_idname : GeometryNodeRotateInstances

### sample_index_boolean

SampleIndex, value=self, data_type='BOOLEAN'

Node
----
 - class_name : [SampleIndex](/docs/classes/SampleIndex.md)
 - bl_idname : GeometryNodeSampleIndex

### sample_index_color

SampleIndex, value=self, data_type='FLOAT_COLOR'

Node
----
 - class_name : [SampleIndex](/docs/classes/SampleIndex.md)
 - bl_idname : GeometryNodeSampleIndex

### sample_index_float

SampleIndex, value=self, data_type='FLOAT'

Node
----
 - class_name : [SampleIndex](/docs/classes/SampleIndex.md)
 - bl_idname : GeometryNodeSampleIndex

### sample_index_int

SampleIndex, value=self, data_type='INT'

Node
----
 - class_name : [SampleIndex](/docs/classes/SampleIndex.md)
 - bl_idname : GeometryNodeSampleIndex

### sample_index_quaternion

SampleIndex, value=self, data_type='QUATERNION'

Node
----
 - class_name : [SampleIndex](/docs/classes/SampleIndex.md)
 - bl_idname : GeometryNodeSampleIndex

### sample_index_vector

SampleIndex, value=self, data_type='FLOAT_VECTOR'

Node
----
 - class_name : [SampleIndex](/docs/classes/SampleIndex.md)
 - bl_idname : GeometryNodeSampleIndex

### scale_elements

ScaleElements, geometry=self

Node
----
 - class_name : [ScaleElements](/docs/classes/ScaleElements.md)
 - bl_idname : GeometryNodeScaleElements

### scale_instances

ScaleInstances, instances=self

Node
----
 - class_name : [ScaleInstances](/docs/classes/ScaleInstances.md)
 - bl_idname : GeometryNodeScaleInstances

### separate_components

SeparateComponents, geometry=self

Node
----
 - class_name : [SeparateComponents](/docs/classes/SeparateComponents.md)
 - bl_idname : GeometryNodeSeparateComponents

### separate_geometry

SeparateGeometry, geometry=self

Node
----
 - class_name : [SeparateGeometry](/docs/classes/SeparateGeometry.md)
 - bl_idname : GeometryNodeSeparateGeometry

### set_curve_normal

SetCurveNormal, curve=self

Node
----
 - class_name : [SetCurveNormal](/docs/classes/SetCurveNormal.md)
 - bl_idname : GeometryNodeSetCurveNormal

### set_curve_radius

SetCurveRadius, curve=self

Node
----
 - class_name : [SetCurveRadius](/docs/classes/SetCurveRadius.md)
 - bl_idname : GeometryNodeSetCurveRadius

### set_curve_tilt

SetCurveTilt, curve=self

Node
----
 - class_name : [SetCurveTilt](/docs/classes/SetCurveTilt.md)
 - bl_idname : GeometryNodeSetCurveTilt

### set_face_set

SetFaceSet, mesh=self

Node
----
 - class_name : [SetFaceSet](/docs/classes/SetFaceSet.md)
 - bl_idname : GeometryNodeToolSetFaceSet

### set_handle_positions

SetHandlePositions, curve=self

Node
----
 - class_name : [SetHandlePositions](/docs/classes/SetHandlePositions.md)
 - bl_idname : GeometryNodeSetCurveHandlePositions

### set_handle_type

SetHandleType, curve=self

Node
----
 - class_name : [SetHandleType](/docs/classes/SetHandleType.md)
 - bl_idname : GeometryNodeCurveSetHandles

### set_id

SetID, geometry=self

Node
----
 - class_name : [SetID](/docs/classes/SetID.md)
 - bl_idname : GeometryNodeSetID

### set_material

SetMaterial, geometry=self

Node
----
 - class_name : [SetMaterial](/docs/classes/SetMaterial.md)
 - bl_idname : GeometryNodeSetMaterial

### set_material_index

SetMaterialIndex, geometry=self

Node
----
 - class_name : [SetMaterialIndex](/docs/classes/SetMaterialIndex.md)
 - bl_idname : GeometryNodeSetMaterialIndex

### set_point_radius

SetPointRadius, points=self

Node
----
 - class_name : [SetPointRadius](/docs/classes/SetPointRadius.md)
 - bl_idname : GeometryNodeSetPointRadius

### set_position

SetPosition, geometry=self

Node
----
 - class_name : [SetPosition](/docs/classes/SetPosition.md)
 - bl_idname : GeometryNodeSetPosition

### set_selection

SetSelection, geometry=self

Node
----
 - class_name : [SetSelection](/docs/classes/SetSelection.md)
 - bl_idname : GeometryNodeToolSetSelection

### set_shade_smooth

SetShadeSmooth, geometry=self

Node
----
 - class_name : [SetShadeSmooth](/docs/classes/SetShadeSmooth.md)
 - bl_idname : GeometryNodeSetShadeSmooth

### set_spline_cyclic

SetSplineCyclic, geometry=self

Node
----
 - class_name : [SetSplineCyclic](/docs/classes/SetSplineCyclic.md)
 - bl_idname : GeometryNodeSetSplineCyclic

### set_spline_resolution

SetSplineResolution, geometry=self

Node
----
 - class_name : [SetSplineResolution](/docs/classes/SetSplineResolution.md)
 - bl_idname : GeometryNodeSetSplineResolution

### set_spline_type

SetSplineType, curve=self

Node
----
 - class_name : [SetSplineType](/docs/classes/SetSplineType.md)
 - bl_idname : GeometryNodeCurveSplineType

### simulation_output

SimulationOutput, geometry=self

Node
----
 - class_name : [SimulationOutput](/docs/classes/SimulationOutput.md)
 - bl_idname : GeometryNodeSimulationOutput

### split_edges

SplitEdges, mesh=self

Node
----
 - class_name : [SplitEdges](/docs/classes/SplitEdges.md)
 - bl_idname : GeometryNodeSplitEdges

### store_named_attribute

StoreNamedAttribute, geometry=self

Node
----
 - class_name : [StoreNamedAttribute](/docs/classes/StoreNamedAttribute.md)
 - bl_idname : GeometryNodeStoreNamedAttribute

### store_named_boolean

StoreNamedAttribute, geometry=self, data_type='BOOLEAN'

Node
----
 - class_name : [StoreNamedAttribute](/docs/classes/StoreNamedAttribute.md)
 - bl_idname : GeometryNodeStoreNamedAttribute

### store_named_byte_color

StoreNamedAttribute, geometry=self, data_type='BYTE_COLOR'

Node
----
 - class_name : [StoreNamedAttribute](/docs/classes/StoreNamedAttribute.md)
 - bl_idname : GeometryNodeStoreNamedAttribute

### store_named_float

StoreNamedAttribute, geometry=self, data_type='FLOAT'

Node
----
 - class_name : [StoreNamedAttribute](/docs/classes/StoreNamedAttribute.md)
 - bl_idname : GeometryNodeStoreNamedAttribute

### store_named_float2

StoreNamedAttribute, geometry=self, data_type='FLOAT2'

Node
----
 - class_name : [StoreNamedAttribute](/docs/classes/StoreNamedAttribute.md)
 - bl_idname : GeometryNodeStoreNamedAttribute

### store_named_float_color

StoreNamedAttribute, geometry=self, data_type='FLOAT_COLOR'

Node
----
 - class_name : [StoreNamedAttribute](/docs/classes/StoreNamedAttribute.md)
 - bl_idname : GeometryNodeStoreNamedAttribute

### store_named_int

StoreNamedAttribute, geometry=self, data_type='INT'

Node
----
 - class_name : [StoreNamedAttribute](/docs/classes/StoreNamedAttribute.md)
 - bl_idname : GeometryNodeStoreNamedAttribute

### store_named_quaternion

StoreNamedAttribute, geometry=self, data_type='QUATERNION'

Node
----
 - class_name : [StoreNamedAttribute](/docs/classes/StoreNamedAttribute.md)
 - bl_idname : GeometryNodeStoreNamedAttribute

### store_named_vector

StoreNamedAttribute, geometry=self, data_type='FLOAT_VECTOR'

Node
----
 - class_name : [StoreNamedAttribute](/docs/classes/StoreNamedAttribute.md)
 - bl_idname : GeometryNodeStoreNamedAttribute

### subdivide_curve

SubdivideCurve, curve=self

Node
----
 - class_name : [SubdivideCurve](/docs/classes/SubdivideCurve.md)
 - bl_idname : GeometryNodeSubdivideCurve

### subdivide_mesh

SubdivideMesh, mesh=self

Node
----
 - class_name : [SubdivideMesh](/docs/classes/SubdivideMesh.md)
 - bl_idname : GeometryNodeSubdivideMesh

### subdivision_surface

SubdivisionSurface, mesh=self

Node
----
 - class_name : [SubdivisionSurface](/docs/classes/SubdivisionSurface.md)
 - bl_idname : GeometryNodeSubdivisionSurface

### switch

Switch, false=self, input_type='GEOMETRY'

Node
----
 - class_name : [Switch](/docs/classes/Switch.md)
 - bl_idname : GeometryNodeSwitch

### transform_geometry

TransformGeometry, geometry=self

Node
----
 - class_name : [TransformGeometry](/docs/classes/TransformGeometry.md)
 - bl_idname : GeometryNodeTransform

### translate_instances

TranslateInstances, instances=self

Node
----
 - class_name : [TranslateInstances](/docs/classes/TranslateInstances.md)
 - bl_idname : GeometryNodeTranslateInstances

### triangulate

Triangulate, mesh=self

Node
----
 - class_name : [Triangulate](/docs/classes/Triangulate.md)
 - bl_idname : GeometryNodeTriangulate

### trim_curve

TrimCurve, curve=self

Node
----
 - class_name : [TrimCurve](/docs/classes/TrimCurve.md)
 - bl_idname : GeometryNodeTrimCurve

### union

MeshBoolean, mesh=geometry + args

Node
----
 - class_name : [MeshBoolean](/docs/classes/MeshBoolean.md)
 - bl_idname : GeometryNodeMeshBoolean

### volume_to_mesh

VolumeToMesh, volume=self

Node
----
 - class_name : [VolumeToMesh](/docs/classes/VolumeToMesh.md)
 - bl_idname : GeometryNodeVolumeToMesh

## Properties

### ID

Nodes
-----
 - get : [ID](/docs/classes/ID.md)
 - set : [SetID](/docs/classes/SetID.md)

### curve_radius

Curve radius property

Nodes
-----
 - get : [Radius](/docs/classes/Radius.md)
 - set : [SetCurveRadius](/docs/classes/SetCurveRadius.md)

### curve_tilt

Nodes
-----
 - get : [CurveTilt](/docs/classes/CurveTilt.md)
 - set : [SetCurveTilt](/docs/classes/SetCurveTilt.md)

### edge_neighbors

Nodes
-----
 - get : [EdgeNeighbors](/docs/classes/EdgeNeighbors.md)
 - set : None

### edge_shade_smooth

SetShadeSmooth(domain='EDGE')

Nodes
-----
 - get : [IsEdgeSmooth](/docs/classes/IsEdgeSmooth.md)
 - set : [SetSmooth](/docs/classes/SetSmooth.md)

### face_area

Nodes
-----
 - get : [FaceArea](/docs/classes/FaceArea.md)
 - set : None

### face_shade_smooth

SetShadeSmooth(domain='FACE')

Nodes
-----
 - get : [IsFaceSmooth](/docs/classes/IsFaceSmooth.md)
 - set : [SetSmooth](/docs/classes/SetSmooth.md)

### index

Nodes
-----
 - get : [Index](/docs/classes/Index.md)
 - set : None

### offset

SetPosition(offset=value)

Nodes
-----
 - get : None
 - set : [SetPosition](/docs/classes/SetPosition.md)

### point_radius

Point radius property

Nodes
-----
 - get : [Radius](/docs/classes/Radius.md)
 - set : [SetPointRadius](/docs/classes/SetPointRadius.md)

### position

SetPosition(position=value)

Nodes
-----
 - get : [Position](/docs/classes/Position.md)
 - set : [SetPosition](/docs/classes/SetPosition.md)

### spline_cyclic

Nodes
-----
 - get : [IsSplineCyclic](/docs/classes/IsSplineCyclic.md)
 - set : [SetSplineCyclic](/docs/classes/SetSplineCyclic.md)

### spline_resolution

Nodes
-----
 - get : [SplineResolution](/docs/classes/SplineResolution.md)
 - set : [SetSplineResolution](/docs/classes/SetSplineResolution.md)

### tangent

Nodes
-----
 - get : [CurveTangent](/docs/classes/CurveTangent.md)
 - set : None
