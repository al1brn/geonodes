# Class Curve

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

 > **Curve** sub class of [Geometry](Geometry.md)

A **Curve** has two domains:
- `points` of type [ControlPoint](ControlPoint.md)
- `splines` of type [Spline](Spline.md)

### Constructors

Constructors come from the Blender menu *Curve primitives*:        
- [Arc](#Arc), arc from center and radius
- [ArcFromPoints](#ArcFromPoints), arc from 3 points, return a node with sockets curve, center, normal and radius
- [BezierSegment](#BezierSegment)
- [Circle](#Circle), circle from center and radius
- [CircleFromPoints](#CircleFromPoints), corcme from 3 points, return a couple of sockets (circle, center)
- [Line](#Line), line from points
- [LineDirection](#LineDirection), line from a starting point, a direction and a length
- [Spiral](#Spiral)
- [QuadraticBezier](#QuadraticBezier)
- [Quadrilateral](#Quadrilateral)
- [Star](#Star)




### Constructor

```python
Curve(self, socket, node=None, label=None)
```

rom geonodes.nodes import domains

elf.points = Vertex(self) # Initialized before super().__init__ which can override points


## Content

**Properties**

[ID](#ID) | [bounding_box](#bounding_box) | [bounding_box_min](#bounding_box_min) | [convex_hull](#convex_hull) | [curve_component](#curve_component) | [domain_size](#domain_size) | [index](#index) | [instances_component](#instances_component) | [is_viewport](#is_viewport) | [length](#length) | [material_index](#material_index) | [mesh_component](#mesh_component) | [normal](#normal) | [point_count](#point_count) | [points_component](#points_component) | [position](#position) | [radius](#radius) | [separate_components](#separate_components) | [spline_count](#spline_count) | [volume_component](#volume_component)

***Inherited***

[bl_idname](DataSocket.md#bl_idname) | [bnode](DataSocket.md#bnode) | [is_multi_input](DataSocket.md#is_multi_input) | [is_output](DataSocket.md#is_output) | [is_plugged](DataSocket.md#is_plugged) | [links](DataSocket.md#links) | [name](DataSocket.md#name) | [node_chain_label](DataSocket.md#node_chain_label) | [socket_index](DataSocket.md#socket_index)

**Class and static methods**

[Arc](#Arc) | [ArcFromPoints](#ArcFromPoints) | [BezierSegment](#BezierSegment) | [Circle](#Circle) | [CircleFromPoints](#CircleFromPoints) | [Collection](#Collection) | [FromCollection](#FromCollection) | [Input](#Input) | [Line](#Line) | [LineDirection](#LineDirection) | [QuadraticBezier](#QuadraticBezier) | [Quadrilateral](#Quadrilateral) | [Spiral](#Spiral) | [Star](#Star) | [capture_attribute_node](#capture_attribute_node) | [random_boolean](#random_boolean) | [random_float](#random_float) | [random_integer](#random_integer) | [random_vector](#random_vector)

***Inherited***

[get_bl_idname](DataSocket.md#get_bl_idname) | [get_class_name](DataSocket.md#get_class_name) | [gives_bsocket](DataSocket.md#gives_bsocket) | [is_socket](DataSocket.md#is_socket) | [is_vector](DataSocket.md#is_vector) | [python_type_to_socket](DataSocket.md#python_type_to_socket) | [value_data_type](DataSocket.md#value_data_type)

**Methods**

[attribute_statistic](#attribute_statistic) | [capture_attribute](#capture_attribute) | [curve_of_point](#curve_of_point) | [deform_on_surface](#deform_on_surface) | [delete](#delete) | [duplicate](#duplicate) | [field_at_index](#field_at_index) | [fill](#fill) | [fill_ngons](#fill_ngons) | [fill_triangles](#fill_triangles) | [fillet](#fillet) | [fillet_bezier](#fillet_bezier) | [fillet_poly](#fillet_poly) | [instance_on_points](#instance_on_points) | [instantiate](#instantiate) | [interpolate_domain](#interpolate_domain) | [join](#join) | [material_selection](#material_selection) | [merge_by_distance](#merge_by_distance) | [named_attribute](#named_attribute) | [named_boolean](#named_boolean) | [named_color](#named_color) | [named_float](#named_float) | [named_integer](#named_integer) | [named_vector](#named_vector) | [offset_point](#offset_point) | [points_of_curve](#points_of_curve) | [proximity](#proximity) | [proximity_edges](#proximity_edges) | [proximity_faces](#proximity_faces) | [proximity_points](#proximity_points) | [raycast](#raycast) | [raycast_interpolated](#raycast_interpolated) | [raycast_nearest](#raycast_nearest) | [remove_named_attribute](#remove_named_attribute) | [replace_material](#replace_material) | [resample](#resample) | [resample_count](#resample_count) | [resample_evaluated](#resample_evaluated) | [resample_length](#resample_length) | [reverse](#reverse) | [sample](#sample) | [sample_index](#sample_index) | [sample_nearest](#sample_nearest) | [separate](#separate) | [set_ID](#set_ID) | [set_material](#set_material) | [set_material_index](#set_material_index) | [set_position](#set_position) | [show_handles](#show_handles) | [store_named_attribute](#store_named_attribute) | [store_named_boolean](#store_named_boolean) | [store_named_color](#store_named_color) | [store_named_float](#store_named_float) | [store_named_integer](#store_named_integer) | [store_named_vector](#store_named_vector) | [subdivide](#subdivide) | [switch](#switch) | [to_instance](#to_instance) | [to_mesh](#to_mesh) | [to_points](#to_points) | [to_points_count](#to_points_count) | [to_points_evaluated](#to_points_evaluated) | [to_points_length](#to_points_length) | [transform](#transform) | [trim](#trim) | [trim_factor](#trim_factor) | [trim_length](#trim_length) | [view](#view) | [viewer](#viewer)

***Inherited***

[connected_sockets](DataSocket.md#connected_sockets) | [get_blender_socket](DataSocket.md#get_blender_socket) | [init_domains](DataSocket.md#init_domains) | [init_socket](DataSocket.md#init_socket) | [plug](DataSocket.md#plug) | [reroute](DataSocket.md#reroute) | [reset_properties](DataSocket.md#reset_properties) | [stack](DataSocket.md#stack) | [to_output](DataSocket.md#to_output)

## Properties

### ID



> Node: [ID](GeometryNodeInputID.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)

#### Returns:
- socket `ID`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### bounding_box



> Node: [Bounding Box](GeometryNodeBoundBox.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)

#### Returns:
- socket `bounding_box` of class Mesh






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### bounding_box_min



> Node: [Bounding Box](GeometryNodeBoundBox.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)

#### Returns:
- socket `max`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### convex_hull



> Node: [Convex Hull](GeometryNodeConvexHull.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/convex_hull.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeConvexHull.html)

#### Returns:
- socket `convex_hull` of class Mesh






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### curve_component



> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `curve` of class Curve






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### domain_size



> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### index



> Node: [Index](GeometryNodeInputIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

#### Returns:
- socket `index`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### instances_component



> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `instances` of class Instances






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### is_viewport



> Node: [Is Viewport](GeometryNodeIsViewport.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/is_viewport.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeIsViewport.html)

#### Returns:
- socket `is_viewport`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### length



> Node: [Curve Length](GeometryNodeCurveLength.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_length.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveLength.html)

#### Returns:
- socket `length`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### material_index



> Node: [Material Index](GeometryNodeInputMaterialIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)

#### Returns:
- socket `material_index`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mesh_component



> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `mesh` of class Mesh






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### normal



> Node: [Normal](GeometryNodeInputNormal.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)

#### Returns:
- socket `normal`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### point_count



> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `point_count`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### points_component



> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `point_cloud` of class Points






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### position



> Node: [Position](GeometryNodeInputPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)

#### Returns:
- socket `position`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### radius



> Node: [Radius](GeometryNodeInputRadius.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)

#### Returns:
- socket `radius`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### separate_components



> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- node with sockets ['mesh', 'point_cloud', 'curve', 'volume', 'instances']






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### spline_count



> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `spline_count`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### volume_component



> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `volume` of class Volume






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Class and static methods

### Arc

```python
@classmethod
def Arc(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None)
```



> Node: [Arc](GeometryNodeCurveArc.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/arc.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html)

#### Args:
- resolution: Integer
- radius: Float
- start_angle: Float
- sweep_angle: Float
- connect_center: Boolean
- invert_arc: Boolean

#### Returns:
- socket `curve`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### ArcFromPoints

```python
@classmethod
def ArcFromPoints(cls, resolution=None, start=None, middle=None, end=None, offset_angle=None, connect_center=None, invert_arc=None)
```



> Node: [Arc](GeometryNodeCurveArc.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/arc.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html)

#### Args:
- resolution: Integer
- start: Vector
- middle: Vector
- end: Vector
- offset_angle: Float
- connect_center: Boolean
- invert_arc: Boolean

#### Returns:
- node with sockets ['curve', 'center', 'normal', 'radius']






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### BezierSegment

```python
@classmethod
def BezierSegment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION')
```



> Node: [Bezier Segment](GeometryNodeCurvePrimitiveBezierSegment.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/bezier_segment.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveBezierSegment.html)

#### Args:
- resolution: Integer
- start: Vector
- start_handle: Vector
- end_handle: Vector
- end: Vector
- mode (str): 'POSITION' in [POSITION, OFFSET]

#### Returns:
- socket `curve`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Circle

```python
@classmethod
def Circle(cls, resolution=None, radius=None)
```



> Node: [Curve Circle](GeometryNodeCurvePrimitiveCircle.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_circle.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html)

#### Args:
- resolution: Integer
- radius: Float

#### Returns:
- socket `curve`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### CircleFromPoints

```python
@staticmethod
def CircleFromPoints(resolution=None, point_1=None, point_2=None, point_3=None)
```



> Node: [Curve Circle](GeometryNodeCurvePrimitiveCircle.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_circle.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html)

#### Args:
- resolution: Integer
- point_1: Vector
- point_2: Vector
- point_3: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveCircle.webp)

#### Returns:
- tuple ('`curve`', '`center`')






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Collection

```python
@classmethod
def Collection(cls, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL')
```



> Node: [Collection Info](GeometryNodeCollectionInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/collection_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCollectionInfo.html)

#### Args:
- collection: Collection
- separate_children: Boolean
- reset_children: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- socket `geometry`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### FromCollection

```python
@classmethod
def FromCollection(cls, collection=None, separate_children
```

 Get the geometry from a collection



<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Input

```python
@classmethod
def Input(cls, name = None, description = "")
```

 Create a Geometry input socket in the Group Input Node

#### Args:
- name: The socket name
- description: User tip
    
#### Returns:
- Geometry: The Geometry data socket
    
> Note: This method create a new input socket in the Group Input node. To get the **default** input geometry,
  use [Tree.input_geometry](#Tree.md#input_geometry) property.
    



<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Line

```python
@classmethod
def Line(cls, start=None, end=None)
```



> Node: [Curve Line](GeometryNodeCurvePrimitiveLine.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_line.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html)

#### Args:
- start: Vector
- end: Vector

#### Returns:
- socket `curve`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### LineDirection

```python
@classmethod
def LineDirection(cls, start=None, direction=None, length=None)
```



> Node: [Curve Line](GeometryNodeCurvePrimitiveLine.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_line.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html)

#### Args:
- start: Vector
- direction: Vector
- length: Float

#### Returns:
- socket `curve`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### QuadraticBezier

```python
@classmethod
def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None)
```



> Node: [Quadratic Bezier](GeometryNodeCurveQuadraticBezier.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/quadratic_bezier.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveQuadraticBezier.html)

#### Args:
- resolution: Integer
- start: Vector
- middle: Vector
- end: Vector

#### Returns:
- socket `curve`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Quadrilateral

```python
@classmethod
def Quadrilateral(cls, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE')
```



> Node: [Quadrilateral](GeometryNodeCurvePrimitiveQuadrilateral.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/quadrilateral.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveQuadrilateral.html)

#### Args:
- width: Float
- height: Float
- bottom_width: Float
- top_width: Float
- offset: Float
- bottom_height: Float
- top_height: Float
- point_1: Vector
- point_2: Vector
- point_3: Vector
- point_4: Vector
- mode (str): 'RECTANGLE' in [RECTANGLE, PARALLELOGRAM, TRAPEZOID, KITE, POINTS]

#### Returns:
- socket `curve`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Spiral

```python
@classmethod
def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None)
```



> Node: [Spiral](GeometryNodeCurveSpiral.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_spiral.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSpiral.html)

#### Args:
- resolution: Integer
- rotations: Float
- start_radius: Float
- end_radius: Float
- height: Float
- reverse: Boolean

#### Returns:
- socket `curve`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Star

```python
@classmethod
def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None)
```



> Node: [Star](GeometryNodeCurveStar.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/star.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveStar.html)

#### Args:
- points: Integer
- inner_radius: Float
- outer_radius: Float
- twist: Float

#### Returns:
- node with sockets ['curve', 'outer_points']






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### capture_attribute_node

```python
@staticmethod
def capture_attribute_node(geometry=None, value=None, data_type='FLOAT', domain='POINT')
```



> Node: [Capture Attribute](GeometryNodeCaptureAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

#### Args:
- geometry: Geometry
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets ['geometry', 'attribute']






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_boolean

```python
@staticmethod
def random_boolean(probability=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- probability: Float
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_float

```python
@staticmethod
def random_float(min=None, max=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_integer

```python
@staticmethod
def random_integer(min=None, max=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_vector

```python
@staticmethod
def random_vector(min=None, max=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### attribute_statistic

```python
def attribute_statistic(self, selection=None, attribute=None, domain='POINT')
```



> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- selection: Boolean
- attribute: ['Float', 'Vector']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### capture_attribute

```python
def capture_attribute(self, value=None, domain='POINT')
```



> Node: [Capture Attribute](GeometryNodeCaptureAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

#### Args:
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### curve_of_point

```python
def curve_of_point(self, point_index=None)
```



> Node: [Curve of Point](GeometryNodeCurveOfPoint.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/curve_of_point.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html)

#### Args:
- point_index: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveOfPoint.webp)

#### Returns:
- tuple ('`curve_index`', '`index_in_curve`')






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### deform_on_surface

```python
def deform_on_surface(self)
```



> Node: [Deform Curves on Surface](GeometryNodeDeformCurvesOnSurface.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/deform_curves_on_surface.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeformCurvesOnSurface.html)

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### delete

```python
def delete(self, selection=None, domain='POINT', mode='ALL')
```



> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### duplicate

```python
def duplicate(self, selection=None, amount=None, domain='POINT')
```



> Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

#### Args:
- selection: Boolean
- amount: Integer
- domain (str): 'POINT' in [POINT, EDGE, FACE, SPLINE, INSTANCE]

#### Returns:
- socket `duplicate_index`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### field_at_index

```python
def field_at_index(self, index=None, value=None, domain='POINT')
```



> Node: [Field at Index](GeometryNodeFieldAtIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)

#### Args:
- index: Integer
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- socket `value`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fill

```python
def fill(self, mode='TRIANGLES')
```



> Node: [Fill Curve](GeometryNodeFillCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)

#### Args:
- mode (str): 'TRIANGLES' in [TRIANGLES, NGONS]

#### Returns:
- socket `mesh` of class Mesh






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fill_ngons

```python
def fill_ngons(self)
```



> Node: [Fill Curve](GeometryNodeFillCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)

#### Returns:
- socket `mesh` of class Mesh






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fill_triangles

```python
def fill_triangles(self)
```



> Node: [Fill Curve](GeometryNodeFillCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)

#### Returns:
- socket `mesh` of class Mesh






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fillet

```python
def fillet(self, count=None, radius=None, limit_radius=None, mode='BEZIER')
```



> Node: [Fillet Curve](GeometryNodeFilletCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)

#### Args:
- count: Integer
- radius: Float
- limit_radius: Boolean
- mode (str): 'BEZIER' in [BEZIER, POLY]

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fillet_bezier

```python
def fillet_bezier(self, radius=None, limit_radius=None)
```



> Node: [Fillet Curve](GeometryNodeFilletCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)

#### Args:
- radius: Float
- limit_radius: Boolean

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fillet_poly

```python
def fillet_poly(self, count=None, radius=None, limit_radius=None)
```



> Node: [Fillet Curve](GeometryNodeFilletCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)

#### Args:
- count: Integer
- radius: Float
- limit_radius: Boolean

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### instance_on_points

```python
def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None)
```



> Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

#### Args:
- selection: Boolean
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

#### Returns:
- socket `instances`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### instantiate

```python
def instantiate(self, count = 1, realize = False)
```

 Instantiate the geometry

#### Args:
- count: Number of instances to create
- realize: True to realize the instances
    
#### Returns:
- Instances or Geometry
    
The duplication is performed by instantiating the geometry along the vertices
of a Mesh Line initialized with `count` points.

The operator ``*`` can be used to operate this method with `realize = False`:
    
```python
    
curves = curve * 10

# is equivalent to

curves = curve.duplicate(10, realize=False)
```




<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### interpolate_domain

```python
def interpolate_domain(self, value=None, domain='POINT')
```



> Node: [Interpolate Domain](GeometryNodeFieldOnDomain.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/interpolate_domain.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- socket `value`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### join

```python
def join(*geometry)
```



> Node: [Join Geometry](GeometryNodeJoinGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)

#### Args:
- geometry: <m>Geometry

#### Returns:
- socket `geometry`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### material_selection

```python
def material_selection(self, material=None)
```



> Node: [Material Selection](GeometryNodeMaterialSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)

#### Args:
- material: Material

#### Returns:
- socket `selection`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### merge_by_distance

```python
def merge_by_distance(self, selection=None, distance=None, mode='ALL')
```



> Node: [Merge by Distance](GeometryNodeMergeByDistance.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)

#### Args:
- selection: Boolean
- distance: Float
- mode (str): 'ALL' in [ALL, CONNECTED]

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_attribute

```python
def named_attribute(self, name=None, data_type='FLOAT')
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_boolean

```python
def named_boolean(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_color

```python
def named_color(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_float

```python
def named_float(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_integer

```python
def named_integer(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_vector

```python
def named_vector(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### offset_point

```python
def offset_point(self, point_index=None, offset=None)
```



> Node: [Offset Point in Curve](GeometryNodeOffsetPointInCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/offset_point_in_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetPointInCurve.html)

#### Args:
- point_index: Integer
- offset: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeOffsetPointInCurve.webp)

#### Returns:
- tuple ('`is_valid_offset`', '`point_index`')






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### points_of_curve

```python
def points_of_curve(self, curve_index=None, weights=None, sort_index=None)
```



> Node: [Points of Curve](GeometryNodePointsOfCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/points_of_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsOfCurve.html)

#### Args:
- curve_index: Integer
- weights: Float
- sort_index: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePointsOfCurve.webp)

#### Returns:
- tuple ('`point_index`', '`total`')






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### proximity

```python
def proximity(self, target=None, source_position=None, target_element='FACES')
```



> Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector
- target_element (str): 'FACES' in [POINTS, EDGES, FACES]

#### Returns:
- socket `distance`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### proximity_edges

```python
def proximity_edges(self, target=None, source_position=None)
```



> Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

#### Returns:
- socket `distance`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### proximity_faces

```python
def proximity_faces(self, target=None, source_position=None)
```



> Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

#### Returns:
- socket `distance`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### proximity_points

```python
def proximity_points(self, target=None, source_position=None)
```



> Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

#### Returns:
- socket `distance`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### raycast

```python
def raycast(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED')
```



> Node: [Raycast](GeometryNodeRaycast.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

#### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float
- mapping (str): 'INTERPOLATED' in [INTERPOLATED, NEAREST]

#### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### raycast_interpolated

```python
def raycast_interpolated(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None)
```



> Node: [Raycast](GeometryNodeRaycast.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

#### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float

#### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### raycast_nearest

```python
def raycast_nearest(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None)
```



> Node: [Raycast](GeometryNodeRaycast.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

#### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float

#### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### remove_named_attribute

```python
def remove_named_attribute(self, name=None)
```



> Node: [Remove Named Attribute](GeometryNodeRemoveAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)

#### Args:
- name: String

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### replace_material

```python
def replace_material(self, old=None, new=None)
```



> Node: [Replace Material](GeometryNodeReplaceMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeReplaceMaterial.html)

#### Args:
- old: Material
- new: Material

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### resample

```python
def resample(self, selection=None, count=None, length=None, mode='COUNT')
```



> Node: [Resample Curve](GeometryNodeResampleCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

#### Args:
- selection: Boolean
- count: Integer
- length: Float
- mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### resample_count

```python
def resample_count(self, selection=None, count=None)
```



> Node: [Resample Curve](GeometryNodeResampleCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

#### Args:
- selection: Boolean
- count: Integer

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### resample_evaluated

```python
def resample_evaluated(self, selection=None)
```



> Node: [Resample Curve](GeometryNodeResampleCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

#### Args:
- selection: Boolean

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### resample_length

```python
def resample_length(self, selection=None, length=None)
```



> Node: [Resample Curve](GeometryNodeResampleCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

#### Args:
- selection: Boolean
- length: Float

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### reverse

```python
def reverse(self, selection=None)
```



> Node: [Reverse Curve](GeometryNodeReverseCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/reverse_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeReverseCurve.html)

#### Args:
- selection: Boolean

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sample

```python
def sample(self, value=None, factor=None, length=None, curve_index=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False)
```



> Node: [Sample Curve](GeometryNodeSampleCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleCurve.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- factor: Float
- length: Float
- curve_index: Integer
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
- mode (str): 'FACTOR' in [FACTOR, LENGTH]
- use_all_curves (bool): False

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sample_index

```python
def sample_index(self, value=None, index=None, clamp=False, domain='POINT')
```



> Node: [Sample Index](GeometryNodeSampleIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- index: Integer
- clamp (bool): False
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- socket `value`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sample_nearest

```python
def sample_nearest(self, sample_position=None, domain='POINT')
```



> Node: [Sample Nearest](GeometryNodeSampleNearest.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)

#### Args:
- sample_position: Vector
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER]

#### Returns:
- socket `index`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### separate

```python
def separate(self, selection=None, domain='POINT')
```



> Node: [Separate Geometry](GeometryNodeSeparateGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

#### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

#### Returns:
- tuple ('`selection`', '`inverted`')






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_ID

```python
def set_ID(self, selection=None, ID=None)
```



> Node: [Set ID](GeometryNodeSetID.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

#### Args:
- selection: Boolean
- ID: Integer

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_material

```python
def set_material(self, selection=None, material=None)
```



> Node: [Set Material](GeometryNodeSetMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

#### Args:
- selection: Boolean
- material: Material

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_material_index

```python
def set_material_index(self, selection=None, material_index=None)
```



> Node: [Set Material Index](GeometryNodeSetMaterialIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)

#### Args:
- selection: Boolean
- material_index: Integer

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_position

```python
def set_position(self, selection=None, position=None, offset=None)
```



> Node: [Set Position](GeometryNodeSetPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

#### Args:
- selection: Boolean
- position: Vector
- offset: Vector

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### show_handles

```python
def show_handles(self)
```

 Generate a mesh and cloud points to visualize the control points and handles

#### Returns:
- Geometry: The geometry can be joined to the output
    
Example:
    
```python
curve = ... # Curve initialization

visu = curve.show_handles()

tree.output_geometry = curve + visu
```
    




<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_attribute

```python
def store_named_attribute(self, name=None, value=None, domain='POINT')
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_boolean

```python
def store_named_boolean(self, name=None, value=None, domain='POINT')
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_color

```python
def store_named_color(self, name=None, value=None, domain='POINT')
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_float

```python
def store_named_float(self, name=None, value=None, domain='POINT')
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_integer

```python
def store_named_integer(self, name=None, value=None, domain='POINT')
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_vector

```python
def store_named_vector(self, name=None, value=None, domain='POINT')
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### subdivide

```python
def subdivide(self, cuts=None)
```



> Node: [Subdivide Curve](GeometryNodeSubdivideCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/subdivide_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideCurve.html)

#### Args:
- cuts: Integer

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch

```python
def switch(self, switch=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Geometry

#### Returns:
- socket `output`






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_instance

```python
def to_instance(*geometry)
```



> Node: [Geometry to Instance](GeometryNodeGeometryToInstance.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)

#### Args:
- geometry: <m>Geometry

#### Returns:
- socket `instances` of class Instances






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_mesh

```python
def to_mesh(self, profile_curve=None, fill_caps=None)
```



> Node: [Curve to Mesh](GeometryNodeCurveToMesh.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_mesh.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToMesh.html)

#### Args:
- profile_curve: Geometry
- fill_caps: Boolean

#### Returns:
- socket `mesh` of class Mesh






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_points

```python
def to_points(self, count=None, length=None, mode='COUNT')
```



> Node: [Curve to Points](GeometryNodeCurveToPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)

#### Args:
- count: Integer
- length: Float
- mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveToPoints.webp)

#### Returns:
- tuple ('`points`', '`tangent`', '`normal`', '`rotation`')






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_points_count

```python
def to_points_count(self, count=None)
```



> Node: [Curve to Points](GeometryNodeCurveToPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)

#### Args:
- count: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveToPoints.webp)

#### Returns:
- tuple ('`points`', '`tangent`', '`normal`', '`rotation`')






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_points_evaluated

```python
def to_points_evaluated(self)
```



> Node: [Curve to Points](GeometryNodeCurveToPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveToPoints.webp)

#### Returns:
- tuple ('`points`', '`tangent`', '`normal`', '`rotation`')






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_points_length

```python
def to_points_length(self, length=None)
```



> Node: [Curve to Points](GeometryNodeCurveToPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)

#### Args:
- length: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveToPoints.webp)

#### Returns:
- tuple ('`points`', '`tangent`', '`normal`', '`rotation`')






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### transform

```python
def transform(self, translation=None, rotation=None, scale=None)
```



> Node: [Transform](GeometryNodeTransform.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/transform.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html)

#### Args:
- translation: Vector
- rotation: Vector
- scale: Vector

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### trim

```python
def trim(self, start=None, end=None, mode='FACTOR')
```



> Node: [Trim Curve](GeometryNodeTrimCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)

#### Args:
- mode (str): 'FACTOR' in [FACTOR, LENGTH]

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### trim_factor

```python
def trim_factor(self, start=None, end=None)
```



> Node: [Trim Curve](GeometryNodeTrimCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)

#### Args:
- start: Float
- end: Float

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### trim_length

```python
def trim_length(self, start=None, end=None)
```



> Node: [Trim Curve](GeometryNodeTrimCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)

#### Args:
- start: Float
- end: Float

#### Returns:
- self






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### view

```python
def view(self, value=None, domain='AUTO')
```



> Node: [Viewer](GeometryNodeViewer.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)

#### Args:
- value: ['Float', 'Vector', 'Color', 'Integer', 'Boolean']
- domain (str): 'AUTO' in [AUTO, POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets []






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### viewer

```python
def viewer(self, value=None, domain='AUTO')
```



> Node: [Viewer](GeometryNodeViewer.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)

#### Args:
- value: ['Float', 'Vector', 'Color', 'Integer', 'Boolean']
- domain (str): 'AUTO' in [AUTO, POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets []






<sub>Go to [top](#class-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

