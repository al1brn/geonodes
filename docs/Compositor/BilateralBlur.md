# Node BilateralBlur

- Node name : 'Bilateral Blur'
- bl_idname : [CompositorNodeBilateralblur](https://docs.blender.org/api/current/bpy.types.CompositorNodeBilateralblur.html)


``` python
BilateralBlur(image=None, determinator=None, iterations=1, sigma_color=0.30000001192092896, sigma_space=5.0, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- determinator : None
- iterations : 1
- sigma_color : 0.30000001192092896
- sigma_space : 5.0
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, determinator=None, iterations=1, sigma_color=0.30000001192092896, sigma_space=5.0, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeBilateralblur', node_label=node_label, node_color=node_color, **kwargs)

    self.iterations      = iterations
    self.sigma_color     = sigma_color
    self.sigma_space     = sigma_space
    self.tag_need_exec   = tag_need_exec
    self.image           = image
    self.determinator    = determinator
```
