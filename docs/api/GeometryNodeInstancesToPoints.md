# Node 'Instances to Points'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstancesToPoints.html)
- geonodes name: `InstancesToPoints`
- bl_idname: `GeometryNodeInstancesToPoints`

```python
from geonodes import nodes

node = nodes.InstancesToPoints(instances=None, selection=None, position=None, radius=None)
```

### Args:

#### Input socket arguments:

- **instances**: [Instances](Instances.md)
- **selection**: [Boolean](Boolean.md)
- **position**: [Vector](Vector.md)
- **radius**: [Float](Float.md)

### Output sockets:

- **points** : [Points](Points.md)

## Implementation

### [Instance](Instance.md)

| Name | Definition |
|------|------------|
 | [to_points](Instance.md#to_points) | `def to_points(self, position=None, radius=None):` |

### [Instances](Instances.md)

| Name | Definition |
|------|------------|
 | [to_points](Instances.md#to_points) | `def to_points(self, selection=None, position=None, radius=None):` |

<sub>Go to [top](#node-{wnode.bnode.name}) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

