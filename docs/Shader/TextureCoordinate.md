# Node TextureCoordinate

- Node name : 'Texture Coordinate'
- bl_idname : [ShaderNodeTexCoord](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexCoord.html)


``` python
TextureCoordinate(from_instancer=False, object=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- from_instancer : False
- object : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, from_instancer=False, object=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeTexCoord', node_label=node_label, node_color=node_color, **kwargs)

    self.from_instancer  = from_instancer
    self.object          = object
```
