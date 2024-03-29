# Node CombineColor

- Node name : 'Combine Color'
- bl_idname : [FunctionNodeCombineColor](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)


``` python
CombineColor(red=None, green=None, blue=None, alpha=None, mode='RGB', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- red : None
- green : None
- blue : None
- alpha : None
- mode : 'RGB'

## Implementation

- Functions : [combine_color](/docs/GeoNodes/GeoNodesTree.md#combine_color) [hsl](/docs/GeoNodes/GeoNodesTree.md#hsl) [hsv](/docs/GeoNodes/GeoNodesTree.md#hsv) [rgb](/docs/GeoNodes/GeoNodesTree.md#rgb)

## Init

``` python
def __init__(self, red=None, green=None, blue=None, alpha=None, mode='RGB', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'FunctionNodeCombineColor', node_label=node_label, node_color=node_color, **kwargs)

    self.mode            = mode
    self.red             = red
    self.green           = green
    self.blue            = blue
    self.alpha           = alpha
```
