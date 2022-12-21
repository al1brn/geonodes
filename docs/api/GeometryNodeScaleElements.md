# Node Scale Elements

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)
- geonodes name: `ScaleElements`
- bl_idname: `GeometryNodeScaleElements`

```python
from geonodes import nodes

node = nodes.ScaleElements(geometry=None, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM')
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **scale**: [Float](Float.md)
- **center**: [Vector](Vector.md)
- **axis**: [Vector](Vector.md)

#### Node parameter arguments:

- **domain** (str): default = 'FACE' in ('FACE', 'EDGE')
- **scale_mode** (str): default = 'UNIFORM' in ('UNIFORM', 'SINGLE_AXIS')

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1683b1300>>](Mesh.md#scale_elements)
 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1683b2230>>](Mesh.md#scale_uniform)
 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1683b1720>>](Mesh.md#scale_single_axis)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1683b1c30>>](Face.md#scale_uniform)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1683b30d0>>](Face.md#scale_single_axis)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1683b1210>>](Edge.md#scale_uniform)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1683b2d40>>](Edge.md#scale_single_axis)
