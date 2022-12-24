# Node *Instance on Points*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)
- geonodes name: `InstanceOnPoints`
- bl_idname: `GeometryNodeInstanceOnPoints`

```python
from geonodes import nodes

node = nodes.InstanceOnPoints(points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInstanceOnPoints.webp)

### Args:

#### Input socket arguments:

- **points**: [Points](Points.md)
- **selection**: [Boolean](Boolean.md)
- **instance**: [Geometry](Geometry.md)
- **pick_instance**: [Boolean](Boolean.md)
- **instance_index**: [Integer](Integer.md)
- **rotation**: [Vector](Vector.md)
- **scale**: [Vector](Vector.md)

### Output sockets:

- **instances** : [Instances](Instances.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[CloudPoint](CloudPoint.md)** |
| [instance_on_points](CloudPoint.md#instance_on_points) | `def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):` |
| **[ControlPoint](ControlPoint.md)** |
| [instance_on_points](ControlPoint.md#instance_on_points) | `def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):` |
| **[Curve](Curve.md)** |
| [instance_on_points](Curve.md#instance_on_points) | `def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):` |
| **[Instances](Instances.md)** |
| [InstanceOnPoints](Instances.md#InstanceOnPoints) | `@classmethod`<br> `def InstanceOnPoints(cls, points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):` |
| [on_points](Instances.md#on_points) | `def on_points(self, points=None, selection=None, pick_instance=None, instance_index=None, rotation=None, scale=None):` |
| **[Mesh](Mesh.md)** |
| [instance_on_points](Mesh.md#instance_on_points) | `def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):` |
| **[Points](Points.md)** |
| [instance_on_points](Points.md#instance_on_points) | `def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):` |
| **[Vertex](Vertex.md)** |
| [instance_on_points](Vertex.md#instance_on_points) | `def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):` |

<sub>Go to [top](#node-Instance-on-Points) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

