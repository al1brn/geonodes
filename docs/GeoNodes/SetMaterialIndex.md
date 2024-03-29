# Node SetMaterialIndex

- Node name : 'Set Material Index'
- bl_idname : [GeometryNodeSetMaterialIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)


``` python
SetMaterialIndex(geometry=None, selection=None, material_index=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- selection : None
- material_index : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [material_index](/docs/GeoNodes/socket_GEOMETRY.md#material_index) [set_material_index](/docs/GeoNodes/socket_GEOMETRY.md#set_material_index)

## Init

``` python
def __init__(self, geometry=None, selection=None, material_index=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSetMaterialIndex', node_label=node_label, node_color=node_color, **kwargs)

    self.geometry        = geometry
    self.selection       = selection
    self.material_index  = material_index
```
