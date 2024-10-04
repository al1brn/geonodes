# VolumeShader

> Bases classes: [ShaderRoot](macro-shade1-shade-shaderroot.md#shaderroot)

``` python
VolumeShader(socket)
```

> The output socket of a [Node](geono-node.md#node)

**Socket** is the base class for data classes such as [Float](geono-float.md#float), [Image](geono-image.md#image) or [Geometry](geono-geometry.md#geometry).

It refers to an **output** socket of a [Node](geono-node.md#node). A socket can be set to the **input** socket
of another [Node](geono-node.md#node) to create a link between the two nodes:

``` python
# cube is the output socket 'Mesh' of the node 'Cube'
cube = Node("Cube").mesh

# cube is set the to socket 'geometry' of node 'Set Position'
node = Node("Set Position")
node.geometry = cube
```

> [!IMPORTANT]
> You can access to the other output sockets of the node in two different ways:
> - using [node](geono-socket.md#node) attribute
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

[\_\_add__](macro-shade1-shade-shaderroot.md#__add__) :black_small_square: [add](macro-shade1-shade-shaderroot.md#add) :black_small_square: [blur](geono-socket.md#blur) :black_small_square: [\_cache](geono-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [get_socket_class](geono-socket.md#get_socket_class) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [mix](macro-shade1-shade-shaderroot.md#mix) :black_small_square: [Named](geono-attribute.md#named) :black_small_square: [NamedAttribute](geono-attribute.md#namedattribute) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [\_\_radd__](macro-shade1-shade-shaderroot.md#__radd__) :black_small_square: [\_reset](geono-socket.md#_reset) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [surface_out](macro-shade1-shade-shaderroot.md#surface_out) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square: [to_rgb](macro-shade1-shade-shaderroot.md#to_rgb) :black_small_square: [volume_out](macro-shade1-shade-shaderroot.md#volume_out) :black_small_square:

## Content

- [Absorption](macro-shade1-shade-volumeshader.md#absorption)
- [Principled](macro-shade1-shade-volumeshader.md#principled)
- [Scatter](macro-shade1-shade-volumeshader.md#scatter)

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [VolumeShader](macro-shade1-shade-volumeshader.md#volumeshader) :black_small_square: [Content](macro-shade1-shade-volumeshader.md#content) :black_small_square: [Methods](macro-shade1-shade-volumeshader.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [VolumeShader](macro-shade1-shade-volumeshader.md#volumeshader) :black_small_square: [Content](macro-shade1-shade-volumeshader.md#content) :black_small_square: [Methods](macro-shade1-shade-volumeshader.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [VolumeShader](macro-shade1-shade-volumeshader.md#volumeshader) :black_small_square: [Content](macro-shade1-shade-volumeshader.md#content) :black_small_square: [Methods](macro-shade1-shade-volumeshader.md#methods)</sub>