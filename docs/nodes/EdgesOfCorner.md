
# Node EdgesOfCorner

> Geometry node name: [Edges of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_corner.html)<br>
  Blender type: [Edges of Corner](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfCorner.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.EdgesOfCorner(corner_index=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- corner_index : Integer

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- next_edge_index : Integer
- previous_edge_index : Integer
