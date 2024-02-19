# class PointDensity (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : PointDensity
 - bl_idname : ShaderNodeTexPointDensity

Node parameters
 - cache_point_density
 - calc_point_density
 - calc_point_density_minmax
 - interpolation : 'Linear'
 - object : None
 - particle_color_source : 'PARTICLE_AGE'
 - particle_system : None
 - point_source : 'PARTICLE_SYSTEM'
 - radius : 0.30000001192092896
 - resolution : 100
 - space : 'OBJECT'
 - vertex_attribute_name : ''
 - vertex_color_source : 'VERTEX_COLOR'

Input sockets
 - vector : Vect

Output sockets
 - color : Col
 - density : Float

### Header

``` python
def PointDensity(self, vector=None, cache_point_density=None, calc_point_density=None, calc_point_density_minmax=None, interpolation='Linear', object=None, particle_color_source='PARTICLE_AGE', particle_system=None, point_source='PARTICLE_SYSTEM',
radius=0.30000001192092896, resolution=100, space='OBJECT', vertex_attribute_name='', vertex_color_source='VERTEX_COLOR', node_label=None, node_color=None):
```

## Implementations

o Vect : [point_density](/docs/Shader_classes/Vect.md#point_density)

