# Node MaterialSelection

- Node name : 'Material Selection'
- bl_idname : [GeometryNodeMaterialSelection](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
MaterialSelection(material=None, node_label=None, node_color=None)
```
##### Arguments

- material : None

## Implementation

- [Mat](/docs/GeoNodes/Mat.md) : [material_selection](/docs/GeoNodes/Mat.md#material_selection)

## Init

``` python
def __init__(self, material=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeMaterialSelection', node_label=node_label, node_color=node_color)

    self.material        = material
```
