
# Node Switch

> Geometry node name: [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/switch.html)<br>
  Blender type: [Switch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Switch(switch0=None, switch1=None, false=None, true=None, input_type='GEOMETRY', label=None)
```



## Arguments


### Input sockets

switch0 : Boolean
- switch1 : Boolean
- false : input_type dependant
- true : input_type dependant

### Parameters

input_type : str (default = 'GEOMETRY') in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL')

### Node label

- label : Geometry node display label (default=None)

## Data type dependant sockets

- Driving parameter : input_type in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL')
- Input sockets  : ['false', 'true']
- Output sockets : ['output']   
  
  

## Output sockets

output : input_type dependant

## Data sockets

> Data socket classes implementing this node.
  
[class_name](/docs/sockets/Boolean.md) [switch](/docs/sockets/Boolean.md#switch) : Method
- [class_name](/docs/sockets/Collection.md) [switch](/docs/sockets/Collection.md#switch) : Method
- [class_name](/docs/sockets/Float.md) [switch](/docs/sockets/Float.md#switch) : Method
- [class_name](/docs/sockets/Geometry.md) [switch](/docs/sockets/Geometry.md#switch) : Method
- [class_name](/docs/sockets/Image.md) [switch](/docs/sockets/Image.md#switch) : Method
- [class_name](/docs/sockets/Integer.md) [switch](/docs/sockets/Integer.md#switch) : Method
- [class_name](/docs/sockets/Material.md) [switch](/docs/sockets/Material.md#switch) : Method
- [class_name](/docs/sockets/Object.md) [switch](/docs/sockets/Object.md#switch) : Method
- [class_name](/docs/sockets/String.md) [switch](/docs/sockets/String.md#switch) : Method
- [class_name](/docs/sockets/Texture.md) [switch](/docs/sockets/Texture.md#switch) : Method
  
