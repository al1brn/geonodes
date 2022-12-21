# Node Remove Named Attribute

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)
- geonodes name: `RemoveNamedAttribute`
- bl_idname: `GeometryNodeRemoveAttribute`

```python
from geonodes import nodes

node = nodes.RemoveNamedAttribute(geometry=None, name=None)
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **name**: [String](String.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1639dc3d0>>](Geometry.md#remove_named_attribute)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1639dc040>>](Domain.md#remove_named_attribute)
