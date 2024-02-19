# class CheckerTexture (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : CheckerTexture
 - bl_idname : ShaderNodeTexChecker

Node parameters
 - color_mapping
 - texture_mapping

Input sockets
 - vector : Vect
 - color1 : Col
 - color2 : Col
 - scale : Float

Output sockets
 - color : Col
 - fac : Float

### Header

``` python
def CheckerTexture(self, vector=None, color1=None, color2=None, scale=None, color_mapping=None, texture_mapping=None, node_label=None, node_color=None):
```

## Implementations

o Col : [checker_texture](/docs/Shader_classes/Col.md#checker_texture)

