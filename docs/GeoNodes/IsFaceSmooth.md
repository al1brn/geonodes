# Node IsFaceSmooth

- Node name : 'Is Face Smooth'
- bl_idname : [GeometryNodeInputShadeSmooth](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
IsFaceSmooth(node_label=None, node_color=None)
```
## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [face_smooth](/docs/GeoNodes/Geometry.md#face_smooth)

## Init

``` python
def __init__(self, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeInputShadeSmooth', node_label=node_label, node_color=node_color)
```
