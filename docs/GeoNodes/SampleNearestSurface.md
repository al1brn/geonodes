# Node SampleNearestSurface

- Node name : 'Sample Nearest Surface'
- bl_idname : [GeometryNodeSampleNearestSurface](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearestSurface.html)


``` python
SampleNearestSurface(mesh=None, value=None, sample_position=None, data_type='FLOAT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- mesh : None
- value : None
- sample_position : None
- data_type : 'FLOAT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [sample_nearest_surface](/docs/GeoNodes/socket_GEOMETRY.md#sample_nearest_surface) [sample_nearest_surface_boolean](/docs/GeoNodes/socket_GEOMETRY.md#sample_nearest_surface_boolean) [sample_nearest_surface_color](/docs/GeoNodes/socket_GEOMETRY.md#sample_nearest_surface_color) [sample_nearest_surface_float](/docs/GeoNodes/socket_GEOMETRY.md#sample_nearest_surface_float) [sample_nearest_surface_int](/docs/GeoNodes/socket_GEOMETRY.md#sample_nearest_surface_int) [sample_nearest_surface_quaternion](/docs/GeoNodes/socket_GEOMETRY.md#sample_nearest_surface_quaternion) [sample_nearest_surface_vector](/docs/GeoNodes/socket_GEOMETRY.md#sample_nearest_surface_vector)

## Init

``` python
def __init__(self, mesh=None, value=None, sample_position=None, data_type='FLOAT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSampleNearestSurface', node_label=node_label, node_color=node_color, **kwargs)

    self.data_type       = data_type
    self.mesh            = mesh
    self.value           = value
    self.sample_position = sample_position
```
