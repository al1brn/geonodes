# Node SceneTime

- Node name : 'Scene Time'
- bl_idname : [GeometryNodeInputSceneTime](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html)


``` python
SceneTime(node_label=None, node_color=None, **kwargs)
```
## Implementation

- Functions : [frame](/docs/GeoNodes/GeoNodesTree.md#frame) [scene_time](/docs/GeoNodes/GeoNodesTree.md#scene_time) [seconds](/docs/GeoNodes/GeoNodesTree.md#seconds)

## Init

``` python
def __init__(self, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputSceneTime', node_label=node_label, node_color=node_color, **kwargs)
```
