
# Node FieldAtIndex

> Geometry node name: [Field at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/field_at_index.html)<br>
  Blender type: [Field at Index](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.FieldAtIndex(index=None, value=None, data_type='FLOAT', domain='POINT', label=None)
```



## Arguments


### Input sockets

index : Integer
- value : data_type dependant

### Parameters

data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

### Node label

- label : Geometry node display label (default=None)

## Data type dependant sockets

- Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : ['value']
- Output sockets : ['value']   
  
  

## Output sockets

value : data_type dependant

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Boolean) [field_at_index](section:Data socket Boolean/field_at_index) : Method
- [class_name](section:Data socket Color) [field_at_index](section:Data socket Color/field_at_index) : Method
- [class_name](section:Data socket Float) [field_at_index](section:Data socket Float/field_at_index) : Method
- [class_name](section:Data socket Integer) [field_at_index](section:Data socket Integer/field_at_index) : Method
- [class_name](section:Data socket Vector) [field_at_index](section:Data socket Vector/field_at_index) : Method
  
