
# Node FlipFaces

> Geometry node name: [Flip Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/flip_faces.html)<br>
  Blender type: [Flip Faces](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.FlipFaces(mesh=None, selection=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- mesh : Mesh
- selection : Boolean

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- mesh : Mesh
