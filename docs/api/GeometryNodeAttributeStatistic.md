# Node *Attribute Statistic*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
- geonodes name: `AttributeStatistic`
- bl_idname: `GeometryNodeAttributeStatistic`

```python
from geonodes import nodes

node = nodes.AttributeStatistic(geometry=None, selection=None, attribute=None, data_type='FLOAT', domain='POINT')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeStatistic.webp)

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

| Class or method name | Definition |
|----------------------|------------|
| **[Domain](Domain.md)** |
| [attribute_statistic](Domain.md#attribute_statistic) | `def attribute_statistic(self, attribute=None):` |
| [attribute_mean](Domain.md#attribute_mean) | `def attribute_mean(self, attribute=None):` |
| [attribute_median](Domain.md#attribute_median) | `def attribute_median(self, attribute=None):` |
| [attribute_sum](Domain.md#attribute_sum) | `def attribute_sum(self, attribute=None):` |
| [attribute_min](Domain.md#attribute_min) | `def attribute_min(self, attribute=None):` |
| [attribute_max](Domain.md#attribute_max) | `def attribute_max(self, attribute=None):` |
| [attribute_range](Domain.md#attribute_range) | `def attribute_range(self, attribute=None):` |
| [attribute_std](Domain.md#attribute_std) | `def attribute_std(self, attribute=None):` |
| [attribute_var](Domain.md#attribute_var) | `def attribute_var(self, attribute=None):` |
| **[Geometry](Geometry.md)** |
| [attribute_statistic](Geometry.md#attribute_statistic) | `def attribute_statistic(self, selection=None, attribute=None, domain='POINT'):` |

<sub>Go to [top](#node-Attribute-Statistic) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

