# Node Set Material

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

#### class [Face](Face.md)

 - [set_material](Face.md#set_material)
 - [material](Face.md#material-property)
 - [material](Face.md#material)
#### class [Geometry](Geometry.md)

 - [set_material](Geometry.md#set_material)
#### class [Spline](Spline.md)

 - [set_material](Spline.md#set_material)
 - [material](Spline.md#material-property)
 - [material](Spline.md#material)
