# class SkyTexture (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : SkyTexture
 - bl_idname : ShaderNodeTexSky

Node parameters
 - air_density : 1.0
 - altitude : 0.0
 - color_mapping
 - dust_density : 1.0
 - ground_albedo : 0.30000001192092896
 - ozone_density : 1.0
 - sky_type : 'NISHITA'
 - sun_direction : (0.0, 0.0, 1.0)
 - sun_disc : True
 - sun_elevation : 0.2617993950843811
 - sun_intensity : 1.0
 - sun_rotation : 0.0
 - sun_size : 0.009512044489383698
 - texture_mapping
 - turbidity : 2.200000047683716

Input sockets
 - vector : Vect

Output sockets
 - color : Col

### Header

``` python
def SkyTexture(self, vector=None, air_density=1.0, altitude=0.0, color_mapping=None, dust_density=1.0, ground_albedo=0.30000001192092896, ozone_density=1.0, sky_type='NISHITA', sun_direction=(0.0, 0.0, 1.0), sun_disc=True,
sun_elevation=0.2617993950843811, sun_intensity=1.0, sun_rotation=0.0, sun_size=0.009512044489383698, texture_mapping=None, turbidity=2.200000047683716, node_label=None, node_color=None):
```

## Implementations

o functions : [sky_texture](/docs/Shader_classes/GLOBAL.md#sky_texture)
o Vect : [sky_texture](/docs/Shader_classes/Vect.md#sky_texture)

