
# Node DualMesh

> Geometry node name: [Dual Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/dual_mesh.html)<br>
  Blender type: [Dual Mesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeDualMesh.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.DualMesh(mesh=None, keep_boundaries=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- mesh : Mesh
- keep_boundaries : Boolean

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- dual_mesh : Geometry
