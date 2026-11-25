# Shaders

Use `@shader()` to declare a material and `@shader_group()` for a reusable shader
group. Socket classes and `nd` select the shader environment automatically while
the builder runs. Node creation must happen inside a builder or an explicit
`ShaderNodes` context.

## Surface material

```python
from geonodes import *

@shader("Blue Surface", target='ALL')
def blue_surface():
    Shader.Principled(base_color=(0.1, 0.2, 0.8), roughness=0.3).out()

blue_surface.build()
```

A declaration does not create a material until `.build()` is called. Select the
resulting material in Blender to assign it to an object.

## Shader groups

```python
from geonodes import *

@shader_group()
def tinted_surface(color: Color = (0.1, 0.2, 0.8), roughness: float = 0.3):
    Shader.Principled(base_color=color, roughness=roughness).out("Surface")

@shader()
def painted_material():
    tinted_surface(color=(0.8, 0.2, 0.1), roughness=0.5).out()

painted_material.build(full=True)
```

Calling `tinted_surface(...)` inserts a Group node and constructs its definition
if missing. A material builder supports `.build()` only. See
[Packages](packages.md) for organizing materials alongside geometry builders.

## Volume material

```python
from geonodes import *

@shader("Blue Volume", target='CYCLES')
def blue_volume():
    VolumeShader.Principled(color=(0.1, 0.2, 0.8), density=0.01).out()

blue_volume.build()
```

`VolumeShader` provides `Principled`, `Absorption`, `Scatter` and `Coefficients`
constructors. Its `.out()` connects the material's Volume input. In a shader
group, `.out("Name")` creates an ordinary group output instead.

## Material Output inputs

Material Output has four inputs. Surface and Volume receive shaders;
Displacement receives a vector and Thickness a float. Use the tree properties
to address each input explicitly:

```python
from geonodes import *

@shader("Surface and Volume", target='CYCLES')
def surface_and_volume():
    tree = Tree.current_tree()
    tree.surface = Shader.Principled(base_color=(0.6, 0.7, 0.9))
    tree.volume = VolumeShader.Absorption(color=(0.6, 0.7, 0.9), density=0.05)
    tree.displacement = Vector((0, 0, 0))
    tree.thickness = 0.1

surface_and_volume.build()
```

`Shader.out()` selects Surface and `VolumeShader.out()` selects Volume.
Do not use a generic `Float.out()` or `Vector.out()` to select Thickness or
Displacement; use the explicit tree property or `set_*` method.

For a displacement shader, build the displacement vector with the relevant node
(for example `nd.displacement(...)`) and assign it to `tree.displacement`.
A Bump node modifies a surface normal; connect its result to a surface shader's
normal input rather than Material Output's Displacement input.

## Output targets

`@shader(target='ALL')` is the default. Supported values are `'ALL'`, `'EEVEE'`
and `'CYCLES'`. `.out()` and the four tree properties use this default target.
The API reuses an output node with that target or creates one when needed.

For several targets in one material, use the explicit methods:

```python
from geonodes import *

@shader("Two Targets", target='CYCLES')
def two_targets():
    tree = Tree.current_tree()
    tree.set_surface(Shader.Principled(roughness=0.2))
    tree.set_surface(Shader.Principled(roughness=0.6), target='EEVEE')

    # Explicit ALL selects a separate target rather than the decorator default.
    tree.set_thickness(0.1, target='ALL')

two_targets.build()
```

`set_surface`, `set_volume`, `set_displacement` and `set_thickness` accept
`target`. Omitting it uses the tree default. The properties also accept
`tree.surface = (surface, 'EEVEE')` and `tree.volume = (volume, 'CYCLES')`.
For vector-valued displacement, prefer `set_displacement(vector, target=...)`
when selecting a target explicitly.

The same default is available in a direct context:
`with ShaderNodes("My Material", target='CYCLES') as tree:`.
Targets apply to materials, not shader group outputs.

## Rebuilding and material ownership

API materials store their requested root name in the custom property
`geonodes_api`. `.build()` rebuilds the API-owned material's node tree; it does
not assign the material to objects. `.build(full=True)` also rebuilds shader
group dependencies once per operation.

Unmarked user materials are preserved. When the requested name is already in
use, Blender gives the new API material a suffix such as `.001`. Later builds
find the material through its marker, even after it is renamed. Remove that
custom property to take ownership: a subsequent build creates a separate
API-owned material.

Material names passed to the API resolve to the marked material. Pass a Blender
`Material` object when you need to select an exact material. Direct
`ShaderNodes(..., rebuild=False)` contexts preserve existing API materials;
public builder `.build()` always requests reconstruction.
