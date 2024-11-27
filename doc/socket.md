# Socket

``` python
Socket(socket)
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

## Content

- **B** : [blur](socket.md#blur)
- **H** : [hash_value](socket.md#hash_value)
- **I** : [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](socket.md#__init__)
- **L** : [\_lc](socket.md#_lc)
- **M** : [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch)
- **N** : [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label)
- **O** : [out](socket.md#out)
- **S** : [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch)

## Properties



### node

> _type_: **Node**
>

Returns the node owning the socket.

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](socket.md#socket) :black_small_square: [Content](socket.md#content) :black_small_square: [Properties](socket.md#properties)</sub>

### node_color

> _type_: **mathutils**
>

Node color

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](socket.md#socket) :black_small_square: [Content](socket.md#content) :black_small_square: [Properties](socket.md#properties)</sub>

### node_label

> _type_: **str**
>

Node Label

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](socket.md#socket) :black_small_square: [Content](socket.md#content) :black_small_square: [Properties](socket.md#properties)</sub>

## Methods



----------
### blur()

> method

``` python
blur(iterations=None, weight=None)
```

> Node [Blur Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/blur_attribute.html)



#### Arguments:
- **iterations** (_Integer_ = None) : socket 'Iterations' (Iterations)
- **weight** (_Float_ = None) : socket 'Weight' (Weight)



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](socket.md#socket) :black_small_square: [Content](socket.md#content) :black_small_square: [Methods](socket.md#methods)</sub>

----------
### hash_value()

> method

``` python
hash_value(seed=None)
```

> Node [Hash Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/hash_value.html)

#### Arguments:
- **seed** (_Integer_ = None) : socket 'Seed' (Seed)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](socket.md#socket) :black_small_square: [Content](socket.md#content) :black_small_square: [Methods](socket.md#methods)</sub>

----------
### IndexSwitch()

> classmethod

``` python
IndexSwitch(*values, index=0)
```

> Node [Index Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/index_switch.html)

``` python
with GeoNodes("Index Switch demo"):

    # Create some geometries
    geo    = Geometry()
    cube   = Mesh.Cube()
    sphere = Mesh.IcoSphere()
    cone   = Mesh.Cone()

    # Pick in this list
    pick_geo = Geometry.IndexSwitch(geo, cube, sphere, cone, index=Integer(2, 'Index'))

    # Plug the result to the output
    pick_geo.out()
```

#### Arguments:
- **values** : list of Sockets to select into
- **index** (_Integer_ = 0) : socket 'Index' (Index)



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](socket.md#socket) :black_small_square: [Content](socket.md#content) :black_small_square: [Methods](socket.md#methods)</sub>

----------
### index_switch()

> method

``` python
index_switch(*values, index=0)
```

> Node [Index Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/index_switch.html)



Self is used as first socket in the node.

``` python
with GeoNodes("Index Switch demo"):

    # Create some geometries
    geo    = Geometry()
    cube   = Mesh.Cube()
    sphere = Mesh.IcoSphere()
    cone   = Mesh.Cone()

    # Pick in this list
    pick_geo = Geometry.IndexSwitch(geo, cube, sphere, cone, index=Integer(2, 'Index'))

    # Plug the result to the output
    pick_geo.out()
```

#### Arguments:
- **values** : list of Sockets to select into
- **index** (_Integer_ = 0) : socket 'Index' (Index)



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](socket.md#socket) :black_small_square: [Content](socket.md#content) :black_small_square: [Methods](socket.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(socket)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](socket.md#socket) :black_small_square: [Content](socket.md#content) :black_small_square: [Methods](socket.md#methods)</sub>

----------
### \_lc()

> method

``` python
_lc(label=None, color=None)
```

Set node label and color.

This method returns self to be chained to as socket:

``` python
with GeoNodes("Node label and color"):
    Geometry().out()

    a = Float(10)._lc("Var a")
    b = Float(10)._lc("Var b")
    c = (a + b)._lc("a + b", (1, 0, 0))
