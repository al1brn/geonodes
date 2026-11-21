# Shader


The module **geonodes** can be used to script shaders.

Creating _Shader Nodes_ is the same as creating _Geometry Nodes_, with the following differences:

- Use **ShaderNodes** rather that **GeoNodes**
- Use **snd** (for _Shader Nodes_) rather than **nd**
- **out** method takes the class type to select the proper socket between _Surface_, _Volume_, _Displacement_ and _Thickness_

API materials store their requested root name in the custom property
`geonodes_api`. Existing marked materials are rebuilt by default. Unmarked
materials are preserved: Blender gives the new API material a suffix such as
`.001`. Later builds find it by its root-name marker, even after renaming.

Remove the custom property to take ownership of a material. The next build
creates a separate marked material. Material names used by the API resolve to
the marked material; pass a Blender `Material` object to select an exact material.
Use `rebuild=False` to preserve an existing API material without rebuilding it.


## Shader

``` python
from geonodes import *

# Rebuild the API-owned shader; preserve unmarked user materials

with ShaderNodes("Surface Shader", rebuild=True):

    # ----- Principled BSDF

    ped = Shader.Principled(
        base_color = (.1, .2, .3),
        roughness = .2,
    )

    # ----- To surface output

    ped.out()

    # ----- Noise displacement

    noise = Texture.Noise()

    bump = snd.bump(height=noise)
    bump.out()

    # ----- Thickness

    a_float = Float(.1)

    a_float.out()

    # ----- AOV Output

    snd.aov_output(color=Color((.6, .7, .9)), value=pi, aov_name='Test')
```

## Volume Shader

``` python

with ShaderNodes("Volume Shader"):

    # ----- Principled BSDF

    ped = VolumeShader.Principled(
        color = (.1, .2, .3),
        density = .01,
    )

    # ----- To surface output

    ped.out()
```


