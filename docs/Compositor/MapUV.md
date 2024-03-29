# Node MapUV

- Node name : 'Map UV'
- bl_idname : [CompositorNodeMapUV](https://docs.blender.org/api/current/bpy.types.CompositorNodeMapUV.html)


``` python
MapUV(image=None, uv=None, alpha=0, filter_type='ANISOTROPIC', tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- uv : None
- alpha : 0
- filter_type : 'ANISOTROPIC'
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, uv=None, alpha=0, filter_type='ANISOTROPIC', tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeMapUV', node_label=node_label, node_color=node_color, **kwargs)

    self.alpha           = alpha
    self.filter_type     = filter_type
    self.tag_need_exec   = tag_need_exec
    self.image           = image
    self.uv              = uv
```
