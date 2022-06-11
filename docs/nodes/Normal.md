
# Node Normal

> Geometry node name: [Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/normal.html)<br>
  Blender type: [Normal](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Normal(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

normal : Vector

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Geometry) [capture_normal](section:Data socket Geometry/capture_normal) : Capture attribute
- [class_name](section:Data socket Geometry) [normal](section:Data socket Geometry/normal) : Attribute
  
