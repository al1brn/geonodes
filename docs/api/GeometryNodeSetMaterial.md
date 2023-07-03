# Node *Set Material*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)
- geonodes name: `SetMaterial`
- bl_idname: `GeometryNodeSetMaterial`

```python
from geonodes import nodes

node = nodes.SetMaterial(geometry=None, selection=None, material=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetMaterial.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **material**: [Material](Material.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Face](Face.md)** |
| [set_material](Face.md#set_material) | `def set_material(self, material=None):` |
| [material](Face.md#material) | `@property`<br> `def material(self):` |
| [material](Face.md#material) | `@material.setter
`<br> `def material(self, attr_value):` |
| **[Mesh](Mesh.md)** |
| [set_material](Mesh.md#set_material) | `def set_material(self, selection=None, material=None):` |
| **[Points](Points.md)** |
| [set_material](Points.md#set_material) | `def set_material(self, selection=None, material=None):` |
| [set_material](Points.md#set_material) | `def set_material(self, material=None):` |
| [material](Points.md#material) | `@property`<br> `def material(self):` |
| [material](Points.md#material) | `@material.setter
`<br> `def material(self, attr_value):` |
| **[Volume](Volume.md)** |
| [set_material](Volume.md#set_material) | `def set_material(self, selection=None, material=None):` |

<sub>Go to [top](#node-Set-Material) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

