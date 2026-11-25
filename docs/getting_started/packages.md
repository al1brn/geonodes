# Packages

A `Package` organizes related groups, modifiers, tools and materials. It registers
builders without executing them, supports building one member or the complete
package, and gives its trees a shared Blender name prefix.

## Declare a class package

```python
from geonodes import *

class Project(Package):
    prefix = "Project"

    @group()
    def shift(mesh: Mesh, offset: Vector = (0, 0, 0)):
        mesh.set_position(offset=offset).out()

    @modifier()
    def shifted_cube():
        Project.shift(Mesh.Cube(), offset=(1, 2, 3)).out()

    @shader(target='CYCLES')
    def blue():
        Shader.Principled(base_color=(0.1, 0.2, 0.8)).out()

Project.build(full=True)
```

No instance, `self`, `cls`, `@classmethod` or `@staticmethod` is needed for
builders. Declare them directly in the class using the ordinary decorators.
All five decorators are supported, including `@tool()` and `@shader_group()`.

The prefix affects Blender names, not Python member access:
`Project.shift` creates **Project Shift**. Use `Project.shift(...)` inside an
active tree and `Project.shift.build()` outside one. A decorated material such
as `Project.blue` supports construction with `.build()`, not node insertion.

## Build one member or the whole package

```python
Project.shifted_cube.build()           # Rebuild one modifier
Project.shifted_cube.build(full=True)  # Rebuild it and its dependencies
Project.build()                        # Rebuild every registered member
Project.build(full=True)               # Include dependencies, once each
```

Package members are collected in declaration order. Missing dependencies are
built on demand. Existing dependencies outside the selected members are kept
unless `full=True` is used. Rebuilding a package does not apply its modifiers to
objects or assign its materials automatically.

Parameters on construction functions declare input sockets, including required
annotated parameters. They do not become required Python arguments to
`Package.build()`. The methods `build` and `_build`, and the name `prefix`, are
reserved for package control and configuration.

## Naming and inheritance

A decorator's optional prefix follows the package prefix. Leading-dot names
stay private in Blender's name lists: `_helper` in a package with prefix
`Project` becomes **.Project Helper**.

A subclass inherits its parent's builders and applies its own package prefix
without changing the parent. Calls written explicitly as `Parent.helper(...)`
continue to refer to the parent builder; use the intended package name in
construction functions when selecting dependencies.

```python
from geonodes import *

class Primitives(Package):
    prefix = "Primitives"

    @group()
    def cube():
        Mesh.Cube().out()

class Preview(Primitives):
    prefix = "Preview"

Preview.cube.build()  # Builds Preview Cube; Primitives Cube is unchanged
```

## Register on an instance

The instance registration API is also supported, especially for collections
assembled across module-level declarations:

```python
from geonodes import *

furniture = Package("Furniture", prefix="Furn")

@furniture.group("Create Plank")
def create_plank(width: float = 0.4):
    Mesh.Cube(size=(width, 1, 0.02)).out()

@furniture.modifier("Add Plank")
def add_plank():
    create_plank(width=0.6).out()

furniture.build(full=True)
```

Here **Furniture** labels the package's build statistics; `prefix="Furn"`
controls Blender tree names. Without a prefix, the names are **Create Plank**
and **Add Plank**. Declare the package and its registrations at module level.

Registered members are also accessible through the instance using the
unprefixed tree name converted to snake_case:

```python
furniture.create_plank.build()
furniture.add_plank.build(full=True)
```

Both forms share the registered builder: `create_plank` and
`furniture.create_plank`. To reuse it from another module, import the builder or
the package instance and call it inside a tree. Prefixes stay internal to
Blender names; callers should not reconstruct names manually.

See [Modifiers, groups and tools](modifiers_groups.md) for socket signatures,
output conventions, naming and dependency rebuild rules.
