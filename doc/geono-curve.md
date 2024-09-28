# Curve

> Bases classes: [Geometry](geono-geometry.md#geometry)

``` python
Curve(value=None, name=None, tip=None)
```

> Curve Geometry

The **Curve** class exposes all methods specific to curves.
Since there is no ambiguity, the word **curve** is omitted in the name of
the methods:

``` python
curve = Curve.Line() # Node 'Curve Line'
mesh= curve.fill() # Node 'Fill Curve'
```

Nodes requiring a domain parameter, are implemented in one of the two domains of **Curve** [points](geono-curve.md#points),
[splines](geono-curve.md#splines).

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = None) : User tip (for Group Input sockets)

### Inherited

[\_\_add__](geono-geometry.md#__add__) :black_small_square: [bake](geono-geometry.md#bake) :black_small_square: [blur](geono-socket.md#blur) :black_small_square: [bounding_box](geono-geometry.md#bounding_box) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [convex_hull](geono-geometry.md#convex_hull) :black_small_square: [curve](geono-geometry.md#curve) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [\_geo](geono-geometry.md#_geo) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_geo_type](geono-geome-geobase.md#_geo_type) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [\_\_getitem__](geono-geome-geobase.md#__getitem__) :black_small_square: [id](geono-geome-geobase.md#id) :black_small_square: [index_of_nearest](geono-geometry.md#index_of_nearest) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [instances](geono-geometry.md#instances) :black_small_square: [join](geono-geometry.md#join) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [material](geono-geome-geobase.md#material) :black_small_square: [material_index](geono-geome-geobase.md#material_index) :black_small_square: [material_selection](geono-geome-geobase.md#material_selection) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [merge_by_distance](geono-geometry.md#merge_by_distance) :black_small_square: [mesh](geono-geometry.md#mesh) :black_small_square: [\_node](geono-geometry.md#_node) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [offset](geono-geome-geobase.md#offset) :black_small_square: [out](geono-socket.md#out) :black_small_square: [point_cloud](geono-geometry.md#point_cloud) :black_small_square: [position](geono-geome-geobase.md#position) :black_small_square: [\_raw_sel](geono-geome-geobase.md#_raw_sel) :black_small_square: [raycast](geono-geometry.md#raycast) :black_small_square: [remove_named_attribute](geono-geometry.md#remove_named_attribute) :black_small_square: [replace_material](geono-geome-geobase.md#replace_material) :black_small_square: [\_sel](geono-geome-geobase.md#_sel) :black_small_square: [separate_components](geono-geometry.md#separate_components) :black_small_square: [set_id](geono-geometry.md#set_id) :black_small_square: [set_material](geono-geometry.md#set_material) :black_small_square: [set_position](geono-geometry.md#set_position) :black_small_square: [set_shade_smooth](geono-geometry.md#set_shade_smooth) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square: [to_instance](geono-geometry.md#to_instance) :black_small_square: [to_output](geono-socket.md#to_output) :black_small_square: [transform](geono-geometry.md#transform) :black_small_square: [viewer](geono-geometry.md#viewer) :black_small_square: [volume](geono-geometry.md#volume) :black_small_square:

## Content

- **A** : [Arc](geono-curve.md#arc)
- **B** : [BezierSegment](geono-curve.md#beziersegment)
- **C** : [Circle](geono-curve.md#circle) :black_small_square: [curve_of_point](geono-curve.md#curve_of_point)
- **D** : [deform_on_surface](geono-curve.md#deform_on_surface)
- **E** : [endpoint_selection](geono-curve.md#endpoint_selection)
- **F** : [fill](geono-curve.md#fill) :black_small_square: [fillet](geono-curve.md#fillet) :black_small_square: [FromEdgePaths](geono-curve.md#fromedgepaths) :black_small_square: [FromMesh](geono-curve.md#frommesh) :black_small_square: [FromPoints](geono-curve.md#frompoints)
- **I** : [interpolate](geono-curve.md#interpolate)
- **K** : [Kite](geono-curve.md#kite)
- **L** : [length](geono-curve.md#length) :black_small_square: [Line](geono-curve.md#line)
- **O** : [offset_point_in_curve](geono-curve.md#offset_point_in_curve)
- **P** : [Parallelogram](geono-curve.md#parallelogram) :black_small_square: [points](geono-curve.md#points) :black_small_square: [Points](geono-curve.md#points) :black_small_square: [points_of_curve](geono-curve.md#points_of_curve)
- **Q** : [QuadraticBezier](geono-curve.md#quadraticbezier) :black_small_square: [Quadrilateral](geono-curve.md#quadrilateral)
- **R** : [radius](geono-curve.md#radius) :black_small_square: [Rectangle](geono-curve.md#rectangle) :black_small_square: [resample](geono-curve.md#resample) :black_small_square: [reverse](geono-curve.md#reverse)
- **S** : [sample](geono-curve.md#sample) :black_small_square: [set_normal](geono-curve.md#set_normal) :black_small_square: [set_normal_free](geono-curve.md#set_normal_free) :black_small_square: [set_normal_z_up](geono-curve.md#set_normal_z_up) :black_small_square: [Spiral](geono-curve.md#spiral) :black_small_square: [splines](geono-curve.md#splines) :black_small_square: [Star](geono-curve.md#star) :black_small_square: [subdivide](geono-curve.md#subdivide)
- **T** : [tilt](geono-curve.md#tilt) :black_small_square: [to_mesh](geono-curve.md#to_mesh) :black_small_square: [to_points](geono-curve.md#to_points) :black_small_square: [Trapezoid](geono-curve.md#trapezoid) :black_small_square: [trim](geono-curve.md#trim) :black_small_square: [trim_factor](geono-curve.md#trim_factor) :black_small_square: [trim_length](geono-curve.md#trim_length)

## Properties



### length

> _type_: **Float**
>

> **node** : [Curve Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/curve_length.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Properties](geono-curve.md#properties)</sub>

### points

> _type_: **SplinePoint**
>

POINT domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Properties](geono-curve.md#properties)</sub>

### radius

> _type_: **Float**
>

> **node** : [Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/radius.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Properties](geono-curve.md#properties)</sub>

### splines

> _type_: **Spline**
>

CURVE (or SPLINE) domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Properties](geono-curve.md#properties)</sub>

### tilt

> _type_: **Float**
>

> **node** : [Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/curve_tilt.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Properties](geono-curve.md#properties)</sub>

## Methods



----------
### Arc()

> classmethod

``` python
Arc(resolution=None, radius=None, start_angle=None, sweep_angle=None, start=None, middle=None, end=None, offset_angle=None, connect_center=None, invert_arc=None)
```

> **node** : [Arc](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/arc.html)



'mode' is set to 'POINTS' if one in (start, middle, end, offset_angle) is not None, 'RADIUS' otherwise.

- mode (str): Node.mode in ('POINTS', 'RADIUS')

#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (Resolution)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **start_angle** (_Float_ = None) : socket 'Start Angle' (Start Angle)
- **sweep_angle** (_Float_ = None) : socket 'Sweep Angle' (Sweep Angle)
- **start** (_Vector_ = None) : socket 'Start' (Start)
- **middle** (_Vector_ = None) : socket 'Middle' (Middle)
- **end** (_Vector_ = None) : socket 'End' (End)
- **offset_angle** (_Float_ = None) : socket 'Offset Angle' (Offset Angle)
- **connect_center** (_Boolean_ = None) : socket 'Connect Center' (Connect Center)
- **invert_arc** (_Boolean_ = None) : socket 'Invert Arc' (Invert Arc)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### BezierSegment()

> classmethod

``` python
BezierSegment(resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION')
```

> **node** : ERROR: Node 'Bézier Segment' not found



#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (Resolution)
- **start** (_Vector_ = None) : socket 'Start' (Start)
- **start_handle** (_Vector_ = None) : socket 'Start Handle' (Start Handle)
- **end_handle** (_Vector_ = None) : socket 'End Handle' (End Handle)
- **end** (_Vector_ = None) : socket 'End' (End)
- **mode** (_str_ = POSITION) : Node.mode in ('POSITION', 'OFFSET')



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### Circle()

> classmethod

``` python
Circle(resolution=None, radius=None, point_1=None, point_2=None, point_3=None)
```

> **node** : [Curve Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_circle.html)



'mode' is set to 'POINTS' if one in (point_1, point_2, point_) is not None, 'RADIUS' otherwise

- mode (str): Node.mode in ('POINTS', 'RADIUS')

#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (Resolution)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **point_1** (_Vector_ = None) : socket 'Point 1' (Point 1)
- **point_2** (_Vector_ = None) : socket 'Point 2' (Point 2)
- **point_3** (_Vector_ = None) : socket 'Point 3' (Point 3)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### curve_of_point()

> classmethod

``` python
curve_of_point(point_index=None)
```

> **node** : [Curve of Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/curve_of_point.html)



#### Arguments:
- **point_index** (_Integer_ = None) : socket 'Point Index' (Point Index)



#### Returns:
- **Node** : [curve_index (Integer), index_in_curve (Integer)]

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### deform_on_surface()

> method

``` python
deform_on_surface()
```

> **node** : [Deform Curves on Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/deform_curves_on_surface.html)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### endpoint_selection()

> classmethod

``` python
endpoint_selection(start_size=None, end_size=None)
```

> **node** : [Endpoint Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/endpoint_selection.html)



#### Arguments:
- **start_size** (_Integer_ = None) : socket 'Start Size' (Start Size)
- **end_size** (_Integer_ = None) : socket 'End Size' (End Size)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### fill()

> method

``` python
fill(group_id=None, mode='TRIANGLES')
```

> **node** : [Fill Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fill_curve.html)



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group ID)
- **mode** (_str_ = TRIANGLES) : Node.mode in ('TRIANGLES', 'NGONS')



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### fillet()

> method

``` python
fillet(radius=None, limit_radius=None, count=None, mode='BEZIER')
```

> **node** : [Fillet Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fillet_curve.html)



#### Arguments:
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **limit_radius** (_Boolean_ = None) : socket 'Limit Radius' (Limit Radius)
- **count** (_Integer_ = None) : socket 'Integer' (Integer)
- **mode** (_str_ = BEZIER) : Node.mode in ('BEZIER', 'POLY')



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### FromEdgePaths()

> classmethod

``` python
FromEdgePaths(mesh, next_vertex_index=None)
```

> **node** : [Edge Paths to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/edge_paths_to_curves.html)



#### Arguments:
- **mesh** (_Geometry_) : socket 'Mesh' (Mesh)
- **next_vertex_index** (_Integer_ = None) : socket 'Next Vertex Index' (Next Vertex Index)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### FromMesh()

> classmethod

``` python
FromMesh(mesh)
```

> **node** : [Mesh to Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_curve.html)



#### Arguments:
- **mesh** (_Geometry_) : socket 'Mesh' (Mesh)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### FromPoints()

> classmethod

``` python
FromPoints(points, curve_group_id=None, weight=None)
```

> **node** : [Points to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_curves.html)



#### Arguments:
- **points** (_Geometry_) : socket 'Points' (Points)
- **curve_group_id** (_Integer_ = None) : socket 'Curve Group ID' (Curve Group ID)
- **weight** (_Float_ = None) : socket 'Weight' (Weight)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### interpolate()

> method

``` python
interpolate(guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None)
```

> **node** : [Interpolate Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/interpolate_curves.html)



#### Arguments:
- **guide_up** (_Vector_ = None) : socket 'Guide Up' (Guide Up)
- **guide_group_id** (_Integer_ = None) : socket 'Guide Group ID' (Guide Group ID)
- **points** (_Geometry_ = None) : socket 'Points' (Points)
- **point_up** (_Vector_ = None) : socket 'Point Up' (Point Up)
- **point_group_id** (_Integer_ = None) : socket 'Point Group ID' (Point Group ID)
- **max_neighbors** (_Integer_ = None) : socket 'Max Neighbors' (Max Neighbors)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### Kite()

> classmethod

``` python
Kite(width=None, bottom_height=None, top_height=None)
```

> **node** : [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html)



#### Arguments:
- **width** (_Float_ = None) : socket 'Width' (Width)
- **bottom_height** ( = None)
- **top_height** ( = None)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### Line()

> classmethod

``` python
Line(start=None, end=None, direction=None, length=None)
```

> **node** : [Curve Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_line.html)



'mode' is set to 'DIRECTION' if one in (direction, length) is not None, 'POINTS' otherwise.

- mode (str): Node.mode in ('POINTS', 'DIRECTION')

#### Arguments:
- **start** (_Vector_ = None) : socket 'Start' (Start)
- **end** (_Vector_ = None) : socket 'End' (End)
- **direction** ( = None)
- **length** ( = None)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### offset_point_in_curve()

> classmethod

``` python
offset_point_in_curve(point_index=None, offset=None)
```

> **node** : [Offset Point in Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/offset_point_in_curve.html)



#### Arguments:
- **point_index** (_Integer_ = None) : socket 'Point Index' (Point Index)
- **offset** (_Integer_ = None) : socket 'Offset' (Offset)



#### Returns:
- **Node** : [is_valid_offset (Boolean), point_index (Integer)]

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### Parallelogram()

> classmethod

``` python
Parallelogram(width=None, height=None, offset=None)
```

> **node** : [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html)



#### Arguments:
- **width** (_Float_ = None) : socket 'Width' (Width)
- **height** (_Float_ = None) : socket 'Height' (Height)
- **offset** ( = None)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### Points()

> classmethod

``` python
Points(point_1=None, point_2=None, point_3=None, point_4=None)
```

> **node** : [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html)



#### Arguments:
- **point_1** ( = None)
- **point_2** ( = None)
- **point_3** ( = None)
- **point_4** ( = None)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### points_of_curve()

> classmethod

``` python
points_of_curve(curve_index=None, weights=None, sort_index=None)
```

> **node** : [Points of Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/points_of_curve.html)



#### Arguments:
- **curve_index** (_Integer_ = None) : socket 'Curve Index' (Curve Index)
- **weights** (_Float_ = None) : socket 'Weights' (Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (Sort Index)



#### Returns:
- **Node** : [point_index (Integer), total (Integer)]

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### QuadraticBezier()

> classmethod

``` python
QuadraticBezier(resolution=None, start=None, middle=None, end=None)
```

> **node** : ERROR: Node 'Quadratic Bézier' not found



#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (Resolution)
- **start** (_Vector_ = None) : socket 'Start' (Start)
- **middle** (_Vector_ = None) : socket 'Middle' (Middle)
- **end** (_Vector_ = None) : socket 'End' (End)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### Quadrilateral()

> classmethod

``` python
Quadrilateral(width=None, height=None)
```

> **node** : [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html)



#### Arguments:
- **width** (_Float_ = None) : socket 'Width' (Width)
- **height** (_Float_ = None) : socket 'Height' (Height)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### Rectangle()

> classmethod

``` python
Rectangle(width=None, height=None)
```

> **node** : [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html)



#### Arguments:
- **width** (_Float_ = None) : socket 'Width' (Width)
- **height** (_Float_ = None) : socket 'Height' (Height)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### resample()

> method

``` python
resample(count=None, length=None)
```

> **node** : [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/resample_curve.html)



Parameter 'mode'
---------------
- mode (str): Node.mode in ('EVALUATED', 'COUNT', 'LENGTH')
- if 'count' is not None : 'COUNT'
- elif 'length' is not None : 'LENGTH'
- else : 'EVALUATED'

#### Arguments:
- **count** (_Integer_ = None) : socket 'Count' (Count)
- **length** ( = None)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### reverse()

> method

``` python
reverse()
```

> **node** : [Reverse Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/reverse_curve.html)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### sample()

> method

``` python
sample(value=None, factor=None, length=None, curve_index=None, all_curves=False)
```

> **node** : [Sample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample/sample_curve.html)



'mode' is set to 'LENGTH' if factor is None, else 'FACTOR'

- data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
- mode (str): Node.mode in ('FACTOR', 'LENGTH')

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (Value)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **length** (_Float_ = None) : socket 'Length' (Length)
- **curve_index** (_Integer_ = None) : socket 'Curve Index' (Curve Index)
- **all_curves** (_bool_ = False) : Node.use_all_curves



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### set_normal()

> method

``` python
set_normal(mode='MINIMUM_TWIST')
```

> **node** : [Set Curve Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_curve_normal.html)



#### Arguments:
- **mode** (_str_ = MINIMUM_TWIST) : Node.mode in ('MINIMUM_TWIST', 'Z_UP', 'FREE')



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### set_normal_free()

> method

``` python
set_normal_free()
```

> **node** : [Set Curve Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_curve_normal.html)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### set_normal_z_up()

> method

``` python
set_normal_z_up()
```

> **node** : [Set Curve Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_curve_normal.html)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### Spiral()

> classmethod

``` python
Spiral(resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None)
```

> **node** : ERROR: Node 'Spiral' not found



#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (Resolution)
- **rotations** (_Float_ = None) : socket 'Rotations' (Rotations)
- **start_radius** (_Float_ = None) : socket 'Start Radius' (Start Radius)
- **end_radius** (_Float_ = None) : socket 'End Radius' (End Radius)
- **height** (_Float_ = None) : socket 'Height' (Height)
- **reverse** (_Boolean_ = None) : socket 'Reverse' (Reverse)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### Star()

> classmethod

``` python
Star(points=None, inner_radius=None, outer_radius=None, twist=None)
```

> **node** : [Star](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/star.html)



#### Arguments:
- **points** (_Integer_ = None) : socket 'Points' (Points)
- **inner_radius** (_Float_ = None) : socket 'Inner Radius' (Inner Radius)
- **outer_radius** (_Float_ = None) : socket 'Outer Radius' (Outer Radius)
- **twist** (_Float_ = None) : socket 'Twist' (Twist)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### subdivide()

> method

``` python
subdivide(cuts=None)
```

> **node** : [Subdivide Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/subdivide_curve.html)



#### Arguments:
- **cuts** (_Integer_ = None) : socket 'Cuts' (Cuts)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### to_mesh()

> method

``` python
to_mesh(profile_curve=None, fill_caps=None)
```

> **node** : [Curve to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_mesh.html)



#### Arguments:
- **profile_curve** (_Geometry_ = None) : socket 'Profile Curve' (Profile Curve)
- **fill_caps** (_Boolean_ = None) : socket 'Fill Caps' (Fill Caps)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### to_points()

> method

``` python
to_points(count=None, length=None, mode='EVALUATED')
```

> **node** : [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_points.html)



#### Arguments:
- **count** (_Integer_ = None) : socket 'Count' (Count)
- **length** ( = None)
- **mode** (_str_ = EVALUATED) : Node.mode in ('EVALUATED', 'COUNT', 'LENGTH')



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### Trapezoid()

> classmethod

``` python
Trapezoid(height=None, bottom_width=None, top_width=None, offset=None)
```

> **node** : [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html)



#### Arguments:
- **height** (_Float_ = None) : socket 'Height' (Height)
- **bottom_width** (_Float_ = None) : socket 'Bottom Width' (Bottom Width)
- **top_width** (_Float_ = None) : socket 'Top Width' (Top Width)
- **offset** (_Float_ = None) : socket 'Offset' (Offset)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### trim()

> method

``` python
trim(start=None, end=None, mode='FACTOR')
```

> **node** : [Trim Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/trim_curve.html)



#### Arguments:
- **start** (_Float_ = None) : socket 'Start' (Start)
- **end** (_Float_ = None) : socket 'End' (End)
- **mode** (_str_ = FACTOR) : Node.mode in ('FACTOR', 'LENGTH')



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### trim_factor()

> method

``` python
trim_factor(start=None, end=None)
```

> **node** : [Trim Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/trim_curve.html)



#### Arguments:
- **start** (_Float_ = None) : socket 'Start' (Start)
- **end** (_Float_ = None) : socket 'End' (End)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>

----------
### trim_length()

> method

``` python
trim_length(start=None, end=None)
```

> **node** : [Trim Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/trim_curve.html)



#### Arguments:
- **start** (_Float_ = None) : socket 'Start' (Start)
- **end** (_Float_ = None) : socket 'End' (End)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](geono-curve.md#curve) :black_small_square: [Content](geono-curve.md#content) :black_small_square: [Methods](geono-curve.md#methods)</sub>