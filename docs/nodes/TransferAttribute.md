
# Node TransferAttribute

> Geometry node name: [Transfer Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/transfer_attribute.html)<br>
  Blender type: [Transfer Attribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeTransfer.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.TransferAttribute(source=None, attribute=None, source_position=None, index=None, data_type='FLOAT', domain='POINT', mapping='NEAREST_FACE_INTERPOLATED', label=None)
```



## Arguments


### Input sockets

source : Geometry
- attribute : data_type dependant
- source_position : Vector
- index : Integer

### Parameters

data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- mapping : str (default = 'NEAREST_FACE_INTERPOLATED') in ('NEAREST_FACE_INTERPOLATED', 'NEAREST', 'INDEX')

### Node label

- label : Geometry node display label (default=None)

## Data type dependant sockets

- Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : ['attribute']
- Output sockets : ['attribute']   
  
  

## Output sockets

attribute : data_type dependant

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Boolean) [transfer_attribute](section:Data socket Boolean/transfer_attribute) : Method
- [class_name](section:Data socket Color) [transfer_attribute](section:Data socket Color/transfer_attribute) : Method
- [class_name](section:Data socket Float) [transfer_attribute](section:Data socket Float/transfer_attribute) : Method
- [class_name](section:Data socket Geometry) [transfer_boolean](section:Data socket Geometry/transfer_boolean) : Method
- [class_name](section:Data socket Geometry) [transfer_color](section:Data socket Geometry/transfer_color) : Method
- [class_name](section:Data socket Geometry) [transfer_float](section:Data socket Geometry/transfer_float) : Method
- [class_name](section:Data socket Geometry) [transfer_integer](section:Data socket Geometry/transfer_integer) : Method
- [class_name](section:Data socket Geometry) [transfer_vector](section:Data socket Geometry/transfer_vector) : Method
- [class_name](section:Data socket Integer) [transfer_attribute](section:Data socket Integer/transfer_attribute) : Method
- [class_name](section:Data socket Vector) [transfer_attribute](section:Data socket Vector/transfer_attribute) : Method
  
