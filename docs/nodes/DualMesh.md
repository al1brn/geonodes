
# Node DualMesh

> Geometry node name: [Dual Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/dual_mesh.html)<br>
  Blender type: [Dual Mesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeDualMesh.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.DualMesh(mesh=None, keep_boundaries=None, label=None)
```



## Arguments


### Input sockets

mesh : Mesh
- keep_boundaries : Boolean

### Node label

- label : Geometry node display label (default=None)

## Output sockets

dual_mesh : Geometry

## Data sockets

> Data socket classes implementing this node.
  
[class_name](docs/sockets/Mesh.md) [dual](docs/sockets/Mesh.md#dual) : Method

