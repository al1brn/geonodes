# Node SetID

- Node name : 'Set ID'
- bl_idname : [GeometryNodeSetID](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)


``` python
SetID(geometry=None, selection=None, ID=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- selection : None
- ID : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [id](/docs/GeoNodes/socket_GEOMETRY.md#id) [set_id](/docs/GeoNodes/socket_GEOMETRY.md#set_id)

## Init

``` python
def __init__(self, geometry=None, selection=None, ID=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSetID', node_label=node_label, node_color=node_color, **kwargs)

    self.geometry        = geometry
    self.selection       = selection
    self.ID              = ID
```
