# Node GradientTexture

- Node name : 'Gradient Texture'
- bl_idname : ShaderNodeTexGradient


``` python
GradientTexture(vector=None, color_mapping=None, gradient_type='LINEAR', texture_mapping=None, node_label=None, node_color=None)
```
##### Arguments

- vector : None
- color_mapping : None
- gradient_type : 'LINEAR'
- texture_mapping : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, vector=None, color_mapping=None, gradient_type='LINEAR', texture_mapping=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeTexGradient', node_label=node_label, node_color=node_color)

    self.color_mapping   = color_mapping
    self.gradient_type   = gradient_type
    self.texture_mapping = texture_mapping
    self.vector          = vector
```
