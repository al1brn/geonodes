# Curve

``` python
Curve(value: geonodes.core.socket_class.Socket = None, name: str = None, tip: str = '', panel: str = '', **props)
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
- **tip** (_str_ = ) : Property description
- **panel** (_str_ = ) : Panel name
- **props** (_dict_) : input properties

### Inherited

[\_\_add__](boolean.md#__add__) :black_small_square: [bake](geometry.md#bake) :black_small_square: [bounding_box](core-gener-geome-geometry.md#bounding_box) :black_small_square: ['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socke-socket.md#check_in_list) :black_small_square: [\_class_test](core-socke-socket.md#_class_test) :black_small_square: [Constant](core-socke-socket.md#constant) :black_small_square: [convex_hull](core-gener-geome-geometry.md#convex_hull) :black_small_square: [\_create_input_socket](core-gener-geome-geometry.md#_create_input_socket) :black_small_square: [curve](core-gener-geome-geometry.md#curve) :black_small_square: [default_value](core-socke-socket.md#default_value) :black_small_square: [\_domain_to_geometry](core-socke-socket.md#_domain_to_geometry) :black_small_square: [Empty](core-socke-socket.md#empty) :black_small_square: [enable_output](core-gener-geome-geometry.md#enable_output) :black_small_square: [\_\_enter__](core-socke-socket.md#__enter__) :black_small_square: [\_\_exit__](core-socke-socket.md#__exit__) :black_small_square: [\_geo](cloudpoint.md#_geo) :black_small_square: [\_geo_type](geom.md#_geo_type) :black_small_square: [\_\_getattr__](core-socke-socket.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socke-socket.md#_get_bsocket_from_input) :black_small_square: [\_\_getitem__](geom.md#__getitem__) :black_small_square: [get_selection](geom.md#get_selection) :black_small_square: [grease_pencil](core-gener-geome-geometry.md#grease_pencil) :black_small_square: [\_\_iadd__](float.md#__iadd__) :black_small_square: [id](core-gener-geome-geometry.md#id) :black_small_square: [index_of_nearest](core-gener-geome-geometry.md#index_of_nearest) :black_small_square: [IndexSwitch](core-socke-socket.md#indexswitch) :black_small_square: [index_switch](core-socke-socket.md#index_switch) :black_small_square: [\_\_init__](colorramp.md#__init__) :black_small_square: [Input](core-socke-socket.md#input) :black_small_square: [instance_on_points](core-gener-geome-geometry.md#instance_on_points) :black_small_square: [instances](core-gener-geome-geometry.md#instances) :black_small_square: [\_interface_socket](core-socke-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socke-socket.md#_is_empty) :black_small_square: [is_grid](core-socke-socket.md#is_grid) :black_small_square: [Join](core-gener-geome-geometry.md#join) :black_small_square: [join](core-gener-geome-geometry.md#join) :black_small_square: [\_jump](core-socke-socket.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](core-socke-socket.md#_lc) :black_small_square: [\_lcop](core-socke-socket.md#_lcop) :black_small_square: [link_inputs](core-socke-socket.md#link_inputs) :black_small_square: [material](core-gener-geome-geometry.md#material) :black_small_square: [material_index](core-gener-geome-geometry.md#material_index) :black_small_square: [MenuSwitch](core-socke-socket.md#menuswitch) :black_small_square: [menu_switch](core-socke-socket.md#menu_switch) :black_small_square: [merge](core-gener-geome-geometry.md#merge) :black_small_square: [merge_by_distance](core-gener-geome-geometry.md#merge_by_distance) :black_small_square: [mesh](core-gener-geome-geometry.md#mesh) :black_small_square: [\_name](core-socke-socket.md#_name) :black_small_square: [name](core-gener-geome-geometry.md#name) :black_small_square: [Named](core-socke-socket.md#named) :black_small_square: [NewInput](core-socke-socket.md#newinput) :black_small_square: [node](core-socke-socket.md#node) :black_small_square: [node_color](core-socke-socket.md#node_color) :black_small_square: [node_label](core-socke-socket.md#node_label) :black_small_square: [offset](core-gener-geome-geometry.md#offset) :black_small_square: [out](core-socke-socket.md#out) :black_small_square: [out_OLD](geometry.md#out_old) :black_small_square: [\_panel_name](core-socke-socket.md#_panel_name) :black_small_square: [pin_gizmo](core-socke-socket.md#pin_gizmo) :black_small_square: [point_cloud](core-gener-geome-geometry.md#point_cloud) :black_small_square: [\_pop](core-socke-socket.md#_pop) :black_small_square: [position](core-gener-geome-geometry.md#position) :black_small_square: [proximity](core-gener-geome-geometry.md#proximity) :black_small_square: [proximity_edges](core-gener-geome-geometry.md#proximity_edges) :black_small_square: [proximity_faces](core-gener-geome-geometry.md#proximity_faces) :black_small_square: [proximity_points](core-gener-geome-geometry.md#proximity_points) :black_small_square: [\_push](core-socke-socket.md#_push) :black_small_square: [raycast](core-gener-geome-geometry.md#raycast) :black_small_square: [realize](core-gener-geome-geometry.md#realize) :black_small_square: [remove_named_attribute](core-gener-geome-geometry.md#remove_named_attribute) :black_small_square: [repeat](core-socke-socket.md#repeat) :black_small_square: [replace_material](core-gener-geome-geometry.md#replace_material) :black_small_square: ['_selection' not found]() :black_small_square: [separate_components](core-gener-geome-geometry.md#separate_components) :black_small_square: [set_id](core-gener-geome-geometry.md#set_id) :black_small_square: [set_material](core-gener-geome-geometry.md#set_material) :black_small_square: [set_material_index](core-gener-geome-geometry.md#set_material_index) :black_small_square: [set_name](core-gener-geome-geometry.md#set_name) :black_small_square: [set_position](core-gener-geome-geometry.md#set_position) :black_small_square: [simulation](core-socke-socket.md#simulation) :black_small_square: [\_socket_type](core-socke-socket.md#_socket_type) :black_small_square: [\_\_str__](core-socke-socket.md#__str__) :black_small_square: [Switch](core-socke-socket.md#switch) :black_small_square: [switch](core-socke-socket.md#switch) :black_small_square: [switch_false](core-socke-socket.md#switch_false) :black_small_square: [to_instance](core-gener-geome-geometry.md#to_instance) :black_small_square: [transform](core-gener-geome-geometry.md#transform) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square: [viewer](core-gener-geome-geometry.md#viewer) :black_small_square: [volume](core-gener-geome-geometry.md#volume) :black_small_square:

## Content

- **A** : [Arc](curve.md#arc) :black_small_square: [ArcPoints](curve.md#arcpoints) :black_small_square: [ArcRadius](curve.md#arcradius)
- **B** : [BezierSegment](curve.md#beziersegment) :black_small_square: [BeziersegmentOffset](curve.md#beziersegmentoffset) :black_small_square: [BeziersegmentPosition](curve.md#beziersegmentposition)
- **C** : [Circle](curve.md#circle) :black_small_square: [CirclePoints](curve.md#circlepoints) :black_small_square: [CircleRadius](curve.md#circleradius) :black_small_square: [curve_of_point](curve.md#curve_of_point)
- **D** : [deform_on_surface](curve.md#deform_on_surface) :black_small_square: [domain_size](curve.md#domain_size)
- **E** : [endpoint_selection](curve.md#endpoint_selection)
- **F** : [fill](curve.md#fill) :black_small_square: [fillet](curve.md#fillet)
- **H** : [handle_positions](curve.md#handle_positions) :black_small_square: [handle_type](curve.md#handle_type) :black_small_square: [handle_type_selection](curve.md#handle_type_selection)
- **I** : [Interpolate](curve.md#interpolate) :black_small_square: [interpolate](curve.md#interpolate) :black_small_square: [is_cyclic](curve.md#is_cyclic)
- **L** : [left_handle_offset](curve.md#left_handle_offset) :black_small_square: [left_handle_position](curve.md#left_handle_position) :black_small_square: [left_handle_type](curve.md#left_handle_type) :black_small_square: [length](curve.md#length) :black_small_square: [Line](curve.md#line) :black_small_square: [LineDirection](curve.md#linedirection) :black_small_square: [LinePoints](curve.md#linepoints)
- **M** : [material_selection](curve.md#material_selection)
- **N** : [normal](curve.md#normal)
- **O** : [offset_point_in_curve](curve.md#offset_point_in_curve)
- **P** : [points](curve.md#points) :black_small_square: [points_of_curve](curve.md#points_of_curve)
- **Q** : [QuadraticBezier](curve.md#quadraticbezier) :black_small_square: [Quadrilateral](curve.md#quadrilateral) :black_small_square: [QuadrilateralKite](curve.md#quadrilateralkite) :black_small_square: [QuadrilateralParallelogram](curve.md#quadrilateralparallelogram) :black_small_square: [QuadrilateralPoints](curve.md#quadrilateralpoints) :black_small_square: [QuadrilateralRectangle](curve.md#quadrilateralrectangle) :black_small_square: [QuadrilateralTrapezoid](curve.md#quadrilateraltrapezoid)
- **R** : [radius](curve.md#radius) :black_small_square: [resample](curve.md#resample) :black_small_square: [resolution](curve.md#resolution) :black_small_square: [reverse](curve.md#reverse) :black_small_square: [right_handle_offset](curve.md#right_handle_offset) :black_small_square: [right_handle_position](curve.md#right_handle_position) :black_small_square: [right_handle_type](curve.md#right_handle_type)
- **S** : [sample](curve.md#sample) :black_small_square: [sample_factor](curve.md#sample_factor) :black_small_square: [sample_length](curve.md#sample_length) :black_small_square: [set_both_handle_type](curve.md#set_both_handle_type) :black_small_square: [set_handle_positions](curve.md#set_handle_positions) :black_small_square: [set_handle_type](curve.md#set_handle_type) :black_small_square: [set_left_handle_positions](curve.md#set_left_handle_positions) :black_small_square: [set_left_handle_type](curve.md#set_left_handle_type) :black_small_square: [set_normal](curve.md#set_normal) :black_small_square: [set_radius](curve.md#set_radius) :black_small_square: [set_right_handle_positions](curve.md#set_right_handle_positions) :black_small_square: [set_right_handle_type](curve.md#set_right_handle_type) :black_small_square: [set_spline_cyclic](curve.md#set_spline_cyclic) :black_small_square: [set_spline_resolution](curve.md#set_spline_resolution) :black_small_square: [set_spline_type](curve.md#set_spline_type) :black_small_square: [set_tilt](curve.md#set_tilt) :black_small_square: [Spiral](curve.md#spiral) :black_small_square: [spline_length](curve.md#spline_length) :black_small_square: [spline_parameter](curve.md#spline_parameter) :black_small_square: [splines](curve.md#splines) :black_small_square: [Star](curve.md#star) :black_small_square: [subdivide](curve.md#subdivide)
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
Arc(resolution: 'Integer' = None, radius: 'Float' = None, start_angle: 'Float' = None, sweep_angle: 'Float' = None, connect_center: 'Boolean' = None, invert_arc: 'Boolean' = None, mode: "Literal['POINTS', 'RADIUS']" = 'RADIUS')
```

