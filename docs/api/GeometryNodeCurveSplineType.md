# Node Set Spline Type

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)
- geonodes name: `SetSplineType`
- bl_idname: `GeometryNodeCurveSplineType`

```python
from geonodes import nodes

node = nodes.SetSplineType(curve=None, selection=None, spline_type='POLY')
```

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)
- **selection**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **spline_type** (str): default = 'POLY' in ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS')

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1640975b0>>](Spline.md#set_type)
 - [<bound method Generator.fname of <generator.code_gen.PropReadError object at 0x164096c50>>](Spline.md#type-property)
 - [<bound method Generator.fname of <generator.code_gen.DomSetter object at 0x1683b1960>>](Spline.md#type)
