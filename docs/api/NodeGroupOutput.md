# Node 'Group Output'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/r.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.NodeGroupOutput.html)
- geonodes name: `GroupOutput`
- bl_idname: `NodeGroupOutput`

```python
from geonodes import nodes

node = nodes.GroupOutput(geometry=None, is_active_output=True)
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)

#### Node parameter arguments:

- **is_active_output** (bool): default = True

<sub>Go to [top](#node-{wnode.bnode.name}) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

