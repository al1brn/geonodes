# Node Cone

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cone.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCone.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeMeshCone`

```python
from geonodes import nodes

node = nodes.Cone(vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON')
```

#### Input socket arguments:

- vertices: Integer
- side_segments: Integer
- fill_segments: Integer
- radius_top: Float
- radius_bottom: Float
- depth: Float

#### Node parameter arguments:

- fill_type (str): Node parameter, default = 'NGON' in ('NONE', 'NGON', 'TRIANGLE_FAN')

#### Output sockets:

- **mesh** : Mesh
- **top** : Boolean
- **bottom** : Boolean
- **side** : Boolean

