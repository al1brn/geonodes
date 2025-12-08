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
> - using ['#node' not found]() attribute
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

[\_\_add__](shaderroot.md#__add__) :black_small_square: ['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socke-socket.md#check_in_list) :black_small_square: [\_classes_test](core-socke-socket.md#_classes_test) :black_small_square: [default_value](core-socke-socket.md#default_value) :black_small_square: [\_domain_to_geometry](core-socke-socket.md#_domain_to_geometry) :black_small_square: [\_\_enter__](core-socke-socket.md#__enter__) :black_small_square: [\_\_exit__](core-socke-socket.md#__exit__) :black_small_square: [\_\_getattr__](core-socke-socket.md#__getattr__) :black_small_square: [IndexSwitch](core-socke-socket.md#indexswitch) :black_small_square: [index_switch](core-socke-socket.md#index_switch) :black_small_square: [\_\_init__](core-socke-socket.md#__init__) :black_small_square: [Input](core-socke-socket.md#input) :black_small_square: [\_interface_socket](core-socke-socket.md#_interface_socket) :black_small_square: [is_grid](core-socke-socket.md#is_grid) :black_small_square: [\_jump](core-socke-socket.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](core-socke-socket.md#_lc) :black_small_square: [\_lcop](core-socke-socket.md#_lcop) :black_small_square: [link_from](core-socke-socket.md#link_from) :black_small_square: [MenuSwitch](core-socke-socket.md#menuswitch) :black_small_square: [menu_switch](core-socke-socket.md#menu_switch) :black_small_square: [\_\_mul__](shaderroot.md#__mul__) :black_small_square: [\_name](core-socke-socket.md#_name) :black_small_square: [node](core-socke-socket.md#node) :black_small_square: [node_color](core-socke-socket.md#node_color) :black_small_square: [node_label](core-socke-socket.md#node_label) :black_small_square: [\_panel_name](core-socke-socket.md#_panel_name) :black_small_square: [pin_gizmo](core-socke-socket.md#pin_gizmo) :black_small_square: [\_pop](core-socke-socket.md#_pop) :black_small_square: [\_push](core-socke-socket.md#_push) :black_small_square: [repeat](core-socke-socket.md#repeat) :black_small_square: [\_reset](core-socke-socket.md#_reset) :black_small_square: [simulation](core-socke-socket.md#simulation) :black_small_square: ['_socket_type' not found]() :black_small_square: [\_\_str__](core-socke-socket.md#__str__) :black_small_square: [surface_out](shaderroot.md#surface_out) :black_small_square: [Switch](core-socke-socket.md#switch) :black_small_square: [switch](core-socke-socket.md#switch) :black_small_square: [switch_false](core-socke-socket.md#switch_false) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square: [volume_out](shaderroot.md#volume_out) :black_small_square:

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