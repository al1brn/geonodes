# Node Position

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)
- geonodes name: `Position`
- bl_idname: `GeometryNodeInputPosition`

```python
from geonodes import nodes

node = nodes.Position()
```

### Output sockets:

- **position** : [Vector](Vector.md)

## Implementation

#### [Domain](Domain.md)

 - [position](Domain.md#position-property)
  ```python
  def position(self)
  ```

#### [Geometry](Geometry.md)

 - [position](Geometry.md#position-property)
  ```python
  def position(self)
  ```

