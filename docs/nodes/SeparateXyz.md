
# Node SeparateXyz

> Geometry node name: [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/separate_xyz.html)<br>
  Blender type: [Separate XYZ](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SeparateXyz(vector=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- vector : Vector

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- x : Float
- y : Float
- z : Float
