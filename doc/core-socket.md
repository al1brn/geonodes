# Socket

``` python
Socket(socket=None, name: str = None, tip: str = '', panel: str = '', **props)
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

['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: ['_layout' not found]() :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square:

## Content

- **C** : [Constant](core-socket.md#constant)
- **E** : [Empty](core-socket.md#empty)
- **G** : [\_get_bsocket_from_input](core-socket.md#_get_bsocket_from_input)
- **I** : [IndexSwitch](core-socket.md#indexswitch) :black_small_square: [index_switch](core-socket.md#index_switch) :black_small_square: [\_\_init__](core-socket.md#__init__) :black_small_square: [Input](core-socket.md#input) :black_small_square: [\_interface_socket](core-socket.md#_interface_socket) :black_small_square: [is_grid](core-socket.md#is_grid)
- **L** : [\_lc](core-socket.md#_lc) :black_small_square: [link_inputs](core-socket.md#link_inputs)
- **M** : [MenuSwitch](core-socket.md#menuswitch) :black_small_square: [menu_switch](core-socket.md#menu_switch)
- **N** : [\_name](core-socket.md#_name) :black_small_square: [Named](core-socket.md#named) :black_small_square: [NewInput](core-socket.md#newinput) :black_small_square: [node_color](core-socket.md#node_color) :black_small_square: [node_label](core-socket.md#node_label)
- **O** : [out](core-socket.md#out)
- **P** : [\_panel_name](core-socket.md#_panel_name)
- **R** : [repeat](core-socket.md#repeat)
- **S** : [simulation](core-socket.md#simulation) :black_small_square: [Switch](core-socket.md#switch) :black_small_square: [switch](core-socket.md#switch) :black_small_square: [switch_false](core-socket.md#switch_false)

## Properties



### \_interface_socket

> _type_: **Interface**
>

Return the interface socket if exists

An interface socket exists when the socket a tree input or output socket or
when it is the socket of a group

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Properties](core-socket.md#properties)</sub>

### is_grid

> _type_: **?**
>

bool property

Returns True if socket is a grid (inferred_structure_type == 'GRID').

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Properties](core-socket.md#properties)</sub>

### \_name

> _type_: **str**
>

Return the name or the label

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Properties](core-socket.md#properties)</sub>

### node_color

> _type_: **mathutils**
>

Node color

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Properties](core-socket.md#properties)</sub>

### node_label

> _type_: **str**
>

Node Label

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Properties](core-socket.md#properties)</sub>

### \_panel_name

> _type_: **str**
>

Return the name of the panel

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Properties](core-socket.md#properties)</sub>

## Methods



----------
### Constant()

> classmethod

``` python
Constant(value: None)
```

Create an input socket from a constant Node.

#### Arguments:
- **value**

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Methods](core-socket.md#methods)</sub>

----------
### Empty()

> classmethod

``` python
Empty(value=None)
```

Create an empty socket.

An empty socket is used temporarily as an input for nodes with dynamic sockets:

``` python
    # 10 iterations starting from an empty geometry
    for rep in Geometry.Repeat(10):
        pass
    result = rep.geometry
```

#### Arguments:
- **value** (_Any_ = None) : default value

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Methods](core-socket.md#methods)</sub>

----------
### \_get_bsocket_from_input()

> method

``` python
_get_bsocket_from_input(name: str = None) -> _bpy_types.NodeSocket
```

Get the availble input socket if any.

The socket is get a an OUTPUT socket of the current input.

#### Arguments:
- **name** (_str_ = None) : name filter



#### Returns:
- **NodeSocket** : or None if not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Methods](core-socket.md#methods)</sub>

----------
### IndexSwitch()

> classmethod

``` python
IndexSwitch(*values, index=None, default_index: int = 0)
```

> Node [Index Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/index_switch.html)

``` python
with GeoNodes("IndexSwitch demo"):

    # Create some geometries
    geo    = Geometry()
    cube   = Mesh.Cube()
    sphere = Mesh.IcoSphere()
    cone   = Mesh.Cone()

    # Pick in this list
    pick_geo = Geometry.IndexSwitch(geo, cube, sphere, cone, index=tree.new_input("Geometry index", default_value=2))

    # Plug the result to the output
    pick_geo.out()
```

#### Arguments:
- **values** : list of Sockets to select into
- **index** (_Integer_ = None) : socket 'Index' (Index)
- **default_index** (_int_ = 0)



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Methods](core-socket.md#methods)</sub>

----------
### index_switch()

> method

``` python
index_switch(*values, index=None, default_index: int = 0)
```

> Node [Index Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/index_switch.html)

``` python
with GeoNodes("index_switch demo") as tree:

    # Create some geometries
    geo    = Geometry()
    cube   = Mesh.Cube()
    sphere = Mesh.IcoSphere()
    cone   = Mesh.Cone()

    # Pick in this list
    pick_geo = geo.index_switch(cube, sphere, cone, index=tree.new_input("Geometry index", default_value=2))

    # Plug the result to the output
    pick_geo.out()
