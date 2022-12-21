# Node Instance Rotation

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_rotation.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceRotation.html)
- geonodes name: `InstanceRotation`
- bl_idname: `GeometryNodeInputInstanceRotation`

```python
from geonodes import nodes

node = nodes.InstanceRotation()
```

### Output sockets:

- **rotation** : [Vector](Vector.md)

## Implementation

#### [Instance](Instance.md)

 - [rotation](Instance.md#rotation-property)
  ```python
  def rotation(self)
  ```

#### [Instances](Instances.md)

 - [rotation](Instances.md#rotation-property)
  ```python
  def rotation(self)
  ```

