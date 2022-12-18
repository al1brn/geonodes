
# Node IcoSphere

> Geometry node name: [Ico Sphere](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/icosphere.html)<br>
  Blender type: [Ico Sphere](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshIcoSphere.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.IcoSphere(radius=None, subdivisions=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- radius : Float
- subdivisions : Integer

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- mesh : Mesh
