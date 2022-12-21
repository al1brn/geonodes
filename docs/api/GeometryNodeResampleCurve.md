# Node Resample Curve

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)
- geonodes name: `ResampleCurve`
- bl_idname: `GeometryNodeResampleCurve`

```python
from geonodes import nodes

node = nodes.ResampleCurve(curve=None, selection=None, count=None, length=None, mode='COUNT')
```

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)
- **selection**: [Boolean](Boolean.md)
- **count**: [Integer](Integer.md)
- **length**: [Float](Float.md)

#### Node parameter arguments:

- **mode** (str): default = 'COUNT' in ('EVALUATED', 'COUNT', 'LENGTH')

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1640972b0>>](Curve.md#resample)
 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x164097220>>](Curve.md#resample_count)
 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x164097100>>](Curve.md#resample_length)
 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x164095b70>>](Curve.md#resample_evaluated)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1640970d0>>](Spline.md#resample)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1640978e0>>](Spline.md#resample_count)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x164096e30>>](Spline.md#resample_length)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x164096f20>>](Spline.md#resample_evaluated)
