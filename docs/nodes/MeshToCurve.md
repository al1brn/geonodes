
# Node MeshToCurve

> Geometry node name: [Mesh to Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_curve.html)<br>
  Blender type: [Mesh to Curve](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------
```python
from geonodes import nodes
node = nodes.MeshToCurve(mesh=None, selection=None, label=None)
```



## Arguments


### Input sockets

- mesh : Mesh
- selection : Boolean

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- curve : Curve

## Data sockets

> Data socket classes implementing this node.
  
  
- [Mesh](/docs/sockets/Mesh.md).[to_curve](/docs/sockets/Mesh.md#to_curve) : Method
  
