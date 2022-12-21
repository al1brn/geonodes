# Node Set ID

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeSetID`

```python
from geonodes import nodes

node = nodes.SetID(geometry=None, selection=None, ID=None)
```

#### Input socket arguments:

- geometry: Geometry
- selection: Boolean
- ID: Integer

#### Output sockets:

- **geometry** : Geometry

