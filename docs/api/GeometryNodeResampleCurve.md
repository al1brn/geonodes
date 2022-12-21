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

#### Input socket arguments:

- curve: [Curve](Curve.md)
- selection: [Boolean](Boolean.md)
- count: [Integer](Integer.md)
- length: [Float](Float.md)

#### Node parameter arguments:

- mode (str): Node parameter, default = 'COUNT' in ('EVALUATED', 'COUNT', 'LENGTH')

#### Output sockets:

- **curve** : Curve

