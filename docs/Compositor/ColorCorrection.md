# Node ColorCorrection

- Node name : 'Color Correction'
- bl_idname : [CompositorNodeColorCorrection](https://docs.blender.org/api/current/bpy.types.CompositorNodeColorCorrection.html)


``` python
ColorCorrection(image=None, mask=None, blue=True, green=True, highlights_contrast=1.0, highlights_gain=1.0, highlights_gamma=1.0, highlights_lift=0.0, highlights_saturation=1.0, master_contrast=1.0, master_gain=1.0, master_gamma=1.0, master_lift=0.0, master_saturation=1.0, midtones_contrast=1.0, midtones_end=0.699999988079071, midtones_gain=1.0, midtones_gamma=1.0, midtones_lift=0.0, midtones_saturation=1.0, midtones_start=0.20000000298023224, red=True, shadows_contrast=1.0, shadows_gain=1.0, shadows_gamma=1.0, shadows_lift=0.0, shadows_saturation=1.0, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- mask : None
- blue : True
- green : True
- highlights_contrast : 1.0
- highlights_gain : 1.0
- highlights_gamma : 1.0
- highlights_lift : 0.0
- highlights_saturation : 1.0
- master_contrast : 1.0
- master_gain : 1.0
- master_gamma : 1.0
- master_lift : 0.0
- master_saturation : 1.0
- midtones_contrast : 1.0
- midtones_end : 0.699999988079071
- midtones_gain : 1.0
- midtones_gamma : 1.0
- midtones_lift : 0.0
- midtones_saturation : 1.0
- midtones_start : 0.20000000298023224
- red : True
- shadows_contrast : 1.0
- shadows_gain : 1.0
- shadows_gamma : 1.0
- shadows_lift : 0.0
- shadows_saturation : 1.0
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, mask=None, blue=True, green=True, highlights_contrast=1.0, highlights_gain=1.0, highlights_gamma=1.0, highlights_lift=0.0, highlights_saturation=1.0, master_contrast=1.0, master_gain=1.0, master_gamma=1.0, master_lift=0.0, master_saturation=1.0, midtones_contrast=1.0, midtones_end=0.699999988079071, midtones_gain=1.0, midtones_gamma=1.0, midtones_lift=0.0, midtones_saturation=1.0, midtones_start=0.20000000298023224, red=True, shadows_contrast=1.0, shadows_gain=1.0, shadows_gamma=1.0, shadows_lift=0.0, shadows_saturation=1.0, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeColorCorrection', node_label=node_label, node_color=node_color, **kwargs)

    self.blue            = blue
    self.green           = green
    self.highlights_contrast = highlights_contrast
    self.highlights_gain = highlights_gain
    self.highlights_gamma = highlights_gamma
    self.highlights_lift = highlights_lift
    self.highlights_saturation = highlights_saturation
    self.master_contrast = master_contrast
    self.master_gain     = master_gain
    self.master_gamma    = master_gamma
    self.master_lift     = master_lift
    self.master_saturation = master_saturation
    self.midtones_contrast = midtones_contrast
    self.midtones_end    = midtones_end
    self.midtones_gain   = midtones_gain
    self.midtones_gamma  = midtones_gamma
    self.midtones_lift   = midtones_lift
    self.midtones_saturation = midtones_saturation
    self.midtones_start  = midtones_start
    self.red             = red
    self.shadows_contrast = shadows_contrast
    self.shadows_gain    = shadows_gain
    self.shadows_gamma   = shadows_gamma
    self.shadows_lift    = shadows_lift
    self.shadows_saturation = shadows_saturation
    self.tag_need_exec   = tag_need_exec
    self.image           = image
    self.mask            = mask
```
