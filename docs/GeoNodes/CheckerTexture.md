# Node CheckerTexture

- Node name : 'Checker Texture'
- bl_idname : [ShaderNodeTexChecker](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexChecker.html)


``` python
CheckerTexture(vector=None, color1=None, color2=None, scale=None, color_mapping=None, texture_mapping=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vector : None
- color1 : None
- color2 : None
- scale : None
- color_mapping : None
- texture_mapping : None

## Implementation

- Functions : [checker_texture](/docs/GeoNodes/GeoNodesTree.md#checker_texture)

## Init

``` python
def __init__(self, vector=None, color1=None, color2=None, scale=None, color_mapping=None, texture_mapping=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeTexChecker', node_label=node_label, node_color=node_color, **kwargs)

    self.color_mapping   = color_mapping
    self.texture_mapping = texture_mapping
    self.vector          = vector
    self.color1          = color1
    self.color2          = color2
    self.scale           = scale
```
