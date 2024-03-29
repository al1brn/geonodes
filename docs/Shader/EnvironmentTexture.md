# Node EnvironmentTexture

- Node name : 'Environment Texture'
- bl_idname : [ShaderNodeTexEnvironment](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexEnvironment.html)


``` python
EnvironmentTexture(vector=None, color_mapping=None, image=None, image_user=None, interpolation='Linear', projection='EQUIRECTANGULAR', texture_mapping=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- vector : None
- color_mapping : None
- image : None
- image_user : None
- interpolation : Linear
- projection : 'EQUIRECTANGULAR'
- texture_mapping : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, vector=None, color_mapping=None, image=None, image_user=None, interpolation='Linear', projection='EQUIRECTANGULAR', texture_mapping=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeTexEnvironment', node_label=node_label, node_color=node_color, **kwargs)

    self.color_mapping   = color_mapping
    self.image           = image
    self.image_user      = image_user
    self.interpolation   = interpolation
    self.projection      = projection
    self.texture_mapping = texture_mapping
    self.vector          = vector
```
