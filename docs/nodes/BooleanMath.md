
# Class BooleanMath

> Geometry node name: _'Boolean Math'_<br>Blender type:  **FunctionNodeBooleanMath**
[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.BooleanMath(boolean0=None, boolean1=None, operation='AND', label=None)
```


### Arguments


#### Input sockets



- **boolean0** : _Boolean_
- **boolean1** : _Boolean_



#### Parameters



- **operation** : _'AND'_ in ('AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY')



#### Node label



- **label** : Geometry node label



## Output sockets



- **boolean** : _Boolean_



## Data sockets

> Data socket classes implementing this node


- [Boolean](../sockets/Boolean.md) [b_and](../sockets/Boolean.md#b_and) : Method
- [Boolean](../sockets/Boolean.md) [b_not](../sockets/Boolean.md#b_not) : Method
- [Boolean](../sockets/Boolean.md) [b_or](../sockets/Boolean.md#b_or) : Method
- [Boolean](../sockets/Boolean.md) [imply](../sockets/Boolean.md#imply) : Method
- [Boolean](../sockets/Boolean.md) [nand](../sockets/Boolean.md#nand) : Method
- [Boolean](../sockets/Boolean.md) [nimply](../sockets/Boolean.md#nimply) : Method
- [Boolean](../sockets/Boolean.md) [nor](../sockets/Boolean.md#nor) : Method
- [Boolean](../sockets/Boolean.md) [xnor](../sockets/Boolean.md#xnor) : Method
- [Boolean](../sockets/Boolean.md) [xor](../sockets/Boolean.md#xor) : Method


