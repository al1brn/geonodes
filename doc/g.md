# G

``` python
G(prefix: str = '', verbose: bool = False)
```

Group functional call

This class is provided to expose ***Group*** nodes as functions with keyword arguments.
When a Group named "Do Something" is created, it can be called with two syntaxes:
- Using `Group` node: `node = Group("Do Something", ...)`
- Using `G` function with the snake case name : `node = G().do_someting(...)`

This facility can be particularilty usedful for projects with a lot of groups. The groups
can be grouped by prefixes. The prefixes are hidden in the code.


``` python

from geonodes import GeoNodes, Geometry, Float, Mesh, G

with GeoNodes("Do Something", is_group=True, prefix="Utils"):
    
    g = Geometry()
    a = Float(3.14, "Pi")
    b = Float(6.28, "Tau")
    g += Mesh.Cube()
    
    g = Mesh(g)
    g.points.Pi = a + b
    
    g.out()

    a.out("Pi")
    
with GeoNodes("Do Something Else", is_group=True, prefix="Utils"):
    
    g = Geometry()
    a = Float(3.14, "Pi")
    b = Float(6.28, "Tau")
    g += Mesh.Cube()
    
    g = Mesh(g)
    g.points.Pi = a + b
    
    g.out()
    
with GeoNodes("Calling Groups"):

    utils = G("Utils")
    
    g = utils.do_something(Geometry(), pi=6.28)
    g = utils.do_something_else(g, g.pi, tau=7)
    g.out()   
```

#### Arguments:
- **prefix** (_str_ = ) : prefix to use when searching a tree
- **verbose** (_bool_ = False)

## Content

- [build_function](g.md#build_function)
- [error](g.md#error)
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
### error()

> method

``` python
error(f, exception=None)
```

Raise an error when function call fails.

#### Raises:
- **NodeError** : 



#### Arguments:
- **f** (_function_) : the function in error
- **exception** (_Exception_ = None) : the exception that was raised

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [G](g.md#g) :black_small_square: [Content](g.md#content) :black_small_square: [Methods](g.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(prefix: str = '', verbose: bool = False)
```

Group functional call

This class is provided to expose ***Group*** nodes as functions with keyword arguments.
When a Group named "Do Something" is created, it can be called with two syntaxes:
- Using `Group` node: `node = Group("Do Something", ...)`
- Using `G` function with the snake case name : `node = G().do_someting(...)`

This facility can be particularilty usedful for projects with a lot of groups. The groups
can be grouped by prefixes. The prefixes are hidden in the code.


``` python

from geonodes import GeoNodes, Geometry, Float, Mesh, G

with GeoNodes("Do Something", is_group=True, prefix="Utils"):
    
    g = Geometry()
    a = Float(3.14, "Pi")
    b = Float(6.28, "Tau")
    g += Mesh.Cube()
    
    g = Mesh(g)
    g.points.Pi = a + b
    
    g.out()

    a.out("Pi")
    
with GeoNodes("Do Something Else", is_group=True, prefix="Utils"):
    
    g = Geometry()
    a = Float(3.14, "Pi")
    b = Float(6.28, "Tau")
    g += Mesh.Cube()
    
    g = Mesh(g)
    g.points.Pi = a + b
    
    g.out()
    
with GeoNodes("Calling Groups"):

    utils = G("Utils")
    
    g = utils.do_something(Geometry(), pi=6.28)
    g = utils.do_something_else(g, g.pi, tau=7)
    g.out()   
```

#### Arguments:
- **prefix** (_str_ = ) : prefix to use when searching a tree
- **verbose** (_bool_ = False)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [G](g.md#g) :black_small_square: [Content](g.md#content) :black_small_square: [Methods](g.md#methods)</sub>