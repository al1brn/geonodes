# Node *Boolean*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/boolean.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputBool.html)
- geonodes name: `Boolean`
- bl_idname: `FunctionNodeInputBool`

```python
from geonodes import nodes

node = nodes.Boolean(boolean=False)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeInputBool.webp)

### Args:

#### Node parameter arguments:

- **boolean** (bool): default = False

### Output sockets:

- **boolean** : [Boolean](Boolean.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Boolean](Boolean.md)** |
| [Boolean](Boolean.md#Boolean) | `@classmethod`<br> `def Boolean(cls, boolean=False):` |

<sub>Go to [top](#node-Boolean) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

