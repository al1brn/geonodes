# VolumeShader

``` python
VolumeShader(socket=None, name: str = None, tip: str = '', panel: str = '', **props)
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
- **name** (_str_ = None)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **props**

### Inherited

[\_\_add__](shaderroot.md#__add__) :black_small_square: ['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socket.md#check_in_list) :black_small_square: [\_class_test](boolean.md#_class_test) :black_small_square: [Constant](core-socket.md#constant) :black_small_square: [default_value](core-socket.md#default_value) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [Empty](core-socket.md#empty) :black_small_square: [\_\_enter__](layout.md#__enter__) :black_small_square: [\_\_exit__](layout.md#__exit__) :black_small_square: [\_\_getattr__](g.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socket.md#_get_bsocket_from_input) :black_small_square: [IndexSwitch](core-socket.md#indexswitch) :black_small_square: [index_switch](core-socket.md#index_switch) :black_small_square: [\_\_init__](colorramp.md#__init__) :black_small_square: [Input](input.md#input) :black_small_square: [\_interface_socket](core-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socket.md#_is_empty) :black_small_square: [is_grid](core-socket.md#is_grid) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](node.md#_lc) :black_small_square: [\_lcop](core-socket.md#_lcop) :black_small_square: [link_inputs](node.md#link_inputs) :black_small_square: [MenuSwitch](core-socket.md#menuswitch) :black_small_square: [menu_switch](menu.md#menu_switch) :black_small_square: [\_\_mul__](shaderroot.md#__mul__) :black_small_square: [\_name](core-socket.md#_name) :black_small_square: [Named](boolean.md#named) :black_small_square: [NewInput](core-socket.md#newinput) :black_small_square: [node](core-socket.md#node) :black_small_square: [node_color](core-socket.md#node_color) :black_small_square: [node_label](core-socket.md#node_label) :black_small_square: [\_panel_name](core-socket.md#_panel_name) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [\_pop](closure.md#_pop) :black_small_square: [\_push](closure.md#_push) :black_small_square: [repeat](core-socket.md#repeat) :black_small_square: [\_reset](cloud.md#_reset) :black_small_square: [simulation](core-socket.md#simulation) :black_small_square: [\_socket_type](core-socket.md#_socket_type) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [surface_out](shaderroot.md#surface_out) :black_small_square: [Switch](core-socket.md#switch) :black_small_square: [switch](core-socket.md#switch) :black_small_square: [switch_false](core-socket.md#switch_false) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square: [volume_out](shaderroot.md#volume_out) :black_small_square:

## Content

- [Absorption](volumeshader.md#absorption)
- [Principled](volumeshader.md#principled)
- [Scatter](volumeshader.md#scatter)

## Methods



----------
### Absorption()

> classmethod

``` python
Absorption(color: 'Color' = None, density: 'Float' = None)
```

> Node ERROR: Node 'Volume Absorption' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **density** (_Float_ = None) : socket 'Density' (id: Density)



#### Returns:
- **VolumeShader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [VolumeShader](volumeshader.md#volumeshader) :black_small_square: [Content](volumeshader.md#content) :black_small_square: [Methods](volumeshader.md#methods)</sub>

----------
### Principled()

> classmethod

``` python
Principled(color: 'Color' = None, color_attribute: 'String' = None, density: 'Float' = None, density_attribute: 'String' = None, anisotropy: 'Float' = None, absorption_color: 'Color' = None, emission_strength: 'Float' = None, emission_color: 'Color' = None, blackbody_intensity: 'Float' = None, blackbody_tint: 'Color' = None, temperature: 'Float' = None, temperature_attribute: 'String' = None)
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
Scatter(color: 'Color' = None, density: 'Float' = None, anisotropy: 'Float' = None, phase: "Literal['HENYEY_GREENSTEIN', 'FOURNIER_FORAND', 'DRAINE', 'RAYLEIGH', 'MIE']" = 'HENYEY_GREENSTEIN')
```

> Node ERROR: Node 'Volume Scatter' not found

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **anisotropy** (_Float_ = None) : socket 'Anisotropy' (id: Anisotropy)
- **phase** (_Literal['HENYEY_GREENSTEIN', 'FOURNIER_FORAND', 'DRAINE', 'RAYLEIGH', 'MIE']_ = HENYEY_GREENSTEIN) : parameter 'phase' in ['HENYEY_GREENSTEIN', 'FOURNIER_FORAND', 'DRAINE', 'RAYLEIGH', 'MIE']



#### Returns:
- **VolumeShader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [VolumeShader](volumeshader.md#volumeshader) :black_small_square: [Content](volumeshader.md#content) :black_small_square: [Methods](volumeshader.md#methods)</sub>