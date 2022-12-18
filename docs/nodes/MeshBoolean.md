
# Node MeshBoolean

> Geometry node name: [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html)<br>
  Blender type: [Mesh Boolean](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.MeshBoolean(*mesh_2, mesh_1=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE', label=None, node_color=None)
```



## Arguments


### Input sockets

- mesh_1 : Geometry
- mesh_2 : <m> Geometry
- self_intersection : Boolean
- hole_tolerant : Boolean

### Parameters

- operation : str (default = 'DIFFERENCE') in ('INTERSECT', 'UNION', 'DIFFERENCE')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- mesh : Mesh
- intersecting_edges : Boolean
