
# Node EdgesOfVertex

> Geometry node name: [Edges of Vertex](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_vertex.html)<br>
  Blender type: [Edges of Vertex](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfVertex.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.EdgesOfVertex(vertex_index=None, weights=None, sort_index=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- vertex_index : Integer
- weights : Float
- sort_index : Integer

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- edge_index : Integer
- total : Integer
