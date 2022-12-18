
# Node EdgePathsToCurves

> Geometry node name: [Edge Paths to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_curves.html)<br>
  Blender type: [Edge Paths to Curves](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.EdgePathsToCurves(mesh=None, start_vertices=None, next_vertex_index=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- mesh : Mesh
- start_vertices : Boolean
- next_vertex_index : Integer

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- curves : Curve
