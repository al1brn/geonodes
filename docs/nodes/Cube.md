
# Node Cube

> Geometry node name: [Cube](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cube.html)<br>
  Blender type: [Cube](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCube.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Cube(size=None, vertices_x=None, vertices_y=None, vertices_z=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- size : Vector
- vertices_x : Integer
- vertices_y : Integer
- vertices_z : Integer

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- mesh : Mesh
