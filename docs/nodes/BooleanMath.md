
# Class BooleanMath

> Geometry node name: _'Boolean Math'_<br>Blender type:  **FunctionNodeBooleanMath**

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


- [Boolean](aaa). [b_and](bbb) : Method
- [Boolean](aaa). [b_not](bbb) : Method
- [Boolean](aaa). [b_or](bbb) : Method
- [Boolean](aaa). [imply](bbb) : Method
- [Boolean](aaa). [nand](bbb) : Method
- [Boolean](aaa). [nimply](bbb) : Method
- [Boolean](aaa). [nor](bbb) : Method
- [Boolean](aaa). [xnor](bbb) : Method
- [Boolean](aaa). [xor](bbb) : Method


