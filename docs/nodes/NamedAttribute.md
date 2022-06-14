
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
