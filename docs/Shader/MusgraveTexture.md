# Node MusgraveTexture

- Node name : 'Musgrave Texture'
- bl_idname : [ShaderNodeTexMusgrave](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMusgrave.html)


``` python
MusgraveTexture(vector=None, scale=None, detail=None, dimension=None, lacunarity=None, w=None, offset=None, gain=None, color_mapping=None, musgrave_dimensions='3D', musgrave_type='FBM', texture_mapping=None, node_label=None, node_color=None)
```
##### Arguments

- vector : None
- scale : None
- detail : None
- dimension : None
- lacunarity : None
- w : None
- offset : None
- gain : None
- color_mapping : None
- musgrave_dimensions : '3D'
- musgrave_type : 'FBM'
- texture_mapping : None

## Implementation

- Functions : [musgrave_texture](/docs/Shader/ShaderTree.md#musgrave_texture)

## Init

``` python
def __init__(self, vector=None, scale=None, detail=None, dimension=None, lacunarity=None, w=None, offset=None, gain=None, color_mapping=None, musgrave_dimensions='3D', musgrave_type='FBM', texture_mapping=None, node_label=None, node_color=None):

    Node.__init__(self, 'ShaderNodeTexMusgrave', node_label=node_label, node_color=node_color)

    self.color_mapping   = color_mapping
    self.musgrave_dimensions = musgrave_dimensions
    self.musgrave_type   = musgrave_type
    self.texture_mapping = texture_mapping
    self.vector          = vector
    self.scale           = scale
    self.detail          = detail
    self.dimension       = dimension
    self.lacunarity      = lacunarity
    self.w               = w
    self.offset          = offset
    self.gain            = gain
```
