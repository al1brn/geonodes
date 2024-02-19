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

> BoundingBox, geometry=self

``` python
def bounding_box(self, node_label=None, node_color=None):
```
Node
 - class_name : [BoundingBox](/docs/GeoNodes_classes/BoundingBox.md)
 - bl_idname : GeometryNodeBoundBox

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - node_label : node_label
 - node_color : node_color

### capture_attribute

> CaptureAttribute, geometry=self

``` python
def capture_attribute(self, value=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [CaptureAttribute](/docs/GeoNodes_classes/CaptureAttribute.md)
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

### capture_boolean

> CaptureAttribute, geometry=self, data_type='BOOLEAN'

``` python
def capture_boolean(self, value=None, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [CaptureAttribute](/docs/GeoNodes_classes/CaptureAttribute.md)
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

### capture_color

> CaptureAttribute, geometry=self, data_type='FLOAT_COLOR'

``` python
def capture_color(self, value=None, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [CaptureAttribute](/docs/GeoNodes_classes/CaptureAttribute.md)
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

### capture_float

> CaptureAttribute, geometry=self, data_type='FLOAT'

``` python
def capture_float(self, value=None, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [CaptureAttribute](/docs/GeoNodes_classes/CaptureAttribute.md)
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

### capture_int

> CaptureAttribute, geometry=self, data_type='INT'

``` python
def capture_int(self, value=None, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [CaptureAttribute](/docs/GeoNodes_classes/CaptureAttribute.md)
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

### capture_quaternion

> CaptureAttribute, geometry=self, data_type='QUATERNION'

``` python
def capture_quaternion(self, value=None, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [CaptureAttribute](/docs/GeoNodes_classes/CaptureAttribute.md)
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

### capture_vector

> CaptureAttribute, geometry=self, data_type='FLOAT_VECTOR'

``` python
def capture_vector(self, value=None, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [CaptureAttribute](/docs/GeoNodes_classes/CaptureAttribute.md)
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

### convex_hull

> ConvexHull, geometry=self

``` python
def convex_hull(self, node_label=None, node_color=None):
```
Node
 - class_name : [ConvexHull](/docs/GeoNodes_classes/ConvexHull.md)
 - bl_idname : GeometryNodeConvexHull

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - node_label : node_label
 - node_color : node_color

### curve_length

> CurveLength, curve=self, return socket

``` python
def curve_length(self, node_label=None, node_color=None):
```
Node
 - class_name : [CurveLength](/docs/GeoNodes_classes/CurveLength.md)
 - bl_idname : GeometryNodeCurveLength

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - curve : self
 - node_label : node_label
 - node_color : node_color

### curve_to_mesh

> CurveToMesh, curve=self

``` python
def curve_to_mesh(self, profile_curve=None, fill_caps=None, node_label=None, node_color=None):
```
Node
 - class_name : [CurveToMesh](/docs/GeoNodes_classes/CurveToMesh.md)
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

### curve_to_points

> CurveToPoints, curve=self

``` python
def curve_to_points(self, count=None, length=None, mode='COUNT', node_label=None, node_color=None):
```
Node
 - class_name : [CurveToPoints](/docs/GeoNodes_classes/CurveToPoints.md)
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

### deform_curves_on_surface

> DeformCurvesOnSurface, curves=self

``` python
def deform_curves_on_surface(self, node_label=None, node_color=None):
```
Node
 - class_name : [DeformCurvesOnSurface](/docs/GeoNodes_classes/DeformCurvesOnSurface.md)
 - bl_idname : GeometryNodeDeformCurvesOnSurface

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - curves : self
 - node_label : node_label
 - node_color : node_color

### delete_geometry

> DeleteGeometry, geometry=self

``` python
def delete_geometry(self, selection=None, domain='POINT', mode='ALL', node_label=None, node_color=None):
```
Node
 - class_name : [DeleteGeometry](/docs/GeoNodes_classes/DeleteGeometry.md)
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

### difference

> MeshBoolean, mesh_1=self, mesh_2=args

``` python
def difference(self, *args, mesh_2=None, self_intersection=None, hole_tolerant=None, node_label=None, node_color=None):
```
Node
 - class_name : [MeshBoolean](/docs/GeoNodes_classes/MeshBoolean.md)
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

### distribute_points_in_volume

> DistributePointsInVolume, volume=self

``` python
def distribute_points_in_volume(self, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM', node_label=None, node_color=None):
```
Node
 - class_name : [DistributePointsInVolume](/docs/GeoNodes_classes/DistributePointsInVolume.md)
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

### distribute_points_on_faces

> DistributePointsOnFaces, mesh=self

``` python
def distribute_points_on_faces(self, density=None, seed=None, distance_min=None, density_max=None, density_factor=None, selection=None, distribute_method='RANDOM', use_legacy_normal=False, node_label=None, node_color=None):
```
Node
 - class_name : [DistributePointsOnFaces](/docs/GeoNodes_classes/DistributePointsOnFaces.md)
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

### domain_size

> DomainSize, geometry=self, return node

``` python
def domain_size(self, component='MESH', node_label=None, node_color=None):
```
Node
 - class_name : [DomainSize](/docs/GeoNodes_classes/DomainSize.md)
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

### dual_mesh

> DualMesh, mesh=self

``` python
def dual_mesh(self, keep_boundaries=None, node_label=None, node_color=None):
```
Node
 - class_name : [DualMesh](/docs/GeoNodes_classes/DualMesh.md)
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

### duplicate_elements

> DuplicateElements, geometry=self

``` python
def duplicate_elements(self, amount=None, selection=None, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [DuplicateElements](/docs/GeoNodes_classes/DuplicateElements.md)
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

### edge_paths_to_curves

> EdgePathsToCurves, mesh=self

``` python
def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None, node_label=None, node_color=None):
```
Node
 - class_name : [EdgePathsToCurves](/docs/GeoNodes_classes/EdgePathsToCurves.md)
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

### extrude_mesh

> ExtrudeMesh, mesh=self

``` python
def extrude_mesh(self, offset=None, offset_scale=None, individual=None, selection=None, mode='FACES', node_label=None, node_color=None):
```
Node
 - class_name : [ExtrudeMesh](/docs/GeoNodes_classes/ExtrudeMesh.md)
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

### fill_curve

> FillCurve, curve=self

``` python
def fill_curve(self, mode='TRIANGLES', node_label=None, node_color=None):
```
Node
 - class_name : [FillCurve](/docs/GeoNodes_classes/FillCurve.md)
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

### fillet_curve

> FilletCurve, curve=self

``` python
def fillet_curve(self, radius=None, limit_radius=None, count=None, mode='BEZIER', node_label=None, node_color=None):
```
Node
 - class_name : [FilletCurve](/docs/GeoNodes_classes/FilletCurve.md)
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

### flip_faces

> FlipFaces, mesh=self

``` python
def flip_faces(self, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [FlipFaces](/docs/GeoNodes_classes/FlipFaces.md)
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

### geometry_to_instance

> GeometryToInstance, geometry=self

``` python
def geometry_to_instance(self, *args, node_label=None, node_color=None):
```
Node
 - class_name : [GeometryToInstance](/docs/GeoNodes_classes/GeometryToInstance.md)
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

### instance_on_points

> InstanceOnPoints, points=self

``` python
def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [InstanceOnPoints](/docs/GeoNodes_classes/InstanceOnPoints.md)
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

### instances_to_points

> InstancesToPoints, instances=self

``` python
def instances_to_points(self, position=None, radius=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [InstancesToPoints](/docs/GeoNodes_classes/InstancesToPoints.md)
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

### interpolate_curves

> InterpolateCurves, guide_curves=self

``` python
def interpolate_curves(self, guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None, node_label=None, node_color=None):
```
Node
 - class_name : [InterpolateCurves](/docs/GeoNodes_classes/InterpolateCurves.md)
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

### intersect

> MeshBoolean, mesh=geometry + args

``` python
def intersect(self, *args, self_intersection=None, hole_tolerant=None, node_label=None, node_color=None):
```
Node
 - class_name : [MeshBoolean](/docs/GeoNodes_classes/MeshBoolean.md)
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

### join_geometry

> JoinGeometry, geometry=self

``` python
def join_geometry(self, *args, node_label=None, node_color=None):
```
Node
 - class_name : [JoinGeometry](/docs/GeoNodes_classes/JoinGeometry.md)
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

### mean_filter_sdf_volume

> MeanFilterSDFVolume, volume=self

``` python
def mean_filter_sdf_volume(self, iterations=None, width=None, node_label=None, node_color=None):
```
Node
 - class_name : [MeanFilterSDFVolume](/docs/GeoNodes_classes/MeanFilterSDFVolume.md)
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

### merge_by_distance

> MergeByDistance, geometry=self

``` python
def merge_by_distance(self, distance=None, selection=None, mode='ALL', node_label=None, node_color=None):
```
Node
 - class_name : [MergeByDistance](/docs/GeoNodes_classes/MergeByDistance.md)
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

### mesh_boolean

> MeshBoolean, mesh_1=self

``` python
def mesh_boolean(self, *args, mesh_2=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE', node_label=None, node_color=None):
```
Node
 - class_name : [MeshBoolean](/docs/GeoNodes_classes/MeshBoolean.md)
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

### mesh_to_curve

> MeshToCurve, mesh=self

``` python
def mesh_to_curve(self, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [MeshToCurve](/docs/GeoNodes_classes/MeshToCurve.md)
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

### mesh_to_points

> MeshToPoints, mesh=self

``` python
def mesh_to_points(self, position=None, radius=None, selection=None, mode='VERTICES', node_label=None, node_color=None):
```
Node
 - class_name : [MeshToPoints](/docs/GeoNodes_classes/MeshToPoints.md)
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

### mesh_to_sdf_volume

> MeshToSDFVolume, mesh=self

``` python
def mesh_to_sdf_volume(self, voxel_amount=None, half_band_width=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None):
```
Node
 - class_name : [MeshToSDFVolume](/docs/GeoNodes_classes/MeshToSDFVolume.md)
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

### mesh_to_volume

> MeshToVolume, mesh=self

``` python
def mesh_to_volume(self, density=None, voxel_amount=None, interior_band_width=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None):
```
Node
 - class_name : [MeshToVolume](/docs/GeoNodes_classes/MeshToVolume.md)
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

### offset_sdf_volume

> OffsetSDFVolume, volume=self

``` python
def offset_sdf_volume(self, distance=None, node_label=None, node_color=None):
```
Node
 - class_name : [OffsetSDFVolume](/docs/GeoNodes_classes/OffsetSDFVolume.md)
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

### points_to_curves

> PointsToCurves, points=self

``` python
def points_to_curves(self, curve_group_id=None, weight=None, node_label=None, node_color=None):
```
Node
 - class_name : [PointsToCurves](/docs/GeoNodes_classes/PointsToCurves.md)
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

### points_to_sdf_volume

> PointsToSDFVolume, points=self

``` python
def points_to_sdf_volume(self, voxel_amount=None, radius=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None):
```
Node
 - class_name : [PointsToSDFVolume](/docs/GeoNodes_classes/PointsToSDFVolume.md)
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

### points_to_vertices

> PointsToVertices, points=self

``` python
def points_to_vertices(self, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [PointsToVertices](/docs/GeoNodes_classes/PointsToVertices.md)
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

### points_to_volume

> PointsToVolume, points=self

``` python
def points_to_volume(self, density=None, voxel_amount=None, radius=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None):
```
Node
 - class_name : [PointsToVolume](/docs/GeoNodes_classes/PointsToVolume.md)
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

### realize_instances

> RealizeInstances, geometry=self

``` python
def realize_instances(self, node_label=None, node_color=None):
```
Node
 - class_name : [RealizeInstances](/docs/GeoNodes_classes/RealizeInstances.md)
 - bl_idname : GeometryNodeRealizeInstances

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - node_label : node_label
 - node_color : node_color

### remove_named_attribute

> RemoveNamedAttribute, geometry=self

``` python
def remove_named_attribute(self, name=None, node_label=None, node_color=None):
```
Node
 - class_name : [RemoveNamedAttribute](/docs/GeoNodes_classes/RemoveNamedAttribute.md)
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

### repeat_output

> RepeatOutput, geometry=self

``` python
def repeat_output(self, active_index=0, active_item=None, inspection_index=0, repeat_items=None, node_label=None, node_color=None):
```
Node
 - class_name : [RepeatOutput](/docs/GeoNodes_classes/RepeatOutput.md)
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

### replace_material

> ReplaceMaterial, geometry=self

``` python
def replace_material(self, old=None, new=None, node_label=None, node_color=None):
```
Node
 - class_name : [ReplaceMaterial](/docs/GeoNodes_classes/ReplaceMaterial.md)
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

### resample_curve

> ResampleCurve, curve=self

``` python
def resample_curve(self, count=None, length=None, selection=None, mode='COUNT', node_label=None, node_color=None):
```
Node
 - class_name : [ResampleCurve](/docs/GeoNodes_classes/ResampleCurve.md)
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

### reverse_curve

> ReverseCurve, curve=self

``` python
def reverse_curve(self, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [ReverseCurve](/docs/GeoNodes_classes/ReverseCurve.md)
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

### rotate_instances

> RotateInstances, instances=self

``` python
def rotate_instances(self, rotation=None, pivot_point=None, local_space=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [RotateInstances](/docs/GeoNodes_classes/RotateInstances.md)
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

### sample_index_boolean

> SampleIndex, value=self, data_type='BOOLEAN'

``` python
def sample_index_boolean(self, value=None, index=None, clamp=False, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [SampleIndex](/docs/GeoNodes_classes/SampleIndex.md)
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

### sample_index_color

> SampleIndex, value=self, data_type='FLOAT_COLOR'

``` python
def sample_index_color(self, value=None, index=None, clamp=False, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [SampleIndex](/docs/GeoNodes_classes/SampleIndex.md)
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

### sample_index_float

> SampleIndex, value=self, data_type='FLOAT'

``` python
def sample_index_float(self, value=None, index=None, clamp=False, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [SampleIndex](/docs/GeoNodes_classes/SampleIndex.md)
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

### sample_index_int

> SampleIndex, value=self, data_type='INT'

``` python
def sample_index_int(self, value=None, index=None, clamp=False, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [SampleIndex](/docs/GeoNodes_classes/SampleIndex.md)
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

### sample_index_quaternion

> SampleIndex, value=self, data_type='QUATERNION'

``` python
def sample_index_quaternion(self, value=None, index=None, clamp=False, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [SampleIndex](/docs/GeoNodes_classes/SampleIndex.md)
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

### sample_index_vector

> SampleIndex, value=self, data_type='FLOAT_VECTOR'

``` python
def sample_index_vector(self, value=None, index=None, clamp=False, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [SampleIndex](/docs/GeoNodes_classes/SampleIndex.md)
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

### scale_elements

> ScaleElements, geometry=self

``` python
def scale_elements(self, scale=None, center=None, axis=None, selection=None, domain='FACE', scale_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [ScaleElements](/docs/GeoNodes_classes/ScaleElements.md)
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

### scale_instances

> ScaleInstances, instances=self

``` python
def scale_instances(self, scale=None, center=None, local_space=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [ScaleInstances](/docs/GeoNodes_classes/ScaleInstances.md)
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

### separate_components

> SeparateComponents, geometry=self

``` python
def separate_components(self, node_label=None, node_color=None):
```
Node
 - class_name : [SeparateComponents](/docs/GeoNodes_classes/SeparateComponents.md)
 - bl_idname : GeometryNodeSeparateComponents

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - geometry : self
 - node_label : node_label
 - node_color : node_color

### separate_geometry

> SeparateGeometry, geometry=self

``` python
def separate_geometry(self, selection=None, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [SeparateGeometry](/docs/GeoNodes_classes/SeparateGeometry.md)
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

### set_curve_normal

> SetCurveNormal, curve=self

``` python
def set_curve_normal(self, selection=None, mode='MINIMUM_TWIST', node_label=None, node_color=None):
```
Node
 - class_name : [SetCurveNormal](/docs/GeoNodes_classes/SetCurveNormal.md)
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

### set_curve_radius

> SetCurveRadius, curve=self

``` python
def set_curve_radius(self, radius=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetCurveRadius](/docs/GeoNodes_classes/SetCurveRadius.md)
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

### set_curve_tilt

> SetCurveTilt, curve=self

``` python
def set_curve_tilt(self, tilt=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetCurveTilt](/docs/GeoNodes_classes/SetCurveTilt.md)
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

### set_face_set

> SetFaceSet, mesh=self

``` python
def set_face_set(self, face_set=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetFaceSet](/docs/GeoNodes_classes/SetFaceSet.md)
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

### set_handle_positions

> SetHandlePositions, curve=self

``` python
def set_handle_positions(self, position=None, offset=None, selection=None, mode='LEFT', node_label=None, node_color=None):
```
Node
 - class_name : [SetHandlePositions](/docs/GeoNodes_classes/SetHandlePositions.md)
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

### set_handle_type

> SetHandleType, curve=self

``` python
def set_handle_type(self, selection=None, handle_type='AUTO', mode={'RIGHT', 'LEFT'}, node_label=None, node_color=None):
```
Node
 - class_name : [SetHandleType](/docs/GeoNodes_classes/SetHandleType.md)
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

### set_id

> SetID, geometry=self

``` python
def set_id(self, ID=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetID](/docs/GeoNodes_classes/SetID.md)
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

### set_material

> SetMaterial, geometry=self

``` python
def set_material(self, material=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetMaterial](/docs/GeoNodes_classes/SetMaterial.md)
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

### set_material_index

> SetMaterialIndex, geometry=self

``` python
def set_material_index(self, material_index=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetMaterialIndex](/docs/GeoNodes_classes/SetMaterialIndex.md)
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

### set_point_radius

> SetPointRadius, points=self

``` python
def set_point_radius(self, radius=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetPointRadius](/docs/GeoNodes_classes/SetPointRadius.md)
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

### set_position

> SetPosition, geometry=self

``` python
def set_position(self, position=None, offset=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetPosition](/docs/GeoNodes_classes/SetPosition.md)
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

### set_selection

> SetSelection, geometry=self

``` python
def set_selection(self, selection=None, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [SetSelection](/docs/GeoNodes_classes/SetSelection.md)
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

### set_shade_smooth

> SetShadeSmooth, geometry=self

``` python
def set_shade_smooth(self, shade_smooth=None, selection=None, domain='FACE', node_label=None, node_color=None):
```
Node
 - class_name : [SetShadeSmooth](/docs/GeoNodes_classes/SetShadeSmooth.md)
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

### set_spline_cyclic

> SetSplineCyclic, geometry=self

``` python
def set_spline_cyclic(self, cyclic=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetSplineCyclic](/docs/GeoNodes_classes/SetSplineCyclic.md)
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

### set_spline_resolution

> SetSplineResolution, geometry=self

``` python
def set_spline_resolution(self, resolution=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetSplineResolution](/docs/GeoNodes_classes/SetSplineResolution.md)
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

### set_spline_type

> SetSplineType, curve=self

``` python
def set_spline_type(self, selection=None, spline_type='POLY', node_label=None, node_color=None):
```
Node
 - class_name : [SetSplineType](/docs/GeoNodes_classes/SetSplineType.md)
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

### simulation_output

> SimulationOutput, geometry=self

``` python
def simulation_output(self, skip=None, active_index=0, active_item=None, state_items=None, node_label=None, node_color=None):
```
Node
 - class_name : [SimulationOutput](/docs/GeoNodes_classes/SimulationOutput.md)
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

### split_edges

> SplitEdges, mesh=self

``` python
def split_edges(self, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SplitEdges](/docs/GeoNodes_classes/SplitEdges.md)
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

### store_named_attribute

> StoreNamedAttribute, geometry=self

``` python
def store_named_attribute(self, name=None, value=None, selection=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [StoreNamedAttribute](/docs/GeoNodes_classes/StoreNamedAttribute.md)
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

### store_named_boolean

> StoreNamedAttribute, geometry=self, data_type='BOOLEAN'

``` python
def store_named_boolean(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [StoreNamedAttribute](/docs/GeoNodes_classes/StoreNamedAttribute.md)
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

### store_named_byte_color

> StoreNamedAttribute, geometry=self, data_type='BYTE_COLOR'

``` python
def store_named_byte_color(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [StoreNamedAttribute](/docs/GeoNodes_classes/StoreNamedAttribute.md)
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

### store_named_float

> StoreNamedAttribute, geometry=self, data_type='FLOAT'

``` python
def store_named_float(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [StoreNamedAttribute](/docs/GeoNodes_classes/StoreNamedAttribute.md)
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

### store_named_float2

> StoreNamedAttribute, geometry=self, data_type='FLOAT2'

``` python
def store_named_float2(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [StoreNamedAttribute](/docs/GeoNodes_classes/StoreNamedAttribute.md)
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

### store_named_float_color

> StoreNamedAttribute, geometry=self, data_type='FLOAT_COLOR'

``` python
def store_named_float_color(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [StoreNamedAttribute](/docs/GeoNodes_classes/StoreNamedAttribute.md)
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

### store_named_int

> StoreNamedAttribute, geometry=self, data_type='INT'

``` python
def store_named_int(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [StoreNamedAttribute](/docs/GeoNodes_classes/StoreNamedAttribute.md)
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

### store_named_quaternion

> StoreNamedAttribute, geometry=self, data_type='QUATERNION'

``` python
def store_named_quaternion(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [StoreNamedAttribute](/docs/GeoNodes_classes/StoreNamedAttribute.md)
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

### store_named_vector

> StoreNamedAttribute, geometry=self, data_type='FLOAT_VECTOR'

``` python
def store_named_vector(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [StoreNamedAttribute](/docs/GeoNodes_classes/StoreNamedAttribute.md)
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

### subdivide_curve

> SubdivideCurve, curve=self

``` python
def subdivide_curve(self, cuts=None, node_label=None, node_color=None):
```
Node
 - class_name : [SubdivideCurve](/docs/GeoNodes_classes/SubdivideCurve.md)
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

### subdivide_mesh

> SubdivideMesh, mesh=self

``` python
def subdivide_mesh(self, level=None, node_label=None, node_color=None):
```
Node
 - class_name : [SubdivideMesh](/docs/GeoNodes_classes/SubdivideMesh.md)
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

### subdivision_surface

> SubdivisionSurface, mesh=self

``` python
def subdivision_surface(self, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', node_label=None, node_color=None):
```
Node
 - class_name : [SubdivisionSurface](/docs/GeoNodes_classes/SubdivisionSurface.md)
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

### switch

> Switch, false=self, input_type='GEOMETRY'

``` python
def switch(self, switch=None, true=None, node_label=None, node_color=None):
```
Node
 - class_name : [Switch](/docs/GeoNodes_classes/Switch.md)
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

### transform_geometry

> TransformGeometry, geometry=self

``` python
def transform_geometry(self, translation=None, rotation=None, scale=None, node_label=None, node_color=None):
```
Node
 - class_name : [TransformGeometry](/docs/GeoNodes_classes/TransformGeometry.md)
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

### translate_instances

> TranslateInstances, instances=self

``` python
def translate_instances(self, translation=None, local_space=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [TranslateInstances](/docs/GeoNodes_classes/TranslateInstances.md)
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

### triangulate

> Triangulate, mesh=self

``` python
def triangulate(self, minimum_vertices=None, selection=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL', node_label=None, node_color=None):
```
Node
 - class_name : [Triangulate](/docs/GeoNodes_classes/Triangulate.md)
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

### trim_curve

> TrimCurve, curve=self

``` python
def trim_curve(self, start=None, end=None, selection=None, mode='FACTOR', node_label=None, node_color=None):
```
Node
 - class_name : [TrimCurve](/docs/GeoNodes_classes/TrimCurve.md)
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

### union

> MeshBoolean, mesh=geometry + args

``` python
def union(self, *args, self_intersection=None, hole_tolerant=None, node_label=None, node_color=None):
```
Node
 - class_name : [MeshBoolean](/docs/GeoNodes_classes/MeshBoolean.md)
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

### volume_to_mesh

> VolumeToMesh, volume=self

``` python
def volume_to_mesh(self, threshold=None, adaptivity=None, voxel_amount=None, voxel_size=None, resolution_mode='GRID', node_label=None, node_color=None):
```
Node
 - class_name : [VolumeToMesh](/docs/GeoNodes_classes/VolumeToMesh.md)
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

## Properties

### ID

Nodes
 - get : [ID](/docs/GeoNodes_classes/ID.md)
 - set : [SetID](/docs/GeoNodes_classes/SetID.md)

``` python
@property
def ID(self):
	return self.tree.ID().output_socket

@ID.setter
def ID(self, value):
	self.set_id(value)
```
### curve_radius

> Curve radius property

Nodes
 - get : [Radius](/docs/GeoNodes_classes/Radius.md)
 - set : [SetCurveRadius](/docs/GeoNodes_classes/SetCurveRadius.md)

``` python
@property
def curve_radius(self):
	return self.tree.Radius().output_socket

@curve_radius.setter
def curve_radius(self, value):
	self.set_curve_radius(value)
```
### curve_tilt

Nodes
 - get : [CurveTilt](/docs/GeoNodes_classes/CurveTilt.md)
 - set : [SetCurveTilt](/docs/GeoNodes_classes/SetCurveTilt.md)

``` python
@property
def curve_tilt(self):
	return self.tree.CurveTilt().output_socket

@curve_tilt.setter
def curve_tilt(self, value):
	self.set_curve_tilt(value)
```
### edge_neighbors

Nodes
 - get : [EdgeNeighbors](/docs/GeoNodes_classes/EdgeNeighbors.md)
 - set : None

``` python
@property
def edge_neighbors(self):
	return self.tree.EdgeNeighbors().output_socket
```
### edge_shade_smooth

> SetShadeSmooth(domain='EDGE')

Nodes
 - get : [IsEdgeSmooth](/docs/GeoNodes_classes/IsEdgeSmooth.md)
 - set : [SetSmooth](/docs/GeoNodes_classes/SetSmooth.md)

``` python
@property
def edge_shade_smooth(self):
	return self.tree.IsEdgeSmooth().output_socket

@edge_shade_smooth.setter
def edge_shade_smooth(self, value):
	self.set_shade_smooth(value, domain='EDGE')
```
### face_area

Nodes
 - get : [FaceArea](/docs/GeoNodes_classes/FaceArea.md)
 - set : None

``` python
@property
def face_area(self):
	return self.tree.FaceArea().output_socket
```
### face_shade_smooth

> SetShadeSmooth(domain='FACE')

Nodes
 - get : [IsFaceSmooth](/docs/GeoNodes_classes/IsFaceSmooth.md)
 - set : [SetSmooth](/docs/GeoNodes_classes/SetSmooth.md)

``` python
@property
def face_shade_smooth(self):
	return self.tree.IsFaceSmooth().output_socket

@face_shade_smooth.setter
def face_shade_smooth(self, value):
	self.set_shade_smooth(value, domain='FACE')
```
### index

Nodes
 - get : [Index](/docs/GeoNodes_classes/Index.md)
 - set : None

``` python
@property
def index(self):
	return self.tree.Index().output_socket
```
### offset

> SetPosition(offset=value)

Nodes
 - get : None
 - set : [SetPosition](/docs/GeoNodes_classes/SetPosition.md)

``` python
# Write only property

@offset.setter
def offset(self, value):
	self.set_position(offset=value)
```
### point_radius

> Point radius property

Nodes
 - get : [Radius](/docs/GeoNodes_classes/Radius.md)
 - set : [SetPointRadius](/docs/GeoNodes_classes/SetPointRadius.md)

``` python
@property
def point_radius(self):
	return self.tree.Radius().output_socket

@point_radius.setter
def point_radius(self, value):
	self.set_point_radius(value)
```
### position

> SetPosition(position=value)

Nodes
 - get : [Position](/docs/GeoNodes_classes/Position.md)
 - set : [SetPosition](/docs/GeoNodes_classes/SetPosition.md)

``` python
@property
def position(self):
	return self.tree.Position().output_socket

@position.setter
def position(self, value):
	self.set_position(value)
```
### spline_cyclic

Nodes
 - get : [IsSplineCyclic](/docs/GeoNodes_classes/IsSplineCyclic.md)
 - set : [SetSplineCyclic](/docs/GeoNodes_classes/SetSplineCyclic.md)

``` python
@property
def spline_cyclic(self):
	return self.tree.IsSplineCyclic().output_socket

@spline_cyclic.setter
def spline_cyclic(self, value):
	self.set_spline_cyclic(value)
```
### spline_resolution

Nodes
 - get : [SplineResolution](/docs/GeoNodes_classes/SplineResolution.md)
 - set : [SetSplineResolution](/docs/GeoNodes_classes/SetSplineResolution.md)

``` python
@property
def spline_resolution(self):
	return self.tree.SplineResolution().output_socket

@spline_resolution.setter
def spline_resolution(self, value):
	self.set_spline_resolution(value)
```
### tangent

Nodes
 - get : [CurveTangent](/docs/GeoNodes_classes/CurveTangent.md)
 - set : None

``` python
@property
def tangent(self):
	return self.tree.CurveTangent().output_socket
```