# Node Radius

- Node name : 'Radius'
- bl_idname : [GeometryNodeInputRadius](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
Radius(node_label=None, node_color=None)
```
## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [radius](/docs/GeoNodes/Geometry.md#radius)

## Init

``` python
def __init__(self, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeInputRadius', node_label=node_label, node_color=node_color)
```
