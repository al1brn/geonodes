# Node SampleIndex

- Node name : 'Sample Index'
- bl_idname : [GeometryNodeSampleIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)


``` python
SampleIndex(geometry=None, value=None, index=None, clamp=False, data_type='FLOAT', domain='POINT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- value : None
- index : None
- clamp : False
- data_type : 'FLOAT'
- domain : 'POINT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [sample_index](/docs/GeoNodes/socket_GEOMETRY.md#sample_index) [sample_index_boolean](/docs/GeoNodes/socket_GEOMETRY.md#sample_index_boolean) [sample_index_color](/docs/GeoNodes/socket_GEOMETRY.md#sample_index_color) [sample_index_float](/docs/GeoNodes/socket_GEOMETRY.md#sample_index_float) [sample_index_int](/docs/GeoNodes/socket_GEOMETRY.md#sample_index_int) [sample_index_quaternion](/docs/GeoNodes/socket_GEOMETRY.md#sample_index_quaternion) [sample_index_vector](/docs/GeoNodes/socket_GEOMETRY.md#sample_index_vector)

## Init

``` python
def __init__(self, geometry=None, value=None, index=None, clamp=False, data_type='FLOAT', domain='POINT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSampleIndex', node_label=node_label, node_color=node_color, **kwargs)

    self.clamp           = clamp
    self.data_type       = data_type
    self.domain          = domain
    self.geometry        = geometry
    self.value           = value
    self.index           = index
```
