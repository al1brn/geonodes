
# Node FieldAtIndex

> Geometry node name: [Field at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html)<br>
  Blender type: [Field at Index](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.FieldAtIndex(index=None, value=None, data_type='FLOAT', domain='POINT', label=None, node_color=None)
```



## Arguments


### Input sockets

- index : Integer
- value : data_type dependant

### Parameters

- data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Data type dependant sockets

- Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : ['value']
- Output sockets : ['value']   
  
  

## Output sockets

- value : data_type dependant

## Data sockets

> Data socket classes implementing this node.
  
  
- [Boolean](/docs/sockets/Boolean.md).[field_at_index](/docs/sockets/Boolean.md#field_at_index) : Method
- [Color](/docs/sockets/Color.md).[field_at_index](/docs/sockets/Color.md#field_at_index) : Method
- [Float](/docs/sockets/Float.md).[field_at_index](/docs/sockets/Float.md#field_at_index) : Method
- [Integer](/docs/sockets/Integer.md).[field_at_index](/docs/sockets/Integer.md#field_at_index) : Method
- [Vector](/docs/sockets/Vector.md).[field_at_index](/docs/sockets/Vector.md#field_at_index) : Method
  
