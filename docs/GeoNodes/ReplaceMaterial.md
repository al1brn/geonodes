# Node ReplaceMaterial

- Node name : 'Replace Material'
- bl_idname : [GeometryNodeReplaceMaterial](https://docs.blender.org/api/current/bpy.types.GeometryNodeReplaceMaterial.html)


``` python
ReplaceMaterial(geometry=None, old=None, new=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- old : None
- new : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [replace_material](/docs/GeoNodes/socket_GEOMETRY.md#replace_material)

## Init

``` python
def __init__(self, geometry=None, old=None, new=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeReplaceMaterial', node_label=node_label, node_color=node_color, **kwargs)

    self.geometry        = geometry
    self.old             = old
    self.new             = new
```