```

#### Arguments:
- **values** : list of Sockets to select into
- **index** (_Integer_ = None) : socket 'Index' (Index)
- **default_index** (_int_ = 0)



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Methods](core-socket.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(socket=None, name: str = None, tip: str = '', panel: str = '', **props)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Methods](core-socket.md#methods)</sub>

----------
### Input()

> classmethod

``` python
Input(name: str, panel: str = '', halt: bool = True)
```

Get an exist input socket from its name and panel.

> [!NOTE]
> The "input" socket here is an "output" socket of the current input node

To create a input socket use NewInput.

If the 'name' argument is None, the first socket of the proper type is returned.

#### Raises:
- **NodeError** : 



#### Arguments:
- **name** (_str_) : socket name
- **panel** (_str_ = ) : panel name
- **halt** (_bool_ = True) : raises an error if not found



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Methods](core-socket.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Methods](core-socket.md#methods)</sub>

----------
### link_inputs()

> method

``` python
link_inputs(from_node: geonodes.core.nodeclass.Node = None, from_panel: str = '', *, include: list = None, exclude: list = [], panel: str = '')
```

Link input sockets of the node

Allow to chain input sockets linking.

#### Arguments:
- **from_node** (_Node_ = None)
- **from_panel** (_str_ = )
- **include** (_list_ = None)
- **exclude** (_list_ = [])
- **panel** (_str_ = )

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Methods](core-socket.md#methods)</sub>

----------
### MenuSwitch()

> classmethod

``` python
MenuSwitch(named_sockets: dict = {}, default_menu: str = None, **sockets)
```

> Node [Menu Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/menu_switch.html)

The items of the Menu Switch node are provided in the 'items' dict.

#### Arguments:
- **named_sockets** (_dict_ = {}) : sockets to create
- **default_menu** (_str_ = None) : default menu value
- **sockets** (_dict_) : items



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Methods](core-socket.md#methods)</sub>

----------
### menu_switch()

> method

``` python
menu_switch(self_name: str = 'Self', named_sockets: dict = {}, default_menu: str = None, **sockets)
```

> Node [Menu Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/menu_switch.html)



Self is connected to the first menu item with the name provided as argument.

The items of the Menu Switch node are provided in the 'items' dict.
An group input socket named after the 'name' argument is linked to menu selector.

#### Arguments:
- **self_name** (_str_ = Self)
- **named_sockets** (_dict_ = {}) : sockets to create
- **default_menu** (_str_ = None) : default menu value
- **sockets** (_dict_) : items



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Methods](core-socket.md#methods)</sub>

----------
### Named()

> classmethod

``` python
Named(name)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **name** (_String_) : socket 'Name' (id: Name)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Methods](core-socket.md#methods)</sub>

----------
### NewInput()

> classmethod

``` python
NewInput(name: str, value=None, tip: str = '', panel: str = '', **props)
```

Create an new input socket

> [!NOTE]
> The "input" socket here is an "output" socket of the current input node

To get an existing input socket use Input.

#### Raises:
- **NodeError** : 



#### Arguments:
- **name** (_str_) : socket name
- **value** (_Any_ = None) : default_value
- **tip** (_str_ = )
- **panel** (_str_ = ) : panel name
- **props**



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Methods](core-socket.md#methods)</sub>

----------
### out()

> method

``` python
out(name: str = None, panel: str = '', **props)
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
- **panel** (_str_ = )
- **props**



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Methods](core-socket.md#methods)</sub>

----------
### repeat()

> method

``` python
repeat(iterations=1, named_sockets: dict = {}, **sockets)
```

Repeat zone

#### Arguments:
- **iterations** ( = 1)
- **named_sockets** (_dict_ = {})
- **sockets** (_dict_) : other sockets



#### Returns:
- **ZoneIterator** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Methods](core-socket.md#methods)</sub>

----------
### simulation()

> method

``` python
simulation(named_sockets: dict = {}, **sockets)
```

Simulation zone

#### Arguments:
- **named_sockets** (_dict_ = {})
- **sockets** (_dict_) : other sockets



#### Returns:
- **ZoneIterator** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Methods](core-socket.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Methods](core-socket.md#methods)</sub>

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

    choice = Boolean(True, "Use Sphere")

    # Two possible geometries
    cube   = Mesh.Cube()
    sphere = Mesh.IcoSphere()

    # Select
    geo = cube.switch(choice, sphere)

    # To group output
    geo.out()
```

#### Information:
- **Socket** : self



#### Arguments:
- **condition** (_Boolean_ = None) : socket 'Switch' (Switch)
- **true** ( = None) : socket 'True' (True)



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Methods](core-socket.md#methods)</sub>

----------
### switch_false()

> method

``` python
switch_false(condition=None, false=None)
```

> Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)



Self is connected to 'true' socket.

> [!IMPORTANT]
> This methods behaves the inverse of [switch](core-socket.md#switch) : self is connected to "True" socket and  the argument to "False", socket

> [!NOTE]
> This method is mainly provided to cover the case when 'False' socket is None

``` python
with GeoNodes("Switch demo"):

    geo = Geometry()

    show_geometry = Boolean(False, "Merge with Cube")

    cube = Mesh.Cube()

    geo += cube.switch_false(show_geometry)

    # Is equivalent to
    geo += Geometry.Switch(show_geometry, None, cube)

    # To group output
    geo.out()
```

> [!NOTE]
> This method let self socket unchanged. To set self socket to the result

#### Information:
- **Socket** : self



#### Arguments:
- **condition** (_Boolean_ = None) : socket 'Switch' (Switch)
- **false** ( = None) : socket 'False' (False)



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](core-socket.md#socket) :black_small_square: [Content](core-socket.md#content) :black_small_square: [Methods](core-socket.md#methods)</sub>