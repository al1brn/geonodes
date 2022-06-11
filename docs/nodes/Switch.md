
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
  
[class_name](section:Data socket Boolean) [switch](section:Data socket Boolean/switch) : Method
- [class_name](section:Data socket Collection) [switch](section:Data socket Collection/switch) : Method
- [class_name](section:Data socket Float) [switch](section:Data socket Float/switch) : Method
- [class_name](section:Data socket Geometry) [switch](section:Data socket Geometry/switch) : Method
- [class_name](section:Data socket Image) [switch](section:Data socket Image/switch) : Method
- [class_name](section:Data socket Integer) [switch](section:Data socket Integer/switch) : Method
- [class_name](section:Data socket Material) [switch](section:Data socket Material/switch) : Method
- [class_name](section:Data socket Object) [switch](section:Data socket Object/switch) : Method
- [class_name](section:Data socket String) [switch](section:Data socket String/switch) : Method
- [class_name](section:Data socket Texture) [switch](section:Data socket Texture/switch) : Method
  
