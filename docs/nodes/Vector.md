
# Node Vector

> Geometry node name: [Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/vector.html)<br>
  Blender type: [Vector](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputVector.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Vector(vector=[0.0, 0.0, 0.0], label=None, node_color=None)
```



## Arguments


### Parameters

- vector : Vector (default = [0.0, 0.0, 0.0])

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- vector : Vector
