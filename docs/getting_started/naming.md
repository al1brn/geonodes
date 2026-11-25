# Naming conventions

## Builders and Blender names

Decorators use an optional explicit Blender name. Without one, the Python
function name is converted to title case: `shift_mesh` becomes **Shift Mesh**.
A leading underscore becomes a leading dot: `_helper` becomes **.Helper**.
Explicit names are preserved. These rules apply to all five decorators and
[Packages](packages.md).

```python
from geonodes import *

@group(prefix="Utils")
def _shift_mesh(mesh: Mesh, offset: Vector = (0, 0, 0)):
    mesh.set_position(offset=offset).out()

_shift_mesh.build()  # .Utils Shift Mesh
```

The Python name stays `_shift_mesh`; callers do not need the Blender prefix.
Function parameter names define input socket names. Use explicit named socket
constructors when an interface must retain exact display names or panels.

## Node methods

Node operations generally use snake_case, such as `mesh.set_position(...)`.
Constructors use CamelCase, such as `Mesh.Cube()` and `Curve.Circle()`.
Redundant type names are often removed: **Curve to Mesh** becomes
`curve.to_mesh(...)`, and **Mesh Line** becomes `Mesh.Line(...)`.

```python
from geonodes import *

@modifier()
def naming_example():
    cube = Mesh.Cube()
    cube.set_position(offset=(1, 2, 3))
    cube.out()

naming_example.build()
```

These conventions are a guide, not a promise that every possible abbreviated
name exists. Check the [cross reference](../api/cross_reference.md), generated
signatures or Node Help for the exact method names supported by your Blender
version. Shader nodes have a [separate cross reference](../api/shader_cross_reference.md).

## Geometry classes and domains

`Mesh`, `Curve`, `Cloud`, `Instances`, `Volume` and `GreasePencil` specialize
`Geometry`. They inherit common geometry operations and add their own nodes.
Domain-specific operations are available through properties such as
`mesh.points`, `mesh.edges`, `mesh.faces`, `curve.points` and `curve.splines`.

Selections use domain indexing, for example
`mesh.faces[selection].store_named_attribute("Weight", value)`.
A domain method selects the Blender domain for you. Where a method computes its
data type from a value, you do not need to pass a separate `data_type` argument.
The exact behavior is documented in each method's signature.

## Arguments

Socket names normally become snake_case arguments: **Base Color** becomes
`base_color`, and **Instance Index** becomes `instance_index`. Blender node
parameters retain their Python names, such as `operation` and `blend_type`.

Prefer keyword arguments for node calls with many inputs. Parameter enum values
are case-sensitive Blender identifiers; use the values documented in the
signature rather than guessing them from UI labels. Some operations have
convenience variants, but not every enum value has a separate method.

## Outputs and peer sockets

Most node methods return their first output socket. Additional output sockets
can be accessed through their snake_case names on the result, or through its
`.node`. Geometry methods that jump to the result keep the geometry object and
make the node's other outputs accessible from it. Some methods explicitly
return a `Node`; check their return documentation.

A decorated group call follows the `G()` convention and returns its first
output socket. The builder's Python `return` does not define Blender outputs:
use `.out("Name")` for each output.

## Properties and named attributes

Properties can provide concise forms of node operations, such as
`mesh.position = value` and `mesh.offset = value`. Named attributes can be read
with `Float.Named("Weight")` or `Float("Weight")`. For storing attributes, use
an explicit domain operation such as
`mesh.points.store_named_attribute("Weight", value)`.

## Active node environment

`nd`, `gnmath` and public socket constructors select the active tree environment.
Use the same `nd` in Geometry Nodes and shader builders; a separate `snd` import
is not required by the current API. See [Shaders](shaders.md).
