# Modifiers and Groups

## Function builders and packages

Use `group`, `modifier`, `tool`, `shader_group`, or `shader` to build
a tree inside a function with its own local variables. Options such as `prefix`
and `color_tag` belong to the decorator; `is_group` is set by the
decorator type. Use `.build()` to construct the tree. Calling the decorated
object inside another tree inserts a Group node and connects its input sockets,
using the same implementation and return convention as `G()`.

The tree name is optional: `@group()` on `def my_group()` creates **My Group**.
A leading underscore creates a leading dot: `_extract_items` becomes
**.Extract Items**. An explicit name, such as `@group("My /// ?? Name")`,
is preserved exactly. This convention applies to all five decorators, including
their package variants.

`group` creates a Geometry Nodes group, `modifier` creates a modifier, `tool`
creates a Geometry Nodes tool, `shader` creates a material, and `shader_group`
creates a reusable shader group. A package can mix all five types.

Tool options are forwarded to `GeoNodes.Tool`, for example:

```python
from geonodes import tool

@tool("Edit Mesh", object_mode=False, edit_mode=True, mesh=True)
def edit_mesh():
    """Description displayed in a Comment node."""
    # Construct the tool here.

edit_mesh.build()
```

Use `@package.tool(...)` to register a tool in a package. Tools also support
the package/decorator name prefix and the usual rebuild policy. The old
decorator names have been replaced, without compatibility aliases.

A nonempty builder docstring creates a Comment node when its tree is built.
A `:color:` line sets the comment's custom color using the strings supported
by `kernel.colors`, such as `red`, `blue`, or `#405A80`; this metadata
line is removed from the displayed text. Without it, the default color is kept.
Invalid color directives raise a `ValueError`.
An optional `:width: 200` line sets the Comment node's width. The value must be
a positive finite number. This metadata is also removed from the displayed text;
without it, Blender's default width is kept.

`:horizontal:` accepts `outer_left`, `left`, `mid`, `right`, or `outer_right`;
`:vertical:` accepts `outer_top`, `top`, `mid`, `bottom`, or `outer_bottom`.
Docstring comments default to `left` and `outer_top`. These lines are removed
from the displayed text and stored as Blender custom properties
`arrange_horizontal` and `arrange_vertical`. Arrangement does not use these
hints yet; positioning will be implemented separately.

The same hints can be set on manually created nodes:

```python
nd.comment("Another comment")._set_arrange(horizontal="left", vertical="outer_top")
```

`Node._custom_property(name, value)` creates or updates any Blender custom
property. Both methods return the node for chaining. In `_set_arrange`, an
omitted axis (`None`) keeps its current value; invalid positions raise
`ValueError` before either axis is changed.

```python
@group("My Group")
def my_group():
    """
    :color: #405A80
    :width: 200
    :horizontal: left
    :vertical: outer_top

    Description of the group.
    """
    # Construct the group here.
```

A `Package` automatically registers its decorated functions, so a demo does not
need to maintain a separate list of calls:

### Static class packages

```python
from geonodes import Package, group, modifier, Mesh, Vector

class Project(Package):
    prefix = "Body"

    @group()
    def move(mesh: Mesh, position: Vector = (0, 0, 0)):
        mesh.set_position(offset=position).out()

    @modifier()
    def demo():
        Project.move(Mesh.Cube(), position=(1, 2, 3)).out()

Project.demo.build(full=True)
```

No instance, `self`, `cls`, or explicit `@staticmethod` is needed. Builders are
collected in declaration order. The class prefix only changes Blender names:
`Project.move` builds **Body Move**. Inherited builders receive their subclass's
prefix without changing the parent class. Python member names `_build`, `build`
and `prefix` are reserved for package control/configuration.

Function parameters are the Python signature of the input sockets. During a
build, they receive symbolic inputs. Socket classes (such as `Mesh`, `Vector`,
or `Float`) and Python types (`float`, `int`, `bool`, `str`) can be annotations;
otherwise a non-None default determines the type. A required input needs an
annotation. Positional-only and keyword-only parameters are supported; variadic
parameters are not. Outputs still use `.out()`.

Inside an active tree, both `Project.move(mesh, position=...)` and a free
decorated function call build a missing group before inserting its Group node.
The supplied arguments connect to sockets and are never used as build-time
Python options. Calling a builder outside a tree requires `.build()`.

| Call | Existing target | Existing dependencies |
| --- | --- | --- |
| `._build()` (internal) | Kept | Kept |
| `.build()` | Rebuilt | Kept |
| `.build(full=True)` | Rebuilt | Rebuilt once per operation |

`full` accepts only a boolean; strings and other types are rejected. Missing dependencies are
always built. Full mode propagates across free builders and different packages,
and dependency cycles raise an error. Build state is discarded after the
operation, including after failure.

`Project.build(full=False)` rebuilds all package members;
`Project.move.build(full=False)` targets one member. Pass `full=True` to include
dependencies. Internal `._build(rebuild=False, full=False)` builds missing trees.

### Instance registration

The existing registration syntax also remains available:

```python
from geonodes import Package, Mesh

furniture = Package("Furniture")

@furniture.group("Create Plank")
def create_plank():
    Mesh.Cube().out()

@furniture.modifier("Add Plank")
def add_plank():
    create_plank().out()

def demo():
    furniture.build()
```

Declare the package and builders at module level. Registration does not execute
the functions. `build()` invokes each builder's `.build()` in declaration order
and displays a package heading and final build statistics. Declare dependencies
before their callers. Construction functions should have no required Python
arguments when used in a package.

When a decorated group is called inside another tree and its Blender node group
is missing, it is built automatically before insertion. Its own missing
dependencies are built the same way. Existing groups are kept unchanged, even
outside a full rebuild operation. This allows a targeted
rebuild after unused groups have disappeared on reloading a `.blend` file.
Circular build dependencies raise an error. `G()` retains its existing behavior;
automatic construction requires the imported decorated builder.

Use `Package("Furniture", prefix="Furn")` to prefix all its tree names:
`Add Plank` becomes `Furn Add Plank`, and `.Extract Items` becomes
`.Furn Extract Items`. With the default `prefix=""`, names are unchanged.
Private names keep their leading dot before all prefixes: `_extract_items`
with package prefix `Furn` becomes `.Furn Extract Items`.
An additional decorator prefix is placed after the package prefix. Both
`.build()` and direct group calls use the same full name.

Registered builders are also accessible through their package using the
unprefixed tree name in snake_case. For example:

```python
from geonodes.demos.meshutil import ordered_selection

# Inside a tree: calls the Blender group "OSel Count".
count = ordered_selection.count(mesh)

# Outside a tree: rebuild just that group.
ordered_selection.count.build()
```

Likewise,
`ordered_selection.build()` forces a build of the entire package.

Use the package's declared Python name (`ordered_selection` or `curve_bones` in
`meshutil`); the prefix remains internal to its Blender tree names.

`build()` forces all registered trees to rebuild; `build(full=True)` also
rebuilds dependencies once per operation. Internally, `_build()` keeps existing
trees and creates missing ones. Both `rebuild` and `full` must be booleans.
To reconstruct just one tree, use `create_plank.build()`.
Arguments to a direct
call such as `create_plank(width=0.4)` are group input sockets. A prefixed group keeps its full
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


Materials created by shader builders store their root name in the custom property
`geonodes_api`. Unmarked materials are preserved; a new API material receives a
Blender suffix and is reused on later builds via its marker. Removing the marker
transfers ownership to the user. API material references by root name resolve to
the owned material, including its suffix.
