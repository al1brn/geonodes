# Curve

``` python
Curve(value=None, name=None, tip=None, panel='', hide_value=False, hide_in_modifier=False)
```

> Curve Geometry

The **Curve** class exposes all methods specific to curves.
Since there is no ambiguity, the word **curve** is omitted in the name of
the methods:

``` python
curve = Curve.Line() # Node 'Curve Line'
mesh= curve.fill() # Node 'Fill Curve'
```

Nodes requiring a domain parameter, are implemented in one of the two domains of **Curve** [points](curve.md#points),
[splines](curve.md#splines).

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **panel** (_str_ = ) : panel name (overrides tree panel if exists)
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option

### Inherited

[\_\_add__](boolean.md#__add__) :black_small_square: [bake](geometry.md#bake) :black_small_square: [bounding_box](core-gener-geome-geometry.md#bounding_box) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [convex_hull](core-gener-geome-geometry.md#convex_hull) :black_small_square: [curve](core-gener-geome-geometry.md#curve) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](socket.md#_domain_to_geometry) :black_small_square: [\_geo](cloudpoint.md#_geo) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [grease_pencil](core-gener-geome-geometry.md#grease_pencil) :black_small_square: [id](core-gener-geome-geometry.md#id) :black_small_square: [index_of_nearest](core-gener-geome-geometry.md#index_of_nearest) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](boolean.md#__init__) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [instance_on_points](core-gener-geome-geometry.md#instance_on_points) :black_small_square: [instances](core-gener-geome-geometry.md#instances) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [Join](core-gener-geome-geometry.md#join) :black_small_square: [join](core-gener-geome-geometry.md#join) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [link_from](socket.md#link_from) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [\_mark_for_delete](socket.md#_mark_for_delete) :black_small_square: [material](core-gener-geome-geometry.md#material) :black_small_square: [material_index](core-gener-geome-geometry.md#material_index) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [merge](core-gener-geome-geometry.md#merge) :black_small_square: [merge_all](core-gener-geome-geometry.md#merge_all) :black_small_square: [merge_by_distance](core-gener-geome-geometry.md#merge_by_distance) :black_small_square: [merge_connected](core-gener-geome-geometry.md#merge_connected) :black_small_square: [mesh](core-gener-geome-geometry.md#mesh) :black_small_square: [\_name](socket.md#_name) :black_small_square: [name](core-gener-geome-geometry.md#name) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [offset](core-gener-geome-geometry.md#offset) :black_small_square: [option](socket.md#option) :black_small_square: [option_index](socket.md#option_index) :black_small_square: [out](socket.md#out) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [point_cloud](core-gener-geome-geometry.md#point_cloud) :black_small_square: [position](core-gener-geome-geometry.md#position) :black_small_square: [proximity](core-gener-geome-geometry.md#proximity) :black_small_square: [proximity_edges](core-gener-geome-geometry.md#proximity_edges) :black_small_square: [proximity_faces](core-gener-geome-geometry.md#proximity_faces) :black_small_square: [proximity_points](core-gener-geome-geometry.md#proximity_points) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [raycast](core-gener-geome-geometry.md#raycast) :black_small_square: [raycast_interpolated](core-gener-geome-geometry.md#raycast_interpolated) :black_small_square: [raycast_nearest](core-gener-geome-geometry.md#raycast_nearest) :black_small_square: [realize](core-gener-geome-geometry.md#realize) :black_small_square: [remove_named_attribute](core-gener-geome-geometry.md#remove_named_attribute) :black_small_square: [remove_names](core-gener-geome-geometry.md#remove_names) :black_small_square: [replace_material](core-gener-geome-geometry.md#replace_material) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_sel](geobase.md#_sel) :black_small_square: [separate_components](core-gener-geome-geometry.md#separate_components) :black_small_square: [\_\_setattr__](socket.md#__setattr__) :black_small_square: [set_id](core-gener-geome-geometry.md#set_id) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [set_material](core-gener-geome-geometry.md#set_material) :black_small_square: [set_material_index](core-gener-geome-geometry.md#set_material_index) :black_small_square: [set_name](core-gener-geome-geometry.md#set_name) :black_small_square: [set_position](core-gener-geome-geometry.md#set_position) :black_small_square: [set_spline_cyclic](core-gener-geome-geometry.md#set_spline_cyclic) :black_small_square: [set_spline_resolution](core-gener-geome-geometry.md#set_spline_resolution) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [switch_false](socket.md#switch_false) :black_small_square: [to_instance](core-gener-geome-geometry.md#to_instance) :black_small_square: [transform](core-gener-geome-geometry.md#transform) :black_small_square: [transform_components](core-gener-geome-geometry.md#transform_components) :black_small_square: [transform_matrix](core-gener-geome-geometry.md#transform_matrix) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square: [viewer](core-gener-geome-geometry.md#viewer) :black_small_square: [volume](core-gener-geome-geometry.md#volume) :black_small_square:

## Content

- **A** : [Arc](curve.md#arc) :black_small_square: [ArcPoints](curve.md#arcpoints) :black_small_square: [ArcRadius](curve.md#arcradius)
- **B** : [BezierSegment](curve.md#beziersegment) :black_small_square: [BeziersegmentOffset](curve.md#beziersegmentoffset) :black_small_square: [BeziersegmentPosition](curve.md#beziersegmentposition)
- **C** : [Circle](curve.md#circle) :black_small_square: [CirclePoints](curve.md#circlepoints) :black_small_square: [CircleRadius](curve.md#circleradius) :black_small_square: [curve_of_point](curve.md#curve_of_point)
- **D** : [deform_on_surface](curve.md#deform_on_surface) :black_small_square: [domain_size](curve.md#domain_size)
- **E** : [endpoint_selection](curve.md#endpoint_selection)
- **F** : [fill](curve.md#fill) :black_small_square: [fillet](curve.md#fillet) :black_small_square: [fillet_bezier](curve.md#fillet_bezier) :black_small_square: [fillet_poly](curve.md#fillet_poly) :black_small_square: [fill_ngons](curve.md#fill_ngons) :black_small_square: [fill_triangles](curve.md#fill_triangles)
- **H** : [handle_positions](curve.md#handle_positions) :black_small_square: [handle_type](curve.md#handle_type) :black_small_square: [handle_type_selection](curve.md#handle_type_selection)
- **I** : [Interpolate](curve.md#interpolate) :black_small_square: [interpolate](curve.md#interpolate) :black_small_square: [is_cyclic](curve.md#is_cyclic)
- **L** : [left_handle_offset](curve.md#left_handle_offset) :black_small_square: [left_handle_position](curve.md#left_handle_position) :black_small_square: [left_handle_type](curve.md#left_handle_type) :black_small_square: [length](curve.md#length) :black_small_square: [Line](curve.md#line) :black_small_square: [LineDirection](curve.md#linedirection) :black_small_square: [LinePoints](curve.md#linepoints)
- **M** : [material_selection](curve.md#material_selection)
- **N** : [normal](curve.md#normal)
- **O** : [offset_point_in_curve](curve.md#offset_point_in_curve)
- **P** : [points](curve.md#points) :black_small_square: [points_of_curve](curve.md#points_of_curve)
- **Q** : [QuadraticBezier](curve.md#quadraticbezier) :black_small_square: [Quadrilateral](curve.md#quadrilateral) :black_small_square: [QuadrilateralKite](curve.md#quadrilateralkite) :black_small_square: [QuadrilateralParallelogram](curve.md#quadrilateralparallelogram) :black_small_square: [QuadrilateralPoints](curve.md#quadrilateralpoints) :black_small_square: [QuadrilateralRectangle](curve.md#quadrilateralrectangle) :black_small_square: [QuadrilateralTrapezoid](curve.md#quadrilateraltrapezoid)
- **R** : [radius](curve.md#radius) :black_small_square: [resample](curve.md#resample) :black_small_square: [resample_count](curve.md#resample_count) :black_small_square: [resample_evaluated](curve.md#resample_evaluated) :black_small_square: [resample_length](curve.md#resample_length) :black_small_square: [resolution](curve.md#resolution) :black_small_square: [reverse](curve.md#reverse) :black_small_square: [right_handle_offset](curve.md#right_handle_offset) :black_small_square: [right_handle_position](curve.md#right_handle_position) :black_small_square: [right_handle_type](curve.md#right_handle_type)
- **S** : [sample](curve.md#sample) :black_small_square: [sample_factor](curve.md#sample_factor) :black_small_square: [sample_length](curve.md#sample_length) :black_small_square: [set_both_handle_type](curve.md#set_both_handle_type) :black_small_square: [set_handle_positions](curve.md#set_handle_positions) :black_small_square: [set_handle_type](curve.md#set_handle_type) :black_small_square: [set_left_handle_positions](curve.md#set_left_handle_positions) :black_small_square: [set_left_handle_type](curve.md#set_left_handle_type) :black_small_square: [set_normal](curve.md#set_normal) :black_small_square: [set_normal_free](curve.md#set_normal_free) :black_small_square: [set_normal_minimum_twist](curve.md#set_normal_minimum_twist) :black_small_square: [set_normal_z_up](curve.md#set_normal_z_up) :black_small_square: [set_radius](curve.md#set_radius) :black_small_square: [set_right_handle_positions](curve.md#set_right_handle_positions) :black_small_square: [set_right_handle_type](curve.md#set_right_handle_type) :black_small_square: [set_spline_type](curve.md#set_spline_type) :black_small_square: [set_tilt](curve.md#set_tilt) :black_small_square: [Spiral](curve.md#spiral) :black_small_square: [spline_length](curve.md#spline_length) :black_small_square: [spline_parameter](curve.md#spline_parameter) :black_small_square: [splines](curve.md#splines) :black_small_square: [Star](curve.md#star) :black_small_square: [subdivide](curve.md#subdivide)
- **T** : [tilt](curve.md#tilt) :black_small_square: [to_grease_pencil](curve.md#to_grease_pencil) :black_small_square: [to_mesh](curve.md#to_mesh) :black_small_square: [to_points](curve.md#to_points) :black_small_square: [to_points_count](curve.md#to_points_count) :black_small_square: [to_points_evaluated](curve.md#to_points_evaluated) :black_small_square: [to_points_length](curve.md#to_points_length) :black_small_square: [trim](curve.md#trim) :black_small_square: [trim_factor](curve.md#trim_factor) :black_small_square: [trim_length](curve.md#trim_length) :black_small_square: [type](curve.md#type)

## Properties



### handle_type

> _type_: **?**
>

Write only property for node <Node Set Handle Type>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Properties](curve.md#properties)</sub>

### is_cyclic

> _type_: **?**
>

Property get node <Node Set Spline Cyclic>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Properties](curve.md#properties)</sub>

### left_handle_offset

> _type_: **?**
>

Property get node <Node Set Handle Positions>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Properties](curve.md#properties)</sub>

### left_handle_position

> _type_: **?**
>

Property get node <Node Set Handle Positions>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Properties](curve.md#properties)</sub>

### left_handle_type

> _type_: **?**
>

Write only property for node <Node Set Handle Type>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Properties](curve.md#properties)</sub>

### normal

> _type_: **?**
>

Write only property for node <Node Set Curve Normal>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Properties](curve.md#properties)</sub>

### points

> _type_: **SplinePoint**
>

POINT domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Properties](curve.md#properties)</sub>

### radius

> _type_: **?**
>

Property get node <Node Set Curve Radius>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Properties](curve.md#properties)</sub>

### resolution

> _type_: **?**
>

Property get node <Node Set Spline Resolution>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Properties](curve.md#properties)</sub>

### right_handle_offset

> _type_: **?**
>

Property get node <Node Set Handle Positions>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Properties](curve.md#properties)</sub>

### right_handle_position

> _type_: **?**
>

Property get node <Node Set Handle Positions>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Properties](curve.md#properties)</sub>

### right_handle_type

> _type_: **?**
>

Write only property for node <Node Set Handle Type>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Properties](curve.md#properties)</sub>

### splines

> _type_: **Spline**
>

CURVE (or SPLINE) domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Properties](curve.md#properties)</sub>

### tilt

> _type_: **?**
>

Property get node <Node Set Curve Tilt>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Properties](curve.md#properties)</sub>

### type

> _type_: **?**
>

Write only property for node <Node Set Spline Type>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Properties](curve.md#properties)</sub>

## Methods



----------
### Arc()

> classmethod

``` python
Arc(resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None, mode='RADIUS')
```

> Node [Arc](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/arc.html)

#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (id: Resolution)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)
- **start_angle** (_Float_ = None) : socket 'Start Angle' (id: Start Angle)
- **sweep_angle** (_Float_ = None) : socket 'Sweep Angle' (id: Sweep Angle)
- **connect_center** (_Boolean_ = None) : socket 'Connect Center' (id: Connect Center)
- **invert_arc** (_Boolean_ = None) : socket 'Invert Arc' (id: Invert Arc)
- **mode** (_str_ = RADIUS) : parameter 'mode' in ['POINTS', 'RADIUS']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### ArcPoints()

> classmethod

``` python
ArcPoints(resolution=None, start=None, middle=None, end=None, offset_angle=None, connect_center=None, invert_arc=None)
```

> Node [Arc](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/arc.html)

#### Information:
- **Parameter** : 'POINTS'



#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (id: Resolution)
- **start** (_Vector_ = None) : socket 'Start' (id: Start)
- **middle** (_Vector_ = None) : socket 'Middle' (id: Middle)
- **end** (_Vector_ = None) : socket 'End' (id: End)
- **offset_angle** (_Float_ = None) : socket 'Offset Angle' (id: Offset Angle)
- **connect_center** (_Boolean_ = None) : socket 'Connect Center' (id: Connect Center)
- **invert_arc** (_Boolean_ = None) : socket 'Invert Arc' (id: Invert Arc)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### ArcRadius()

> classmethod

``` python
ArcRadius(resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None)
```

> Node [Arc](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/arc.html)

#### Information:
- **Parameter** : 'RADIUS'



#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (id: Resolution)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)
- **start_angle** (_Float_ = None) : socket 'Start Angle' (id: Start Angle)
- **sweep_angle** (_Float_ = None) : socket 'Sweep Angle' (id: Sweep Angle)
- **connect_center** (_Boolean_ = None) : socket 'Connect Center' (id: Connect Center)
- **invert_arc** (_Boolean_ = None) : socket 'Invert Arc' (id: Invert Arc)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### BezierSegment()

> classmethod

``` python
BezierSegment(resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION')
```

> Node ERROR: Node 'Bézier Segment' not found

#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (id: Resolution)
- **start** (_Vector_ = None) : socket 'Start' (id: Start)
- **start_handle** (_Vector_ = None) : socket 'Start Handle' (id: Start Handle)
- **end_handle** (_Vector_ = None) : socket 'End Handle' (id: End Handle)
- **end** (_Vector_ = None) : socket 'End' (id: End)
- **mode** (_str_ = POSITION) : parameter 'mode' in ['POSITION', 'OFFSET']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### BeziersegmentOffset()

> classmethod

``` python
BeziersegmentOffset(resolution=None, start=None, start_handle=None, end_handle=None, end=None)
```

> Node ERROR: Node 'Bézier Segment' not found

#### Information:
- **Parameter** : 'OFFSET'



#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (id: Resolution)
- **start** (_Vector_ = None) : socket 'Start' (id: Start)
- **start_handle** (_Vector_ = None) : socket 'Start Handle' (id: Start Handle)
- **end_handle** (_Vector_ = None) : socket 'End Handle' (id: End Handle)
- **end** (_Vector_ = None) : socket 'End' (id: End)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### BeziersegmentPosition()

> classmethod

``` python
BeziersegmentPosition(resolution=None, start=None, start_handle=None, end_handle=None, end=None)
```

> Node ERROR: Node 'Bézier Segment' not found

#### Information:
- **Parameter** : 'POSITION'



#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (id: Resolution)
- **start** (_Vector_ = None) : socket 'Start' (id: Start)
- **start_handle** (_Vector_ = None) : socket 'Start Handle' (id: Start Handle)
- **end_handle** (_Vector_ = None) : socket 'End Handle' (id: End Handle)
- **end** (_Vector_ = None) : socket 'End' (id: End)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### Circle()

> classmethod

``` python
Circle(resolution=None, radius=None, mode='RADIUS')
```

> Node [Curve Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_circle.html)

#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (id: Resolution)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)
- **mode** (_str_ = RADIUS) : parameter 'mode' in ['POINTS', 'RADIUS']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### CirclePoints()

> classmethod

``` python
CirclePoints(resolution=None, point_1=None, point_2=None, point_3=None)
```

> Node [Curve Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_circle.html)

#### Information:
- **Parameter** : 'POINTS'



#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (id: Resolution)
- **point_1** (_Vector_ = None) : socket 'Point 1' (id: Point 1)
- **point_2** (_Vector_ = None) : socket 'Point 2' (id: Point 2)
- **point_3** (_Vector_ = None) : socket 'Point 3' (id: Point 3)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### CircleRadius()

> classmethod

``` python
CircleRadius(resolution=None, radius=None)
```

> Node [Curve Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_circle.html)

#### Information:
- **Parameter** : 'RADIUS'



#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (id: Resolution)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### curve_of_point()

> classmethod

``` python
curve_of_point(point_index=None)
```

> Node [Curve of Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/curve_of_point.html)

#### Arguments:
- **point_index** (_Integer_ = None) : socket 'Point Index' (id: Point Index)



#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### deform_on_surface()

> method

``` python
deform_on_surface()
```

> Node [Deform Curves on Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/deform_curves_on_surface.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### domain_size()

> method

``` python
domain_size()
```

> Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)

#### Information:
- **Socket** : self
- **Parameter** : 'CURVE'



#### Returns:
- **node** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### endpoint_selection()

> classmethod

``` python
endpoint_selection(start_size=None, end_size=None)
```

> Node [Endpoint Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/endpoint_selection.html)

#### Arguments:
- **start_size** (_Integer_ = None) : socket 'Start Size' (id: Start Size)
- **end_size** (_Integer_ = None) : socket 'End Size' (id: End Size)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### fill()

> method

``` python
fill(group_id=None, mode='TRIANGLES')
```

> Node [Fill Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fill_curve.html)

#### Information:
- **Socket** : self



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)
- **mode** (_str_ = TRIANGLES) : parameter 'mode' in ['TRIANGLES', 'NGONS']



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### fillet()

> method

``` python
fillet(radius=None, limit_radius=None, mode='BEZIER')
```

> Node [Fillet Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fillet_curve.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)
- **limit_radius** (_Boolean_ = None) : socket 'Limit Radius' (id: Limit Radius)
- **mode** (_str_ = BEZIER) : parameter 'mode' in ['BEZIER', 'POLY']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### fillet_bezier()

> method

``` python
fillet_bezier(radius=None, limit_radius=None)
```

> Node [Fillet Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fillet_curve.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Parameter** : 'BEZIER'



#### Arguments:
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)
- **limit_radius** (_Boolean_ = None) : socket 'Limit Radius' (id: Limit Radius)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### fillet_poly()

> method

``` python
fillet_poly(count=None, radius=None, limit_radius=None)
```

> Node [Fillet Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fillet_curve.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Parameter** : 'POLY'



#### Arguments:
- **count** (_Integer_ = None) : socket 'Count' (id: Count)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)
- **limit_radius** (_Boolean_ = None) : socket 'Limit Radius' (id: Limit Radius)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### fill_ngons()

> method

``` python
fill_ngons(group_id=None)
```

> Node [Fill Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fill_curve.html)

#### Information:
- **Socket** : self
- **Parameter** : 'NGONS'



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### fill_triangles()

> method

``` python
fill_triangles(group_id=None)
```

> Node [Fill Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fill_curve.html)

#### Information:
- **Socket** : self
- **Parameter** : 'TRIANGLES'



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### handle_positions()

> classmethod

``` python
handle_positions(relative=None)
```

> Node [Curve Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/curve_handle_positions.html)

#### Arguments:
- **relative** (_Boolean_ = None) : socket 'Relative' (id: Relative)



#### Returns:
- **Vector** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### handle_type_selection()

> classmethod

``` python
handle_type_selection(handle_type='AUTO', mode={'LEFT', 'RIGHT'})
```

> Node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/handle_type_selection.html)

#### Arguments:
- **handle_type** (_str_ = AUTO) : parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']
- **mode** (_set_ = {'LEFT', 'RIGHT'}) : parameter 'mode'



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### Interpolate()

> classmethod

``` python
Interpolate(guide_curves=None, guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None)
```

> Node [Interpolate Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/interpolate_curves.html)

#### Arguments:
- **guide_curves** (_Geometry_ = None) : socket 'Guide Curves' (id: Guide Curves)
- **guide_up** (_Vector_ = None) : socket 'Guide Up' (id: Guide Up)
- **guide_group_id** (_Integer_ = None) : socket 'Guide Group ID' (id: Guide Group ID)
- **points** (_Geometry_ = None) : socket 'Points' (id: Points)
- **point_up** (_Vector_ = None) : socket 'Point Up' (id: Point Up)
- **point_group_id** (_Integer_ = None) : socket 'Point Group ID' (id: Point Group ID)
- **max_neighbors** (_Integer_ = None) : socket 'Max Neighbors' (id: Max Neighbors)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### interpolate()

> method

``` python
interpolate(guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None)
```

> Node [Interpolate Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/interpolate_curves.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **guide_up** (_Vector_ = None) : socket 'Guide Up' (id: Guide Up)
- **guide_group_id** (_Integer_ = None) : socket 'Guide Group ID' (id: Guide Group ID)
- **points** (_Geometry_ = None) : socket 'Points' (id: Points)
- **point_up** (_Vector_ = None) : socket 'Point Up' (id: Point Up)
- **point_group_id** (_Integer_ = None) : socket 'Point Group ID' (id: Point Group ID)
- **max_neighbors** (_Integer_ = None) : socket 'Max Neighbors' (id: Max Neighbors)



#### Returns:
- **Curve** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### length()

> method

``` python
length()
```

> Node [Curve Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/curve_length.html)

#### Information:
- **Socket** : self



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### Line()

> classmethod

``` python
Line(start=None, end=None, mode='POINTS')
```

> Node [Curve Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_line.html)

#### Arguments:
- **start** (_Vector_ = None) : socket 'Start' (id: Start)
- **end** (_Vector_ = None) : socket 'End' (id: End)
- **mode** (_str_ = POINTS) : parameter 'mode' in ['POINTS', 'DIRECTION']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### LineDirection()

> classmethod

``` python
LineDirection(start=None, direction=None, length=None)
```

> Node [Curve Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_line.html)

#### Information:
- **Parameter** : 'DIRECTION'



#### Arguments:
- **start** (_Vector_ = None) : socket 'Start' (id: Start)
- **direction** (_Vector_ = None) : socket 'Direction' (id: Direction)
- **length** (_Float_ = None) : socket 'Length' (id: Length)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### LinePoints()

> classmethod

``` python
LinePoints(start=None, end=None)
```

> Node [Curve Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_line.html)

#### Information:
- **Parameter** : 'POINTS'



#### Arguments:
- **start** (_Vector_ = None) : socket 'Start' (id: Start)
- **end** (_Vector_ = None) : socket 'End' (id: End)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### material_selection()

> classmethod

``` python
material_selection(material=None)
```

> Node [Material Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html)

#### Arguments:
- **material** (_Material_ = None) : socket 'Material' (id: Material)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### offset_point_in_curve()

> classmethod

``` python
offset_point_in_curve(point_index=None, offset=None)
```

> Node [Offset Point in Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/offset_point_in_curve.html)

#### Arguments:
- **point_index** (_Integer_ = None) : socket 'Point Index' (id: Point Index)
- **offset** (_Integer_ = None) : socket 'Offset' (id: Offset)



#### Returns:
- **Boolean** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### points_of_curve()

> classmethod

``` python
points_of_curve(curve_index=None, weights=None, sort_index=None)
```

> Node [Points of Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/points_of_curve.html)

#### Arguments:
- **curve_index** (_Integer_ = None) : socket 'Curve Index' (id: Curve Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### QuadraticBezier()

> classmethod

``` python
QuadraticBezier(resolution=None, start=None, middle=None, end=None)
```

> Node ERROR: Node 'Quadratic Bézier' not found

#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (id: Resolution)
- **start** (_Vector_ = None) : socket 'Start' (id: Start)
- **middle** (_Vector_ = None) : socket 'Middle' (id: Middle)
- **end** (_Vector_ = None) : socket 'End' (id: End)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### Quadrilateral()

> classmethod

``` python
Quadrilateral(width=None, height=None, mode='RECTANGLE')
```

> Node [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html)

#### Arguments:
- **width** (_Float_ = None) : socket 'Width' (id: Width)
- **height** (_Float_ = None) : socket 'Height' (id: Height)
- **mode** (_str_ = RECTANGLE) : parameter 'mode' in ['RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### QuadrilateralKite()

> classmethod

``` python
QuadrilateralKite(width=None, bottom_height=None, top_height=None)
```

> Node [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html)

#### Information:
- **Parameter** : 'KITE'



#### Arguments:
- **width** (_Float_ = None) : socket 'Width' (id: Width)
- **bottom_height** (_Float_ = None) : socket 'Bottom Height' (id: Bottom Height)
- **top_height** (_Float_ = None) : socket 'Top Height' (id: Top Height)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### QuadrilateralParallelogram()

> classmethod

``` python
QuadrilateralParallelogram(width=None, height=None, offset=None)
```

> Node [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html)

#### Information:
- **Parameter** : 'PARALLELOGRAM'



#### Arguments:
- **width** (_Float_ = None) : socket 'Width' (id: Width)
- **height** (_Float_ = None) : socket 'Height' (id: Height)
- **offset** (_Float_ = None) : socket 'Offset' (id: Offset)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### QuadrilateralPoints()

> classmethod

``` python
QuadrilateralPoints(width=None, point_1=None, point_2=None, point_3=None, point_4=None)
```

> Node [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html)

#### Information:
- **Parameter** : 'POINTS'



#### Arguments:
- **width** (_Float_ = None) : socket 'Width' (id: Width)
- **point_1** (_Vector_ = None) : socket 'Point 1' (id: Point 1)
- **point_2** (_Vector_ = None) : socket 'Point 2' (id: Point 2)
- **point_3** (_Vector_ = None) : socket 'Point 3' (id: Point 3)
- **point_4** (_Vector_ = None) : socket 'Point 4' (id: Point 4)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### QuadrilateralRectangle()

> classmethod

``` python
QuadrilateralRectangle(width=None, height=None)
```

> Node [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html)

#### Information:
- **Parameter** : 'RECTANGLE'



#### Arguments:
- **width** (_Float_ = None) : socket 'Width' (id: Width)
- **height** (_Float_ = None) : socket 'Height' (id: Height)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### QuadrilateralTrapezoid()

> classmethod

``` python
QuadrilateralTrapezoid(width=None, height=None, bottom_width=None, top_width=None, offset=None)
```

> Node [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html)

#### Information:
- **Parameter** : 'TRAPEZOID'



#### Arguments:
- **width** (_Float_ = None) : socket 'Width' (id: Width)
- **height** (_Float_ = None) : socket 'Height' (id: Height)
- **bottom_width** (_Float_ = None) : socket 'Bottom Width' (id: Bottom Width)
- **top_width** (_Float_ = None) : socket 'Top Width' (id: Top Width)
- **offset** (_Float_ = None) : socket 'Offset' (id: Offset)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### resample()

> method

``` python
resample(count=None, keep_last_segment=True, mode='COUNT')
```

> Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/resample_curve.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **count** (_Integer_ = None) : socket 'Count' (id: Count)
- **keep_last_segment** (_bool_ = True) : parameter 'keep_last_segment'
- **mode** (_str_ = COUNT) : parameter 'mode' in ['EVALUATED', 'COUNT', 'LENGTH']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### resample_count()

> method

``` python
resample_count(count=None, keep_last_segment=True)
```

> Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/resample_curve.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'COUNT'



#### Arguments:
- **count** (_Integer_ = None) : socket 'Count' (id: Count)
- **keep_last_segment** (_bool_ = True) : parameter 'keep_last_segment'



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### resample_evaluated()

> method

``` python
resample_evaluated(keep_last_segment=True)
```

> Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/resample_curve.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'EVALUATED'



#### Arguments:
- **keep_last_segment** (_bool_ = True) : parameter 'keep_last_segment'



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### resample_length()

> method

``` python
resample_length(length=None, keep_last_segment=True)
```

> Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/resample_curve.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'LENGTH'



#### Arguments:
- **length** (_Float_ = None) : socket 'Length' (id: Length)
- **keep_last_segment** (_bool_ = True) : parameter 'keep_last_segment'



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### reverse()

> method

``` python
reverse()
```

> Node [Reverse Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/reverse_curve.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### sample()

> method

``` python
sample(value=None, curve_index=None, factor=None, mode='FACTOR', use_all_curves=False)
```

> Node [Sample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample/sample_curve.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'value' type



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **curve_index** (_Integer_ = None) : socket 'Curve Index' (id: Curve Index)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)
- **mode** (_str_ = FACTOR) : parameter 'mode' in ['FACTOR', 'LENGTH']
- **use_all_curves** (_bool_ = False) : parameter 'use_all_curves'



#### Returns:
- **Float** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### sample_factor()

> method

``` python
sample_factor(value=None, curve_index=None, factor=None, use_all_curves=False)
```

> Node [Sample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample/sample_curve.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'value' type
- **Parameter** : 'FACTOR'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **curve_index** (_Integer_ = None) : socket 'Curve Index' (id: Curve Index)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)
- **use_all_curves** (_bool_ = False) : parameter 'use_all_curves'



#### Returns:
- **Float** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### sample_length()

> method

``` python
sample_length(value=None, length=None, curve_index=None, use_all_curves=False)
```

> Node [Sample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample/sample_curve.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'value' type
- **Parameter** : 'LENGTH'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **length** (_Float_ = None) : socket 'Length' (id: Length)
- **curve_index** (_Integer_ = None) : socket 'Curve Index' (id: Curve Index)
- **use_all_curves** (_bool_ = False) : parameter 'use_all_curves'



#### Returns:
- **Float** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_both_handle_type()

> method

``` python
set_both_handle_type(handle_type='AUTO')
```

> Node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : {'LEFT', 'RIGHT'}



#### Arguments:
- **handle_type** (_str_ = AUTO) : parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_handle_positions()

> method

``` python
set_handle_positions(position=None, offset=None, mode='LEFT')
```

> Node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_positions.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **offset** (_Vector_ = None) : socket 'Offset' (id: Offset)
- **mode** (_str_ = LEFT) : parameter 'mode' in ['LEFT', 'RIGHT']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_handle_type()

> method

``` python
set_handle_type(handle_type='AUTO', mode={'LEFT', 'RIGHT'})
```

> Node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **handle_type** (_str_ = AUTO) : parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']
- **mode** (_set_ = {'LEFT', 'RIGHT'}) : parameter 'mode'



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_left_handle_positions()

> method

``` python
set_left_handle_positions(position=None, offset=None)
```

> Node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_positions.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'LEFT'



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **offset** (_Vector_ = None) : socket 'Offset' (id: Offset)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_left_handle_type()

> method

``` python
set_left_handle_type(handle_type='AUTO')
```

> Node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : {'LEFT'}



#### Arguments:
- **handle_type** (_str_ = AUTO) : parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_normal()

> method

``` python
set_normal(mode='MINIMUM_TWIST')
```

> Node [Set Curve Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_curve_normal.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **mode** (_str_ = MINIMUM_TWIST) : parameter 'mode' in ['MINIMUM_TWIST', 'Z_UP', 'FREE']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_normal_free()

> method

``` python
set_normal_free(normal=None)
```

> Node [Set Curve Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_curve_normal.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FREE'



#### Arguments:
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_normal_minimum_twist()

> method

``` python
set_normal_minimum_twist()
```

> Node [Set Curve Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_curve_normal.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'MINIMUM_TWIST'



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_normal_z_up()

> method

``` python
set_normal_z_up()
```

> Node [Set Curve Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_curve_normal.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'Z_UP'



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_radius()

> method

``` python
set_radius(radius=None)
```

> Node [Set Curve Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_curve_radius.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_right_handle_positions()

> method

``` python
set_right_handle_positions(position=None, offset=None)
```

> Node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_positions.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'RIGHT'



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **offset** (_Vector_ = None) : socket 'Offset' (id: Offset)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_right_handle_type()

> method

``` python
set_right_handle_type(handle_type='AUTO')
```

> Node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : {'RIGHT'}



#### Arguments:
- **handle_type** (_str_ = AUTO) : parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_spline_type()

> method

``` python
set_spline_type(spline_type='POLY')
```

> Node [Set Spline Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_spline_type.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **spline_type** (_str_ = POLY) : parameter 'spline_type' in ['CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_tilt()

> method

``` python
set_tilt(tilt=None)
```

> Node [Set Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_curve_tilt.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **tilt** (_Float_ = None) : socket 'Tilt' (id: Tilt)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### Spiral()

> classmethod

``` python
Spiral(resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None)
```

> Node [Spiral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_spiral.html)

#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (id: Resolution)
- **rotations** (_Float_ = None) : socket 'Rotations' (id: Rotations)
- **start_radius** (_Float_ = None) : socket 'Start Radius' (id: Start Radius)
- **end_radius** (_Float_ = None) : socket 'End Radius' (id: End Radius)
- **height** (_Float_ = None) : socket 'Height' (id: Height)
- **reverse** (_Boolean_ = None) : socket 'Reverse' (id: Reverse)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### spline_length()

> classmethod

``` python
spline_length()
```

> Node [Spline Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/spline_length.html)

#### Returns:
- **Float** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### spline_parameter()

> classmethod

``` python
spline_parameter()
```

> Node [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/spline_parameter.html)

#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### Star()

> classmethod

``` python
Star(points=None, inner_radius=None, outer_radius=None, twist=None)
```

> Node [Star](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/star.html)

#### Arguments:
- **points** (_Integer_ = None) : socket 'Points' (id: Points)
- **inner_radius** (_Float_ = None) : socket 'Inner Radius' (id: Inner Radius)
- **outer_radius** (_Float_ = None) : socket 'Outer Radius' (id: Outer Radius)
- **twist** (_Float_ = None) : socket 'Twist' (id: Twist)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### subdivide()

> method

``` python
subdivide(cuts=None)
```

> Node [Subdivide Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/subdivide_curve.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **cuts** (_Integer_ = None) : socket 'Cuts' (id: Cuts)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### to_grease_pencil()

> method

``` python
to_grease_pencil(instances_as_layers=None)
```

> Node [Curves to Grease Pencil](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curves_to_grease_pencil.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **instances_as_layers** (_Boolean_ = None) : socket 'Instances as Layers' (id: Instances as Layers)



#### Returns:
- **GreasePencil** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### to_mesh()

> method

``` python
to_mesh(profile_curve=None, scale=None, fill_caps=None)
```

> Node [Curve to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_mesh.html)

#### Information:
- **Socket** : self



#### Arguments:
- **profile_curve** (_Geometry_ = None) : socket 'Profile Curve' (id: Profile Curve)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **fill_caps** (_Boolean_ = None) : socket 'Fill Caps' (id: Fill Caps)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### to_points()

> method

``` python
to_points(count=None, mode='COUNT')
```

> Node [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_points.html)

#### Information:
- **Socket** : self



#### Arguments:
- **count** (_Integer_ = None) : socket 'Count' (id: Count)
- **mode** (_str_ = COUNT) : parameter 'mode' in ['EVALUATED', 'COUNT', 'LENGTH']



#### Returns:
- **Cloud** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### to_points_count()

> method

``` python
to_points_count(count=None)
```

> Node [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_points.html)

#### Information:
- **Socket** : self
- **Parameter** : 'COUNT'



#### Arguments:
- **count** (_Integer_ = None) : socket 'Count' (id: Count)



#### Returns:
- **Cloud** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### to_points_evaluated()

> method

``` python
to_points_evaluated()
```

> Node [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_points.html)

#### Information:
- **Socket** : self
- **Parameter** : 'EVALUATED'



#### Returns:
- **Cloud** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### to_points_length()

> method

``` python
to_points_length(length=None)
```

> Node [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_points.html)

#### Information:
- **Socket** : self
- **Parameter** : 'LENGTH'



#### Arguments:
- **length** (_Float_ = None) : socket 'Length' (id: Length)



#### Returns:
- **Cloud** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### trim()

> method

``` python
trim(start=None, end=None, mode='FACTOR')
```

> Node [Trim Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/trim_curve.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **start** (_Float_ = None) : socket 'Start' (id: Start)
- **end** (_Float_ = None) : socket 'End' (id: End)
- **mode** (_str_ = FACTOR) : parameter 'mode' in ['FACTOR', 'LENGTH']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### trim_factor()

> method

``` python
trim_factor(start=None, end=None)
```

> Node [Trim Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/trim_curve.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACTOR'



#### Arguments:
- **start** (_Float_ = None) : socket 'Start' (id: Start)
- **end** (_Float_ = None) : socket 'End' (id: End)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### trim_length()

> method

``` python
trim_length(start=None, end=None)
```

> Node [Trim Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/trim_curve.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'LENGTH'



#### Arguments:
- **start** (_Float_ = None) : socket 'Start' (id: Start_001)
- **end** (_Float_ = None) : socket 'End' (id: End_001)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>