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

#### class [Curve](Curve.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x16d4fab60>>](Curve.md#resample)
 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x16d4fab30>>](Curve.md#resample_count)
 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x16d4fab00>>](Curve.md#resample_length)
 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x16d4faad0>>](Curve.md#resample_evaluated)
#### class [Spline](Spline.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4faaa0>>](Spline.md#resample)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4faa70>>](Spline.md#resample_count)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4faa40>>](Spline.md#resample_length)
 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4faa10>>](Spline.md#resample_evaluated)
