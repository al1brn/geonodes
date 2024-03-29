# Node Keying

- Node name : 'Keying'
- bl_idname : [CompositorNodeKeying](https://docs.blender.org/api/current/bpy.types.CompositorNodeKeying.html)


``` python
Keying(image=None, key_color=None, garbage_matte=None, core_matte=None, blur_post=0, blur_pre=0, clip_black=0.0, clip_white=1.0, despill_balance=0.5, despill_factor=1.0, dilate_distance=0, edge_kernel_radius=3, edge_kernel_tolerance=0.10000000149011612, feather_distance=0, feather_falloff='SMOOTH', screen_balance=0.5, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- key_color : None
- garbage_matte : None
- core_matte : None
- blur_post : 0
- blur_pre : 0
- clip_black : 0.0
- clip_white : 1.0
- despill_balance : 0.5
- despill_factor : 1.0
- dilate_distance : 0
- edge_kernel_radius : 3
- edge_kernel_tolerance : 0.10000000149011612
- feather_distance : 0
- feather_falloff : 'SMOOTH'
- screen_balance : 0.5
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, key_color=None, garbage_matte=None, core_matte=None, blur_post=0, blur_pre=0, clip_black=0.0, clip_white=1.0, despill_balance=0.5, despill_factor=1.0, dilate_distance=0, edge_kernel_radius=3, edge_kernel_tolerance=0.10000000149011612, feather_distance=0, feather_falloff='SMOOTH', screen_balance=0.5, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeKeying', node_label=node_label, node_color=node_color, **kwargs)

    self.blur_post       = blur_post
    self.blur_pre        = blur_pre
    self.clip_black      = clip_black
    self.clip_white      = clip_white
    self.despill_balance = despill_balance
    self.despill_factor  = despill_factor
    self.dilate_distance = dilate_distance
    self.edge_kernel_radius = edge_kernel_radius
    self.edge_kernel_tolerance = edge_kernel_tolerance
    self.feather_distance = feather_distance
    self.feather_falloff = feather_falloff
    self.screen_balance  = screen_balance
    self.tag_need_exec   = tag_need_exec
    self.image           = image
    self.key_color       = key_color
    self.garbage_matte   = garbage_matte
    self.core_matte      = core_matte
```
