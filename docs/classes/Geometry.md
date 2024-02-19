# class Geometry (Socket)

<sub>go to [index](/docs/index.md)</sub>

Socket
 - Type : GEOMETRY
 - bl_idname : NodeSocketGeometry

Methods
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
 - class_name : [BoundingBox](/docs/classes/BoundingBox.md)
 - bl_idname : GeometryNodeBoundBox

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - node_label : node_label
 - node_color : node_color

``` python
def bounding_box(self, node_label=None, node_color=None):
```
### capture_attribute

CaptureAttribute, geometry=self

Node
 - class_name : [CaptureAttribute](/docs/classes/CaptureAttribute.md)
 - bl_idname : GeometryNodeCaptureAttribute

Arguments
 - value : None
 - data_type : 'FLOAT'
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - value : value
 - data_type : data_type
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def capture_attribute(self, value=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):
```
### capture_boolean

CaptureAttribute, geometry=self, data_type='BOOLEAN'

Node
 - class_name : [CaptureAttribute](/docs/classes/CaptureAttribute.md)
 - bl_idname : GeometryNodeCaptureAttribute

Arguments
 - value : None
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - value : value
 - data_type : 'BOOLEAN'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def capture_boolean(self, value=None, domain='POINT', node_label=None, node_color=None):
```
### capture_color

CaptureAttribute, geometry=self, data_type='FLOAT_COLOR'

Node
 - class_name : [CaptureAttribute](/docs/classes/CaptureAttribute.md)
 - bl_idname : GeometryNodeCaptureAttribute

Arguments
 - value : None
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - value : value
 - data_type : 'FLOAT_COLOR'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def capture_color(self, value=None, domain='POINT', node_label=None, node_color=None):
```
### capture_float

CaptureAttribute, geometry=self, data_type='FLOAT'

Node
 - class_name : [CaptureAttribute](/docs/classes/CaptureAttribute.md)
 - bl_idname : GeometryNodeCaptureAttribute

Arguments
 - value : None
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - value : value
 - data_type : 'FLOAT'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def capture_float(self, value=None, domain='POINT', node_label=None, node_color=None):
```
### capture_int

CaptureAttribute, geometry=self, data_type='INT'

Node
 - class_name : [CaptureAttribute](/docs/classes/CaptureAttribute.md)
 - bl_idname : GeometryNodeCaptureAttribute

Arguments
 - value : None
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - value : value
 - data_type : 'INT'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def capture_int(self, value=None, domain='POINT', node_label=None, node_color=None):
```
### capture_quaternion

CaptureAttribute, geometry=self, data_type='QUATERNION'

Node
 - class_name : [CaptureAttribute](/docs/classes/CaptureAttribute.md)
 - bl_idname : GeometryNodeCaptureAttribute

Arguments
 - value : None
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - value : value
 - data_type : 'QUATERNION'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def capture_quaternion(self, value=None, domain='POINT', node_label=None, node_color=None):
```
### capture_vector

CaptureAttribute, geometry=self, data_type='FLOAT_VECTOR'

Node
 - class_name : [CaptureAttribute](/docs/classes/CaptureAttribute.md)
 - bl_idname : GeometryNodeCaptureAttribute

Arguments
 - value : None
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - value : value
 - data_type : 'FLOAT_VECTOR'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def capture_vector(self, value=None, domain='POINT', node_label=None, node_color=None):
