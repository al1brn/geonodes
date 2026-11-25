# Builders and packages

Import builders from the public API:

```python
from geonodes import group, modifier, tool, shader_group, shader, Package
```

| Declaration | Result | Main options |
| --- | --- | --- |
| `@group(name=None, **options)` | Geometry Nodes group | `prefix`, `color_tag`, `fake_user` |
| `@modifier(name=None, **options)` | Modifier tree | `prefix`, `color_tag`, `fake_user` |
| `@tool(name=None, **options)` | Geometry Nodes tool | Options of `GeoNodes.Tool` |
| `@shader_group(name=None, **options)` | Shader group | `prefix`, `color_tag`, `fake_user` |
| `@shader(name=None, target='ALL', **options)` | Material | `target`, `prefix`, `fake_user` |

Declare the function with parentheses on the decorator. An omitted name is
derived from the function name. Options are forwarded to the corresponding
tree constructor; `is_group` is supplied by the decorator. Material targets are
`ALL`, `EEVEE` and `CYCLES`.

## Builder interface

- `builder.build(full=False)` reconstructs the selected tree. With `full=True`,
  dependencies are reconstructed once in the operation.
- `builder(*args, **kwargs)` inserts a Group node inside an active tree and
  creates a missing definition. Arguments are socket connections. The return
  value follows `G()` and is the first output socket. Material builders reject
  this form; call `.build()` instead.
- `builder.full_name` is the complete Blender name, including prefixes.

Function parameters declare symbolic inputs. Required parameters need type
annotations; otherwise a non-`None` default can infer the type. Use `.out()` to
declare outputs. `.build()` takes no socket arguments and no `rebuild` argument.

## Package interface

Declare a subclass of `Package`, set its optional `prefix`, and add ordinary
decorated functions without `self` or `cls`. `Project.build(full=False)`
reconstructs every member; `Project.member.build()` reconstructs one member.
`full=True` includes dependencies. Inherited builders receive the subclass's
prefix. `build`, `_build` and `prefix` are reserved names.

Alternatively use `package = Package(name, prefix="")` and register functions
with `@package.group(...)`, `@package.modifier(...)`, `@package.tool(...)`,
`@package.shader_group(...)` or `@package.shader(...)`. The instance exposes its
registered builders through their unprefixed tree names in snake_case.

See the [builder guide](../getting_started/modifiers_groups.md),
[Package guide](../getting_started/packages.md) and
[migration guide](../getting_started/migration.md) for complete examples.
