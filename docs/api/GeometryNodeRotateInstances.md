# Node Rotate Instances

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRotateInstances.html)
- geonodes name: `RotateInstances`
- bl_idname: `GeometryNodeRotateInstances`

```python
from geonodes import nodes

node = nodes.RotateInstances(instances=None, selection=None, rotation=None, pivot_point=None, local_space=None)
```

### Args:

#### Input socket arguments:

- **instances**: [Instances](Instances.md)
- **selection**: [Boolean](Boolean.md)
- **rotation**: [Vector](Vector.md)
- **pivot_point**: [Vector](Vector.md)
- **local_space**: [Boolean](Boolean.md)

### Output sockets:

- **instances** : [Instances](Instances.md)

## Implementation

### [Instance](Instance.md)

| Name | Definition |
|------|------------|
 | [rotate](Instance.md#rotate) | `def rotate(self, rotation=None, pivot_point=None, local_space=None):` |

### [Instances](Instances.md)

| Name | Definition |
|------|------------|
 | [rotate](Instances.md#rotate) | `def rotate(self, selection=None, rotation=None, pivot_point=None, local_space=None):` |

