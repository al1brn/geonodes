# class EnvironmentTexture (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : EnvironmentTexture
 - bl_idname : ShaderNodeTexEnvironment

Node parameters
 - color_mapping
 - image : None
 - image_user
 - interpolation : 'Linear'
 - projection : 'EQUIRECTANGULAR'
 - texture_mapping

Input sockets
 - vector : Vect

Output sockets
 - color : Col

### Header

``` python
def EnvironmentTexture(self, vector=None, color_mapping=None, image=None, image_user=None, interpolation='Linear', projection='EQUIRECTANGULAR', texture_mapping=None, node_label=None, node_color=None):
```

## Implementations

o functions : [environment_texture](/docs/Shader_classes/GLOBAL.md#environment_texture)
o Vect : [environment_texture](/docs/Shader_classes/Vect.md#environment_texture)


