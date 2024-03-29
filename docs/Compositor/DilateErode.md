# Node DilateErode

- Node name : 'Dilate/Erode'
- bl_idname : [CompositorNodeDilateErode](https://docs.blender.org/api/current/bpy.types.CompositorNodeDilateErode.html)


``` python
DilateErode(mask=None, distance=0, edge=0.0, falloff='SMOOTH', mode='STEP', tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- mask : None
- distance : 0
- edge : 0.0
- falloff : 'SMOOTH'
- mode : 'STEP'
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, mask=None, distance=0, edge=0.0, falloff='SMOOTH', mode='STEP', tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeDilateErode', node_label=node_label, node_color=node_color, **kwargs)

    self.distance        = distance
    self.edge            = edge
    self.falloff         = falloff
    self.mode            = mode
    self.tag_need_exec   = tag_need_exec
    self.mask            = mask
```
