# Node PackUVIslands

- Node name : 'Pack UV Islands'
- bl_idname : [GeometryNodeUVPackIslands](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html)


``` python
PackUVIslands(uv=None, selection=None, margin=None, rotate=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- uv : None
- selection : None
- margin : None
- rotate : None

## Implementation

- [VECTOR](/docs/GeoNodes/socket_VECTOR.md) : [pack_uv_islands](/docs/GeoNodes/socket_VECTOR.md#pack_uv_islands)

## Init

``` python
def __init__(self, uv=None, selection=None, margin=None, rotate=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeUVPackIslands', node_label=node_label, node_color=node_color, **kwargs)

    self.uv              = uv
    self.selection       = selection
    self.margin          = margin
    self.rotate          = rotate
```
