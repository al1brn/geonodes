# Node ColorBalance

- Node name : 'Color Balance'
- bl_idname : [CompositorNodeColorBalance](https://docs.blender.org/api/current/bpy.types.CompositorNodeColorBalance.html)


``` python
ColorBalance(fac=None, image=None, correction_method='LIFT_GAMMA_GAIN', gain=None, gamma=None, lift=None, offset=None, offset_basis=0.0, power=None, slope=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- fac : None
- image : None
- correction_method : 'LIFT_GAMMA_GAIN'
- gain : None
- gamma : None
- lift : None
- offset : None
- offset_basis : 0.0
- power : None
- slope : None
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, fac=None, image=None, correction_method='LIFT_GAMMA_GAIN', gain=None, gamma=None, lift=None, offset=None, offset_basis=0.0, power=None, slope=None, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeColorBalance', node_label=node_label, node_color=node_color, **kwargs)

    self.correction_method = correction_method
    self.gain            = gain
    self.gamma           = gamma
    self.lift            = lift
    self.offset          = offset
    self.offset_basis    = offset_basis
    self.power           = power
    self.slope           = slope
    self.tag_need_exec   = tag_need_exec
    self.fac             = fac
    self.image           = image
```
