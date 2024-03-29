# Node SceneTime

- Node name : 'Scene Time'
- bl_idname : [CompositorNodeSceneTime](https://docs.blender.org/api/current/bpy.types.CompositorNodeSceneTime.html)


``` python
SceneTime(tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- tag_need_exec : None

## Implementation

- Functions : [frame](/docs/Compositor/CompositorTree.md#frame) [scene_time](/docs/Compositor/CompositorTree.md#scene_time) [seconds](/docs/Compositor/CompositorTree.md#seconds)

## Init

``` python
def __init__(self, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeSceneTime', node_label=node_label, node_color=node_color, **kwargs)

    self.tag_need_exec   = tag_need_exec
```
