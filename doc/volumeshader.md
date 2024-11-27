# VolumeShader

> Bases classes: [Attribute](attribute.md#attribute)

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

#### Arguments:
- **socket** (_NodeSocket_) : the output socket to wrap

### Inherited

[blur](socket.md#blur) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [hash_value](socket.md#hash_value) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](socket.md#__init__) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [Named](attribute.md#named) :black_small_square: [NamedAttribute](attribute.md#namedattribute) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square:

## Content

- [Absorption](volumeshader.md#absorption)
- [Principled](volumeshader.md#principled)
- [Scatter](volumeshader.md#scatter)

## Methods



----------
### Absorption()

> classmethod

``` python
Absorption(color=None, density=None)
```

Node 'Volume Absorption' (ShaderNodeVolumeAbsorption)

#### Arguments:
- **color** ( = None)
- **density** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [VolumeShader](volumeshader.md#volumeshader) :black_small_square: [Content](volumeshader.md#content) :black_small_square: [Methods](volumeshader.md#methods)</sub>

----------
### Principled()

> classmethod

``` python
Principled(color=None, color_attribute=None, density=None, density_attribute=None, anisotropy=None, absorption_color=None, emission_strength=None, emission_color=None, blackbody_intensity=None, blackbody_tint=None, temperature=None, temperature_attribute=None)
```

Node 'Principled Volume' (ShaderNodeVolumePrincipled)

#### Arguments:
- **color** ( = None)
- **color_attribute** ( = None)
- **density** ( = None)
- **density_attribute** ( = None)
- **anisotropy** ( = None)
- **absorption_color** ( = None)
- **emission_strength** ( = None)
- **emission_color** ( = None)
- **blackbody_intensity** ( = None)
- **blackbody_tint** ( = None)
- **temperature** ( = None)
- **temperature_attribute** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [VolumeShader](volumeshader.md#volumeshader) :black_small_square: [Content](volumeshader.md#content) :black_small_square: [Methods](volumeshader.md#methods)</sub>

----------
### Scatter()

> classmethod

``` python
Scatter(color=None, density=None, anisotropy=None)
```

Node 'Volume Scatter' (ShaderNodeVolumeScatter)

#### Arguments:
- **color** ( = None)
- **density** ( = None)
- **anisotropy** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [VolumeShader](volumeshader.md#volumeshader) :black_small_square: [Content](volumeshader.md#content) :black_small_square: [Methods](volumeshader.md#methods)</sub>