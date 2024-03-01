# Node SetMaterial

- Node name : 'Set Material'
- bl_idname : GeometryNodeSetMaterial


``` python
SetMaterial(geometry=None, selection=None, material=None, node_label=None, node_color=None)
```
##### Arguments

- geometry : None
- selection : None
- material : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [material](/docs/GeoNodes/Geometry.md#material) [set_material](/docs/GeoNodes/Geometry.md#set_material)

## Init

``` python
def __init__(self, geometry=None, selection=None, material=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSetMaterial', node_label=node_label, node_color=node_color)

    self.geometry        = geometry
    self.selection       = selection
    self.material        = material
```
