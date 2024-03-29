# Node SetMaterial

- Node name : 'Set Material'
- bl_idname : [GeometryNodeSetMaterial](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)


``` python
SetMaterial(geometry=None, selection=None, material=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- geometry : None
- selection : None
- material : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [material](/docs/GeoNodes/socket_GEOMETRY.md#material) [set_material](/docs/GeoNodes/socket_GEOMETRY.md#set_material)

## Init

``` python
def __init__(self, geometry=None, selection=None, material=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeSetMaterial', node_label=node_label, node_color=node_color, **kwargs)

    self.geometry        = geometry
    self.selection       = selection
    self.material        = material
```
