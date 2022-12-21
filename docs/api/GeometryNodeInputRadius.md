# Node Radius

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)
- geonodes name: `Radius`
- bl_idname: `GeometryNodeInputRadius`

```python
from geonodes import nodes

node = nodes.Radius()
```

### Output sockets:

- **radius** : [Float](Float.md)

## Implementation

#### [CloudPoint](CloudPoint.md)

 - [radius](CloudPoint.md#radius-property)
  ```python
  def radius(self)
  ```

#### [ControlPoint](ControlPoint.md)

 - [radius](ControlPoint.md#radius-property)
  ```python
  def radius(self)
  ```

#### [Geometry](Geometry.md)

 - [radius](Geometry.md#radius-property)
  ```python
  def radius(self)
  ```

