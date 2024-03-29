# Node DirectionalBlur

- Node name : 'Directional Blur'
- bl_idname : [CompositorNodeDBlur](https://docs.blender.org/api/current/bpy.types.CompositorNodeDBlur.html)


``` python
DirectionalBlur(image=None, angle=0.0, center_x=0.5, center_y=0.5, distance=0.0, iterations=1, spin=0.0, tag_need_exec=None, zoom=0.0, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- angle : 0.0
- center_x : 0.5
- center_y : 0.5
- distance : 0.0
- iterations : 1
- spin : 0.0
- tag_need_exec : None
- zoom : 0.0

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, angle=0.0, center_x=0.5, center_y=0.5, distance=0.0, iterations=1, spin=0.0, tag_need_exec=None, zoom=0.0, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeDBlur', node_label=node_label, node_color=node_color, **kwargs)

    self.angle           = angle
    self.center_x        = center_x
    self.center_y        = center_y
    self.distance        = distance
    self.iterations      = iterations
    self.spin            = spin
    self.tag_need_exec   = tag_need_exec
    self.zoom            = zoom
    self.image           = image
```
