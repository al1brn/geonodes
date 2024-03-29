# Node InvertColor

- Node name : 'Invert Color'
- bl_idname : [ShaderNodeInvert](https://docs.blender.org/api/current/bpy.types.ShaderNodeInvert.html)


``` python
InvertColor(fac=None, color=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- fac : None
- color : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, fac=None, color=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'ShaderNodeInvert', node_label=node_label, node_color=node_color, **kwargs)

    self.fac             = fac
    self.color           = color
```
