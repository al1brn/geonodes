# Node *Duplicate Elements*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)
- geonodes name: `DuplicateElements`
- bl_idname: `GeometryNodeDuplicateElements`

```python
from geonodes import nodes

node = nodes.DuplicateElements(geometry=None, selection=None, amount=None, domain='POINT')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDuplicateElements.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **amount**: [Integer](Integer.md)

#### Node parameter arguments:

- **domain** (str): default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'SPLINE', 'INSTANCE')

### Output sockets:

- **geometry** : [Geometry](Geometry.md)
- **duplicate_index** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[CloudPoint](CloudPoint.md)** |
| [duplicate](CloudPoint.md#duplicate) | `def duplicate(self, amount=None):` |
| **[ControlPoint](ControlPoint.md)** |
| [duplicate](ControlPoint.md#duplicate) | `def duplicate(self, amount=None):` |
| **[Edge](Edge.md)** |
| [duplicate](Edge.md#duplicate) | `def duplicate(self, amount=None):` |
| **[Face](Face.md)** |
| [duplicate](Face.md#duplicate) | `def duplicate(self, amount=None):` |
| **[Geometry](Geometry.md)** |
| [duplicate](Geometry.md#duplicate) | `def duplicate(self, selection=None, amount=None, domain='POINT'):` |
| **[Instance](Instance.md)** |
| [duplicate](Instance.md#duplicate) | `def duplicate(self, amount=None):` |
| **[Spline](Spline.md)** |
| [duplicate](Spline.md#duplicate) | `def duplicate(self, amount=None):` |
| **[Vertex](Vertex.md)** |
| [duplicate](Vertex.md#duplicate) | `def duplicate(self, amount=None):` |

<sub>Go to [top](#node-Duplicate-Elements) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

