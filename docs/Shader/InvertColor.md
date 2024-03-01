# Node InvertColor

- Node name : 'Invert Color'
- bl_idname : [Invert Color](https://docs.blender.org/api/current/bpy.types.Invert Color.html)


``` python
InvertColor(fac=None, color=None, node_label=None, node_color=None)
```
##### Arguments

- fac : None
- color : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, fac=None, color=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'ShaderNodeInvert', node_label=node_label, node_color=node_color)

    self.fac             = fac
    self.color           = color
```
