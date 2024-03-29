# Node DifferenceKey

- Node name : 'Difference Key'
- bl_idname : [CompositorNodeDiffMatte](https://docs.blender.org/api/current/bpy.types.CompositorNodeDiffMatte.html)


``` python
DifferenceKey(image_1=None, image_2=None, falloff=0.10000000149011612, tag_need_exec=None, tolerance=0.10000000149011612, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image_1 : None
- image_2 : None
- falloff : 0.10000000149011612
- tag_need_exec : None
- tolerance : 0.10000000149011612

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image_1=None, image_2=None, falloff=0.10000000149011612, tag_need_exec=None, tolerance=0.10000000149011612, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeDiffMatte', node_label=node_label, node_color=node_color, **kwargs)

    self.falloff         = falloff
    self.tag_need_exec   = tag_need_exec
    self.tolerance       = tolerance
    self.image_1         = image_1
    self.image_2         = image_2
```
