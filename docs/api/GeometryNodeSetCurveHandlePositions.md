# Node Set Handle Positions

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeSetCurveHandlePositions`

```python
from geonodes import nodes

node = nodes.SetHandlePositions(curve=None, selection=None, position=None, offset=None, mode='LEFT')
```

#### Input socket arguments:

- curve: Curve
- selection: Boolean
- position: Vector
- offset: Vector

#### Node parameter arguments:

- mode (str): Node parameter, default = 'LEFT' in ('LEFT', 'RIGHT')

#### Output sockets:

- **curve** : Curve