```

#### Arguments:
- **label** (_str_ = None) : node label
- **color** (_color_ = None) : node color



#### Returns:
- **self** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](socket.md#socket) :black_small_square: [Content](socket.md#content) :black_small_square: [Methods](socket.md#methods)</sub>

----------
### MenuSwitch()

> classmethod

``` python
MenuSwitch(items={'A': None, 'B': None}, menu=0, name='Menu', tip=None)
```

> Node [Menu Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/menu_switch.html)

The items of the Menu Switch node are provided in the 'items' dict.
An group input socket named after the 'name' argument is linked to menu selector.

``` python
with GeoNodes("Menu Switch demo"):

    # Create some geometries
    geo    = Geometry()
    cube   = Mesh.Cube()
    sphere = Mesh.IcoSphere()
    cone   = Mesh.Cone()

    # Pick in this list
    pick_geo = Geometry.MenuSwitch({"Input": geo, "Cube": cube, "Sphere": sphere, "Cone": cone}, menu="Cube")

    # Plug the result to the output
    pick_geo.out()
```

#### Arguments:
- **items** (_dict_ = {'A': None, 'B': None}) : menu names and values
- **menu** (_int or str_ = 0) : index or name of the default value
- **name** (_str_ = Menu) : name of the group input socket
- **tip** (_str_ = None) : user tip



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](socket.md#socket) :black_small_square: [Content](socket.md#content) :black_small_square: [Methods](socket.md#methods)</sub>

----------
### menu_switch()

> method

``` python
menu_switch(self_name='A', items={'B': None}, menu=0, name='Menu', tip=None)
```

> Node [Menu Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/menu_switch.html)



Self is connected to the first menu item with the name provided as argument.

``` python
with GeoNodes("Menu Switch demo"):

    # Create some geometries
    geo    = Geometry()
    cube   = Mesh.Cube()
    sphere = Mesh.IcoSphere()
    cone   = Mesh.Cone()

    # Pick in this list
    pick_geo = geo.menu_switch("Input", {"Cube": cube, "Sphere": sphere, "Cone": cone}, menu="Cube")

    # Plug the result to the output
    pick_geo.out()
```

#### Arguments:
- **self_name** (_str_ = A) : name to use
- **items** (_dict_ = {'B': None}) : other menu names and values
- **menu** (_int or str_ = 0) : index or name of the default value
- **name** (_str_ = Menu) : name of the group input socket
- **tip** (_str_ = None) : user tip



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](socket.md#socket) :black_small_square: [Content](socket.md#content) :black_small_square: [Methods](socket.md#methods)</sub>

----------
### out()

> method

``` python
out(name=None)
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



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](socket.md#socket) :black_small_square: [Content](socket.md#content) :black_small_square: [Methods](socket.md#methods)</sub>

----------
### Switch()

> classmethod

``` python
Switch(condition=None, false=None, true=None)
```

> Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)

``` python
with GeoNodes("Switch demo"):

    # Two possible geometries
    cube   = Mesh.Cube()
    sphere = Mesh.IcoSphere()

    # Select
    geo = Geometry.Switch(Boolean(True, "Use Sphere"), cube, sphere)

    # To group output
    geo.out()
```

#### Arguments:
- **condition** (_Boolean_ = None) : socket 'Switch' (Switch)
- **false** ( = None) : socket 'False' (False)
- **true** ( = None) : socket 'True' (True)



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](socket.md#socket) :black_small_square: [Content](socket.md#content) :black_small_square: [Methods](socket.md#methods)</sub>

----------
### switch()

> method

``` python
switch(condition=None, true=None)
```

> Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)



Self is connected to 'false' socket.

``` python
with GeoNodes("Switch demo"):

    # Two possible geometries
    cube   = Mesh.Cube()
    sphere = Mesh.IcoSphere()

    # Select
    geo = cube.switch(Boolean(True, "Use Sphere"), sphere)

    # To group output
    geo.out()
```

#### Arguments:
- **condition** (_Boolean_ = None) : socket 'Switch' (Switch)
- **true** ( = None) : socket 'True' (True)



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](socket.md#socket) :black_small_square: [Content](socket.md#content) :black_small_square: [Methods](socket.md#methods)</sub>