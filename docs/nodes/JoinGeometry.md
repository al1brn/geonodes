
# Node JoinGeometry

> Geometry node name: [Join Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html)<br>
  Blender type: [Join Geometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.JoinGeometry(*geometry, label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : <m> Geometry

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- geometry : Geometry
