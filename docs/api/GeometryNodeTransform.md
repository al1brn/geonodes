# Node Transform

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/transform.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html)
- geonodes name: `Transform`
- bl_idname: `GeometryNodeTransform`

```python
from geonodes import nodes

node = nodes.Transform(geometry=None, translation=None, rotation=None, scale=None)
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **translation**: [Vector](Vector.md)
- **rotation**: [Vector](Vector.md)
- **scale**: [Vector](Vector.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1683b0130>>](Geometry.md#transform)
