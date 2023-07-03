# Node *Handle Type Selection*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)
- geonodes name: `HandleTypeSelection`
- bl_idname: `GeometryNodeCurveHandleTypeSelection`

```python
from geonodes import nodes

node = nodes.HandleTypeSelection(handle_type='AUTO', mode={'RIGHT', 'LEFT'})
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveHandleTypeSelection.webp)

### Args:

#### Node parameter arguments:

- **handle_type** (str): default = 'AUTO' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
- **mode** (set): default = {'RIGHT', 'LEFT'}

### Output sockets:

- **selection** : [Boolean](Boolean.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[ControlPoint](ControlPoint.md)** |
| [handle_type_selection_node](ControlPoint.md#handle_type_selection_node) | `def handle_type_selection_node(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):` |
| [handle_type_selection](ControlPoint.md#handle_type_selection) | `def handle_type_selection(self, left=True, right=True, handle_type='AUTO'):` |
| [handle_type_selection](ControlPoint.md#handle_type_selection) | `def handle_type_selection_free(self, left=True, right=True):` |
| [handle_type_selection](ControlPoint.md#handle_type_selection) | `def handle_type_selection_auto(self, left=True, right=True):` |
| [handle_type_selection](ControlPoint.md#handle_type_selection) | `def handle_type_selection_vector(self, left=True, right=True):` |
| [handle_type_selection](ControlPoint.md#handle_type_selection) | `def handle_type_selection_align(self, left=True, right=True):` |

<sub>Go to [top](#node-Handle-Type-Selection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

