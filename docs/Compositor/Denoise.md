# Node Denoise

- Node name : 'Denoise'
- bl_idname : [CompositorNodeDenoise](https://docs.blender.org/api/current/bpy.types.CompositorNodeDenoise.html)


``` python
Denoise(image=None, normal=None, albedo=None, prefilter='ACCURATE', tag_need_exec=None, use_hdr=True, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- normal : None
- albedo : None
- prefilter : 'ACCURATE'
- tag_need_exec : None
- use_hdr : True

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, normal=None, albedo=None, prefilter='ACCURATE', tag_need_exec=None, use_hdr=True, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeDenoise', node_label=node_label, node_color=node_color, **kwargs)

    self.prefilter       = prefilter
    self.tag_need_exec   = tag_need_exec
    self.use_hdr         = use_hdr
    self.image           = image
    self.normal          = normal
    self.albedo          = albedo
```
