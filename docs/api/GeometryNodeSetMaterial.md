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

#### class [Geometry](Geometry.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x16d4f8700>>](Geometry.md#set_material)
#### class [Face](Face.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f86d0>>](Face.md#set_material)
 - [<bound method Generator.fname of <generator.code_gen.PropReadError object at 0x16d4f86a0>>](Face.md#material-property)
 - [<bound method Generator.fname of <generator.code_gen.DomSetter object at 0x16d4f8670>>](Face.md#material)
#### class [Spline](Spline.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f86d0>>](Spline.md#set_material)
 - [<bound method Generator.fname of <generator.code_gen.PropReadError object at 0x16d4f86a0>>](Spline.md#material-property)
 - [<bound method Generator.fname of <generator.code_gen.DomSetter object at 0x16d4f8670>>](Spline.md#material)
