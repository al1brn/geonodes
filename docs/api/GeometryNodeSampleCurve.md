# Node *Sample Curve*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleCurve.html)
- geonodes name: `SampleCurve`
- bl_idname: `GeometryNodeSampleCurve`

```python
from geonodes import nodes

node = nodes.SampleCurve(curves=None, value=None, factor=None, length=None, curve_index=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleCurve.webp)

### Args:

#### Input socket arguments:

- **curves**: [Curve](Curve.md)
- **value**: **data_type** dependant
- **factor**: [Float](Float.md)
- **length**: [Float](Float.md)
- **curve_index**: [Integer](Integer.md)

#### Node parameter arguments:

- **data_type** (str): default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- **mode** (str): default = 'FACTOR' in ('FACTOR', 'LENGTH')
- **use_all_curves** (bool): default = False

### Output sockets:

- **value** : ``data_type`` dependant
- **position** : [Vector](Vector.md)
- **tangent** : [Vector](Vector.md)
- **normal** : [Vector](Vector.md)

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : ['value']
- Output sockets : ['value']
## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Curve](Curve.md)** |
| [sample](Curve.md#sample) | `def sample(self, value=None, factor=None, length=None, curve_index=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False):` |

<sub>Go to [top](#node-Sample-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

