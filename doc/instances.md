# Instances

``` python
Instances(value: geonodes.core.socket_class.Socket = None, name: str = None, tip: str = '', panel: str = '', **props)
```

> Instances Geometry

> [!NOTE]
> The name of geometry class is plural : **Instances** when the name of the
> domain is singular : [Instance](instance.md#instance). The named of the domain property is [insts](instances.md#insts).

The **Instances** class exposes all methods specific to instances.
Since there is no ambiguity, the word **instances** is omitted in the name of
the methods:

``` python
realized = instances.realize() # Node 'Realize Instances'
```
Nodes requiring a domain parameter, are implemented in the domain [insts](instances.md#insts).

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = ) : Property description
- **panel** (_str_ = ) : Panel name
- **props** (_dict_) : input properties

### Inherited

[\_\_add__](boolean.md#__add__) :black_small_square: [bake](geometry.md#bake) :black_small_square: [bounding_box](core-gener-geome-geometry.md#bounding_box) :black_small_square: ['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socket.md#check_in_list) :black_small_square: [\_class_test](boolean.md#_class_test) :black_small_square: [Constant](core-socket.md#constant) :black_small_square: [convex_hull](core-gener-geome-geometry.md#convex_hull) :black_small_square: [\_create_input_socket](core-gener-geome-geometry.md#_create_input_socket) :black_small_square: [curve](core-gener-geome-geometry.md#curve) :black_small_square: [default_value](core-socket.md#default_value) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [Empty](core-socket.md#empty) :black_small_square: [enable_output](core-gener-geome-geometry.md#enable_output) :black_small_square: [\_\_enter__](layout.md#__enter__) :black_small_square: [\_\_exit__](layout.md#__exit__) :black_small_square: [\_geo](cloudpoint.md#_geo) :black_small_square: [\_geo_type](geom.md#_geo_type) :black_small_square: [\_\_getattr__](g.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socket.md#_get_bsocket_from_input) :black_small_square: [\_\_getitem__](geom.md#__getitem__) :black_small_square: [get_selection](geom.md#get_selection) :black_small_square: [grease_pencil](core-gener-geome-geometry.md#grease_pencil) :black_small_square: [\_\_iadd__](float.md#__iadd__) :black_small_square: [id](core-gener-geome-geometry.md#id) :black_small_square: [index_of_nearest](core-gener-geome-geometry.md#index_of_nearest) :black_small_square: [IndexSwitch](core-socket.md#indexswitch) :black_small_square: [index_switch](core-socket.md#index_switch) :black_small_square: [\_\_init__](colorramp.md#__init__) :black_small_square: [Input](input.md#input) :black_small_square: [instance_on_points](core-gener-geome-geometry.md#instance_on_points) :black_small_square: [instances](core-gener-geome-geometry.md#instances) :black_small_square: [\_interface_socket](core-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socket.md#_is_empty) :black_small_square: [is_grid](core-socket.md#is_grid) :black_small_square: [Join](core-gener-geome-geometry.md#join) :black_small_square: [join](core-gener-geome-geometry.md#join) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](node.md#_lc) :black_small_square: [\_lcop](core-socket.md#_lcop) :black_small_square: [link_inputs](node.md#link_inputs) :black_small_square: [material](core-gener-geome-geometry.md#material) :black_small_square: [material_index](core-gener-geome-geometry.md#material_index) :black_small_square: [MenuSwitch](core-socket.md#menuswitch) :black_small_square: [menu_switch](menu.md#menu_switch) :black_small_square: [merge](core-gener-geome-geometry.md#merge) :black_small_square: [merge_by_distance](core-gener-geome-geometry.md#merge_by_distance) :black_small_square: [mesh](core-gener-geome-geometry.md#mesh) :black_small_square: [\_name](core-socket.md#_name) :black_small_square: [name](core-gener-geome-geometry.md#name) :black_small_square: [Named](boolean.md#named) :black_small_square: [NewInput](core-socket.md#newinput) :black_small_square: [node](core-socket.md#node) :black_small_square: [node_color](core-socket.md#node_color) :black_small_square: [node_label](core-socket.md#node_label) :black_small_square: [offset](core-gener-geome-geometry.md#offset) :black_small_square: [out](color.md#out) :black_small_square: [out_OLD](geometry.md#out_old) :black_small_square: [\_panel_name](core-socket.md#_panel_name) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [point_cloud](core-gener-geome-geometry.md#point_cloud) :black_small_square: [\_pop](closure.md#_pop) :black_small_square: [position](core-gener-geome-geometry.md#position) :black_small_square: [proximity](core-gener-geome-geometry.md#proximity) :black_small_square: [proximity_edges](core-gener-geome-geometry.md#proximity_edges) :black_small_square: [proximity_faces](core-gener-geome-geometry.md#proximity_faces) :black_small_square: [proximity_points](core-gener-geome-geometry.md#proximity_points) :black_small_square: [\_push](closure.md#_push) :black_small_square: [raycast](core-gener-geome-geometry.md#raycast) :black_small_square: [realize](core-gener-geome-geometry.md#realize) :black_small_square: [remove_named_attribute](core-gener-geome-geometry.md#remove_named_attribute) :black_small_square: [repeat](core-socket.md#repeat) :black_small_square: [replace_material](core-gener-geome-geometry.md#replace_material) :black_small_square: ['_selection' not found]() :black_small_square: [separate_components](core-gener-geome-geometry.md#separate_components) :black_small_square: [set_id](core-gener-geome-geometry.md#set_id) :black_small_square: [set_material](core-gener-geome-geometry.md#set_material) :black_small_square: [set_material_index](core-gener-geome-geometry.md#set_material_index) :black_small_square: [set_name](core-gener-geome-geometry.md#set_name) :black_small_square: [set_position](core-gener-geome-geometry.md#set_position) :black_small_square: [simulation](core-socket.md#simulation) :black_small_square: [\_socket_type](core-socket.md#_socket_type) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](core-socket.md#switch) :black_small_square: [switch](core-socket.md#switch) :black_small_square: [switch_false](core-socket.md#switch_false) :black_small_square: [to_instance](core-gener-geome-geometry.md#to_instance) :black_small_square: [transform](core-gener-geome-geometry.md#transform) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square: [viewer](core-gener-geome-geometry.md#viewer) :black_small_square: [volume](core-gener-geome-geometry.md#volume) :black_small_square:

## Content

- [domain_size](instances.md#domain_size)
- [FromGeometry](instances.md#fromgeometry)
- [ImportOBJ](instances.md#importobj)
- [insts](instances.md#insts)
- [rotate](instances.md#rotate)
- [scale](instances.md#scale)
- [set_transform](instances.md#set_transform)
- [to_points](instances.md#to_points)
- [translate](instances.md#translate)

## Properties



### insts

> _type_: **Instance**
>

INSTANCES domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Properties](instances.md#properties)</sub>

## Methods



----------
### domain_size()

> method

``` python
domain_size()
```

> Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INSTANCES'



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### FromGeometry()

> classmethod

``` python
FromGeometry(*geometry: 'Geometry')
```

> Node [Geometry to Instance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html)

#### Arguments:
- **geometry** (_Geometry_) : socket 'Geometry' (id: Geometry)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### ImportOBJ()

> classmethod

``` python
ImportOBJ(path: 'String' = None)
```

> Node ERROR: Node 'Import OBJ' not found

#### Arguments:
- **path** (_String_ = None) : socket 'Path' (id: Path)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### rotate()

> method

``` python
rotate(rotation: 'Rotation' = None, pivot_point: 'Vector' = None, local_space: 'Boolean' = None)
```

> Node [Rotate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **rotation** (_Rotation_ = None) : socket 'Rotation' (id: Rotation)
- **pivot_point** (_Vector_ = None) : socket 'Pivot Point' (id: Pivot Point)
- **local_space** (_Boolean_ = None) : socket 'Local Space' (id: Local Space)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### scale()

> method

``` python
scale(scale: 'Vector' = None, center: 'Vector' = None, local_space: 'Boolean' = None)
```

> Node [Scale Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/scale_instances.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **scale** (_Vector_ = None) : socket 'Scale' (id: Scale)
- **center** (_Vector_ = None) : socket 'Center' (id: Center)
- **local_space** (_Boolean_ = None) : socket 'Local Space' (id: Local Space)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### set_transform()

> method

``` python
set_transform(transform: 'Matrix' = None)
```

> Node [Set Instance Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/set_instance_transform.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **transform** (_Matrix_ = None) : socket 'Transform' (id: Transform)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### to_points()

> method

``` python
to_points(position: 'Vector' = None, radius: 'Float' = None)
```

> Node [Instances to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### translate()

> method

``` python
translate(translation: 'Vector' = None, local_space: 'Boolean' = None)
```

> Node [Translate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **translation** (_Vector_ = None) : socket 'Translation' (id: Translation)
- **local_space** (_Boolean_ = None) : socket 'Local Space' (id: Local Space)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>