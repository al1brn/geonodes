
# Node SplitEdges

> Geometry node name: [Split Edges](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/split_edges.html)<br>
  Blender type: [Split Edges](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SplitEdges(mesh=None, selection=None, label=None)
```



## Arguments


### Input sockets

mesh : Mesh
- selection : Boolean

### Node label

- label : Geometry node display label (default=None)

## Output sockets

mesh : Mesh

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Mesh) [split_edges](section:Data socket Mesh/split_edges) : Method

