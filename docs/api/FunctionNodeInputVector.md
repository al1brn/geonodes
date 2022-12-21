# Node Vector

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/vector.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputVector.html)
- geonodes name: `Vector`
- bl_idname: `FunctionNodeInputVector`

```python
from geonodes import nodes

node = nodes.Vector(vector=[0.0, 0.0, 0.0])
```

#### Node parameter arguments:

- vector (Vector): Node parameter, default = [0.0, 0.0, 0.0]

#### Output sockets:

- **vector** : Vector

