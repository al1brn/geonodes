
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


- [Boolean](../sockets/Boolean.md) [switch](../sockets/Boolean.md#switch) : Method
- [Collection](../sockets/Collection.md) [switch](../sockets/Collection.md#switch) : Method
- [Float](../sockets/Float.md) [switch](../sockets/Float.md#switch) : Method
- [Geometry](../sockets/Geometry.md) [switch](../sockets/Geometry.md#switch) : Method
- [Image](../sockets/Image.md) [switch](../sockets/Image.md#switch) : Method
- [Integer](../sockets/Integer.md) [switch](../sockets/Integer.md#switch) : Method
- [Material](../sockets/Material.md) [switch](../sockets/Material.md#switch) : Method
- [Object](../sockets/Object.md) [switch](../sockets/Object.md#switch) : Method
- [String](../sockets/String.md) [switch](../sockets/String.md#switch) : Method
- [Texture](../sockets/Texture.md) [switch](../sockets/Texture.md#switch) : Method


