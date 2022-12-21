# Node Set Handle Positions

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)
- geonodes name: `SetHandlePositions`
- bl_idname: `GeometryNodeSetCurveHandlePositions`

```python
from geonodes import nodes

node = nodes.SetHandlePositions(curve=None, selection=None, position=None, offset=None, mode='LEFT')
```

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)
- **selection**: [Boolean](Boolean.md)
- **position**: [Vector](Vector.md)
- **offset**: [Vector](Vector.md)

#### Node parameter arguments:

- **mode** (str): default = 'LEFT' in ('LEFT', 'RIGHT')

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

#### [ControlPoint](ControlPoint.md)

 - [set_handle_positions](ControlPoint.md#set_handle_positions)
  ```python
  nodes.SetHandlePositions(curve=self.data_socket, selection=self.selection, position=position, offset=offset, mode=mode  ```

 - [set_handle_positions_left](ControlPoint.md#set_handle_positions_left)
  ```python
  nodes.SetHandlePositions(curve=curve, selection=self.selection, position=position, offset=offset, mode='LEFT'  ```

 - [set_handle_positions_right](ControlPoint.md#set_handle_positions_right)
  ```python
  nodes.SetHandlePositions(curve=curve, selection=self.selection, position=position, offset=offset, mode='RIGHT'  ```

 - [left_handle_positions](ControlPoint.md#left_handle_positions)
  ```python
  nodes.SetHandlePositions(curve=curve, selection=self.selection, position=attr_value, offset=offset, mode='LEFT'  ```

 - [right_handle_positions](ControlPoint.md#right_handle_positions)
  ```python
  nodes.SetHandlePositions(curve=curve, selection=self.selection, position=attr_value, offset=offset, mode='RIGHT'  ```

