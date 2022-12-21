# Node Attribute Statistic

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
- geonodes name: `AttributeStatistic`
- bl_idname: `GeometryNodeAttributeStatistic`

```python
from geonodes import nodes

node = nodes.AttributeStatistic(geometry=None, selection=None, attribute=None, data_type='FLOAT', domain='POINT')
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **attribute**: **data_type** dependant

#### Node parameter arguments:

- **data_type** (str): default = 'FLOAT' in ('FLOAT', 'FLOAT_VECTOR')
- **domain** (str): default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

### Output sockets:

- **mean** : ``data_type`` dependant
- **median** : ``data_type`` dependant
- **sum** : ``data_type`` dependant
- **min** : ``data_type`` dependant
- **max** : ``data_type`` dependant
- **range** : ``data_type`` dependant
- **standard_deviation** : ``data_type`` dependant
- **variance** : ``data_type`` dependant

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'FLOAT_VECTOR')
- Input sockets  : ['attribute']
- Output sockets : ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']
## Implementation

#### class [Geometry](Geometry.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e111c30>>](Geometry.md#attribute_statistic)
#### class [Domain](Domain.md)

 - [<bound method Generator.fname of <generator.code_gen.DomMethod object at 0x16e111b10>>](Domain.md#attribute_statistic)
 - [<bound method Generator.fname of <generator.code_gen.DomMethod object at 0x16e111bd0>>](Domain.md#attribute_mean)
 - [<bound method Generator.fname of <generator.code_gen.DomMethod object at 0x16e112020>>](Domain.md#attribute_median)
 - [<bound method Generator.fname of <generator.code_gen.DomMethod object at 0x16e111960>>](Domain.md#attribute_sum)
 - [<bound method Generator.fname of <generator.code_gen.DomMethod object at 0x16e111b70>>](Domain.md#attribute_min)
 - [<bound method Generator.fname of <generator.code_gen.DomMethod object at 0x16e111f30>>](Domain.md#attribute_max)
 - [<bound method Generator.fname of <generator.code_gen.DomMethod object at 0x16e111a20>>](Domain.md#attribute_range)
 - [<bound method Generator.fname of <generator.code_gen.DomMethod object at 0x16e111a50>>](Domain.md#attribute_std)
 - [<bound method Generator.fname of <generator.code_gen.DomMethod object at 0x16e1a3df0>>](Domain.md#attribute_var)
