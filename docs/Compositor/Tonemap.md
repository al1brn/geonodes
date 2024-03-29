# Node Tonemap

- Node name : 'Tonemap'
- bl_idname : [CompositorNodeTonemap](https://docs.blender.org/api/current/bpy.types.CompositorNodeTonemap.html)


``` python
Tonemap(image=None, adaptation=1.0, contrast=0.0, correction=0.0, gamma=1.0, intensity=0.0, key=0.18000000715255737, offset=1.0, tag_need_exec=None, tonemap_type='RD_PHOTORECEPTOR', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- adaptation : 1.0
- contrast : 0.0
- correction : 0.0
- gamma : 1.0
- intensity : 0.0
- key : 0.18000000715255737
- offset : 1.0
- tag_need_exec : None
- tonemap_type : 'RD_PHOTORECEPTOR'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, adaptation=1.0, contrast=0.0, correction=0.0, gamma=1.0, intensity=0.0, key=0.18000000715255737, offset=1.0, tag_need_exec=None, tonemap_type='RD_PHOTORECEPTOR', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeTonemap', node_label=node_label, node_color=node_color, **kwargs)

    self.adaptation      = adaptation
    self.contrast        = contrast
    self.correction      = correction
    self.gamma           = gamma
    self.intensity       = intensity
    self.key             = key
    self.offset          = offset
    self.tag_need_exec   = tag_need_exec
    self.tonemap_type    = tonemap_type
    self.image           = image
```
