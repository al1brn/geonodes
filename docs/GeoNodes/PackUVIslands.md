# Node PackUVIslands

- Node name : 'Pack UV Islands'
- bl_idname : GeometryNodeUVPackIslands


``` python
PackUVIslands(uv=None, selection=None, margin=None, rotate=None, node_label=None, node_color=None)
```
##### Arguments

- uv : None
- selection : None
- margin : None
- rotate : None

## Implementation

- [Vect](/docs/GeoNodes/Vect.md) : [pack_uv_islands](/docs/GeoNodes/Vect.md#pack_uv_islands)

## Init

``` python
def __init__(self, uv=None, selection=None, margin=None, rotate=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeUVPackIslands', node_label=node_label, node_color=node_color)

    self.uv              = uv
    self.selection       = selection
    self.margin          = margin
    self.rotate          = rotate
```
