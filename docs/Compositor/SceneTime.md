# Node SceneTime

- Node name : 'Scene Time'
- bl_idname : [CompositorNodeSceneTime](https://docs.blender.org/api/current/bpy.types.CompositorNodeSceneTime.html)


``` python
SceneTime(tag_need_exec=None, node_label=None, node_color=None)
```
##### Arguments

- tag_need_exec : None

## Implementation

- Functions : [frame](/docs/Compositor/Compositor.md#frame) [scene_time](/docs/Compositor/Compositor.md#scene_time) [seconds](/docs/Compositor/Compositor.md#seconds)

## Init

``` python
def __init__(self, tag_need_exec=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'CompositorNodeSceneTime', node_label=node_label, node_color=node_color)

    self.tag_need_exec   = tag_need_exec
```
