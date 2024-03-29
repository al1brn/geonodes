# Node InstanceRotation

- Node name : 'Instance Rotation'
- bl_idname : [GeometryNodeInputInstanceRotation](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceRotation.html)


``` python
InstanceRotation(node_label=None, node_color=None, **kwargs)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [instance_rotation](/docs/GeoNodes/socket_GEOMETRY.md#instance_rotation)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputInstanceRotation', node_label=node_label, node_color=node_color, **kwargs)
```
