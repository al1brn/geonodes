# Node GradientTexture

- Node name : 'Gradient Texture'
- bl_idname : [ShaderNodeTexGradient](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)


``` python
GradientTexture(vector=None, color_mapping=None, gradient_type='LINEAR', texture_mapping=None, node_label=None, node_color=None)
```
##### Arguments

- vector : None
- color_mapping : None
- gradient_type : 'LINEAR'
- texture_mapping : None

## Implementation

- Functions : [gradient_texture](/docs/Shader/ShaderTree.md#gradient_texture)

## Init

``` python
def __init__(self, vector=None, color_mapping=None, gradient_type='LINEAR', texture_mapping=None, node_label=None, node_color=None):

    Node.__init__(self, 'ShaderNodeTexGradient', node_label=node_label, node_color=node_color)

    self.color_mapping   = color_mapping
    self.gradient_type   = gradient_type
    self.texture_mapping = texture_mapping
    self.vector          = vector
```