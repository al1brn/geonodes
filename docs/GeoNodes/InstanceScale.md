# Node InstanceScale

- Node name : 'Instance Scale'
- bl_idname : [GeometryNodeInputInstanceScale](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceScale.html)


``` python
InstanceScale(node_label=None, node_color=None)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/GEOMETRY.md) : [instance_scale](/docs/GeoNodes/socket_GEOMETRY.md#instance_scale) [instance_scale](/docs/GeoNodes/socket_GEOMETRY.md#instance_scale)

## Init

``` python
def __init__(self, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeInputInstanceScale', node_label=node_label, node_color=node_color)
```
