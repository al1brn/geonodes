
# Node AccumulateField

> Geometry node name: [Accumulate Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/accumulate_field.html)<br>
  Blender type: [Accumulate Field](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.AccumulateField(value=None, group_index=None, data_type='FLOAT', domain='POINT', label=None)
```



## Arguments


### Input sockets

- value : data_type dependant
- group_index : Integer

### Parameters

- data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR')
- domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

### Node label

- label : Geometry node display label (default=None)

## Data type dependant sockets

- Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR')
- Input sockets  : ['value']
- Output sockets : ['leading', 'trailing', 'total']   
  
  

## Output sockets

- leading : data_type dependant
- trailing : data_type dependant
- total : data_type dependant

## Data sockets

> Data socket classes implementing this node.
  
  
- [Float](/docs/sockets/Float.md).[accumulate_field](/docs/sockets/Float.md#accumulate_field) : Method
- [Integer](/docs/sockets/Integer.md).[accumulate_field](/docs/sockets/Integer.md#accumulate_field) : Method
- [Vector](/docs/sockets/Vector.md).[accumulate_field](/docs/sockets/Vector.md#accumulate_field) : Method
  
