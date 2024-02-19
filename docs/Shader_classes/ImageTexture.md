# class ImageTexture (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : ImageTexture
 - bl_idname : ShaderNodeTexImage

Node parameters
 - color_mapping
 - extension : 'REPEAT'
 - image : None
 - image_user
 - interpolation : 'Linear'
 - projection : 'FLAT'
 - projection_blend : 0.0
 - texture_mapping

Input sockets
 - vector : Vect

Output sockets
 - color : Col
 - alpha : Float

### Header

``` python
def ImageTexture(self, vector=None, color_mapping=None, extension='REPEAT', image=None, image_user=None, interpolation='Linear', projection='FLAT', projection_blend=0.0, texture_mapping=None, node_label=None, node_color=None):
```

## Implementations

o Vect : [image_texture](/docs/Shader_classes/Vect.md#image_texture)


