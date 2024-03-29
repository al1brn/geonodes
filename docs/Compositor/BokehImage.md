# Node BokehImage

- Node name : 'Bokeh Image'
- bl_idname : [CompositorNodeBokehImage](https://docs.blender.org/api/current/bpy.types.CompositorNodeBokehImage.html)


``` python
BokehImage(angle=0.0, catadioptric=0.0, flaps=5, rounding=0.0, shift=0.0, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- angle : 0.0
- catadioptric : 0.0
- flaps : 5
- rounding : 0.0
- shift : 0.0
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, angle=0.0, catadioptric=0.0, flaps=5, rounding=0.0, shift=0.0, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeBokehImage', node_label=node_label, node_color=node_color, **kwargs)

    self.angle           = angle
    self.catadioptric    = catadioptric
    self.flaps           = flaps
    self.rounding        = rounding
    self.shift           = shift
    self.tag_need_exec   = tag_need_exec
```
