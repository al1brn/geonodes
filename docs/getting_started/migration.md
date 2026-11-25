# Migrating existing scripts

The function decorators provide a common way to declare modifiers, reusable
groups, tools, shader groups and materials. Explicit tree contexts are still
supported. You can migrate one tree at a time.

## From a tree context to a builder

Before:

```python
from geonodes import *

with GeoNodes("Shift Mesh", is_group=True):
    mesh = Mesh(name="Mesh")
    offset = Vector((0, 0, 1), name="Offset")
    mesh.set_position(offset=offset).out()
```

After:

```python
from geonodes import *

@group("Shift Mesh")
def shift_mesh(mesh: Mesh, offset: Vector = (0, 0, 1)):
    mesh.set_position(offset=offset).out()

shift_mesh.build()
```

Choose `@modifier()` for a modifier, `@tool()` for a tool,
`@shader_group()` for a shader group, or `@shader()` for a material. Move tree
options onto the decorator and remove `is_group`: the decorator sets it.

Parameter names become interface socket names. If an existing `.blend` relies
on exact names, panels, descriptions or limits, keep the explicit named socket
constructors in the builder instead of replacing them with function parameters.

## Separate construction from insertion

Use `shift_mesh.build()` to rebuild a definition outside a tree. Inside a tree,
`shift_mesh(mesh, offset=...)` inserts a Group node. Arguments connect sockets;
they do not rerun the builder with Python configuration values. Keep `.out()`
for Blender outputs; replacing it with `return` does not expose an output.

A direct call builds missing dependencies automatically. Use
`.build(full=True)` to also refresh existing dependencies after changing their
Python definitions. `.build(rebuild=True)` is not a supported signature.

`Group(...)` and `G()` remain useful for preexisting Blender groups. Calling an
imported decorated builder also knows how to construct its missing definition.

## Organize a collection

Collect related definitions in a [Package](packages.md). Class packages use
ordinary decorators and no `self` or `cls` parameter. Instance packages use
`@package.group(...)`, `@package.modifier(...)`, and the corresponding shader
and tool decorators. Both forms expose `.build()` and `.build(full=True)`.

## Shader scripts

Use `nd` inside both Geometry Nodes and Shader Nodes builders; the active tree
selects the node environment. New shader scripts should not depend on `snd`.

`Shader.out()` connects Surface, and `VolumeShader.out()` connects Volume in a
material. For the other material inputs, use
`Tree.current_tree().displacement = value` and
`Tree.current_tree().thickness = value`. In a shader group, `.out("Name")`
creates a group output instead. See [Shaders](shaders.md).

Set `@shader(target='CYCLES')` or `@shader(target='EEVEE')` for a material-specific
default target. The default is `'ALL'`. Explicit `set_*` calls can select a
different target when a material needs several output nodes.

## Version scope

These guides describe the current decorator API. The package selects the legacy
`core` for Blender 5.2.0 and `core_new` for other supported builds. Some additions,
including the material target option, require the current `core_new`; use a
matching Blender build and regenerated node API when following these examples.
