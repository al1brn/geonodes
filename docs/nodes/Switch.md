
# Class Switch

> Geometry node name: _'Switch'_<br>Blender type:  **GeometryNodeSwitch**

## Initialization


```python
from geonodes import nodes
node = nodes.Switch(switch0=None, switch1=None, false=None, true=None, input_type='GEOMETRY', label=None)
```


### Arguments


#### Input sockets



- **switch0** : _Boolean_
- **switch1** : _Boolean_
- **false** : **input_type** dependant
- **true** : **input_type** dependant



#### Parameters



- **input_type** : _'GEOMETRY'_ in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL')



#### Node label



- **label** : Geometry node label



## Data type dependant sockets



- Driving parameter : **input_type** in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL')
- Input sockets : false true
- Output sockets : output



## Output sockets



- **output** : **input_type** dependant



## Data sockets

> Data socket classes implementing this node


- [Boolean](aaa). [switch](bbb) : Method
- [Collection](aaa). [switch](bbb) : Method
- [Float](aaa). [switch](bbb) : Method
- [Geometry](aaa). [switch](bbb) : Method
- [Image](aaa). [switch](bbb) : Method
- [Integer](aaa). [switch](bbb) : Method
- [Material](aaa). [switch](bbb) : Method
- [Object](aaa). [switch](bbb) : Method
- [String](aaa). [switch](bbb) : Method
- [Texture](aaa). [switch](bbb) : Method


