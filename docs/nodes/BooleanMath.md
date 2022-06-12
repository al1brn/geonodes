
# Node BooleanMath

> Geometry node name: [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html)<br>
  Blender type: [Boolean Math](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------

```python
from geonodes import nodes
node = nodes.BooleanMath(boolean0=None, boolean1=None, operation='AND', label=None)
```



## Arguments


### Input sockets

- boolean0 : Boolean
- boolean1 : Boolean

### Parameters

- operation : str (default = 'AND') in ('AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- boolean : Boolean

## Data sockets

> Data socket classes implementing this node.
  
  
- [Boolean](/docs/sockets/Boolean.md).[b_and](/docs/sockets/Boolean.md#b_and) : Method
- [Boolean](/docs/sockets/Boolean.md).[b_not](/docs/sockets/Boolean.md#b_not) : Method
- [Boolean](/docs/sockets/Boolean.md).[b_or](/docs/sockets/Boolean.md#b_or) : Method
- [Boolean](/docs/sockets/Boolean.md).[imply](/docs/sockets/Boolean.md#imply) : Method
- [Boolean](/docs/sockets/Boolean.md).[nand](/docs/sockets/Boolean.md#nand) : Method
- [Boolean](/docs/sockets/Boolean.md).[nimply](/docs/sockets/Boolean.md#nimply) : Method
- [Boolean](/docs/sockets/Boolean.md).[nor](/docs/sockets/Boolean.md#nor) : Method
- [Boolean](/docs/sockets/Boolean.md).[xnor](/docs/sockets/Boolean.md#xnor) : Method
- [Boolean](/docs/sockets/Boolean.md).[xor](/docs/sockets/Boolean.md#xor) : Method
  
