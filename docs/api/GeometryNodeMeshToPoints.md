# Node Mesh to Points

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_points.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html)
- geonodes name: `MeshToPoints`
- bl_idname: `GeometryNodeMeshToPoints`

```python
from geonodes import nodes

node = nodes.MeshToPoints(mesh=None, selection=None, position=None, radius=None, mode='VERTICES')
```

#### Input socket arguments:

- `mesh`: [Mesh](Mesh.md)
- `selection`: [Boolean](Boolean.md)
- `position`: [Vector](Vector.md)
- `radius`: [Float](Float.md)

#### Node parameter arguments:

- mode (str): Node parameter, default = 'VERTICES' in ('VERTICES', 'EDGES', 'FACES', 'CORNERS')

#### Output sockets:

- **points** : [Points](Points.md)