> Node [Arc](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/arc.html)

#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (id: Resolution)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)
- **start_angle** (_Float_ = None) : socket 'Start Angle' (id: Start Angle)
- **sweep_angle** (_Float_ = None) : socket 'Sweep Angle' (id: Sweep Angle)
- **connect_center** (_Boolean_ = None) : socket 'Connect Center' (id: Connect Center)
- **invert_arc** (_Boolean_ = None) : socket 'Invert Arc' (id: Invert Arc)
- **mode** (_Literal['POINTS', 'RADIUS']_ = RADIUS) : parameter 'mode' in ['POINTS', 'RADIUS']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### ArcPoints()

> classmethod

``` python
ArcPoints(resolution: 'Integer' = None, start: 'Vector' = None, middle: 'Vector' = None, end: 'Vector' = None, offset_angle: 'Float' = None, connect_center: 'Boolean' = None, invert_arc: 'Boolean' = None)
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
ArcRadius(resolution: 'Integer' = None, radius: 'Float' = None, start_angle: 'Float' = None, sweep_angle: 'Float' = None, connect_center: 'Boolean' = None, invert_arc: 'Boolean' = None)
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
BezierSegment(resolution: 'Integer' = None, start: 'Vector' = None, start_handle: 'Vector' = None, end_handle: 'Vector' = None, end: 'Vector' = None, mode: "Literal['POSITION', 'OFFSET']" = 'POSITION')
```

