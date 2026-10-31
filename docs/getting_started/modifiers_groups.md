# Modifiers and Groups

## Function builders and packages

Use `geo_group`, `geo_modifier`, `shader_group`, or `shader_material` to build
a tree inside a function with its own local variables. Options such as `prefix`,
`rebuild`, and `color_tag` belong to the decorator; `is_group` is set by the
decorator type. Use `.build()` to construct the tree. Calling the decorated
object inside another tree inserts a Group node and connects its input sockets,
using the same implementation and return convention as `G()`.

The tree name is optional: `@geo_group()` on `def my_group()` creates **My Group**.
A leading underscore creates a leading dot: `_extract_items` becomes
**.Extract Items**. An explicit name, such as `@geo_group("My /// ?? Name")`,
is preserved exactly. This convention applies to all four decorators, including
their package variants.

A `Package` automatically registers its decorated functions, so a demo does not
need to maintain a separate list of calls:

```python
from geonodes import Package, Mesh

furniture = Package("Furniture")

@furniture.geo_group("Create Plank")
def create_plank():
    Mesh.Cube().out()

@furniture.geo_modifier("Add Plank")
def add_plank():
    create_plank().out()

def demo(rebuild=False):
    furniture.build(rebuild=rebuild)
```

Declare the package and builders at module level. Registration does not execute
the functions. `build()` invokes each builder's `.build()` in declaration order
and displays a package heading and final build statistics. Declare dependencies
before their callers. Construction functions should have no required Python
arguments when used in a package.

When a decorated group is called inside another tree and its Blender node group
is missing, it is built automatically before insertion. Its own missing
dependencies are built the same way. Existing groups are kept unchanged, even
when the decorator's default rebuild policy is True. This allows a targeted
rebuild after unused groups have disappeared on reloading a `.blend` file.
Circular build dependencies raise an error. `G()` retains its existing behavior;
automatic construction requires the imported decorated builder.

Use `Package("Furniture", prefix="Furn")` to prefix all its tree names:
`Add Plank` becomes `Furn Add Plank`, and `.Extract Items` becomes
`Furn .Extract Items`. With the default `prefix=""`, names are unchanged.
An additional decorator prefix is placed after the package prefix. Both
`.build()` and direct group calls use the same full name.

Registered builders are also accessible through their package using the
unprefixed tree name in snake_case. For example:

```python
from geonodes.demos.meshutil import ordered_selection

# Inside a tree: calls the Blender group "OSel Count".
count = ordered_selection.count(mesh)

# Outside a tree: rebuild just that group.
ordered_selection.count.build(rebuild=True)
```

`ordered_selection.count.rebuild()` is a shortcut for
`ordered_selection.count.build(rebuild=True)`. Likewise,
`ordered_selection.rebuild()` forces a build of the entire package.

Use the package's declared Python name (`ordered_selection` or `curve_bones` in
`meshutil`); the prefix remains internal to its Blender tree names.

`build(rebuild=True)` forces all trees to rebuild; `build(rebuild=False)` keeps
existing trees and creates missing ones. With no override (`rebuild=None`), each
decorator retains its own policy. For materials, `rebuild` controls
`replace_material`. To reconstruct just one tree, use
`create_plank.build(rebuild=True)`, without building the rest of the package.
Arguments to `.build()` are Python construction parameters; arguments to a direct
call such as `create_plank(width=0.4)` are group input sockets. The construction
function is not executed by this group call. A prefixed group keeps its full
Blender name when called from another module. Materials expose `.build()` only,
because a material cannot be inserted as a Group node.

## Creating a Group

When creating a new tree, the argument **is_group** is used to specify to create a **group of nodes** rather
than a **modifier**:

``` python
with GeoNodes("A Function", is_group=True):

    a = Float(name="Value 1")
    b = Float(name="Value 2")

    (a + b).out("Sum")
```

This creates the following group:

<img src="doc/images/group_sample.png" width="300" class="center">

## Calling a Group

Calling a group is made by instantiating a **Group** class.
The first parameter of the **Group** instantiation is the name of the _Group_ to call.
The sockets to plug th the input sockets of the group can be passed in two ways:
- as a dict
- as keyword arguments using their _snake_case_ name

The output sockets of the group are read as properties of the **Group** instance,
using their _snake_case_ name.


``` python
from geonodes import *

with GeoNodes("A Function", is_group=True):
    (Float(0, "Value 1") + Float(0, "Value 2")).out("Sum")

with GeoNodes("A Function is called"):

    a, b = 1, 2

    # ---------------------------------------------------------------------------
    # Standard method
    # ---------------------------------------------------------------------------

    # dict syntax

    val1 = Group("A Function", {'Value 1': a, 'Value 2': b}).sum

    # snake_case syntax

    val2 = Group("A Function", value_1=a, value_2=b).sum

    # ---------------------------------------------------------------------------
    # Alternative method
    # ---------------------------------------------------------------------------
    
    # For big projects, one can prefer the python syntax
    # Class G makes it possible

    val3 = G().a_function(val1, val2)
    
    geo = Geometry()
    geo.offset = (val1, val2, val3)
    geo.out()        
```

