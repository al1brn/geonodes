# Node ReplaceMaterial

- Node name : 'Replace Material'
- bl_idname : GeometryNodeReplaceMaterial


``` python
ReplaceMaterial(geometry=None, old=None, new=None, node_label=None, node_color=None)
```
##### Arguments

- geometry : None
- old : None
- new : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [replace_material](/docs/GeoNodes/Geometry.md#replace_material)

## Init

``` python
def __init__(self, geometry=None, old=None, new=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeReplaceMaterial', node_label=node_label, node_color=node_color)

    self.geometry        = geometry
    self.old             = old
    self.new             = new
```
