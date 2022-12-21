# Node Sample Curve

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleCurve.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeSampleCurve`

```python
from geonodes import nodes

node = nodes.SampleCurve(curves=None, value=None, factor=None, length=None, curve_index=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False)
```

#### Input socket arguments:

- curves: Curve
- value: `data_type` dependant
- factor: Float
- length: Float
- curve_index: Integer

#### Node parameter arguments:

- data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- mode (str): Node parameter, default = 'FACTOR' in ('FACTOR', 'LENGTH')
- use_all_curves (bool): Node parameter, default = False

#### Output sockets:

- **value** : ``data_type`` dependant
- **position** : Vector
- **tangent** : Vector
- **normal** : Vector

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')- Input sockets  : ['value']- Output sockets : ['value']