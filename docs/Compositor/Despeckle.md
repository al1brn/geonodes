# Node Despeckle

- Node name : 'Despeckle'
- bl_idname : [CompositorNodeDespeckle](https://docs.blender.org/api/current/bpy.types.CompositorNodeDespeckle.html)


``` python
Despeckle(fac=None, image=None, tag_need_exec=None, threshold=0.5, threshold_neighbor=0.5, node_label=None, node_color=None)
```
##### Arguments

- fac : None
- image : None
- tag_need_exec : None
- threshold : 0.5
- threshold_neighbor : 0.5

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, fac=None, image=None, tag_need_exec=None, threshold=0.5, threshold_neighbor=0.5, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeDespeckle', node_label=node_label, node_color=node_color)

    self.tag_need_exec   = tag_need_exec
    self.threshold       = threshold
    self.threshold_neighbor = threshold_neighbor
    self.fac             = fac
    self.image           = image
```
