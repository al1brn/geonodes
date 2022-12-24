# Node *Group Output*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/r.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.NodeGroupOutput.html)
- geonodes name: `GroupOutput`
- bl_idname: `NodeGroupOutput`

```python
from geonodes import nodes

node = nodes.GroupOutput(geometry=None, is_active_output=True)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_NodeGroupOutput.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)

#### Node parameter arguments:

- **is_active_output** (bool): default = True


<sub>Go to [top](#node-Group-Output) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

