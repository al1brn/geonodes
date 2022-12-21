# Node Set Curve Tilt

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_tilt.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)
- geonodes name: `SetCurveTilt`
- bl_idname: `GeometryNodeSetCurveTilt`

```python
from geonodes import nodes

node = nodes.SetCurveTilt(curve=None, selection=None, tilt=None)
```

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)
- **selection**: [Boolean](Boolean.md)
- **tilt**: [Float](Float.md)

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

#### [ControlPoint](ControlPoint.md)

 - [set_tilt](ControlPoint.md#set_tilt)
  ```python
  nodes.SetCurveTilt(curve=self.data_socket, selection=self.selection, tilt=tilt  ```

 - [tilt](ControlPoint.md#tilt)
  ```python
  nodes.SetCurveTilt(curve=self.data_socket, selection=self.selection, tilt=attr_value  ```

