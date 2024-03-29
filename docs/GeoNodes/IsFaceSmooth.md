# Node IsFaceSmooth

- Node name : 'Is Face Smooth'
- bl_idname : [GeometryNodeInputShadeSmooth](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html)


``` python
IsFaceSmooth(node_label=None, node_color=None, **kwargs)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [face_smooth](/docs/GeoNodes/socket_GEOMETRY.md#face_smooth)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputShadeSmooth', node_label=node_label, node_color=node_color, **kwargs)
```