> Node ERROR: Node 'Bézier Segment' not found

#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (id: Resolution)
- **start** (_Vector_ = None) : socket 'Start' (id: Start)
- **start_handle** (_Vector_ = None) : socket 'Start Handle' (id: Start Handle)
- **end_handle** (_Vector_ = None) : socket 'End Handle' (id: End Handle)
- **end** (_Vector_ = None) : socket 'End' (id: End)
- **mode** (_Literal['POSITION', 'OFFSET']_ = POSITION) : parameter 'mode' in ['POSITION', 'OFFSET']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### BeziersegmentOffset()

> classmethod

``` python
BeziersegmentOffset(resolution: 'Integer' = None, start: 'Vector' = None, start_handle: 'Vector' = None, end_handle: 'Vector' = None, end: 'Vector' = None)
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
BeziersegmentPosition(resolution: 'Integer' = None, start: 'Vector' = None, start_handle: 'Vector' = None, end_handle: 'Vector' = None, end: 'Vector' = None)
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
Circle(resolution: 'Integer' = None, radius: 'Float' = None, mode: "Literal['POINTS', 'RADIUS']" = 'RADIUS')
```

> Node [Curve Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_circle.html)

#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (id: Resolution)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)
- **mode** (_Literal['POINTS', 'RADIUS']_ = RADIUS) : parameter 'mode' in ['POINTS', 'RADIUS']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### CirclePoints()

