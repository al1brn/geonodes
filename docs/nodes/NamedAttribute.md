
# Node NamedAttribute

> Geometry node name: [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)<br>
  Blender type: [Named Attribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.NamedAttribute(name=None, data_type='FLOAT', label=None, node_color=None)
```



## Arguments


### Input sockets

- name : String

### Parameters

- data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Data type dependant sockets

- Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : []
- Output sockets : ['attribute']   
  
  

## Output sockets

- attribute : data_type dependant

## Data sockets

> Data socket classes implementing this node.
  
  
- [Geometry](/docs/sockets/Geometry.md).[capture_named_attribute](/docs/sockets/Geometry.md#capture_named_attribute) : Capture attribute
- [Geometry](/docs/sockets/Geometry.md).[capture_named_boolean](/docs/sockets/Geometry.md#capture_named_boolean) : Capture attribute
- [Geometry](/docs/sockets/Geometry.md).[capture_named_boolean](/docs/sockets/Geometry.md#capture_named_boolean) : Capture attribute
- [Geometry](/docs/sockets/Geometry.md).[capture_named_color](/docs/sockets/Geometry.md#capture_named_color) : Capture attribute
- [Geometry](/docs/sockets/Geometry.md).[capture_named_integer](/docs/sockets/Geometry.md#capture_named_integer) : Capture attribute
- [Geometry](/docs/sockets/Geometry.md).[capture_named_vector](/docs/sockets/Geometry.md#capture_named_vector) : Capture attribute
  
