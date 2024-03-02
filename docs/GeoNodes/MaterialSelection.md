# Node MaterialSelection

- Node name : 'Material Selection'
- bl_idname : [GeometryNodeMaterialSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)


``` python
MaterialSelection(material=None, node_label=None, node_color=None)
```
##### Arguments

- material : None

## Implementation

- [MATERIAL](/docs/GeoNodes/socket_MATERIAL.md) : [material_selection](/docs/GeoNodes/socket_MATERIAL.md#material_selection) [material_selection](/docs/GeoNodes/socket_MATERIAL.md#material_selection)

## Init

``` python
def __init__(self, material=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeMaterialSelection', node_label=node_label, node_color=node_color)

    self.material        = material
```
