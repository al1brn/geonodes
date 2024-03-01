# Node Index

- Node name : 'Index'
- bl_idname : [Index](https://docs.blender.org/api/current/bpy.types.Index.html)


``` python
Index(node_label=None, node_color=None)
```
## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [index](/docs/GeoNodes/Geometry.md#index)

## Init

``` python
def __init__(self, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeInputIndex', node_label=node_label, node_color=node_color)
```
