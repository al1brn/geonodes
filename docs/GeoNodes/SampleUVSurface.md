# Node SampleUVSurface

- Node name : 'Sample UV Surface'
- bl_idname : [GeometryNodeSampleUVSurface](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleUVSurface.html)


``` python
SampleUVSurface(mesh=None, value=None, uv_map=None, sample_uv=None, data_type='FLOAT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- mesh : None
- value : None
- uv_map : None
- sample_uv : None
- data_type : 'FLOAT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [sample_uv_surface](/docs/GeoNodes/socket_GEOMETRY.md#sample_uv_surface) [sample_uv_surface_boolean](/docs/GeoNodes/socket_GEOMETRY.md#sample_uv_surface_boolean) [sample_uv_surface_color](/docs/GeoNodes/socket_GEOMETRY.md#sample_uv_surface_color) [sample_uv_surface_float](/docs/GeoNodes/socket_GEOMETRY.md#sample_uv_surface_float) [sample_uv_surface_int](/docs/GeoNodes/socket_GEOMETRY.md#sample_uv_surface_int) [sample_uv_surface_quaternion](/docs/GeoNodes/socket_GEOMETRY.md#sample_uv_surface_quaternion) [sample_uv_surface_vector](/docs/GeoNodes/socket_GEOMETRY.md#sample_uv_surface_vector)

## Init

``` python
def __init__(self, mesh=None, value=None, uv_map=None, sample_uv=None, data_type='FLOAT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSampleUVSurface', node_label=node_label, node_color=node_color, **kwargs)

    self.data_type       = data_type
    self.mesh            = mesh
    self.value           = value
    self.uv_map          = uv_map
    self.sample_uv       = sample_uv
```
