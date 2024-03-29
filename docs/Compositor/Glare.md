# Node Glare

- Node name : 'Glare'
- bl_idname : [CompositorNodeGlare](https://docs.blender.org/api/current/bpy.types.CompositorNodeGlare.html)


``` python
Glare(image=None, angle_offset=0.0, color_modulation=0.25, fade=0.8999999761581421, glare_type='STREAKS', iterations=3, mix=0.0, quality='MEDIUM', size=8, streaks=4, tag_need_exec=None, threshold=1.0, use_rotate_45=True, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- angle_offset : 0.0
- color_modulation : 0.25
- fade : 0.8999999761581421
- glare_type : 'STREAKS'
- iterations : 3
- mix : 0.0
- quality : 'MEDIUM'
- size : 8
- streaks : 4
- tag_need_exec : None
- threshold : 1.0
- use_rotate_45 : True

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, angle_offset=0.0, color_modulation=0.25, fade=0.8999999761581421, glare_type='STREAKS', iterations=3, mix=0.0, quality='MEDIUM', size=8, streaks=4, tag_need_exec=None, threshold=1.0, use_rotate_45=True, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeGlare', node_label=node_label, node_color=node_color, **kwargs)

    self.angle_offset    = angle_offset
    self.color_modulation = color_modulation
    self.fade            = fade
    self.glare_type      = glare_type
    self.iterations      = iterations
    self.mix             = mix
    self.quality         = quality
    self.size            = size
    self.streaks         = streaks
    self.tag_need_exec   = tag_need_exec
    self.threshold       = threshold
    self.use_rotate_45   = use_rotate_45
    self.image           = image
```
