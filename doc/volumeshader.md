# VolumeShader

``` python
VolumeShader(socket)
```

> The output socket of a [Node](node.md#node)

**Socket** is the base class for data classes such as [Float](float.md#float), [Image](image.md#image) or [Geometry](geometry.md#geometry).

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
> - using [node](socket.md#node) attribute
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
- **socket** (_NodeSocket_) : the output socket to wrap

### Inherited

[\_\_add__](shaderroot.md#__add__) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](socket.md#_domain_to_geometry) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](socket.md#__init__) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [link_from](socket.md#link_from) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [\_mark_for_delete](socket.md#_mark_for_delete) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [\_\_mul__](shaderroot.md#__mul__) :black_small_square: [\_name](socket.md#_name) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [option](socket.md#option) :black_small_square: [option_index](socket.md#option_index) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_\_setattr__](socket.md#__setattr__) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [surface_out](shaderroot.md#surface_out) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [switch_false](socket.md#switch_false) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square: [volume_out](shaderroot.md#volume_out) :black_small_square:

## Content

- [Absorption](volumeshader.md#absorption)
- [info](volumeshader.md#info)
- [Principled](volumeshader.md#principled)
- [Scatter](volumeshader.md#scatter)

## Methods



----------
### Absorption()

> classmethod

``` python
Absorption(color=None, density=None)
```

> Node ERROR: Node 'Volume Absorption' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **density** (_Float_ = None) : socket 'Density' (id: Density)



#### Returns:
- **VolumeShader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [VolumeShader](volumeshader.md#volumeshader) :black_small_square: [Content](volumeshader.md#content) :black_small_square: [Methods](volumeshader.md#methods)</sub>

----------
### info()

> classmethod

``` python
info()
```

> Node [Volume Info](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/volume_info.html)

#### Returns:
- **node** (_Color_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [VolumeShader](volumeshader.md#volumeshader) :black_small_square: [Content](volumeshader.md#content) :black_small_square: [Methods](volumeshader.md#methods)</sub>

----------
### Principled()

> classmethod

``` python
Principled(color=None, color_attribute=None, density=None, density_attribute=None, anisotropy=None, absorption_color=None, emission_strength=None, emission_color=None, blackbody_intensity=None, blackbody_tint=None, temperature=None, temperature_attribute=None)
```

> Node ERROR: Node 'Principled Volume' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **color_attribute** (_String_ = None) : socket 'Color Attribute' (id: Color Attribute)
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **density_attribute** (_String_ = None) : socket 'Density Attribute' (id: Density Attribute)
- **anisotropy** (_Float_ = None) : socket 'Anisotropy' (id: Anisotropy)
- **absorption_color** (_Color_ = None) : socket 'Absorption Color' (id: Absorption Color)
- **emission_strength** (_Float_ = None) : socket 'Emission Strength' (id: Emission Strength)
- **emission_color** (_Color_ = None) : socket 'Emission Color' (id: Emission Color)
- **blackbody_intensity** (_Float_ = None) : socket 'Blackbody Intensity' (id: Blackbody Intensity)
- **blackbody_tint** (_Color_ = None) : socket 'Blackbody Tint' (id: Blackbody Tint)
- **temperature** (_Float_ = None) : socket 'Temperature' (id: Temperature)
- **temperature_attribute** (_String_ = None) : socket 'Temperature Attribute' (id: Temperature Attribute)



#### Returns:
- **VolumeShader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [VolumeShader](volumeshader.md#volumeshader) :black_small_square: [Content](volumeshader.md#content) :black_small_square: [Methods](volumeshader.md#methods)</sub>

----------
### Scatter()

> classmethod

``` python
Scatter(color=None, density=None, anisotropy=None, phase='HENYEY_GREENSTEIN')
```

> Node ERROR: Node 'Volume Scatter' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **anisotropy** (_Float_ = None) : socket 'Anisotropy' (id: Anisotropy)
- **phase** (_str_ = HENYEY_GREENSTEIN) : parameter 'phase' in ['HENYEY_GREENSTEIN', 'FOURNIER_FORAND', 'DRAINE', 'RAYLEIGH', 'MIE']



#### Returns:
- **VolumeShader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [VolumeShader](volumeshader.md#volumeshader) :black_small_square: [Content](volumeshader.md#content) :black_small_square: [Methods](volumeshader.md#methods)</sub>