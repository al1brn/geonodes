
# Node SceneTime

> Geometry node name: [Scene Time](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene_time.html)<br>
  Blender type: [Scene Time](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SceneTime(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

- seconds : Float
- frame : Float

## Data sockets

> Data socket classes implementing this node.
  
  
- [functions](/docs/sockets/functions.md).[scene](/docs/sockets/functions.md#scene) : Function
  
