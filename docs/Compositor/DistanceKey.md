# Node DistanceKey

- Node name : 'Distance Key'
- bl_idname : [CompositorNodeDistanceMatte](https://docs.blender.org/api/current/bpy.types.CompositorNodeDistanceMatte.html)


``` python
DistanceKey(image=None, key_color=None, channel='RGB', falloff=0.10000000149011612, tag_need_exec=None, tolerance=0.10000000149011612, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- key_color : None
- channel : 'RGB'
- falloff : 0.10000000149011612
- tag_need_exec : None
- tolerance : 0.10000000149011612

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, key_color=None, channel='RGB', falloff=0.10000000149011612, tag_need_exec=None, tolerance=0.10000000149011612, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeDistanceMatte', node_label=node_label, node_color=node_color, **kwargs)

    self.channel         = channel
    self.falloff         = falloff
    self.tag_need_exec   = tag_need_exec
    self.tolerance       = tolerance
    self.image           = image
    self.key_color       = key_color
```
