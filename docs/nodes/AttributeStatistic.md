
# Class AttributeStatistic

> Geometry node name: _'Attribute Statistic'_<br>Blender type:  **GeometryNodeAttributeStatistic**

## Initialization


```python
from geonodes import nodes
node = nodes.AttributeStatistic(geometry=None, selection=None, attribute=None, data_type='FLOAT', domain='POINT', label=None)
```


### Arguments


#### Input sockets



- **geometry** : _Geometry_
- **selection** : _Boolean_
- **attribute** : **data_type** dependant



#### Parameters



- **data_type** : _'FLOAT'_ in ('FLOAT', 'FLOAT_VECTOR')
- **domain** : _'POINT'_ in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')



#### Node label



- **label** : Geometry node label



## Data type dependant sockets



- Driving parameter : **data_type** in ('FLOAT', 'FLOAT_VECTOR')
- Input sockets : attribute
- Output sockets : mean median sum min max range standard_deviation variance



## Output sockets



- **mean** : **data_type** dependant
- **median** : **data_type** dependant
- **sum** : **data_type** dependant
- **min** : **data_type** dependant
- **max** : **data_type** dependant
- **range** : **data_type** dependant
- **standard_deviation** : **data_type** dependant
- **variance** : **data_type** dependant



## Data sockets

> Data socket classes implementing this node


- [Float](aaa). [attribute_statistic](bbb) : Method
- [Vector](aaa). [attribute_statistic](bbb) : Method


