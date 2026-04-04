# Cloud

``` python
Cloud(socket=None, name: str = None, tip: str = '', panel: str = '', user_label: str = None, **props)
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

!!! important
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

- [domain_size](core-gener-cloud-cloud.md#domain_size)
- [ImportCSV](core-gener-cloud-cloud.md#importcsv)
- [instance_on](core-gener-cloud-cloud.md#instance_on)
- [interpolate_curves](core-gener-cloud-cloud.md#interpolate_curves)
- [Points](core-gener-cloud-cloud.md#points)
- [radius](core-gener-cloud-cloud.md#radius)
- [to_curves](core-gener-cloud-cloud.md#to_curves)
- [to_sdf_grid](core-gener-cloud-cloud.md#to_sdf_grid)
- [to_vertices](core-gener-cloud-cloud.md#to_vertices)
- [to_volume](core-gener-cloud-cloud.md#to_volume)

## Properties



### radius

> _type_: **?**
>

Property get node <Node Set Point Radius>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](core-gener-cloud-cloud.md#cloud) :black_small_square: [Content](core-gener-cloud-cloud.md#content) :black_small_square: [Properties](core-gener-cloud-cloud.md#properties)</sub>

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
- **Parameter** : 'POINTCLOUD'



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](core-gener-cloud-cloud.md#cloud) :black_small_square: [Content](core-gener-cloud-cloud.md#content) :black_small_square: [Methods](core-gener-cloud-cloud.md#methods)</sub>

----------
### ImportCSV()

> classmethod

``` python
ImportCSV(path: 'String' = None, delimiter: 'String' = None)
```

> Node ERROR: Node 'Import CSV' not found

#### Arguments:
- **path** (_String_ = None) : socket 'Path' (id: Path)
- **delimiter** (_String_ = None) : socket 'Delimiter' (id: Delimiter)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](core-gener-cloud-cloud.md#cloud) :black_small_square: [Content](core-gener-cloud-cloud.md#content) :black_small_square: [Methods](core-gener-cloud-cloud.md#methods)</sub>

----------
### instance_on()

> method

``` python
instance_on(instance: 'Instances' = None, pick_instance: 'Boolean' = None, instance_index: 'Integer' = None, rotation: 'Rotation' = None, scale: 'Vector' = None)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](core-gener-cloud-cloud.md#cloud) :black_small_square: [Content](core-gener-cloud-cloud.md#content) :black_small_square: [Methods](core-gener-cloud-cloud.md#methods)</sub>

----------
### interpolate_curves()

> method

``` python
interpolate_curves(guide_curves: 'Curve' = None, guide_up: 'Vector' = None, guide_group_id: 'Integer' = None, point_up: 'Vector' = None, point_group_id: 'Integer' = None, max_neighbors: 'Integer' = None)
```

> Node [Interpolate Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/interpolate_curves.html)

#### Information:
- **Socket** : self



#### Arguments:
- **guide_curves** (_Curve_ = None) : socket 'Guide Curves' (id: Guide Curves)
- **guide_up** (_Vector_ = None) : socket 'Guide Up' (id: Guide Up)
- **guide_group_id** (_Integer_ = None) : socket 'Guide Group ID' (id: Guide Group ID)
- **point_up** (_Vector_ = None) : socket 'Point Up' (id: Point Up)
- **point_group_id** (_Integer_ = None) : socket 'Point Group ID' (id: Point Group ID)
- **max_neighbors** (_Integer_ = None) : socket 'Max Neighbors' (id: Max Neighbors)



#### Returns:
- **Curve** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](core-gener-cloud-cloud.md#cloud) :black_small_square: [Content](core-gener-cloud-cloud.md#content) :black_small_square: [Methods](core-gener-cloud-cloud.md#methods)</sub>

----------
### Points()

> classmethod

``` python
Points(count: 'Integer' = None, position: 'Vector' = None, radius: 'Float' = None)
```

> Node [Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points.html)

#### Arguments:
- **count** (_Integer_ = None) : socket 'Count' (id: Count)
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](core-gener-cloud-cloud.md#cloud) :black_small_square: [Content](core-gener-cloud-cloud.md#content) :black_small_square: [Methods](core-gener-cloud-cloud.md#methods)</sub>

----------
### to_curves()

> method

``` python
to_curves(curve_group_id: 'Integer' = None, weight: 'Float' = None)
```

> Node [Points to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_curves.html)

#### Information:
- **Socket** : self



#### Arguments:
- **curve_group_id** (_Integer_ = None) : socket 'Curve Group ID' (id: Curve Group ID)
- **weight** (_Float_ = None) : socket 'Weight' (id: Weight)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](core-gener-cloud-cloud.md#cloud) :black_small_square: [Content](core-gener-cloud-cloud.md#content) :black_small_square: [Methods](core-gener-cloud-cloud.md#methods)</sub>

----------
### to_sdf_grid()

> method

``` python
to_sdf_grid(radius: 'Float' = None, voxel_size: 'Float' = None)
```

> Node ERROR: Node 'Points to SDF Grid' not found

#### Information:
- **Socket** : self



#### Arguments:
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)
- **voxel_size** (_Float_ = None) : socket 'Voxel Size' (id: Voxel Size)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](core-gener-cloud-cloud.md#cloud) :black_small_square: [Content](core-gener-cloud-cloud.md#content) :black_small_square: [Methods](core-gener-cloud-cloud.md#methods)</sub>

----------
### to_vertices()

> method

``` python
to_vertices()
```

> Node [Points to Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](core-gener-cloud-cloud.md#cloud) :black_small_square: [Content](core-gener-cloud-cloud.md#content) :black_small_square: [Methods](core-gener-cloud-cloud.md#methods)</sub>

----------
### to_volume()

> method

``` python
to_volume(density: 'Float' = None, resolution_mode: "Literal['Amount', 'Size']" = None, voxel_size: 'Float' = None, voxel_amount: 'Float' = None, radius: 'Float' = None)
```

> Node [Points to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html)

#### Information:
- **Socket** : self



#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **resolution_mode** (_Literal['Amount', 'Size']_ = None) : ('Amount', 'Size')
- **voxel_size** (_Float_ = None) : socket 'Voxel Size' (id: Voxel Size)
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount' (id: Voxel Amount)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)



#### Returns:
- **Volume** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](core-gener-cloud-cloud.md#cloud) :black_small_square: [Content](core-gener-cloud-cloud.md#content) :black_small_square: [Methods](core-gener-cloud-cloud.md#methods)</sub>