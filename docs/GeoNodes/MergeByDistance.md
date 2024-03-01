# Node MergeByDistance

- Node name : 'Merge by Distance'
- bl_idname : [Merge by Distance](https://docs.blender.org/api/current/bpy.types.Merge by Distance.html)


``` python
MergeByDistance(geometry=None, selection=None, distance=None, mode='ALL', node_label=None, node_color=None)
```
##### Arguments

- geometry : None
- selection : None
- distance : None
- mode : 'ALL'

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [merge_by_distance](/docs/GeoNodes/Geometry.md#merge_by_distance)

## Init

``` python
def __init__(self, geometry=None, selection=None, distance=None, mode='ALL', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeMergeByDistance', node_label=node_label, node_color=node_color)

    self.mode            = mode
    self.geometry        = geometry
    self.selection       = selection
    self.distance        = distance
```
