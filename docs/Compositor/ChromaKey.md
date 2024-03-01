# Node ChromaKey

- Node name : 'Chroma Key'
- bl_idname : [Chroma Key](https://docs.blender.org/api/current/bpy.types.Chroma Key.html)


``` python
ChromaKey(image=None, key_color=None, gain=1.0, lift=0.0, shadow_adjust=0.0, tag_need_exec=None, threshold=0.1745329201221466, tolerance=0.5235987901687622, node_label=None, node_color=None)
```
##### Arguments

- image : None
- key_color : None
- gain : 1.0
- lift : 0.0
- shadow_adjust : 0.0
- tag_need_exec : None
- threshold : 0.1745329201221466
- tolerance : 0.5235987901687622

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, key_color=None, gain=1.0, lift=0.0, shadow_adjust=0.0, tag_need_exec=None, threshold=0.1745329201221466, tolerance=0.5235987901687622, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeChromaMatte', node_label=node_label, node_color=node_color)

    self.gain            = gain
    self.lift            = lift
    self.shadow_adjust   = shadow_adjust
    self.tag_need_exec   = tag_need_exec
    self.threshold       = threshold
    self.tolerance       = tolerance
    self.image           = image
    self.key_color       = key_color
```
