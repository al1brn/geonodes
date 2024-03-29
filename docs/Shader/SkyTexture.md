# Node SkyTexture

- Node name : 'Sky Texture'
- bl_idname : [ShaderNodeTexSky](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexSky.html)


``` python
SkyTexture(vector=None, air_density=1.0, altitude=0.0, color_mapping=None, dust_density=1.0, ground_albedo=0.30000001192092896, ozone_density=1.0, sky_type='NISHITA', sun_direction=(0.0, 0.0, 1.0), sun_disc=True, sun_elevation=0.2617993950843811, sun_intensity=1.0, sun_rotation=0.0, sun_size=0.009512044489383698, texture_mapping=None, turbidity=2.200000047683716, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vector : None
- air_density : 1.0
- altitude : 0.0
- color_mapping : None
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
- texture_mapping : None
- turbidity : 2.200000047683716

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, vector=None, air_density=1.0, altitude=0.0, color_mapping=None, dust_density=1.0, ground_albedo=0.30000001192092896, ozone_density=1.0, sky_type='NISHITA', sun_direction=(0.0, 0.0, 1.0), sun_disc=True, sun_elevation=0.2617993950843811, sun_intensity=1.0, sun_rotation=0.0, sun_size=0.009512044489383698, texture_mapping=None, turbidity=2.200000047683716, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeTexSky', node_label=node_label, node_color=node_color, **kwargs)

    self.air_density     = air_density
    self.altitude        = altitude
    self.color_mapping   = color_mapping
    self.dust_density    = dust_density
    self.ground_albedo   = ground_albedo
    self.ozone_density   = ozone_density
    self.sky_type        = sky_type
    self.sun_direction   = sun_direction
    self.sun_disc        = sun_disc
    self.sun_elevation   = sun_elevation
    self.sun_intensity   = sun_intensity
    self.sun_rotation    = sun_rotation
    self.sun_size        = sun_size
    self.texture_mapping = texture_mapping
    self.turbidity       = turbidity
    self.vector          = vector
```
