# Node *Viewer*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)
- geonodes name: `Viewer`
- bl_idname: `GeometryNodeViewer`

```python
from geonodes import nodes

node = nodes.Viewer(geometry=None, value=None, data_type='FLOAT', domain='AUTO')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeViewer.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **value**: **data_type** dependant

#### Node parameter arguments:

- **data_type** (str): default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- **domain** (str): default = 'AUTO' in ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : ['value']
- Output sockets : []
## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Domain](Domain.md)** |
| [viewer](Domain.md#viewer) | `def viewer(self, value=None):` |
| [view](Domain.md#view) | `def view(self, value=None):` |
| **[Geometry](Geometry.md)** |
| [viewer](Geometry.md#viewer) | `def viewer(self, value=None, domain='AUTO'):` |
| [view](Geometry.md#view) | `def view(self, value=None, domain='AUTO'):` |

<sub>Go to [top](#node-Viewer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

