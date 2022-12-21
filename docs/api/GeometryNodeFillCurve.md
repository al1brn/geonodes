# Node Fill Curve

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)
- geonodes name: `FillCurve`
- bl_idname: `GeometryNodeFillCurve`

```python
from geonodes import nodes

node = nodes.FillCurve(curve=None, mode='TRIANGLES')
```

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)

#### Node parameter arguments:

- **mode** (str): default = 'TRIANGLES' in ('TRIANGLES', 'NGONS')

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164097af0>>](Curve.md#fill)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164097b80>>](Curve.md#fill_triangles)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x164097a60>>](Curve.md#fill_ngons)
