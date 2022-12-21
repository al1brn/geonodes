# Node 'Set Material'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)
- geonodes name: `SetMaterial`
- bl_idname: `GeometryNodeSetMaterial`

```python
from geonodes import nodes

node = nodes.SetMaterial(geometry=None, selection=None, material=None)
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **material**: [Material](Material.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

### [Face](Face.md)

| Name | Definition |
|------|------------|
 | [set_material](Face.md#set_material) | `def set_material(self, material=None):` |
 | [material](Face.md#material-property) | `def material(self):` |
 | [material](Face.md#material) | `def material(self, attr_value):` |

### [Geometry](Geometry.md)

| Name | Definition |
|------|------------|
 | [set_material](Geometry.md#set_material) | `def set_material(self, selection=None, material=None):` |

### [Spline](Spline.md)

| Name | Definition |
|------|------------|
 | [set_material](Spline.md#set_material) | `def set_material(self, material=None):` |
 | [material](Spline.md#material-property) | `def material(self):` |
 | [material](Spline.md#material) | `def material(self, attr_value):` |

<sub>Go to [top](#node-{wnode.bnode.name}) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

