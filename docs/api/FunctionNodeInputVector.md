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

### Args:

#### Node parameter arguments:

- **vector** (Vector): default = [0.0, 0.0, 0.0]

### Output sockets:

- **vector** : [Vector](Vector.md)

## Implementation

#### [Vector](Vector.md)

 - [Vector](Vector.md#Vector-classmethod) ```python nodes.Vector(vector=vector````
