
# Node Switch

> Geometry node name: [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)<br>
  Blender type: [Switch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Switch(switch=None, false=None, true=None, input_type='GEOMETRY', label=None, node_color=None)
```



## Arguments


### Input sockets

- switch : input_type dependant
- false : input_type dependant
- true : input_type dependant

### Parameters

- input_type : str (default = 'GEOMETRY') in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Data type dependant sockets

- Driving parameter : input_type in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL')
- Input sockets  : ['switch', 'false', 'true']
- Output sockets : ['output']   
  
  

## Output sockets

- output : input_type dependant
