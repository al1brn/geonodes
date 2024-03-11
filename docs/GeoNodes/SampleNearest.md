# Node SampleNearest

- Node name : 'Sample Nearest'
- bl_idname : [GeometryNodeSampleNearest](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)


``` python
SampleNearest(geometry=None, sample_position=None, domain='POINT', node_label=None, node_color=None)
```
##### Arguments

- geometry : None
- sample_position : None
- domain : 'POINT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [sample_nearest](/docs/GeoNodes/socket_GEOMETRY.md#sample_nearest)

## Init

``` python
def __init__(self, geometry=None, sample_position=None, domain='POINT', node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodeSampleNearest', node_label=node_label, node_color=node_color)

    self.domain          = domain
    self.geometry        = geometry
    self.sample_position = sample_position
```
