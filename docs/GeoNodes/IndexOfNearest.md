# Node IndexOfNearest

- Node name : 'Index of Nearest'
- bl_idname : [GeometryNodeIndexOfNearest](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
IndexOfNearest(position=None, group_id=None, node_label=None, node_color=None)
```
##### Arguments

- position : None
- group_id : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [index_of_nearest](/docs/GeoNodes/Geometry.md#index_of_nearest)

## Init

``` python
def __init__(self, position=None, group_id=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeIndexOfNearest', node_label=node_label, node_color=node_color)

    self.position        = position
    self.group_id        = group_id
```