> classmethod

``` python
CirclePoints(resolution: 'Integer' = None, point_1: 'Vector' = None, point_2: 'Vector' = None, point_3: 'Vector' = None)
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
CircleRadius(resolution: 'Integer' = None, radius: 'Float' = None)
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
curve_of_point(point_index: 'Integer' = None)
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
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### endpoint_selection()

> classmethod

``` python
endpoint_selection(start_size: 'Integer' = None, end_size: 'Integer' = None)
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
fill(group_id: 'Integer' = None, mode: "Literal['Triangles', 'N-gons']" = None)
```

> Node [Fill Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fill_curve.html)

#### Information:
- **Socket** : self



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)
- **mode** (_Literal['Triangles', 'N-gons']_ = None) : ('Triangles', 'N-gons')



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### fillet()

> method

``` python
fillet(radius: 'Float' = None, limit_radius: 'Boolean' = None, mode: "Literal['Bézier', 'Poly']" = None, count: 'Integer' = None)
```

> Node [Fillet Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fillet_curve.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)
- **limit_radius** (_Boolean_ = None) : socket 'Limit Radius' (id: Limit Radius)
- **mode** (_Literal['Bézier', 'Poly']_ = None) : ('Bézier', 'Poly')
- **count** (_Integer_ = None) : socket 'Count' (id: Count)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### handle_positions()

> classmethod

``` python
handle_positions(relative: 'Boolean' = None)
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
handle_type_selection(handle_type: "Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN']" = 'AUTO', mode={'RIGHT', 'LEFT'})
```

> Node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/handle_type_selection.html)

#### Arguments:
- **handle_type** (_Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN']_ = AUTO) : parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']
- **mode** (_set_ = {'RIGHT', 'LEFT'}) : parameter 'mode'



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### Interpolate()

> classmethod

``` python
Interpolate(guide_curves: 'Curve' = None, guide_up: 'Vector' = None, guide_group_id: 'Integer' = None, points: 'Cloud' = None, point_up: 'Vector' = None, point_group_id: 'Integer' = None, max_neighbors: 'Integer' = None)
```

> Node [Interpolate Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/interpolate_curves.html)

#### Arguments:
- **guide_curves** (_Curve_ = None) : socket 'Guide Curves' (id: Guide Curves)
- **guide_up** (_Vector_ = None) : socket 'Guide Up' (id: Guide Up)
- **guide_group_id** (_Integer_ = None) : socket 'Guide Group ID' (id: Guide Group ID)
- **points** (_Cloud_ = None) : socket 'Points' (id: Points)
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
interpolate(guide_up: 'Vector' = None, guide_group_id: 'Integer' = None, points: 'Cloud' = None, point_up: 'Vector' = None, point_group_id: 'Integer' = None, max_neighbors: 'Integer' = None)
```

