# Node Rotate

- Node name : 'Rotate'
- bl_idname : [CompositorNodeRotate](https://docs.blender.org/api/current/bpy.types.CompositorNodeRotate.html)


``` python
Rotate(image=None, degr=None, filter_type='BILINEAR', tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- image : None
- degr : None
- filter_type : 'BILINEAR'
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, degr=None, filter_type='BILINEAR', tag_need_exec=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeRotate', node_label=node_label, node_color=node_color)

    self.filter_type     = filter_type
    self.tag_need_exec   = tag_need_exec
    self.image           = image
    self.degr            = degr
```
