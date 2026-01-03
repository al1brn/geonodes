# Geometry

``` python
Geometry(value: geonodes.core.socket_class.Socket = None, name: str = None, tip: str = '', panel: str = '', **props)
```

Socket of type 'GEOMETRY'.

If value is None, a Group Input socket of type Geometry is created.
When a Group Input socket is created, default name 'Geometry' is used if name argument is None.

``` python
geometry = Geometry() # Default group input geometry
geometry = Geometry(name="Mesh") # Input group geometry
```

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = ) : Property description
- **panel** (_str_ = ) : Panel name
- **props** (_dict_) : input properties

### Inherited

['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socke-socket.md#check_in_list) :black_small_square: [\_class_test](core-socke-socket.md#_class_test) :black_small_square: [Constant](core-socke-socket.md#constant) :black_small_square: [default_value](core-socke-socket.md#default_value) :black_small_square: [\_domain_to_geometry](core-socke-socket.md#_domain_to_geometry) :black_small_square: [Empty](core-socke-socket.md#empty) :black_small_square: [\_\_enter__](core-socke-socket.md#__enter__) :black_small_square: [\_\_exit__](core-socke-socket.md#__exit__) :black_small_square: [\_geo](cloudpoint.md#_geo) :black_small_square: [\_geo_type](geom.md#_geo_type) :black_small_square: [\_\_getattr__](core-socke-socket.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socke-socket.md#_get_bsocket_from_input) :black_small_square: [\_\_getitem__](geom.md#__getitem__) :black_small_square: [get_selection](geom.md#get_selection) :black_small_square: [IndexSwitch](core-socke-socket.md#indexswitch) :black_small_square: [index_switch](core-socke-socket.md#index_switch) :black_small_square: [Input](core-socke-socket.md#input) :black_small_square: [\_interface_socket](core-socke-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socke-socket.md#_is_empty) :black_small_square: [is_grid](core-socke-socket.md#is_grid) :black_small_square: [\_jump](core-socke-socket.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](core-socke-socket.md#_lc) :black_small_square: [\_lcop](core-socke-socket.md#_lcop) :black_small_square: [link_inputs](core-socke-socket.md#link_inputs) :black_small_square: [MenuSwitch](core-socke-socket.md#menuswitch) :black_small_square: [menu_switch](core-socke-socket.md#menu_switch) :black_small_square: [\_name](core-socke-socket.md#_name) :black_small_square: [Named](core-socke-socket.md#named) :black_small_square: [NewInput](core-socke-socket.md#newinput) :black_small_square: [node](core-socke-socket.md#node) :black_small_square: [node_color](core-socke-socket.md#node_color) :black_small_square: [node_label](core-socke-socket.md#node_label) :black_small_square: [out](core-socke-socket.md#out) :black_small_square: [\_panel_name](core-socke-socket.md#_panel_name) :black_small_square: [pin_gizmo](core-socke-socket.md#pin_gizmo) :black_small_square: [\_pop](core-socke-socket.md#_pop) :black_small_square: [\_push](core-socke-socket.md#_push) :black_small_square: [repeat](core-socke-socket.md#repeat) :black_small_square: [\_reset](core-socke-socket.md#_reset) :black_small_square: ['_selection' not found]() :black_small_square: [simulation](core-socke-socket.md#simulation) :black_small_square: [\_socket_type](core-socke-socket.md#_socket_type) :black_small_square: [\_\_str__](core-socke-socket.md#__str__) :black_small_square: [Switch](core-socke-socket.md#switch) :black_small_square: [switch](core-socke-socket.md#switch) :black_small_square: [switch_false](core-socke-socket.md#switch_false) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square:

## Content

- **B** : [bake](geometry.md#bake) :black_small_square: [bounding_box](geometry.md#bounding_box)
- **C** : [convex_hull](geometry.md#convex_hull) :black_small_square: [\_create_input_socket](geometry.md#_create_input_socket) :black_small_square: [curve](geometry.md#curve)
- **E** : [enable_output](geometry.md#enable_output)
- **G** : [grease_pencil](geometry.md#grease_pencil)
- **I** : [id](geometry.md#id) :black_small_square: [index_of_nearest](geometry.md#index_of_nearest) :black_small_square: [\_\_init__](geometry.md#__init__) :black_small_square: [instance_on_points](geometry.md#instance_on_points) :black_small_square: [instances](geometry.md#instances)
- **J** : [Join](geometry.md#join) :black_small_square: [join](geometry.md#join)
- **M** : [material](geometry.md#material) :black_small_square: [material_index](geometry.md#material_index) :black_small_square: [merge](geometry.md#merge) :black_small_square: [merge_by_distance](geometry.md#merge_by_distance) :black_small_square: [mesh](geometry.md#mesh)
- **N** : [name](geometry.md#name)
- **O** : [offset](geometry.md#offset) :black_small_square: [out_OLD](geometry.md#out_old)
- **P** : [point_cloud](geometry.md#point_cloud) :black_small_square: [position](geometry.md#position) :black_small_square: [proximity](geometry.md#proximity) :black_small_square: [proximity_edges](geometry.md#proximity_edges) :black_small_square: [proximity_faces](geometry.md#proximity_faces) :black_small_square: [proximity_points](geometry.md#proximity_points)
- **R** : [raycast](geometry.md#raycast) :black_small_square: [realize](geometry.md#realize) :black_small_square: [remove_named_attribute](geometry.md#remove_named_attribute) :black_small_square: [replace_material](geometry.md#replace_material)
- **S** : [separate_components](geometry.md#separate_components) :black_small_square: [set_id](geometry.md#set_id) :black_small_square: [set_material](geometry.md#set_material) :black_small_square: [set_material_index](geometry.md#set_material_index) :black_small_square: [set_name](geometry.md#set_name) :black_small_square: [set_position](geometry.md#set_position)
- **T** : [to_instance](geometry.md#to_instance) :black_small_square: [transform](geometry.md#transform)
- **V** : [viewer](geometry.md#viewer) :black_small_square: [volume](geometry.md#volume)

## Properties



### curve

> _type_: **curve**
>

> Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### grease_pencil

> _type_: **grease_pencil**
>

> Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### id

> _type_: **?**
>

Property get node <Node Set ID>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### instances

> _type_: **instances**
>

> Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### material

> _type_: **?**
>

Write only property for node <Node Set Material>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### material_index

> _type_: **?**
>

Property get node <Node Set Material Index>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### mesh

> _type_: **mesh**
>

> Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### name

> _type_: **?**
>

Write only property for node <Node Set Geometry Name>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### offset

> _type_: **?**
>

Write only property for node <Node Set Position>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### point_cloud

> _type_: **point_cloud**
>

> Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### position

> _type_: **?**
>

Property get node <Node Set Position>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### volume

> _type_: **volume**
>

> Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

## Methods



----------
### bake()

> method

``` python
bake(**kwargs)
```

Node [Bake](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/bake.html)



#### Arguments:
- **kwargs**



#### Returns:
- **Geometry** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### bounding_box()

> method

``` python
bounding_box(use_radius: 'Boolean' = None)
```

> Node [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/bounding_box.html)

#### Information:
- **Socket** : self



#### Arguments:
- **use_radius** (_Boolean_ = None) : socket 'Use Radius' (id: Use Radius)



#### Returns:
- **Mesh** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### convex_hull()

> method

``` python
convex_hull()
```

> Node [Convex Hull](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/convex_hull.html)

#### Information:
- **Socket** : self



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(name: 'str' = 'Geometry', tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False)
```

> Geometry Input

New [Geometry](geometry.md#geometry) input with subtype 'NONE'.

Aguments
--------
- name  (str = 'Geometry') : Input socket name
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier

#### Arguments:
- **name** (_str_ = Geometry)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### enable_output()

> method

``` python
enable_output(enable: 'Boolean' = None)
```

> Node [Enable Output](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/output/enable_output.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Parameter** : 'GEOMETRY'



#### Arguments:
- **enable** (_Boolean_ = None) : socket 'Enable' (id: Enable)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### index_of_nearest()

> classmethod

``` python
index_of_nearest(position: 'Vector' = None, group_id: 'Integer' = None)
```

> Node ERROR: Node 'Index of Nearest' not found

#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)



#### Returns:
- **Integer** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(value: geonodes.core.socket_class.Socket = None, name: str = None, tip: str = '', panel: str = '', **props)
```

Socket of type 'GEOMETRY'.

If value is None, a Group Input socket of type Geometry is created.
When a Group Input socket is created, default name 'Geometry' is used if name argument is None.

``` python
geometry = Geometry() # Default group input geometry
geometry = Geometry(name="Mesh") # Input group geometry
```

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = ) : Property description
- **panel** (_str_ = ) : Panel name
- **props** (_dict_) : input properties

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### instance_on_points()

> method

``` python
instance_on_points(instance: 'Instances' = None, pick_instance: 'Boolean' = None, instance_index: 'Integer' = None, rotation: 'Rotation' = None, scale: 'Vector' = None)
```

> Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **instance** (_Instances_ = None) : socket 'Instance' (id: Instance)
- **pick_instance** (_Boolean_ = None) : socket 'Pick Instance' (id: Pick Instance)
- **instance_index** (_Integer_ = None) : socket 'Instance Index' (id: Instance Index)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (id: Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (id: Scale)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### Join()

> classmethod

``` python
Join(*geometry: 'Geometry')
```

> Node [Join Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html)

#### Arguments:
- **geometry** (_Geometry_) : socket 'Geometry' (id: Geometry)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### join()

> method

``` python
join(*geometry: 'Geometry')
```

> Node [Join Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Arguments:
- **geometry** (_Geometry_) : socket 'Geometry' (id: Geometry)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### merge()

> method

``` python
merge(mode: "Literal['All', 'Connected']" = None, distance: 'Float' = None)
```

> Node [Merge by Distance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/merge_by_distance.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **mode** (_Literal['All', 'Connected']_ = None) : ('All', 'Connected')
- **distance** (_Float_ = None) : socket 'Distance' (id: Distance)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### merge_by_distance()

> method

``` python
merge_by_distance(mode: "Literal['All', 'Connected']" = None, distance: 'Float' = None)
```

> Node [Merge by Distance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/merge_by_distance.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **mode** (_Literal['All', 'Connected']_ = None) : ('All', 'Connected')
- **distance** (_Float_ = None) : socket 'Distance' (id: Distance)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### out_OLD()

> method

``` python
out_OLD(name: str = None, panel: str = '', **props)
```

Plug the value to the Group Output Node.

``` python
with GeoNodes("Plug to group output"):
    # Create a cube
    geo = Mesh.Cube()
    # To Group Output geometry as socket named "Cube"
    geo.out("Cube")
```

The "Do nothing" modifier is simply ``` Geometry().out() ```

#### Arguments:
- **name** (_str_ = None) : socket name
- **panel** (_str_ = )
- **props**



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### proximity()

> method

``` python
proximity(group_id: 'Integer' = None, sample_position: 'Vector' = None, sample_group_id: 'Integer' = None, target_element: "Literal['POINTS', 'EDGES', 'FACES']" = 'FACES')
```

> Node [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/geometry_proximity.html)

#### Information:
- **Socket** : self



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (id: Source Position)
- **sample_group_id** (_Integer_ = None) : socket 'Sample Group ID' (id: Sample Group ID)
- **target_element** (_Literal['POINTS', 'EDGES', 'FACES']_ = FACES) : parameter 'target_element' in ['POINTS', 'EDGES', 'FACES']



#### Returns:
- **Vector** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### proximity_edges()

> method

``` python
proximity_edges(group_id: 'Integer' = None, sample_position: 'Vector' = None, sample_group_id: 'Integer' = None)
```

> Node [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/geometry_proximity.html)

#### Information:
- **Socket** : self
- **Parameter** : 'EDGES'



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (id: Source Position)
- **sample_group_id** (_Integer_ = None) : socket 'Sample Group ID' (id: Sample Group ID)



#### Returns:
- **Vector** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### proximity_faces()

> method

``` python
proximity_faces(group_id: 'Integer' = None, sample_position: 'Vector' = None, sample_group_id: 'Integer' = None)
```

> Node [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/geometry_proximity.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FACES'



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (id: Source Position)
- **sample_group_id** (_Integer_ = None) : socket 'Sample Group ID' (id: Sample Group ID)



#### Returns:
- **Vector** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### proximity_points()

> method

``` python
proximity_points(group_id: 'Integer' = None, sample_position: 'Vector' = None, sample_group_id: 'Integer' = None)
```

> Node [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/geometry_proximity.html)

#### Information:
- **Socket** : self
- **Parameter** : 'POINTS'



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (id: Source Position)
- **sample_group_id** (_Integer_ = None) : socket 'Sample Group ID' (id: Sample Group ID)



#### Returns:
- **Vector** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### raycast()

> method

``` python
raycast(attribute: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix' = None, interpolation: "Literal['Interpolated', 'Nearest']" = None, source_position: 'Vector' = None, ray_direction: 'Vector' = None, ray_length: 'Float' = None)
```

> Node [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/raycast.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'attribute' type



#### Arguments:
- **attribute** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix_ = None) : socket 'Attribute' (id: Attribute)
- **interpolation** (_Literal['Interpolated', 'Nearest']_ = None) : ('Interpolated', 'Nearest')
- **source_position** (_Vector_ = None) : socket 'Source Position' (id: Source Position)
- **ray_direction** (_Vector_ = None) : socket 'Ray Direction' (id: Ray Direction)
- **ray_length** (_Float_ = None) : socket 'Ray Length' (id: Ray Length)



#### Returns:
- **Boolean** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### realize()

> method

``` python
realize(realize_all: 'Boolean' = None, depth: 'Integer' = None)
```

> Node [Realize Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/realize_instances.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **realize_all** (_Boolean_ = None) : socket 'Realize All' (id: Realize All)
- **depth** (_Integer_ = None) : socket 'Depth' (id: Depth)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### remove_named_attribute()

> method

``` python
remove_named_attribute(pattern_mode: "Literal['Exact', 'Wildcard']" = None, name: 'String' = None)
```

> Node [Remove Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **pattern_mode** (_Literal['Exact', 'Wildcard']_ = None) : ('Exact', 'Wildcard')
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### replace_material()

> method

``` python
replace_material(old: 'Material' = None, new: 'Material' = None)
```

> Node [Replace Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/material/replace_material.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **old** (_Material_ = None) : socket 'Old' (id: Old)
- **new** (_Material_ = None) : socket 'New' (id: New)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### separate_components()

> method

``` python
separate_components()
```

> Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

#### Information:
- **Socket** : self



#### Returns:
- **node** (_Mesh_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### set_id()

> method

``` python
set_id(id: 'Integer' = None)
```

> Node [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_id.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **id** (_Integer_ = None) : socket 'ID' (id: ID)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### set_material()

> method

``` python
set_material(material: 'Material' = None)
```

> Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/material/set_material.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **material** (_Material_ = None) : socket 'Material' (id: Material)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### set_material_index()

> method

``` python
set_material_index(material_index: 'Integer' = None)
```

> Node [Set Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/material/set_material_index.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **material_index** (_Integer_ = None) : socket 'Material Index' (id: Material Index)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### set_name()

> method

``` python
set_name(name: 'String' = None)
```

> Node [Set Geometry Name](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_geometry_name.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### set_position()

> method

``` python
set_position(position: 'Vector' = None, offset: 'Vector' = None)
```

> Node [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_position.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **offset** (_Vector_ = None) : socket 'Offset' (id: Offset)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### to_instance()

> method

``` python
to_instance(*geometry: 'Geometry')
```

> Node [Geometry to Instance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html)

#### Arguments:
- **geometry** (_Geometry_) : socket 'Geometry' (id: Geometry)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### transform()

> method

``` python
transform(mode: "Literal['Components', 'Matrix']" = None, translation: 'Vector' = None, rotation: 'Rotation' = None, scale: 'Vector' = None, transform: 'Matrix' = None)
```

> Node [Transform Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/transform_geometry.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **mode** (_Literal['Components', 'Matrix']_ = None) : ('Components', 'Matrix')
- **translation** (_Vector_ = None) : socket 'Translation' (id: Translation)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (id: Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (id: Scale)
- **transform** (_Matrix_ = None) : socket 'Transform' (id: Transform)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### viewer()

> classmethod

``` python
viewer(named_sockets: 'dict' = {}, ui_shortcut=0, **sockets)
```

> Node [Viewer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/output/viewer.html)

#### Information:
- **Parameter** : 'AUTO'



#### Arguments:
- **named_sockets** (_dict_ = {})
- **ui_shortcut** (_int_ = 0) : parameter 'ui_shortcut'
- **sockets**

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>