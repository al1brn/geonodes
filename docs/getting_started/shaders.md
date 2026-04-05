# Shader


The module **geonodes** can be used to script shaders.

Creating _Shader Nodes_ is the same as creating _Geometry Nodes_, with the following differences:

- Use **ShaderNodes** rather that **GeoNodes**
- Use **snd** (for _Shader Nodes_) rather than **nd**
- **out** method takes the class type to select the proper socket between _Surface_, _Volume_, _Displacement_ and _Thickness_

!!! warning
    Creating shader nodes can overwrite an existing material. By default, this behavior is blocked. If the material doesn't
    exist, it will be created at first launch. Further modifications will be ignored since the material exists from now on.
    
    You must explicitly ask to overwrite a material using the `replace_material` argument when initiating a new **ShaderNodes**.


## Shader

``` python
from geonodes import *

# Dev mode : replace_material will repalce existing shader

with ShaderNodes("Surface Shader", replace_material=True):

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


