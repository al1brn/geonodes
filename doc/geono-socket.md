# Socket

``` python
Socket(socket)
```

Socket documentation

#### Arguments:
- **socket**

## Content

- **B** : [blur](geono-socket.md#blur)
- **I** : [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch)
- **L** : [\_lc](geono-socket.md#_lc)
- **M** : [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch)
- **N** : [node](geono-socket.md#node)
- **O** : [out](geono-socket.md#out)
- **S** : [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch)
- **T** : [to_output](geono-socket.md#to_output)

## Properties



### node

> _type_: **Node**
>

Returns the node owning the socket.

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](geono-socket.md#socket) :black_small_square: [Content](geono-socket.md#content) :black_small_square: [Properties](geono-socket.md#properties)</sub>

## Methods



----------
### blur()

> method

``` python
blur(iterations=None, weight=None)
```

ERROR: Node 'Blur Attribute' not found

ERROR: Node 'Blur Attribute' not found

#### Arguments:
- **iterations** (_Integer_ = None) : socket 'Iterations' (Iterations)
- **weight** (_Float_ = None) : socket 'Weight' (Weight)



#### Returns:
- **value** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](geono-socket.md#socket) :black_small_square: [Content](geono-socket.md#content) :black_small_square: [Methods](geono-socket.md#methods)</sub>

----------
### IndexSwitch()

> classmethod

``` python
IndexSwitch(*values, index=0)
```

ERROR: Node 'Index Switch' not found

ERROR: Node 'Index Switch' not found

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](geono-socket.md#socket) :black_small_square: [Content](geono-socket.md#content) :black_small_square: [Methods](geono-socket.md#methods)</sub>

----------
### index_switch()

> method

``` python
index_switch(*values, index=0)
```

ERROR: Node 'Index Switch' not found

ERROR: Node 'Index Switch' not found

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
- **output** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](geono-socket.md#socket) :black_small_square: [Content](geono-socket.md#content) :black_small_square: [Methods](geono-socket.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](geono-socket.md#socket) :black_small_square: [Content](geono-socket.md#content) :black_small_square: [Methods](geono-socket.md#methods)</sub>

----------
### MenuSwitch()

> classmethod

``` python
MenuSwitch(items={'A': None, 'B': None}, menu=0, name='Menu', tip=None)
```

ERROR: Node 'Menu Switch' not found

ERROR: Node 'Menu Switch' not found

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
- **output** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](geono-socket.md#socket) :black_small_square: [Content](geono-socket.md#content) :black_small_square: [Methods](geono-socket.md#methods)</sub>

----------
### menu_switch()

> method

``` python
menu_switch(self_name='A', items={'B': None}, menu=0, name='Menu', tip=None)
```

ERROR: Node 'Menu Switch' not found

ERROR: Node 'Menu Switch' not found

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
- **output** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](geono-socket.md#socket) :black_small_square: [Content](geono-socket.md#content) :black_small_square: [Methods](geono-socket.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](geono-socket.md#socket) :black_small_square: [Content](geono-socket.md#content) :black_small_square: [Methods](geono-socket.md#methods)</sub>

----------
### Switch()

> classmethod

``` python
Switch(condition=None, false=None, true=None)
```

ERROR: Node 'Switch' not found

ERROR: Node 'Switch' not found

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](geono-socket.md#socket) :black_small_square: [Content](geono-socket.md#content) :black_small_square: [Methods](geono-socket.md#methods)</sub>

----------
### switch()

> method

``` python
switch(condition=None, true=None)
```

ERROR: Node 'Switch' not found

ERROR: Node 'Switch' not found

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
- **output** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](geono-socket.md#socket) :black_small_square: [Content](geono-socket.md#content) :black_small_square: [Methods](geono-socket.md#methods)</sub>

----------
### to_output()

> method

``` python
to_output(name=None)
```

Plug a socket to an output socket.

#### Arguments:
- **name** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Socket](geono-socket.md#socket) :black_small_square: [Content](geono-socket.md#content) :black_small_square: [Methods](geono-socket.md#methods)</sub>