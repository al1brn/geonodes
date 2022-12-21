# Node Ico Sphere

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/icosphere.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshIcoSphere.html)
- geonodes name: `IcoSphere`
- bl_idname: `GeometryNodeMeshIcoSphere`

```python
from geonodes import nodes

node = nodes.IcoSphere(radius=None, subdivisions=None)
```

### Args:

#### Input socket arguments:

- **radius**: [Float](Float.md)
- **subdivisions**: [Integer](Integer.md)

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

#### class [Mesh](Mesh.md)

 - [IcoSphere](Mesh.md#IcoSphere-classmethod)