# Node SampleIndex

- Node name : 'Sample Index'
- bl_idname : [Sample Index](https://docs.blender.org/api/current/bpy.types.Sample Index.html)


``` python
SampleIndex(geometry=None, value=None, index=None, clamp=False, data_type='FLOAT', domain='POINT', node_label=None, node_color=None)
```
##### Arguments

- geometry : None
- value : None
- index : None
- clamp : False
- data_type : 'FLOAT'
- domain : 'POINT'

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [sample_index](/docs/GeoNodes/Geometry.md#sample_index) [sample_index_boolean](/docs/GeoNodes/Geometry.md#sample_index_boolean) [sample_index_color](/docs/GeoNodes/Geometry.md#sample_index_color) [sample_index_float](/docs/GeoNodes/Geometry.md#sample_index_float) [sample_index_int](/docs/GeoNodes/Geometry.md#sample_index_int) [sample_index_quaternion](/docs/GeoNodes/Geometry.md#sample_index_quaternion) [sample_index_vector](/docs/GeoNodes/Geometry.md#sample_index_vector)

## Init

``` python
def __init__(self, geometry=None, value=None, index=None, clamp=False, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSampleIndex', node_label=node_label, node_color=node_color)

    self.clamp           = clamp
    self.data_type       = data_type
    self.domain          = domain
    self.geometry        = geometry
    self.value           = value
    self.index           = index
```
