# G

``` python
G(prefix: str = '', verbose: bool = False)
```

Group functional call

This class is provided to expose ***Group*** nodes as functions with keyword arguments.

For instance, let's create a group with 3 input sockets named `Geometry`, `Position` and `Parameter` in
this order:


``` python
with GeoNodes("Deform Function"):
    geo = Geometry()
    pos = Vector.Position()
    param = Float(0, "Parameter")
    # ...
    geo.out()
```

To use this group in another tree, you can write:

``` python
with GeoNodes("Modifier"):

    node = Group("Deform Function", {'geometry': Mesh.Cube(), 'position': (1, 2, 3), 'parameter': 3.14})

    # or

    node = Group("Deform Function", geometry=Mesh.Cube(), position = nd.position, parameter = 3.14)
```

The clas G provides a functional interface for the node. You simply use the snake case version
of the node name:

``` python
my_geo = G().deform_function(Mesh.Cube(), position=nd.position, parameter=3.14)

# NOTE: the first output socket is returned
# If you need the node, simply use:

node = my_geo.node
```

As for any function or method, you can omit the argument names if you are sure of the order of the
sockets. This is for instance the case for the `Geometry` socket which remains the first.

#### Prefixes

In big projects, you may want to prefix your groups and modifiers to structure them.
The ***G*** class accepts prefix and use it to build the full name of the tree you are looking for.

The code above could be replaced by:

``` python
my_geo = G("Deform").function(Mesh.Cube(), position=nd.position, parameter=3.14)
```

This allows to regroup modifiers of the same family in a kind of meta class:

``` python
# Prefix for deform modifiers
deform = Group("Deform")

with Group("Function 1", prefix=deform):
    pass

with Group("Function 2", prefix=deform):
    pass

with Group("Function 3", prefix=deform):
    pass

with Group("Main"):

    geo = Geometry()
    geo = deform.function_1(geo)
    geo = deform.function_2(geo)
    geo = deform.function_3(geo)

    geo.out()
```

#### Arguments:
- **prefix** (_str_ = ) : prefix to use when searching a tree
- **verbose** (_bool_ = False) : print the function header in the console

## Content

- [build_function](g.md#build_function)
- [\_\_init__](g.md#__init__)

## Methods



----------
### build_function()

> method

``` python
build_function(btree)
```

Dynamically create a function to call the tree as Group

The name of the function is the snake case version of the tree name.

#### Arguments:
- **btree** (_Blender GeometryNodeTree | ShaderNodeTree_) : the tree



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [G](g.md#g) :black_small_square: [Content](g.md#content) :black_small_square: [Methods](g.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(prefix: str = '', verbose: bool = False)
```

Group functional call

This class is provided to expose ***Group*** nodes as functions with keyword arguments.

For instance, let's create a group with 3 input sockets named `Geometry`, `Position` and `Parameter` in
this order:


``` python
with GeoNodes("Deform Function"):
    geo = Geometry()
    pos = Vector.Position()
    param = Float(0, "Parameter")
    # ...
    geo.out()
```

To use this group in another tree, you can write:

``` python
with GeoNodes("Modifier"):

    node = Group("Deform Function", {'geometry': Mesh.Cube(), 'position': (1, 2, 3), 'parameter': 3.14})

    # or

    node = Group("Deform Function", geometry=Mesh.Cube(), position = nd.position, parameter = 3.14)
```

The clas G provides a functional interface for the node. You simply use the snake case version
of the node name:

``` python
my_geo = G().deform_function(Mesh.Cube(), position=nd.position, parameter=3.14)

# NOTE: the first output socket is returned
# If you need the node, simply use:

node = my_geo.node
```

As for any function or method, you can omit the argument names if you are sure of the order of the
sockets. This is for instance the case for the `Geometry` socket which remains the first.

#### Prefixes

In big projects, you may want to prefix your groups and modifiers to structure them.
The ***G*** class accepts prefix and use it to build the full name of the tree you are looking for.

The code above could be replaced by:

``` python
my_geo = G("Deform").function(Mesh.Cube(), position=nd.position, parameter=3.14)
```

This allows to regroup modifiers of the same family in a kind of meta class:

``` python
# Prefix for deform modifiers
deform = Group("Deform")

with Group("Function 1", prefix=deform):
    pass

with Group("Function 2", prefix=deform):
    pass

with Group("Function 3", prefix=deform):
    pass

with Group("Main"):

    geo = Geometry()
    geo = deform.function_1(geo)
    geo = deform.function_2(geo)
    geo = deform.function_3(geo)

    geo.out()
```

#### Arguments:
- **prefix** (_str_ = ) : prefix to use when searching a tree
- **verbose** (_bool_ = False) : print the function header in the console

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [G](g.md#g) :black_small_square: [Content](g.md#content) :black_small_square: [Methods](g.md#methods)</sub>