> Node [Interpolate Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/interpolate_curves.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **guide_up** (_Vector_ = None) : socket 'Guide Up' (id: Guide Up)
- **guide_group_id** (_Integer_ = None) : socket 'Guide Group ID' (id: Guide Group ID)
- **points** (_Cloud_ = None) : socket 'Points' (id: Points)
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
Line(start: 'Vector' = None, end: 'Vector' = None, mode: "Literal['POINTS', 'DIRECTION']" = 'POINTS')
```

> Node [Curve Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_line.html)

#### Arguments:
- **start** (_Vector_ = None) : socket 'Start' (id: Start)
- **end** (_Vector_ = None) : socket 'End' (id: End)
- **mode** (_Literal['POINTS', 'DIRECTION']_ = POINTS) : parameter 'mode' in ['POINTS', 'DIRECTION']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### LineDirection()

> classmethod

``` python
LineDirection(start: 'Vector' = None, direction: 'Vector' = None, length: 'Float' = None)
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
LinePoints(start: 'Vector' = None, end: 'Vector' = None)
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
material_selection(material: 'Material' = None)
```

> Node [Material Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/material/material_selection.html)

#### Arguments:
- **material** (_Material_ = None) : socket 'Material' (id: Material)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### offset_point_in_curve()

> classmethod

``` python
offset_point_in_curve(point_index: 'Integer' = None, offset: 'Integer' = None)
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
points_of_curve(curve_index: 'Integer' = None, weights: 'Float' = None, sort_index: 'Integer' = None)
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
QuadraticBezier(resolution: 'Integer' = None, start: 'Vector' = None, middle: 'Vector' = None, end: 'Vector' = None)
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
Quadrilateral(width: 'Float' = None, height: 'Float' = None, mode: "Literal['RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS']" = 'RECTANGLE')
```

> Node [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html)

#### Arguments:
- **width** (_Float_ = None) : socket 'Width' (id: Width)
- **height** (_Float_ = None) : socket 'Height' (id: Height)
- **mode** (_Literal['RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS']_ = RECTANGLE) : parameter 'mode' in ['RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### QuadrilateralKite()

> classmethod

``` python
QuadrilateralKite(width: 'Float' = None, bottom_height: 'Float' = None, top_height: 'Float' = None)
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
QuadrilateralParallelogram(width: 'Float' = None, height: 'Float' = None, offset: 'Float' = None)
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
QuadrilateralPoints(point_1: 'Vector' = None, point_2: 'Vector' = None, point_3: 'Vector' = None, point_4: 'Vector' = None)
```

> Node [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html)

#### Information:
- **Parameter** : 'POINTS'



#### Arguments:
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
QuadrilateralRectangle(width: 'Float' = None, height: 'Float' = None)
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
QuadrilateralTrapezoid(height: 'Float' = None, bottom_width: 'Float' = None, top_width: 'Float' = None, offset: 'Float' = None)
```

> Node [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html)

#### Information:
- **Parameter** : 'TRAPEZOID'



#### Arguments:
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
resample(mode: "Literal['Evaluated', 'Count', 'Length']" = None, count: 'Integer' = None, length: 'Float' = None, keep_last_segment=True)
```

> Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/resample_curve.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **mode** (_Literal['Evaluated', 'Count', 'Length']_ = None) : ('Evaluated', 'Count', 'Length')
- **count** (_Integer_ = None) : socket 'Count' (id: Count)
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
sample(value: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix' = None, curve_index: 'Integer' = None, factor: 'Float' = None, mode: "Literal['FACTOR', 'LENGTH']" = 'FACTOR', use_all_curves=False)
```

> Node [Sample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample/sample_curve.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'value' type



#### Arguments:
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix_ = None) : socket 'Value' (id: Value)
- **curve_index** (_Integer_ = None) : socket 'Curve Index' (id: Curve Index)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)
- **mode** (_Literal['FACTOR', 'LENGTH']_ = FACTOR) : parameter 'mode' in ['FACTOR', 'LENGTH']
- **use_all_curves** (_bool_ = False) : parameter 'use_all_curves'



