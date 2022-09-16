
# Node ShortestEdgePaths

> Geometry node name: [Shortest Edge Paths](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/shortest_edge_paths.html)<br>
  Blender type: [Shortest Edge Paths](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShortestEdgePaths.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.ShortestEdgePaths(end_vertex=None, edge_cost=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- end_vertex : Boolean
- edge_cost : Float

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- next_vertex_index : Integer
- total_cost : Float
