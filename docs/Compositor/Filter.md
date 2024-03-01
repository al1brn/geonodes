# Node Filter

- Node name : 'Filter'
- bl_idname : [Filter](https://docs.blender.org/api/current/bpy.types.Filter.html)


``` python
Filter(fac=None, image=None, filter_type='SOFTEN', tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- fac : None
- image : None
- filter_type : 'SOFTEN'
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, fac=None, image=None, filter_type='SOFTEN', tag_need_exec=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeFilter', node_label=node_label, node_color=node_color)

    self.filter_type     = filter_type
    self.tag_need_exec   = tag_need_exec
    self.fac             = fac
    self.image           = image
```