#### Returns:
- **Float** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### sample_factor()

> method

``` python
sample_factor(value: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix' = None, curve_index: 'Integer' = None, factor: 'Float' = None, use_all_curves=False)
```

> Node [Sample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample/sample_curve.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'value' type
- **Parameter** : 'FACTOR'



#### Arguments:
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix_ = None) : socket 'Value' (id: Value)
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
sample_length(value: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix' = None, length: 'Float' = None, curve_index: 'Integer' = None, use_all_curves=False)
```

> Node [Sample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample/sample_curve.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'value' type
- **Parameter** : 'LENGTH'



#### Arguments:
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix_ = None) : socket 'Value' (id: Value)
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
set_both_handle_type(handle_type: "Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN']" = 'AUTO')
```

> Node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : {'RIGHT', 'LEFT'}



#### Arguments:
- **handle_type** (_Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN']_ = AUTO) : parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_handle_positions()

> method

``` python
set_handle_positions(position: 'Vector' = None, offset: 'Vector' = None, mode: "Literal['LEFT', 'RIGHT']" = 'LEFT')
```

> Node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_positions.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **offset** (_Vector_ = None) : socket 'Offset' (id: Offset)
- **mode** (_Literal['LEFT', 'RIGHT']_ = LEFT) : parameter 'mode' in ['LEFT', 'RIGHT']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_handle_type()

> method

``` python
set_handle_type(handle_type: "Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN']" = 'AUTO', mode={'RIGHT', 'LEFT'})
```

> Node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **handle_type** (_Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN']_ = AUTO) : parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']
- **mode** (_set_ = {'RIGHT', 'LEFT'}) : parameter 'mode'



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_left_handle_positions()

> method

``` python
set_left_handle_positions(position: 'Vector' = None, offset: 'Vector' = None)
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
set_left_handle_type(handle_type: "Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN']" = 'AUTO')
```

> Node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : {'LEFT'}



#### Arguments:
- **handle_type** (_Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN']_ = AUTO) : parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_normal()

> method

``` python
set_normal(mode: "Literal['Minimum Twist', 'Z Up', 'Free']" = None, normal: 'Vector' = None)
```

> Node [Set Curve Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_curve_normal.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **mode** (_Literal['Minimum Twist', 'Z Up', 'Free']_ = None) : ('Minimum Twist', 'Z Up', 'Free')
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_radius()

> method

``` python
set_radius(radius: 'Float' = None)
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
set_right_handle_positions(position: 'Vector' = None, offset: 'Vector' = None)
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
set_right_handle_type(handle_type: "Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN']" = 'AUTO')
```

> Node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : {'RIGHT'}



#### Arguments:
- **handle_type** (_Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN']_ = AUTO) : parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_spline_cyclic()

> method

``` python
set_spline_cyclic(cyclic: 'Boolean' = None)
```

> Node [Set Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_spline_cyclic.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **cyclic** (_Boolean_ = None) : socket 'Cyclic' (id: Cyclic)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_spline_resolution()

> method

``` python
set_spline_resolution(resolution: 'Integer' = None)
```

> Node [Set Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_spline_resolution.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (id: Resolution)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_spline_type()

> method

``` python
set_spline_type(spline_type: "Literal['CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS']" = 'POLY')
```

> Node [Set Spline Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_spline_type.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **spline_type** (_Literal['CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS']_ = POLY) : parameter 'spline_type' in ['CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### set_tilt()

> method

``` python
set_tilt(tilt: 'Float' = None)
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
Spiral(resolution: 'Integer' = None, rotations: 'Float' = None, start_radius: 'Float' = None, end_radius: 'Float' = None, height: 'Float' = None, reverse: 'Boolean' = None)
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
Star(points: 'Integer' = None, inner_radius: 'Float' = None, outer_radius: 'Float' = None, twist: 'Float' = None)
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
subdivide(cuts: 'Integer' = None)
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
to_grease_pencil(instances_as_layers: 'Boolean' = None)
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
to_mesh(profile_curve: 'Curve' = None, scale: 'Float' = None, fill_caps: 'Boolean' = None)
```

> Node [Curve to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_mesh.html)

#### Information:
- **Socket** : self



#### Arguments:
- **profile_curve** (_Curve_ = None) : socket 'Profile Curve' (id: Profile Curve)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **fill_caps** (_Boolean_ = None) : socket 'Fill Caps' (id: Fill Caps)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### to_points()

> method

``` python
to_points(count: 'Integer' = None, mode: "Literal['EVALUATED', 'COUNT', 'LENGTH']" = 'COUNT')
```

> Node [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_points.html)

#### Information:
- **Socket** : self



#### Arguments:
- **count** (_Integer_ = None) : socket 'Count' (id: Count)
- **mode** (_Literal['EVALUATED', 'COUNT', 'LENGTH']_ = COUNT) : parameter 'mode' in ['EVALUATED', 'COUNT', 'LENGTH']



#### Returns:
- **Cloud** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### to_points_count()

> method

``` python
to_points_count(count: 'Integer' = None)
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
to_points_length(length: 'Float' = None)
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
trim(start: 'Float' = None, end: 'Float' = None, mode: "Literal['FACTOR', 'LENGTH']" = 'FACTOR')
```

> Node [Trim Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/trim_curve.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **start** (_Float_ = None) : socket 'Start' (id: Start)
- **end** (_Float_ = None) : socket 'End' (id: End)
- **mode** (_Literal['FACTOR', 'LENGTH']_ = FACTOR) : parameter 'mode' in ['FACTOR', 'LENGTH']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Curve](curve.md#curve) :black_small_square: [Content](curve.md#content) :black_small_square: [Methods](curve.md#methods)</sub>

----------
### trim_factor()

> method

``` python
trim_factor(start: 'Float' = None, end: 'Float' = None)
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
trim_length(start: 'Float' = None, end: 'Float' = None)
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