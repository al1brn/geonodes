# If

``` python
If(socket_class, selector, name='Menu', tip='')
```

Initialize If syntax mimicing

This class, together with [Else](else.md#else) and [Elif](elif.md#elif) classes, propose and alternative
to the naive implementation of nodes "Switch", "Index Switch", "Menu Switch".

Each class of the syntax mimicing set creats a syntaxic block into which one
can create the optional socket.

For instance, rather than writing:

``` python
condition = Boolean(True, "Cone")

geo = Geometry.Switch(condition, false=Mesh.Cube(), true=Mesh.Cone)
geo.out()
```

You can mimic if ... else ... syntax with:

``` python
condition = Boolean(True, "Cone")

with If(Geometry, condition) as geo:
    geo.option = Mesh.Cone()

with Else(geo):
    geo.option = Mesh.Cube()

geo.out()
```

### Comments

The first argument of ***If*** is the class you want. The second argument is a [Boolean](boolean.md#boolean).

> [!NOTE]
> The second argument can also be an Integer or a String to create a "Index Switch"
> or a "Menu Switch".

It returns the output socket of the "Switch" Node.
Note than the input sockets of node are not yet linked.
The link is performed by setting the property `geo.option`.

> [IMPORTANT]
> `option` property depends upon the context. In the ***If** block, it is
> the "True" input socket, in the ***Else*** block, it is the "False" input socket.

``` python
with If(Geometry, condition) as geo:
    geo.option = Mesh.Cone()
    # is equivalent to
    geo.node.true = Mesh.Cone()

with Else(geo):
    geo.option = Mesh.Cube()
    # is equivalent to
    geo.node.false = Mesh.Cube()
```

The ***Else** is initialized with a socket previously created with a **If**.

### Index Switch

"Index Switch" can be created by initializing ***If** with an [Integer](integer.md#integer) value rather
than a [Boolean](boolean.md#boolean).

The following code create a "Index Switch" node with 4 entries.

``` python
index = Integer(0, "Geometry Index")

with If(Geometry, index) as geo:
    geo.option = Mesh.Cube()

with Elif(geo):
    geo.option = Mesh.UVSphere()

with Elif(geo):
    geo.option = Mesh.IcoSphere()

with Elif(geo):
    geo.option = Mesh.Cone()

geo.out()
```

### Menu Switch

A "Menu Switch" works similarily by initializing the ***If*** with a ***python string**.

> [!IMPORTANT]
> The 'selector' argument is a a python string, not a [String](string.md#string). It is interpreted as the name
> of the first menu option.

Each ***Elif*** coming after takes a str "menu" argument as the name of the current entry.


``` python
with If(Geometry, "Cube", name="Pick Shape") as geo:
    # "Cube" is the name of the first option in the menu
    geo.option = Mesh.Cube()

with Elif(geo, "Sphere"):
    " "Sphere" is the name of the second option in the menu
    geo.option = Mesh.UVSphere()

with Elif(geo):
    # "C" will be the name of the third option in the menu
    geo.option = Mesh.IcoSphere()

with Elif(geo, "Cone):
    geo.option = Mesh.Cone()

geo.out()
```

> [!NOTE]
> Each block is put in a layout frame.

#### Raises:
- **NodeError** : 



#### Arguments:
- **socket_class** (_type_) : a class valid as input of the switch node
- **selector** (_Boolean, Integer or str_) : Boolean and Integer: socket used to select the option, str: name of the first option in the menu
- **name** (_str_ = Menu) : name of menu socket
- **tip** (_str_ = ) : user tip (used in menu creation and in Layout names)

### Inherited

[\_\_enter__](ifelse.md#__enter__) :black_small_square: [\_\_exit__](ifelse.md#__exit__) :black_small_square: [\_\_str__](ifelse.md#__str__) :black_small_square:

## Content

- [\_\_init__](if.md#__init__)
- [set_option](if.md#set_option)

## Methods



----------
### \_\_init__()

> method

``` python
__init__(socket_class, selector, name='Menu', tip='')
```

Initialize If syntax mimicing

This class, together with [Else](else.md#else) and [Elif](elif.md#elif) classes, propose and alternative
to the naive implementation of nodes "Switch", "Index Switch", "Menu Switch".

Each class of the syntax mimicing set creats a syntaxic block into which one
can create the optional socket.

For instance, rather than writing:

``` python
condition = Boolean(True, "Cone")

geo = Geometry.Switch(condition, false=Mesh.Cube(), true=Mesh.Cone)
geo.out()
```

You can mimic if ... else ... syntax with:

``` python
condition = Boolean(True, "Cone")

with If(Geometry, condition) as geo:
    geo.option = Mesh.Cone()

with Else(geo):
    geo.option = Mesh.Cube()

geo.out()
```

### Comments

The first argument of ***If*** is the class you want. The second argument is a [Boolean](boolean.md#boolean).

> [!NOTE]
> The second argument can also be an Integer or a String to create a "Index Switch"
> or a "Menu Switch".

It returns the output socket of the "Switch" Node.
Note than the input sockets of node are not yet linked.
The link is performed by setting the property `geo.option`.

> [IMPORTANT]
> `option` property depends upon the context. In the ***If** block, it is
> the "True" input socket, in the ***Else*** block, it is the "False" input socket.

``` python
with If(Geometry, condition) as geo:
    geo.option = Mesh.Cone()
    # is equivalent to
    geo.node.true = Mesh.Cone()

with Else(geo):
    geo.option = Mesh.Cube()
    # is equivalent to
    geo.node.false = Mesh.Cube()
```

The ***Else** is initialized with a socket previously created with a **If**.

### Index Switch

"Index Switch" can be created by initializing ***If** with an [Integer](integer.md#integer) value rather
than a [Boolean](boolean.md#boolean).

The following code create a "Index Switch" node with 4 entries.

``` python
index = Integer(0, "Geometry Index")

with If(Geometry, index) as geo:
    geo.option = Mesh.Cube()

with Elif(geo):
    geo.option = Mesh.UVSphere()

with Elif(geo):
    geo.option = Mesh.IcoSphere()

with Elif(geo):
    geo.option = Mesh.Cone()

geo.out()
```

### Menu Switch

A "Menu Switch" works similarily by initializing the ***If*** with a ***python string**.

> [!IMPORTANT]
> The 'selector' argument is a a python string, not a [String](string.md#string). It is interpreted as the name
> of the first menu option.

Each ***Elif*** coming after takes a str "menu" argument as the name of the current entry.


``` python
with If(Geometry, "Cube", name="Pick Shape") as geo:
    # "Cube" is the name of the first option in the menu
    geo.option = Mesh.Cube()

with Elif(geo, "Sphere"):
    " "Sphere" is the name of the second option in the menu
    geo.option = Mesh.UVSphere()

with Elif(geo):
    # "C" will be the name of the third option in the menu
    geo.option = Mesh.IcoSphere()

with Elif(geo, "Cone):
    geo.option = Mesh.Cone()

geo.out()
```

> [!NOTE]
> Each block is put in a layout frame.

#### Raises:
- **NodeError** : 



#### Arguments:
- **socket_class** (_type_) : a class valid as input of the switch node
- **selector** (_Boolean, Integer or str_) : Boolean and Integer: socket used to select the option, str: name of the first option in the menu
- **name** (_str_ = Menu) : name of menu socket
- **tip** (_str_ = ) : user tip (used in menu creation and in Layout names)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [If](if.md#if) :black_small_square: [Content](if.md#content) :black_small_square: [Methods](if.md#methods)</sub>

----------
### set_option()

> method

``` python
set_option(socket)
```

Implements socket.option property

#### Arguments:
- **socket** (_Socket_) : socket to plug in the current option

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [If](if.md#if) :black_small_square: [Content](if.md#content) :black_small_square: [Methods](if.md#methods)</sub>