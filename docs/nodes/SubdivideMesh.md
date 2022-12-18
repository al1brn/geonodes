
# Node SubdivideMesh

> Geometry node name: [Subdivide Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivide_mesh.html)<br>
  Blender type: [Subdivide Mesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideMesh.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SubdivideMesh(mesh=None, level=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- mesh : Mesh
- level : Integer

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- mesh : Mesh
