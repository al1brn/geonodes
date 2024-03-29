# Node PointDensity

- Node name : 'Point Density'
- bl_idname : [ShaderNodeTexPointDensity](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexPointDensity.html)


``` python
PointDensity(vector=None, cache_point_density=None, calc_point_density=None, calc_point_density_minmax=None, interpolation='Linear', object=None, particle_color_source='PARTICLE_AGE', particle_system=None, point_source='PARTICLE_SYSTEM', radius=0.30000001192092896, resolution=100, space='OBJECT', vertex_attribute_name='', vertex_color_source='VERTEX_COLOR', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vector : None
- cache_point_density : None
- calc_point_density : None
- calc_point_density_minmax : None
- interpolation : Linear
- object : None
- particle_color_source : 'PARTICLE_AGE'
- particle_system : None
- point_source : 'PARTICLE_SYSTEM'
- radius : 0.30000001192092896
- resolution : 100
- space : 'OBJECT'
- vertex_attribute_name : ''
- vertex_color_source : 'VERTEX_COLOR'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, vector=None, cache_point_density=None, calc_point_density=None, calc_point_density_minmax=None, interpolation='Linear', object=None, particle_color_source='PARTICLE_AGE', particle_system=None, point_source='PARTICLE_SYSTEM', radius=0.30000001192092896, resolution=100, space='OBJECT', vertex_attribute_name='', vertex_color_source='VERTEX_COLOR', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeTexPointDensity', node_label=node_label, node_color=node_color, **kwargs)

    self.cache_point_density = cache_point_density
    self.calc_point_density = calc_point_density
    self.calc_point_density_minmax = calc_point_density_minmax
    self.interpolation   = interpolation
    self.object          = object
    self.particle_color_source = particle_color_source
    self.particle_system = particle_system
    self.point_source    = point_source
    self.radius          = radius
    self.resolution      = resolution
    self.space           = space
    self.vertex_attribute_name = vertex_attribute_name
    self.vertex_color_source = vertex_color_source
    self.vector          = vector
```
