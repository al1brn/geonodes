# Node SceneTime

- Node name : 'Scene Time'
- bl_idname : [GeometryNodeInputSceneTime](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
SceneTime(node_label=None, node_color=None)
```
## Implementation

- Functions : [frame](/docs/GeoNodes/GeoNodes.md#frame) [scene_time](/docs/GeoNodes/GeoNodes.md#scene_time) [seconds](/docs/GeoNodes/GeoNodes.md#seconds)

## Init

``` python
def __init__(self, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeInputSceneTime', node_label=node_label, node_color=node_color)
```
