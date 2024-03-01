# Node SampleNearest

- Node name : 'Sample Nearest'
- bl_idname : [Sample Nearest](https://docs.blender.org/api/current/bpy.types.Sample Nearest.html)


``` python
SampleNearest(geometry=None, sample_position=None, domain='POINT', node_label=None, node_color=None)
```
##### Arguments

- geometry : None
- sample_position : None
- domain : 'POINT'

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [sample_nearest](/docs/GeoNodes/Geometry.md#sample_nearest)

## Init

``` python
def __init__(self, geometry=None, sample_position=None, domain='POINT', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSampleNearest', node_label=node_label, node_color=node_color)

    self.domain          = domain
    self.geometry        = geometry
    self.sample_position = sample_position
```
