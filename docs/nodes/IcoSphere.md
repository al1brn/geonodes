
# Node IcoSphere

> Geometry node name: [Ico Sphere](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/ico_sphere.html)<br>
  Blender type: [Ico Sphere](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshIcoSphere.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.IcoSphere(radius=None, subdivisions=None, label=None)
```



## Arguments


### Input sockets

radius : Float
- subdivisions : Integer

### Node label

- label : Geometry node display label (default=None)

## Output sockets

mesh : Mesh

## Data sockets

> Data socket classes implementing this node.
  
[Mesh](/docs/sockets/Mesh.md).[IcoSphere](/docs/sockets/Mesh.md#icosphere) : Constructor

