
# Node JoinGeometry

> Geometry node name: [Join Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/join_geometry.html)<br>
  Blender type: [Join Geometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.JoinGeometry(*geometry, label=None)
```



## Arguments


### Input sockets

geometry : *Geometry

### Node label

- label : Geometry node display label (default=None)

## Output sockets

geometry : Geometry

## Data sockets

> Data socket classes implementing this node.
  
[class_name](/docs/sockets/Geometry.md) [join](/docs/sockets/Geometry.md#join) : Method

