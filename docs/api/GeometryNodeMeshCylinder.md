# Node Cylinder

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cylinder.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCylinder.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeMeshCylinder`

```python
from geonodes import nodes

node = nodes.Cylinder(vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON')
```

#### Input socket arguments:

- vertices: Integer
- side_segments: Integer
- fill_segments: Integer
- radius: Float
- depth: Float

#### Node parameter arguments:

- fill_type (str): Node parameter, default = 'NGON' in ('NONE', 'NGON', 'TRIANGLE_FAN')

#### Output sockets:

- **mesh** : Mesh
- **top** : Boolean
- **side** : Boolean
- **bottom** : Boolean

