# Instances

``` python
Instances(socket=None, name: str = None, tip: str = '', panel: str = '', user_label: str = None, **props)
```

> The output socket of a [Node](node.md#node)

**Socket** is the base class for data classes such as [Float](core-gener-float-float.md#float), [Image](core-gener-image-image.md#image) or [Geometry](core-gener-geome-geometry.md#geometry).

It refers to an **output** socket of a [Node](node.md#node). A socket can be set to the **input** socket
of another [Node](node.md#node) to create a link between the two nodes:

``` python
# cube is the output socket 'Mesh' of the node 'Cube'
cube = Node("Cube").mesh

# cube is set the to socket 'geometry' of node 'Set Position'
node = Node("Set Position")
node.geometry = cube
```

> [!IMPORTANT]
> You can access to the other output sockets of the node in two different ways:
> - using [node](core-socket.md#node) attribute
> - using ***peer socket** naming convention where the **snake_case** name of
>.  the other sockets is suffixed by '_'

The example below shows how to access the to 'UV Map' socket of node [Cube](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/cube.html):

``` python
# cube is the output socket 'Mesh' of the node 'Cube'
cube = Mesh.Cube()

# Getting 'UV Map' through the node
uv_map = cube.node.uv_map

# Or using the 'peer socket' naming convention
uv_map = cuve.uv_map_
```

#### Arguments:
- **socket** (_NodeSocket_ = None) : the output socket to wrap
- **name** (_str_ = None) : input name if not None
- **tip** (_str_ = ) : description
- **panel** (_str_ = ) : panel name
- **user_label** (_str_ = None) : user label
- **props**

### Inherited

[add_method](group.md#add_method) :black_small_square: ['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socket.md#check_in_list) :black_small_square: [\_class_test](core-boolean.md#_class_test) :black_small_square: [Constant](core-socket.md#constant) :black_small_square: [default_value](core-socket.md#default_value) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [Empty](core-socket.md#empty) :black_small_square: [\_\_enter__](layout.md#__enter__) :black_small_square: [\_\_exit__](layout.md#__exit__) :black_small_square: [\_\_getattr__](g.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socket.md#_get_bsocket_from_input) :black_small_square: [IndexSwitch](core-socket.md#indexswitch) :black_small_square: [index_switch](core-socket.md#index_switch) :black_small_square: [\_\_init__](colorramp.md#__init__) :black_small_square: [Input](input.md#input) :black_small_square: [\_interface_socket](core-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socket.md#_is_empty) :black_small_square: [is_grid](core-socket.md#is_grid) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](node.md#_lc) :black_small_square: [\_lcop](core-socket.md#_lcop) :black_small_square: [link_inputs](node.md#link_inputs) :black_small_square: [menu](core-gener-menu---menu.md#menu) :black_small_square: [MenuSwitch](core-socket.md#menuswitch) :black_small_square: [menu_switch](core-gener-menu-menu.md#menu_switch) :black_small_square: [\_name](core-socket.md#_name) :black_small_square: [Named](core-gener-boole-boolean.md#named) :black_small_square: [NewInput](core-socket.md#newinput) :black_small_square: [node](core-socket.md#node) :black_small_square: [node_color](core-socket.md#node_color) :black_small_square: [node_label](core-socket.md#node_label) :black_small_square: [out](core-color.md#out) :black_small_square: [\_panel_name](core-socket.md#_panel_name) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [\_pop](core-closure.md#_pop) :black_small_square: [\_push](core-closure.md#_push) :black_small_square: [repeat](core-socket.md#repeat) :black_small_square: [\_reset](core-cloud.md#_reset) :black_small_square: [simulation](core-socket.md#simulation) :black_small_square: [\_socket_type](core-socket.md#_socket_type) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](core-socket.md#switch) :black_small_square: [switch](core-socket.md#switch) :black_small_square: [switch_false](core-socket.md#switch_false) :black_small_square: [\_test_socket_to_data_type](core-socket.md#_test_socket_to_data_type) :black_small_square: ['_tree' not found]() :black_small_square: [\_ul](core-socket.md#_ul) :black_small_square: ['_use_layout' not found]() :black_small_square: [user_label](core-socket.md#user_label) :black_small_square:

## Content

- [domain_size](core-gener-insta-instances.md#domain_size)
- [FromGeometry](core-gener-insta-instances.md#fromgeometry)
- [ImportOBJ](core-gener-insta-instances.md#importobj)
- [rotate](core-gener-insta-instances.md#rotate)
- [scale](core-gener-insta-instances.md#scale)
- [set_transform](core-gener-insta-instances.md#set_transform)
- [to_points](core-gener-insta-instances.md#to_points)
- [transform](core-gener-insta-instances.md#transform)
- [translate](core-gener-insta-instances.md#translate)

## Properties



### transform

> _type_: **?**
>

Property get node <Node Set Instance Transform>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](core-gener-insta-instances.md#instances) :black_small_square: [Content](core-gener-insta-instances.md#content) :black_small_square: [Properties](core-gener-insta-instances.md#properties)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](core-gener-insta-instances.md#instances) :black_small_square: [Content](core-gener-insta-instances.md#content) :black_small_square: [Methods](core-gener-insta-instances.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](core-gener-insta-instances.md#instances) :black_small_square: [Content](core-gener-insta-instances.md#content) :black_small_square: [Methods](core-gener-insta-instances.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](core-gener-insta-instances.md#instances) :black_small_square: [Content](core-gener-insta-instances.md#content) :black_small_square: [Methods](core-gener-insta-instances.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](core-gener-insta-instances.md#instances) :black_small_square: [Content](core-gener-insta-instances.md#content) :black_small_square: [Methods](core-gener-insta-instances.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](core-gener-insta-instances.md#instances) :black_small_square: [Content](core-gener-insta-instances.md#content) :black_small_square: [Methods](core-gener-insta-instances.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](core-gener-insta-instances.md#instances) :black_small_square: [Content](core-gener-insta-instances.md#content) :black_small_square: [Methods](core-gener-insta-instances.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](core-gener-insta-instances.md#instances) :black_small_square: [Content](core-gener-insta-instances.md#content) :black_small_square: [Methods](core-gener-insta-instances.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](core-gener-insta-instances.md#instances) :black_small_square: [Content](core-gener-insta-instances.md#content) :black_small_square: [Methods](core-gener-insta-instances.md#methods)</sub>