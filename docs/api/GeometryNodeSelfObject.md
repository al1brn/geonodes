# Node *Self Object*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/self_object.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSelfObject.html)
- geonodes name: `SelfObject`
- bl_idname: `GeometryNodeSelfObject`

```python
from geonodes import nodes

node = nodes.SelfObject()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSelfObject.webp)

### Output sockets:

- **self_object** : [Object](Object.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Object](Object.md)** |
| [Self](Object.md#Self) | `@classmethod`<br> `def Self(cls):` |

<sub>Go to [top](#node-Self-Object) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

