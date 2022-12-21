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

#### [Domain](Domain.md)

 - [attribute_statistic](Domain.md#attribute_statistic) ```python nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain````
 - [attribute_mean](Domain.md#attribute_mean) ```python nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain````
 - [attribute_median](Domain.md#attribute_median) ```python nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain````
 - [attribute_sum](Domain.md#attribute_sum) ```python nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain````
 - [attribute_min](Domain.md#attribute_min) ```python nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain````
 - [attribute_max](Domain.md#attribute_max) ```python nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain````
 - [attribute_range](Domain.md#attribute_range) ```python nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain````
 - [attribute_std](Domain.md#attribute_std) ```python nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain````
 - [attribute_var](Domain.md#attribute_var) ```python nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain````
#### [Geometry](Geometry.md)

 - [attribute_statistic](Geometry.md#attribute_statistic) ```python nodes.AttributeStatistic(geometry=self, selection=selection, attribute=attribute, data_type=data_type_, domain=domain````