```
### convex_hull

ConvexHull, geometry=self

Node
 - class_name : [ConvexHull](/docs/classes/ConvexHull.md)
 - bl_idname : GeometryNodeConvexHull

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - node_label : node_label
 - node_color : node_color

``` python
def convex_hull(self, node_label=None, node_color=None):
```
### curve_length

CurveLength, curve=self, return socket

Node
 - class_name : [CurveLength](/docs/classes/CurveLength.md)
 - bl_idname : GeometryNodeCurveLength

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - curve : self
 - node_label : node_label
 - node_color : node_color

``` python
def curve_length(self, node_label=None, node_color=None):
```
### curve_to_mesh

CurveToMesh, curve=self

Node
 - class_name : [CurveToMesh](/docs/classes/CurveToMesh.md)
 - bl_idname : GeometryNodeCurveToMesh

Arguments
 - profile_curve : None
 - fill_caps : None
 - node_label : None
 - node_color : None

Node initialization
 - curve : self
 - profile_curve : profile_curve
 - fill_caps : fill_caps
 - node_label : node_label
 - node_color : node_color

``` python
def curve_to_mesh(self, profile_curve=None, fill_caps=None, node_label=None, node_color=None):
```
### curve_to_points

CurveToPoints, curve=self

Node
 - class_name : [CurveToPoints](/docs/classes/CurveToPoints.md)
 - bl_idname : GeometryNodeCurveToPoints

Arguments
 - count : None
 - length : None
 - mode : 'COUNT'
 - node_label : None
 - node_color : None

Node initialization
 - curve : self
 - count : count
 - length : length
 - mode : mode
 - node_label : node_label
 - node_color : node_color

``` python
def curve_to_points(self, count=None, length=None, mode='COUNT', node_label=None, node_color=None):
```
### deform_curves_on_surface

DeformCurvesOnSurface, curves=self

Node
 - class_name : [DeformCurvesOnSurface](/docs/classes/DeformCurvesOnSurface.md)
 - bl_idname : GeometryNodeDeformCurvesOnSurface

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - curves : self
 - node_label : node_label
 - node_color : node_color

``` python
def deform_curves_on_surface(self, node_label=None, node_color=None):
```
### delete_geometry

DeleteGeometry, geometry=self

Node
 - class_name : [DeleteGeometry](/docs/classes/DeleteGeometry.md)
 - bl_idname : GeometryNodeDeleteGeometry

Arguments
 - selection : None
 - domain : 'POINT'
 - mode : 'ALL'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - selection : self._get_selection(selection)
 - domain : domain
 - mode : mode
 - node_label : node_label
 - node_color : node_color

``` python
def delete_geometry(self, selection=None, domain='POINT', mode='ALL', node_label=None, node_color=None):
```
### difference

MeshBoolean, mesh_1=self, mesh_2=args

Node
 - class_name : [MeshBoolean](/docs/classes/MeshBoolean.md)
 - bl_idname : GeometryNodeMeshBoolean

Arguments
 - *args : 
 - mesh_2 : None
 - self_intersection : None
 - hole_tolerant : None
 - node_label : None
 - node_color : None

Node initialization
 - *args : 
 - mesh_1 : self
 - mesh_2 : mesh_2
 - self_intersection : self_intersection
 - hole_tolerant : hole_tolerant
 - operation : 'DIFFERENCE'
 - node_label : node_label
 - node_color : node_color

``` python
def difference(self, *args, mesh_2=None, self_intersection=None, hole_tolerant=None, node_label=None, node_color=None):
```
### distribute_points_in_volume

DistributePointsInVolume, volume=self

Node
 - class_name : [DistributePointsInVolume](/docs/classes/DistributePointsInVolume.md)
 - bl_idname : GeometryNodeDistributePointsInVolume

Arguments
 - density : None
 - seed : None
 - spacing : None
 - threshold : None
 - mode : 'DENSITY_RANDOM'
 - node_label : None
 - node_color : None

Node initialization
 - volume : self
 - density : density
 - seed : seed
 - spacing : spacing
 - threshold : threshold
 - mode : mode
 - node_label : node_label
 - node_color : node_color

``` python
def distribute_points_in_volume(self, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM', node_label=None, node_color=None):
```
### distribute_points_on_faces

DistributePointsOnFaces, mesh=self

Node
 - class_name : [DistributePointsOnFaces](/docs/classes/DistributePointsOnFaces.md)
 - bl_idname : GeometryNodeDistributePointsOnFaces

Arguments
 - density : None
 - seed : None
 - distance_min : None
 - density_max : None
 - density_factor : None
 - selection : None
 - distribute_method : 'RANDOM'
 - use_legacy_normal : False
 - node_label : None
 - node_color : None

Node initialization
 - mesh : self
 - density : density
 - seed : seed
 - distance_min : distance_min
 - density_max : density_max
 - density_factor : density_factor
 - selection : self._get_selection(selection)
 - distribute_method : distribute_method
 - use_legacy_normal : use_legacy_normal
 - node_label : node_label
 - node_color : node_color

``` python
def distribute_points_on_faces(self, density=None, seed=None, distance_min=None, density_max=None, density_factor=None, selection=None, distribute_method='RANDOM', use_legacy_normal=False, node_label=None, node_color=None):
```
### domain_size

DomainSize, geometry=self, return node

Node
 - class_name : [DomainSize](/docs/classes/DomainSize.md)
 - bl_idname : GeometryNodeAttributeDomainSize

Arguments
 - component : 'MESH'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - component : component
 - node_label : node_label
 - node_color : node_color

``` python
def domain_size(self, component='MESH', node_label=None, node_color=None):
```
### dual_mesh

DualMesh, mesh=self

Node
 - class_name : [DualMesh](/docs/classes/DualMesh.md)
 - bl_idname : GeometryNodeDualMesh

Arguments
 - keep_boundaries : None
 - node_label : None
 - node_color : None

Node initialization
 - mesh : self
 - keep_boundaries : keep_boundaries
 - node_label : node_label
 - node_color : node_color

``` python
def dual_mesh(self, keep_boundaries=None, node_label=None, node_color=None):
```
### duplicate_elements

DuplicateElements, geometry=self

Node
 - class_name : [DuplicateElements](/docs/classes/DuplicateElements.md)
 - bl_idname : GeometryNodeDuplicateElements

Arguments
 - amount : None
 - selection : None
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - amount : amount
 - selection : self._get_selection(selection)
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def duplicate_elements(self, amount=None, selection=None, domain='POINT', node_label=None, node_color=None):
```
### edge_paths_to_curves

EdgePathsToCurves, mesh=self

Node
 - class_name : [EdgePathsToCurves](/docs/classes/EdgePathsToCurves.md)
 - bl_idname : GeometryNodeEdgePathsToCurves

Arguments
 - start_vertices : None
 - next_vertex_index : None
 - node_label : None
 - node_color : None

Node initialization
 - mesh : self
 - start_vertices : start_vertices
 - next_vertex_index : next_vertex_index
 - node_label : node_label
 - node_color : node_color

``` python
def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None, node_label=None, node_color=None):
```
### extrude_mesh

ExtrudeMesh, mesh=self

Node
 - class_name : [ExtrudeMesh](/docs/classes/ExtrudeMesh.md)
 - bl_idname : GeometryNodeExtrudeMesh

Arguments
 - offset : None
 - offset_scale : None
 - individual : None
 - selection : None
 - mode : 'FACES'
 - node_label : None
 - node_color : None

Node initialization
 - mesh : self
 - offset : offset
 - offset_scale : offset_scale
 - individual : individual
 - selection : self._get_selection(selection)
 - mode : mode
 - node_label : node_label
 - node_color : node_color

``` python
def extrude_mesh(self, offset=None, offset_scale=None, individual=None, selection=None, mode='FACES', node_label=None, node_color=None):
```
### fill_curve

FillCurve, curve=self

Node
 - class_name : [FillCurve](/docs/classes/FillCurve.md)
 - bl_idname : GeometryNodeFillCurve

Arguments
 - mode : 'TRIANGLES'
 - node_label : None
 - node_color : None

Node initialization
 - curve : self
 - mode : mode
 - node_label : node_label
 - node_color : node_color

``` python
def fill_curve(self, mode='TRIANGLES', node_label=None, node_color=None):
```
### fillet_curve

FilletCurve, curve=self

Node
 - class_name : [FilletCurve](/docs/classes/FilletCurve.md)
 - bl_idname : GeometryNodeFilletCurve

Arguments
 - radius : None
 - limit_radius : None
 - count : None
 - mode : 'BEZIER'
 - node_label : None
 - node_color : None

Node initialization
 - curve : self
 - radius : radius
 - limit_radius : limit_radius
 - count : count
 - mode : mode
 - node_label : node_label
 - node_color : node_color

``` python
def fillet_curve(self, radius=None, limit_radius=None, count=None, mode='BEZIER', node_label=None, node_color=None):
```
### flip_faces

FlipFaces, mesh=self

Node
 - class_name : [FlipFaces](/docs/classes/FlipFaces.md)
 - bl_idname : GeometryNodeFlipFaces

Arguments
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - mesh : self
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def flip_faces(self, selection=None, node_label=None, node_color=None):
```
### geometry_to_instance

GeometryToInstance, geometry=self

Node
 - class_name : [GeometryToInstance](/docs/classes/GeometryToInstance.md)
 - bl_idname : GeometryNodeGeometryToInstance

Arguments
 - *args : 
 - node_label : None
 - node_color : None

Node initialization
 - *args : 
 - geometry : self
 - node_label : node_label
 - node_color : node_color

``` python
def geometry_to_instance(self, *args, node_label=None, node_color=None):
```
### instance_on_points

InstanceOnPoints, points=self

Node
 - class_name : [InstanceOnPoints](/docs/classes/InstanceOnPoints.md)
 - bl_idname : GeometryNodeInstanceOnPoints

Arguments
 - instance : None
 - pick_instance : None
 - instance_index : None
 - rotation : None
 - scale : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - points : self
 - instance : instance
 - pick_instance : pick_instance
 - instance_index : instance_index
 - rotation : rotation
 - scale : scale
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None, selection=None, node_label=None, node_color=None):
```
### instances_to_points

InstancesToPoints, instances=self

Node
 - class_name : [InstancesToPoints](/docs/classes/InstancesToPoints.md)
 - bl_idname : GeometryNodeInstancesToPoints

Arguments
 - position : None
 - radius : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - instances : self
 - position : position
 - radius : radius
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def instances_to_points(self, position=None, radius=None, selection=None, node_label=None, node_color=None):
```
### interpolate_curves

InterpolateCurves, guide_curves=self

Node
 - class_name : [InterpolateCurves](/docs/classes/InterpolateCurves.md)
 - bl_idname : GeometryNodeInterpolateCurves

Arguments
 - guide_up : None
 - guide_group_id : None
 - points : None
 - point_up : None
 - point_group_id : None
 - max_neighbors : None
 - node_label : None
 - node_color : None

Node initialization
 - guide_curves : self
 - guide_up : guide_up
 - guide_group_id : guide_group_id
 - points : points
 - point_up : point_up
 - point_group_id : point_group_id
 - max_neighbors : max_neighbors
 - node_label : node_label
 - node_color : node_color

``` python
def interpolate_curves(self, guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None, node_label=None, node_color=None):
```
### intersect

MeshBoolean, mesh=geometry + args

Node
 - class_name : [MeshBoolean](/docs/classes/MeshBoolean.md)
 - bl_idname : GeometryNodeMeshBoolean

Arguments
 - *args : 
 - self_intersection : None
 - hole_tolerant : None
 - node_label : None
 - node_color : None

Node initialization
 - *args : 
 - mesh_2 : self
 - self_intersection : self_intersection
 - hole_tolerant : hole_tolerant
 - operation : 'INTERSECT'
 - node_label : node_label
 - node_color : node_color

``` python
def intersect(self, *args, self_intersection=None, hole_tolerant=None, node_label=None, node_color=None):
```
### join_geometry

JoinGeometry, geometry=self

Node
 - class_name : [JoinGeometry](/docs/classes/JoinGeometry.md)
 - bl_idname : GeometryNodeJoinGeometry

Arguments
 - *args : 
 - node_label : None
 - node_color : None

Node initialization
 - *args : 
 - geometry : self
 - node_label : node_label
 - node_color : node_color

``` python
def join_geometry(self, *args, node_label=None, node_color=None):
```
### mean_filter_sdf_volume

MeanFilterSDFVolume, volume=self

Node
 - class_name : [MeanFilterSDFVolume](/docs/classes/MeanFilterSDFVolume.md)
 - bl_idname : GeometryNodeMeanFilterSDFVolume

Arguments
 - iterations : None
 - width : None
 - node_label : None
 - node_color : None

Node initialization
 - volume : self
 - iterations : iterations
 - width : width
 - node_label : node_label
 - node_color : node_color

``` python
def mean_filter_sdf_volume(self, iterations=None, width=None, node_label=None, node_color=None):
```
### merge_by_distance

MergeByDistance, geometry=self

Node
 - class_name : [MergeByDistance](/docs/classes/MergeByDistance.md)
 - bl_idname : GeometryNodeMergeByDistance

Arguments
 - distance : None
 - selection : None
 - mode : 'ALL'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - distance : distance
 - selection : self._get_selection(selection)
 - mode : mode
 - node_label : node_label
 - node_color : node_color

``` python
def merge_by_distance(self, distance=None, selection=None, mode='ALL', node_label=None, node_color=None):
```
### mesh_boolean

MeshBoolean, mesh_1=self

Node
 - class_name : [MeshBoolean](/docs/classes/MeshBoolean.md)
 - bl_idname : GeometryNodeMeshBoolean

Arguments
 - *args : 
 - mesh_2 : None
 - self_intersection : None
 - hole_tolerant : None
 - operation : 'DIFFERENCE'
 - node_label : None
 - node_color : None

Node initialization
 - *args : 
 - mesh_1 : self
 - mesh_2 : mesh_2
 - self_intersection : self_intersection
 - hole_tolerant : hole_tolerant
 - operation : operation
 - node_label : node_label
 - node_color : node_color

``` python
def mesh_boolean(self, *args, mesh_2=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE', node_label=None, node_color=None):
```
### mesh_to_curve

MeshToCurve, mesh=self

Node
 - class_name : [MeshToCurve](/docs/classes/MeshToCurve.md)
 - bl_idname : GeometryNodeMeshToCurve

Arguments
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - mesh : self
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def mesh_to_curve(self, selection=None, node_label=None, node_color=None):
```
### mesh_to_points

MeshToPoints, mesh=self

Node
 - class_name : [MeshToPoints](/docs/classes/MeshToPoints.md)
 - bl_idname : GeometryNodeMeshToPoints

Arguments
 - position : None
 - radius : None
 - selection : None
 - mode : 'VERTICES'
 - node_label : None
 - node_color : None

Node initialization
 - mesh : self
 - position : position
 - radius : radius
 - selection : self._get_selection(selection)
 - mode : mode
 - node_label : node_label
 - node_color : node_color

``` python
def mesh_to_points(self, position=None, radius=None, selection=None, mode='VERTICES', node_label=None, node_color=None):
```
### mesh_to_sdf_volume

MeshToSDFVolume, mesh=self

Node
 - class_name : [MeshToSDFVolume](/docs/classes/MeshToSDFVolume.md)
 - bl_idname : GeometryNodeMeshToSDFVolume

Arguments
 - voxel_amount : None
 - half_band_width : None
 - voxel_size : None
 - resolution_mode : 'VOXEL_AMOUNT'
 - node_label : None
 - node_color : None

Node initialization
 - mesh : self
 - voxel_amount : voxel_amount
 - half_band_width : half_band_width
 - voxel_size : voxel_size
 - resolution_mode : resolution_mode
 - node_label : node_label
 - node_color : node_color

``` python
def mesh_to_sdf_volume(self, voxel_amount=None, half_band_width=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None):
```
### mesh_to_volume

MeshToVolume, mesh=self

Node
 - class_name : [MeshToVolume](/docs/classes/MeshToVolume.md)
 - bl_idname : GeometryNodeMeshToVolume

Arguments
 - density : None
 - voxel_amount : None
 - interior_band_width : None
 - voxel_size : None
 - resolution_mode : 'VOXEL_AMOUNT'
 - node_label : None
 - node_color : None

Node initialization
 - mesh : self
 - density : density
 - voxel_amount : voxel_amount
 - interior_band_width : interior_band_width
 - voxel_size : voxel_size
 - resolution_mode : resolution_mode
 - node_label : node_label
 - node_color : node_color

``` python
def mesh_to_volume(self, density=None, voxel_amount=None, interior_band_width=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None):
```
### offset_sdf_volume

OffsetSDFVolume, volume=self

Node
 - class_name : [OffsetSDFVolume](/docs/classes/OffsetSDFVolume.md)
 - bl_idname : GeometryNodeOffsetSDFVolume

Arguments
 - distance : None
 - node_label : None
 - node_color : None

Node initialization
 - volume : self
 - distance : distance
 - node_label : node_label
 - node_color : node_color

``` python
def offset_sdf_volume(self, distance=None, node_label=None, node_color=None):
```
### points_to_curves

PointsToCurves, points=self

Node
 - class_name : [PointsToCurves](/docs/classes/PointsToCurves.md)
 - bl_idname : GeometryNodePointsToCurves

Arguments
 - curve_group_id : None
 - weight : None
 - node_label : None
 - node_color : None

Node initialization
 - points : self
 - curve_group_id : curve_group_id
 - weight : weight
 - node_label : node_label
 - node_color : node_color

``` python
def points_to_curves(self, curve_group_id=None, weight=None, node_label=None, node_color=None):
```
### points_to_sdf_volume

PointsToSDFVolume, points=self

Node
 - class_name : [PointsToSDFVolume](/docs/classes/PointsToSDFVolume.md)
 - bl_idname : GeometryNodePointsToSDFVolume

Arguments
 - voxel_amount : None
 - radius : None
 - voxel_size : None
 - resolution_mode : 'VOXEL_AMOUNT'
 - node_label : None
 - node_color : None

Node initialization
 - points : self
 - voxel_amount : voxel_amount
 - radius : radius
 - voxel_size : voxel_size
 - resolution_mode : resolution_mode
 - node_label : node_label
 - node_color : node_color

``` python
def points_to_sdf_volume(self, voxel_amount=None, radius=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None):
```
### points_to_vertices

PointsToVertices, points=self

Node
 - class_name : [PointsToVertices](/docs/classes/PointsToVertices.md)
 - bl_idname : GeometryNodePointsToVertices

Arguments
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - points : self
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def points_to_vertices(self, selection=None, node_label=None, node_color=None):
```
### points_to_volume

PointsToVolume, points=self

Node
 - class_name : [PointsToVolume](/docs/classes/PointsToVolume.md)
 - bl_idname : GeometryNodePointsToVolume

Arguments
 - density : None
 - voxel_amount : None
 - radius : None
 - voxel_size : None
 - resolution_mode : 'VOXEL_AMOUNT'
 - node_label : None
 - node_color : None

Node initialization
 - points : self
 - density : density
 - voxel_amount : voxel_amount
 - radius : radius
 - voxel_size : voxel_size
 - resolution_mode : resolution_mode
 - node_label : node_label
 - node_color : node_color

``` python
def points_to_volume(self, density=None, voxel_amount=None, radius=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None):
```
### realize_instances

RealizeInstances, geometry=self

Node
 - class_name : [RealizeInstances](/docs/classes/RealizeInstances.md)
 - bl_idname : GeometryNodeRealizeInstances

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - node_label : node_label
 - node_color : node_color

``` python
def realize_instances(self, node_label=None, node_color=None):
```
### remove_named_attribute

RemoveNamedAttribute, geometry=self

Node
 - class_name : [RemoveNamedAttribute](/docs/classes/RemoveNamedAttribute.md)
 - bl_idname : GeometryNodeRemoveAttribute

Arguments
 - name : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - name : name
 - node_label : node_label
 - node_color : node_color

``` python
def remove_named_attribute(self, name=None, node_label=None, node_color=None):
```
### repeat_output

RepeatOutput, geometry=self

Node
 - class_name : [RepeatOutput](/docs/classes/RepeatOutput.md)
 - bl_idname : GeometryNodeRepeatOutput

Arguments
 - active_index : 0
 - active_item
 - inspection_index : 0
 - repeat_items
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - active_index : active_index
 - active_item : active_item
 - inspection_index : inspection_index
 - repeat_items : repeat_items
 - node_label : node_label
 - node_color : node_color

``` python
def repeat_output(self, active_index=0, active_item=None, inspection_index=0, repeat_items=None, node_label=None, node_color=None):
```
### replace_material

ReplaceMaterial, geometry=self

Node
 - class_name : [ReplaceMaterial](/docs/classes/ReplaceMaterial.md)
 - bl_idname : GeometryNodeReplaceMaterial

Arguments
 - old : None
 - new : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - old : old
 - new : new
 - node_label : node_label
 - node_color : node_color

``` python
def replace_material(self, old=None, new=None, node_label=None, node_color=None):
```
### resample_curve

ResampleCurve, curve=self

Node
 - class_name : [ResampleCurve](/docs/classes/ResampleCurve.md)
 - bl_idname : GeometryNodeResampleCurve

Arguments
 - count : None
 - length : None
 - selection : None
 - mode : 'COUNT'
 - node_label : None
 - node_color : None

Node initialization
 - curve : self
 - count : count
 - length : length
 - selection : self._get_selection(selection)
 - mode : mode
 - node_label : node_label
 - node_color : node_color

``` python
def resample_curve(self, count=None, length=None, selection=None, mode='COUNT', node_label=None, node_color=None):
```
### reverse_curve

ReverseCurve, curve=self

Node
 - class_name : [ReverseCurve](/docs/classes/ReverseCurve.md)
 - bl_idname : GeometryNodeReverseCurve

Arguments
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - curve : self
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def reverse_curve(self, selection=None, node_label=None, node_color=None):
```
### rotate_instances

RotateInstances, instances=self

Node
 - class_name : [RotateInstances](/docs/classes/RotateInstances.md)
 - bl_idname : GeometryNodeRotateInstances

Arguments
 - rotation : None
 - pivot_point : None
 - local_space : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - instances : self
 - rotation : rotation
 - pivot_point : pivot_point
 - local_space : local_space
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def rotate_instances(self, rotation=None, pivot_point=None, local_space=None, selection=None, node_label=None, node_color=None):
```
### sample_index_boolean

SampleIndex, value=self, data_type='BOOLEAN'

Node
 - class_name : [SampleIndex](/docs/classes/SampleIndex.md)
 - bl_idname : GeometryNodeSampleIndex

Arguments
 - value : None
 - index : None
 - clamp : False
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - value : value
 - index : index
 - clamp : clamp
 - data_type : 'BOOLEAN'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def sample_index_boolean(self, value=None, index=None, clamp=False, domain='POINT', node_label=None, node_color=None):
```
### sample_index_color

SampleIndex, value=self, data_type='FLOAT_COLOR'

Node
 - class_name : [SampleIndex](/docs/classes/SampleIndex.md)
 - bl_idname : GeometryNodeSampleIndex

Arguments
 - value : None
 - index : None
 - clamp : False
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - value : value
 - index : index
 - clamp : clamp
 - data_type : 'FLOAT_COLOR'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def sample_index_color(self, value=None, index=None, clamp=False, domain='POINT', node_label=None, node_color=None):
```
### sample_index_float

SampleIndex, value=self, data_type='FLOAT'

Node
 - class_name : [SampleIndex](/docs/classes/SampleIndex.md)
 - bl_idname : GeometryNodeSampleIndex

Arguments
 - value : None
 - index : None
 - clamp : False
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - value : value
 - index : index
 - clamp : clamp
 - data_type : 'FLOAT'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def sample_index_float(self, value=None, index=None, clamp=False, domain='POINT', node_label=None, node_color=None):
```
### sample_index_int

SampleIndex, value=self, data_type='INT'

Node
 - class_name : [SampleIndex](/docs/classes/SampleIndex.md)
 - bl_idname : GeometryNodeSampleIndex

Arguments
 - value : None
 - index : None
 - clamp : False
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - value : value
 - index : index
 - clamp : clamp
 - data_type : 'INT'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def sample_index_int(self, value=None, index=None, clamp=False, domain='POINT', node_label=None, node_color=None):
```
### sample_index_quaternion

SampleIndex, value=self, data_type='QUATERNION'

Node
 - class_name : [SampleIndex](/docs/classes/SampleIndex.md)
 - bl_idname : GeometryNodeSampleIndex

Arguments
 - value : None
 - index : None
 - clamp : False
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - value : value
 - index : index
 - clamp : clamp
 - data_type : 'QUATERNION'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def sample_index_quaternion(self, value=None, index=None, clamp=False, domain='POINT', node_label=None, node_color=None):
```
### sample_index_vector

SampleIndex, value=self, data_type='FLOAT_VECTOR'

Node
 - class_name : [SampleIndex](/docs/classes/SampleIndex.md)
 - bl_idname : GeometryNodeSampleIndex

Arguments
 - value : None
 - index : None
 - clamp : False
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - value : value
 - index : index
 - clamp : clamp
 - data_type : 'FLOAT_VECTOR'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def sample_index_vector(self, value=None, index=None, clamp=False, domain='POINT', node_label=None, node_color=None):
```
### scale_elements

ScaleElements, geometry=self

Node
 - class_name : [ScaleElements](/docs/classes/ScaleElements.md)
 - bl_idname : GeometryNodeScaleElements

Arguments
 - scale : None
 - center : None
 - axis : None
 - selection : None
 - domain : 'FACE'
 - scale_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - scale : scale
 - center : center
 - axis : axis
 - selection : self._get_selection(selection)
 - domain : domain
 - scale_mode : scale_mode
 - node_label : node_label
 - node_color : node_color

``` python
def scale_elements(self, scale=None, center=None, axis=None, selection=None, domain='FACE', scale_mode='UNIFORM', node_label=None, node_color=None):
```
### scale_instances

ScaleInstances, instances=self

Node
 - class_name : [ScaleInstances](/docs/classes/ScaleInstances.md)
 - bl_idname : GeometryNodeScaleInstances

Arguments
 - scale : None
 - center : None
 - local_space : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - instances : self
 - scale : scale
 - center : center
 - local_space : local_space
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def scale_instances(self, scale=None, center=None, local_space=None, selection=None, node_label=None, node_color=None):
```
### separate_components

SeparateComponents, geometry=self

Node
 - class_name : [SeparateComponents](/docs/classes/SeparateComponents.md)
 - bl_idname : GeometryNodeSeparateComponents

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - node_label : node_label
 - node_color : node_color

``` python
def separate_components(self, node_label=None, node_color=None):
```
### separate_geometry

SeparateGeometry, geometry=self

Node
 - class_name : [SeparateGeometry](/docs/classes/SeparateGeometry.md)
 - bl_idname : GeometryNodeSeparateGeometry

Arguments
 - selection : None
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - selection : self._get_selection(selection)
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def separate_geometry(self, selection=None, domain='POINT', node_label=None, node_color=None):
```
### set_curve_normal

SetCurveNormal, curve=self

Node
 - class_name : [SetCurveNormal](/docs/classes/SetCurveNormal.md)
 - bl_idname : GeometryNodeSetCurveNormal

Arguments
 - selection : None
 - mode : 'MINIMUM_TWIST'
 - node_label : None
 - node_color : None

Node initialization
 - curve : self
 - selection : self._get_selection(selection)
 - mode : mode
 - node_label : node_label
 - node_color : node_color

``` python
def set_curve_normal(self, selection=None, mode='MINIMUM_TWIST', node_label=None, node_color=None):
```
### set_curve_radius

SetCurveRadius, curve=self

Node
 - class_name : [SetCurveRadius](/docs/classes/SetCurveRadius.md)
 - bl_idname : GeometryNodeSetCurveRadius

Arguments
 - radius : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - curve : self
 - radius : radius
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def set_curve_radius(self, radius=None, selection=None, node_label=None, node_color=None):
```
### set_curve_tilt

SetCurveTilt, curve=self

Node
 - class_name : [SetCurveTilt](/docs/classes/SetCurveTilt.md)
 - bl_idname : GeometryNodeSetCurveTilt

Arguments
 - tilt : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - curve : self
 - tilt : tilt
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def set_curve_tilt(self, tilt=None, selection=None, node_label=None, node_color=None):
```
### set_face_set

SetFaceSet, mesh=self

Node
 - class_name : [SetFaceSet](/docs/classes/SetFaceSet.md)
 - bl_idname : GeometryNodeToolSetFaceSet

Arguments
 - face_set : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - mesh : self
 - face_set : face_set
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def set_face_set(self, face_set=None, selection=None, node_label=None, node_color=None):
```
### set_handle_positions

SetHandlePositions, curve=self

Node
 - class_name : [SetHandlePositions](/docs/classes/SetHandlePositions.md)
 - bl_idname : GeometryNodeSetCurveHandlePositions

Arguments
 - position : None
 - offset : None
 - selection : None
 - mode : 'LEFT'
 - node_label : None
 - node_color : None

Node initialization
 - curve : self
 - position : position
 - offset : offset
 - selection : self._get_selection(selection)
 - mode : mode
 - node_label : node_label
 - node_color : node_color

``` python
def set_handle_positions(self, position=None, offset=None, selection=None, mode='LEFT', node_label=None, node_color=None):
```
### set_handle_type

SetHandleType, curve=self

Node
 - class_name : [SetHandleType](/docs/classes/SetHandleType.md)
 - bl_idname : GeometryNodeCurveSetHandles

Arguments
 - selection : None
 - handle_type : 'AUTO'
 - mode : {'RIGHT', 'LEFT'}
 - node_label : None
 - node_color : None

Node initialization
 - curve : self
 - selection : self._get_selection(selection)
 - handle_type : handle_type
 - mode : mode
 - node_label : node_label
 - node_color : node_color

``` python
def set_handle_type(self, selection=None, handle_type='AUTO', mode={'RIGHT', 'LEFT'}, node_label=None, node_color=None):
```
### set_id

SetID, geometry=self

Node
 - class_name : [SetID](/docs/classes/SetID.md)
 - bl_idname : GeometryNodeSetID

Arguments
 - ID : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - ID : ID
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def set_id(self, ID=None, selection=None, node_label=None, node_color=None):
```
### set_material

SetMaterial, geometry=self

Node
 - class_name : [SetMaterial](/docs/classes/SetMaterial.md)
 - bl_idname : GeometryNodeSetMaterial

Arguments
 - material : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - material : material
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def set_material(self, material=None, selection=None, node_label=None, node_color=None):
```
### set_material_index

SetMaterialIndex, geometry=self

Node
 - class_name : [SetMaterialIndex](/docs/classes/SetMaterialIndex.md)
 - bl_idname : GeometryNodeSetMaterialIndex

Arguments
 - material_index : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - material_index : material_index
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def set_material_index(self, material_index=None, selection=None, node_label=None, node_color=None):
```
### set_point_radius

SetPointRadius, points=self

Node
 - class_name : [SetPointRadius](/docs/classes/SetPointRadius.md)
 - bl_idname : GeometryNodeSetPointRadius

Arguments
 - radius : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - points : self
 - radius : radius
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def set_point_radius(self, radius=None, selection=None, node_label=None, node_color=None):
```
### set_position

SetPosition, geometry=self

Node
 - class_name : [SetPosition](/docs/classes/SetPosition.md)
 - bl_idname : GeometryNodeSetPosition

Arguments
 - position : None
 - offset : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - position : position
 - offset : offset
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def set_position(self, position=None, offset=None, selection=None, node_label=None, node_color=None):
```
### set_selection

SetSelection, geometry=self

Node
 - class_name : [SetSelection](/docs/classes/SetSelection.md)
 - bl_idname : GeometryNodeToolSetSelection

Arguments
 - selection : None
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - selection : self._get_selection(selection)
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def set_selection(self, selection=None, domain='POINT', node_label=None, node_color=None):
```
### set_shade_smooth

SetShadeSmooth, geometry=self

Node
 - class_name : [SetShadeSmooth](/docs/classes/SetShadeSmooth.md)
 - bl_idname : GeometryNodeSetShadeSmooth

Arguments
 - shade_smooth : None
 - selection : None
 - domain : 'FACE'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - shade_smooth : shade_smooth
 - selection : self._get_selection(selection)
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def set_shade_smooth(self, shade_smooth=None, selection=None, domain='FACE', node_label=None, node_color=None):
```
### set_spline_cyclic

SetSplineCyclic, geometry=self

Node
 - class_name : [SetSplineCyclic](/docs/classes/SetSplineCyclic.md)
 - bl_idname : GeometryNodeSetSplineCyclic

Arguments
 - cyclic : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - cyclic : cyclic
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def set_spline_cyclic(self, cyclic=None, selection=None, node_label=None, node_color=None):
```
### set_spline_resolution

SetSplineResolution, geometry=self

Node
 - class_name : [SetSplineResolution](/docs/classes/SetSplineResolution.md)
 - bl_idname : GeometryNodeSetSplineResolution

Arguments
 - resolution : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - resolution : resolution
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def set_spline_resolution(self, resolution=None, selection=None, node_label=None, node_color=None):
```
### set_spline_type

SetSplineType, curve=self

Node
 - class_name : [SetSplineType](/docs/classes/SetSplineType.md)
 - bl_idname : GeometryNodeCurveSplineType

Arguments
 - selection : None
 - spline_type : 'POLY'
 - node_label : None
 - node_color : None

Node initialization
 - curve : self
 - selection : self._get_selection(selection)
 - spline_type : spline_type
 - node_label : node_label
 - node_color : node_color

``` python
def set_spline_type(self, selection=None, spline_type='POLY', node_label=None, node_color=None):
```
### simulation_output

SimulationOutput, geometry=self

Node
 - class_name : [SimulationOutput](/docs/classes/SimulationOutput.md)
 - bl_idname : GeometryNodeSimulationOutput

Arguments
 - skip : None
 - active_index : 0
 - active_item
 - state_items
 - node_label : None
 - node_color : None

Node initialization
 - skip : skip
 - geometry : self
 - active_index : active_index
 - active_item : active_item
 - state_items : state_items
 - node_label : node_label
 - node_color : node_color

``` python
def simulation_output(self, skip=None, active_index=0, active_item=None, state_items=None, node_label=None, node_color=None):
```
### split_edges

SplitEdges, mesh=self

Node
 - class_name : [SplitEdges](/docs/classes/SplitEdges.md)
 - bl_idname : GeometryNodeSplitEdges

Arguments
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - mesh : self
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def split_edges(self, selection=None, node_label=None, node_color=None):
```
### store_named_attribute

StoreNamedAttribute, geometry=self

Node
 - class_name : [StoreNamedAttribute](/docs/classes/StoreNamedAttribute.md)
 - bl_idname : GeometryNodeStoreNamedAttribute

Arguments
 - name : None
 - value : None
 - selection : None
 - data_type : 'FLOAT'
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - name : name
 - value : value
 - selection : self._get_selection(selection)
 - data_type : data_type
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def store_named_attribute(self, name=None, value=None, selection=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):
```
### store_named_boolean

StoreNamedAttribute, geometry=self, data_type='BOOLEAN'

Node
 - class_name : [StoreNamedAttribute](/docs/classes/StoreNamedAttribute.md)
 - bl_idname : GeometryNodeStoreNamedAttribute

Arguments
 - name : None
 - value : None
 - selection : None
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - name : name
 - value : value
 - selection : self._get_selection(selection)
 - data_type : 'BOOLEAN'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def store_named_boolean(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None):
```
### store_named_byte_color

StoreNamedAttribute, geometry=self, data_type='BYTE_COLOR'

Node
 - class_name : [StoreNamedAttribute](/docs/classes/StoreNamedAttribute.md)
 - bl_idname : GeometryNodeStoreNamedAttribute

Arguments
 - name : None
 - value : None
 - selection : None
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - name : name
 - value : value
 - selection : self._get_selection(selection)
 - data_type : 'BYTE_COLOR'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def store_named_byte_color(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None):
```
### store_named_float

StoreNamedAttribute, geometry=self, data_type='FLOAT'

Node
 - class_name : [StoreNamedAttribute](/docs/classes/StoreNamedAttribute.md)
 - bl_idname : GeometryNodeStoreNamedAttribute

Arguments
 - name : None
 - value : None
 - selection : None
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - name : name
 - value : value
 - selection : self._get_selection(selection)
 - data_type : 'FLOAT'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def store_named_float(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None):
```
### store_named_float2

StoreNamedAttribute, geometry=self, data_type='FLOAT2'

Node
 - class_name : [StoreNamedAttribute](/docs/classes/StoreNamedAttribute.md)
 - bl_idname : GeometryNodeStoreNamedAttribute

Arguments
 - name : None
 - value : None
 - selection : None
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - name : name
 - value : value
 - selection : self._get_selection(selection)
 - data_type : 'FLOAT2'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def store_named_float2(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None):
```
### store_named_float_color

StoreNamedAttribute, geometry=self, data_type='FLOAT_COLOR'

Node
 - class_name : [StoreNamedAttribute](/docs/classes/StoreNamedAttribute.md)
 - bl_idname : GeometryNodeStoreNamedAttribute

Arguments
 - name : None
 - value : None
 - selection : None
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - name : name
 - value : value
 - selection : self._get_selection(selection)
 - data_type : 'FLOAT_COLOR'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def store_named_float_color(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None):
```
### store_named_int

StoreNamedAttribute, geometry=self, data_type='INT'

Node
 - class_name : [StoreNamedAttribute](/docs/classes/StoreNamedAttribute.md)
 - bl_idname : GeometryNodeStoreNamedAttribute

Arguments
 - name : None
 - value : None
 - selection : None
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - name : name
 - value : value
 - selection : self._get_selection(selection)
 - data_type : 'INT'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def store_named_int(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None):
```
### store_named_quaternion

StoreNamedAttribute, geometry=self, data_type='QUATERNION'

Node
 - class_name : [StoreNamedAttribute](/docs/classes/StoreNamedAttribute.md)
 - bl_idname : GeometryNodeStoreNamedAttribute

Arguments
 - name : None
 - value : None
 - selection : None
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - name : name
 - value : value
 - selection : self._get_selection(selection)
 - data_type : 'QUATERNION'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def store_named_quaternion(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None):
```
### store_named_vector

StoreNamedAttribute, geometry=self, data_type='FLOAT_VECTOR'

Node
 - class_name : [StoreNamedAttribute](/docs/classes/StoreNamedAttribute.md)
 - bl_idname : GeometryNodeStoreNamedAttribute

Arguments
 - name : None
 - value : None
 - selection : None
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - name : name
 - value : value
 - selection : self._get_selection(selection)
 - data_type : 'FLOAT_VECTOR'
 - domain : domain
 - node_label : node_label
 - node_color : node_color

``` python
def store_named_vector(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None):
```
### subdivide_curve

SubdivideCurve, curve=self

Node
 - class_name : [SubdivideCurve](/docs/classes/SubdivideCurve.md)
 - bl_idname : GeometryNodeSubdivideCurve

Arguments
 - cuts : None
 - node_label : None
 - node_color : None

Node initialization
 - curve : self
 - cuts : cuts
 - node_label : node_label
 - node_color : node_color

``` python
def subdivide_curve(self, cuts=None, node_label=None, node_color=None):
```
### subdivide_mesh

SubdivideMesh, mesh=self

Node
 - class_name : [SubdivideMesh](/docs/classes/SubdivideMesh.md)
 - bl_idname : GeometryNodeSubdivideMesh

Arguments
 - level : None
 - node_label : None
 - node_color : None

Node initialization
 - mesh : self
 - level : level
 - node_label : node_label
 - node_color : node_color

``` python
def subdivide_mesh(self, level=None, node_label=None, node_color=None):
```
### subdivision_surface

SubdivisionSurface, mesh=self

Node
 - class_name : [SubdivisionSurface](/docs/classes/SubdivisionSurface.md)
 - bl_idname : GeometryNodeSubdivisionSurface

Arguments
 - level : None
 - edge_crease : None
 - vertex_crease : None
 - boundary_smooth : 'ALL'
 - uv_smooth : 'PRESERVE_BOUNDARIES'
 - node_label : None
 - node_color : None

Node initialization
 - mesh : self
 - level : level
 - edge_crease : edge_crease
 - vertex_crease : vertex_crease
 - boundary_smooth : boundary_smooth
 - uv_smooth : uv_smooth
 - node_label : node_label
 - node_color : node_color

``` python
def subdivision_surface(self, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', node_label=None, node_color=None):
```
### switch

Switch, false=self, input_type='GEOMETRY'

Node
 - class_name : [Switch](/docs/classes/Switch.md)
 - bl_idname : GeometryNodeSwitch

Arguments
 - switch : None
 - true : None
 - node_label : None
 - node_color : None

Node initialization
 - switch : switch
 - false : self
 - true : true
 - input_type : 'GEOMETRY'
 - node_label : node_label
 - node_color : node_color

``` python
def switch(self, switch=None, true=None, node_label=None, node_color=None):
```
### transform_geometry

TransformGeometry, geometry=self

Node
 - class_name : [TransformGeometry](/docs/classes/TransformGeometry.md)
 - bl_idname : GeometryNodeTransform

Arguments
 - translation : None
 - rotation : None
 - scale : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - translation : translation
 - rotation : rotation
 - scale : scale
 - node_label : node_label
 - node_color : node_color

``` python
def transform_geometry(self, translation=None, rotation=None, scale=None, node_label=None, node_color=None):
```
### translate_instances

TranslateInstances, instances=self

Node
 - class_name : [TranslateInstances](/docs/classes/TranslateInstances.md)
 - bl_idname : GeometryNodeTranslateInstances

Arguments
 - translation : None
 - local_space : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - instances : self
 - translation : translation
 - local_space : local_space
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

``` python
def translate_instances(self, translation=None, local_space=None, selection=None, node_label=None, node_color=None):
```
### triangulate

Triangulate, mesh=self

Node
 - class_name : [Triangulate](/docs/classes/Triangulate.md)
 - bl_idname : GeometryNodeTriangulate

Arguments
 - minimum_vertices : None
 - selection : None
 - ngon_method : 'BEAUTY'
 - quad_method : 'SHORTEST_DIAGONAL'
 - node_label : None
 - node_color : None

Node initialization
 - mesh : self
 - minimum_vertices : minimum_vertices
 - selection : self._get_selection(selection)
 - ngon_method : ngon_method
 - quad_method : quad_method
 - node_label : node_label
 - node_color : node_color

``` python
def triangulate(self, minimum_vertices=None, selection=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL', node_label=None, node_color=None):
```
### trim_curve

TrimCurve, curve=self

Node
 - class_name : [TrimCurve](/docs/classes/TrimCurve.md)
 - bl_idname : GeometryNodeTrimCurve

Arguments
 - start : None
 - end : None
 - selection : None
 - mode : 'FACTOR'
 - node_label : None
 - node_color : None

Node initialization
 - curve : self
 - start : start
 - end : end
 - selection : self._get_selection(selection)
 - mode : mode
 - node_label : node_label
 - node_color : node_color

``` python
def trim_curve(self, start=None, end=None, selection=None, mode='FACTOR', node_label=None, node_color=None):
```
### union

MeshBoolean, mesh=geometry + args

Node
 - class_name : [MeshBoolean](/docs/classes/MeshBoolean.md)
 - bl_idname : GeometryNodeMeshBoolean

Arguments
 - *args : 
 - self_intersection : None
 - hole_tolerant : None
 - node_label : None
 - node_color : None

Node initialization
 - *args : 
 - mesh_2 : self
 - self_intersection : self_intersection
 - hole_tolerant : hole_tolerant
 - operation : 'UNION'
 - node_label : node_label
 - node_color : node_color

``` python
def union(self, *args, self_intersection=None, hole_tolerant=None, node_label=None, node_color=None):
```
### volume_to_mesh

VolumeToMesh, volume=self

Node
 - class_name : [VolumeToMesh](/docs/classes/VolumeToMesh.md)
 - bl_idname : GeometryNodeVolumeToMesh

Arguments
 - threshold : None
 - adaptivity : None
 - voxel_amount : None
 - voxel_size : None
 - resolution_mode : 'GRID'
 - node_label : None
 - node_color : None

Node initialization
 - volume : self
 - threshold : threshold
 - adaptivity : adaptivity
 - voxel_amount : voxel_amount
 - voxel_size : voxel_size
 - resolution_mode : resolution_mode
 - node_label : node_label
 - node_color : node_color

``` python
def volume_to_mesh(self, threshold=None, adaptivity=None, voxel_amount=None, voxel_size=None, resolution_mode='GRID', node_label=None, node_color=None):
```
## Properties

### ID

Nodes
 - get : [ID](/docs/classes/ID.md)
 - set : [SetID](/docs/classes/SetID.md)

### curve_radius

Curve radius property

Nodes
 - get : [Radius](/docs/classes/Radius.md)
 - set : [SetCurveRadius](/docs/classes/SetCurveRadius.md)

### curve_tilt

Nodes
 - get : [CurveTilt](/docs/classes/CurveTilt.md)
 - set : [SetCurveTilt](/docs/classes/SetCurveTilt.md)

### edge_neighbors

Nodes
 - get : [EdgeNeighbors](/docs/classes/EdgeNeighbors.md)
 - set : None

### edge_shade_smooth

SetShadeSmooth(domain='EDGE')

Nodes
 - get : [IsEdgeSmooth](/docs/classes/IsEdgeSmooth.md)
 - set : [SetSmooth](/docs/classes/SetSmooth.md)

### face_area

Nodes
 - get : [FaceArea](/docs/classes/FaceArea.md)
 - set : None

### face_shade_smooth

SetShadeSmooth(domain='FACE')

Nodes
 - get : [IsFaceSmooth](/docs/classes/IsFaceSmooth.md)
 - set : [SetSmooth](/docs/classes/SetSmooth.md)

### index

Nodes
 - get : [Index](/docs/classes/Index.md)
 - set : None

### offset

SetPosition(offset=value)

Nodes
 - get : None
 - set : [SetPosition](/docs/classes/SetPosition.md)

### point_radius

Point radius property

Nodes
 - get : [Radius](/docs/classes/Radius.md)
 - set : [SetPointRadius](/docs/classes/SetPointRadius.md)

### position

SetPosition(position=value)

Nodes
 - get : [Position](/docs/classes/Position.md)
 - set : [SetPosition](/docs/classes/SetPosition.md)

### spline_cyclic

Nodes
 - get : [IsSplineCyclic](/docs/classes/IsSplineCyclic.md)
 - set : [SetSplineCyclic](/docs/classes/SetSplineCyclic.md)

### spline_resolution

Nodes
 - get : [SplineResolution](/docs/classes/SplineResolution.md)
 - set : [SetSplineResolution](/docs/classes/SetSplineResolution.md)

### tangent

Nodes
 - get : [CurveTangent](/docs/classes/CurveTangent.md)
 - set : None
