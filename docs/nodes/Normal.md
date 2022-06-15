
# Node Normal

> Geometry node name: [Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html)<br>
  Blender type: [Normal](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Normal(label=None, node_color=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- normal : Vector
