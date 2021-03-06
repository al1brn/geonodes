
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

## Data sockets

> Data socket classes implementing this node.
  
  
- [Boolean](/docs/sockets/Boolean.md).[switch](/docs/sockets/Boolean.md#switch) : Method
- [Collection](/docs/sockets/Collection.md).[switch](/docs/sockets/Collection.md#switch) : Method
- [Color](/docs/sockets/Color.md).[switch](/docs/sockets/Color.md#switch) : Method
- [Float](/docs/sockets/Float.md).[switch](/docs/sockets/Float.md#switch) : Method
- [Geometry](/docs/sockets/Geometry.md).[switch](/docs/sockets/Geometry.md#switch) : Method
- [Image](/docs/sockets/Image.md).[switch](/docs/sockets/Image.md#switch) : Method
- [Integer](/docs/sockets/Integer.md).[switch](/docs/sockets/Integer.md#switch) : Method
- [Material](/docs/sockets/Material.md).[switch](/docs/sockets/Material.md#switch) : Method
- [Object](/docs/sockets/Object.md).[switch](/docs/sockets/Object.md#switch) : Method
- [String](/docs/sockets/String.md).[switch](/docs/sockets/String.md#switch) : Method
- [Texture](/docs/sockets/Texture.md).[switch](/docs/sockets/Texture.md#switch) : Method
- [Vector](/docs/sockets/Vector.md).[switch](/docs/sockets/Vector.md#switch) : Method
- [functions](/docs/sockets/functions.md).[switch](/docs/sockets/functions.md#switch) : Function
  
