# VectRot

> Bases classes: [VectorLike](geono-vectorlike.md#vectorlike)

``` python
VectRot(socket)
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

The example below shows how to access the to 'UV Map' socket of node <*Cube>:

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

[\_\_abs__](geono-vectorlike.md#__abs__) :black_small_square: [\_\_add__](geono-vectorlike.md#__add__) :black_small_square: [blur](geono-socket.md#blur) :black_small_square: [\_cache](geono-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-nodecache.md#_cache_reset) :black_small_square: [\_\_ceil__](geono-vectorlike.md#__ceil__) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [\_\_floor__](geono-vectorlike.md#__floor__) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [get_socket_class](geono-socket.md#get_socket_class) :black_small_square: [\_\_iadd__](geono-vectorlike.md#__iadd__) :black_small_square: [\_\_imod__](geono-vectorlike.md#__imod__) :black_small_square: [\_\_imul__](geono-vectorlike.md#__imul__) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [\_\_ipow__](geono-vectorlike.md#__ipow__) :black_small_square: [\_\_isub__](geono-vectorlike.md#__isub__) :black_small_square: [\_\_itruediv__](geono-vectorlike.md#__itruediv__) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [\_\_matmul__](geono-vectorlike.md#__matmul__) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [\_\_mod__](geono-vectorlike.md#__mod__) :black_small_square: [\_\_mul__](geono-vectorlike.md#__mul__) :black_small_square: [Named](geono-valuesocket.md#named) :black_small_square: [NamedAttribute](geono-valuesocket.md#namedattribute) :black_small_square: [\_\_neg__](geono-vectorlike.md#__neg__) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [out](geono-socket.md#out) :black_small_square: [\_\_pow__](geono-vectorlike.md#__pow__) :black_small_square: [\_\_radd__](geono-vectorlike.md#__radd__) :black_small_square: [\_\_rmod__](geono-vectorlike.md#__rmod__) :black_small_square: [\_\_rmul__](geono-vectorlike.md#__rmul__) :black_small_square: [\_\_rpow__](geono-vectorlike.md#__rpow__) :black_small_square: [\_\_rsub__](geono-vectorlike.md#__rsub__) :black_small_square: [\_\_rtruediv__](geono-vectorlike.md#__rtruediv__) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [\_\_sub__](geono-vectorlike.md#__sub__) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square: [to_output](geono-socket.md#to_output) :black_small_square: [\_\_truediv__](geono-vectorlike.md#__truediv__) :black_small_square:

## Content

- [Combine](geono-vectrot.md#combine)
- [Random](geono-vectrot.md#random)
- [separate_xyz](geono-vectrot.md#separate_xyz)
- [x](geono-vectrot.md#x)
- [y](geono-vectrot.md#y)
- [z](geono-vectrot.md#z)

## Properties



### separate_xyz

> _type_: **Node**
>

> Node <&Separate XYZ"

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [VectRot](geono-vectrot.md#vectrot) :black_small_square: [Content](geono-vectrot.md#content) :black_small_square: [Properties](geono-vectrot.md#properties)</sub>

### x

> _type_: **Float**
>

Socket 'X' of node <&Separate XYZ>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [VectRot](geono-vectrot.md#vectrot) :black_small_square: [Content](geono-vectrot.md#content) :black_small_square: [Properties](geono-vectrot.md#properties)</sub>

### y

> _type_: **Float**
>

Socket 'Y' of node <&Separate XYZ>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [VectRot](geono-vectrot.md#vectrot) :black_small_square: [Content](geono-vectrot.md#content) :black_small_square: [Properties](geono-vectrot.md#properties)</sub>

### z

> _type_: **Float**
>

Socket 'Z' of node <&Separate XYZ>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [VectRot](geono-vectrot.md#vectrot) :black_small_square: [Content](geono-vectrot.md#content) :black_small_square: [Properties](geono-vectrot.md#properties)</sub>

## Methods



----------
### Combine()

> classmethod

``` python
Combine(x, y, z)
```

Constructor node <&Combine XYZ>

#### Arguments:
- **x**
- **y**
- **z**



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [VectRot](geono-vectrot.md#vectrot) :black_small_square: [Content](geono-vectrot.md#content) :black_small_square: [Methods](geono-vectrot.md#methods)</sub>

----------
### Random()

> classmethod

``` python
Random(min=None, max=None, id=None, seed=None)
```

Constructor node <&Random Value>

#### Arguments:
- **min** ( = None)
- **max** ( = None)
- **id** ( = None)
- **seed** ( = None)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [VectRot](geono-vectrot.md#vectrot) :black_small_square: [Content](geono-vectrot.md#content) :black_small_square: [Methods](geono-vectrot.md#methods)</sub>