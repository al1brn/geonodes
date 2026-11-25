# Modifiers, groups and tools

Declare node trees with a decorated Python function. The decorator selects the
kind of tree and its options; the function constructs its nodes. Declaration
alone does not build anything in Blender.

| Decorator | Creates | Construction |
| --- | --- | --- |
| `@modifier()` | Geometry Nodes modifier tree | `.build()` |
| `@group()` | Reusable Geometry Nodes group | `.build()` or a call inside a tree |
| `@tool()` | Geometry Nodes tool | `.build()` |
| `@shader()` | Material | `.build()` |
| `@shader_group()` | Reusable shader group | `.build()` or a call inside a shader tree |

Use parentheses even when no options are needed: `@group()`, not `@group`.
See [Packages](packages.md) to organize related builders and
[Migration](migration.md) to convert scripts using explicit tree contexts.

## Declare a modifier

```python
from geonodes import *

@modifier("Move Geometry")
def move_geometry(geometry: Geometry, offset: Vector = (0, 0, 1)):
    """Move the input geometry by an adjustable offset."""
    geometry.set_position(offset=offset).out()

move_geometry.build()
```

Run the script in Blender, then select **Move Geometry** as the node group of a
Geometry Nodes modifier. Function parameters become Group Input sockets, so the
offset can be changed in the modifier interface. `.out()` connects the result to
Group Output. A Python `return` does not declare a Blender output.

The function runs inside an automatically managed tree context. Do not open
another `with GeoNodes(...)` inside the builder to create its own tree.

## Inputs and outputs

Annotations select socket types. You can use socket classes (`Mesh`, `Vector`,
`Float`, etc.) or the Python scalar types `float`, `int`, `bool` and `str`.
Without an annotation, a non-`None` default determines the socket type. A required
parameter needs an annotation. Defaults set Blender socket defaults.

```python
from geonodes import *

@group()
def add_values(a: float = 1.0, b: float = 2.0):
    (a + b).out("Sum")

@modifier()
def use_values():
    height = add_values(a=2.0, b=3.0)
    Mesh.Cube(size=(1, 1, height)).out()

use_values.build()
```

These arguments are symbolic sockets during construction, not ordinary Python
build-time settings. Use node operations for calculations depending on them.
Configure naming, target and tree options on the decorator. Keep other Python
construction settings in constants or in a factory that declares a builder.

Positional-only and keyword-only parameters are supported. `*args` and
`**kwargs` parameters on the construction function are not supported.
For interface details such as limits, descriptions and panels, create named
sockets explicitly inside the function; see [Creating Sockets](creating_sockets.md).

Declare each output with `.out("Name")`. Calling a decorated group uses the same
input binding and output convention as `G()`: the call returns the first output
socket, not the construction function's Python return value. Peer outputs can
be read from that result using their socket names in snake_case.

## Call a reusable group

Call the decorated builder inside another tree to insert a Group node:

```python
from geonodes import *

@group("Shift Mesh")
def shift_mesh(mesh: Mesh, offset: Vector = (0, 0, 0)):
    mesh.set_position(offset=offset).out()

@modifier("Shifted Cube")
def shifted_cube():
    shift_mesh(Mesh.Cube(), offset=(1, 2, 3)).out()

shifted_cube.build(full=True)
```

A missing group is built automatically before insertion. Existing dependencies
are reused unless `full=True` is requested. Import the decorated Python builder
to benefit from this behavior. `Group("Shift Mesh", ...)` and
`G().shift_mesh(...)` remain available for calling an already existing Blender
group by name; they cannot reconstruct a missing Python definition.

Calling a builder outside an active tree raises an error: use `.build()` there.
Material builders cannot be inserted as Group nodes; use their `.build()` method.
Modifiers and tools also expose the group-call interface, but prefer `@group()`
for trees intended to be reusable dependencies.

## Names and options

Without an explicit name, `def shift_mesh(...)` becomes **Shift Mesh**.
A leading underscore becomes a leading dot: `_shift_mesh` becomes
**.Shift Mesh**. An explicit decorator name is kept unchanged.

Options such as `prefix`, `fake_user` and `color_tag` are forwarded to the tree
constructor. `is_group` is selected by the decorator; do not pass it yourself.

```python
from geonodes import *

@group(prefix="Utils", color_tag='GEOMETRY')
def _cube():
    Mesh.Cube().out()

_cube.build()  # Blender name: .Utils Cube
```

## Rebuilding

| Operation | Selected tree | Dependencies |
| --- | --- | --- |
| `.build()` | Rebuilt | Existing trees reused; missing trees built |
| `.build(full=True)` | Rebuilt | Rebuilt once per build operation |
| Direct call inside a tree | Built if missing, then inserted | Existing trees reused |

`full` must be a boolean. Full builds propagate through dependencies in other
packages too. Circular dependencies raise an error. `.build()` does not accept
socket values or a `rebuild` argument: `builder.build(rebuild=True)` is invalid.
The internal `._build(rebuild=False, full=False)` creates missing trees while
preserving existing ones; normal scripts should use the public `.build()` API.

## Tools

```python
from geonodes import *

@tool("Edit Mesh", object_mode=False, edit_mode=True, mesh=True)
def edit_mesh(geometry: Geometry):
    geometry.set_position(offset=(0, 0, 1)).out()

edit_mesh.build()
```

Tool-specific options are forwarded to `GeoNodes.Tool`. A tool is configured for
Blender's tool workflow rather than the modifier stack.

## Documentation in the node editor

A nonempty function docstring creates a Comment node when the tree is built.
Optional directives configure that comment and are removed from its text:

```python
from geonodes import *

@group()
def documented_cube():
    """Create a unit cube.

    :color: #405A80
    :width: 240
    :horizontal: left
    :vertical: outer_top
    """
    Mesh.Cube().out()
```

Colors accept the names and hexadecimal strings supported by the API. Width
must be positive and finite. Horizontal hints are `outer_left`, `left`, `mid`,
`right`, `outer_right`; vertical hints are `outer_top`, `top`, `mid`, `bottom`,
`outer_bottom`. The defaults are `left` and `outer_top`. These hints are stored
as custom properties; they do not yet control automatic placement.

## Explicit tree contexts

`with GeoNodes(...)` and `with ShaderNodes(...)` remain available for scripts
that need direct control of tree construction. Most tutorials use decorators;
focused examples elsewhere may still use these equivalent contexts. A context
executes immediately, whereas a decorator waits for `.build()` or a group call.
