# class MusgraveTexture (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : MusgraveTexture
 - bl_idname : ShaderNodeTexMusgrave

Node parameters
 - color_mapping
 - musgrave_dimensions : '3D'
 - musgrave_type : 'FBM'
 - texture_mapping

Input sockets
 - vector : Vect
 - w : Float
 - scale : Float
 - detail : Float
 - dimension : Float
 - lacunarity : Float
 - offset : Float
 - gain : Float

Output sockets
 - fac : Float

### Header

``` python
def MusgraveTexture(self, vector=None, scale=None, detail=None, dimension=None, lacunarity=None, w=None, offset=None, gain=None, color_mapping=None, musgrave_dimensions='3D', musgrave_type='FBM', texture_mapping=None, node_label=None,
node_color=None):
```

## Implementations

o functions : [musgrave_texture](/docs/Shader_classes/musgrave_texture.md)

