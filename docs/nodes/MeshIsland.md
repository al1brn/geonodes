
# Node MeshIsland

> Geometry node name: [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html)<br>
  Blender type: [Mesh Island](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.MeshIsland(label=None, node_color=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- island_index : Integer
- island_count : Integer
