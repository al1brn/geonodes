
# Node BooleanMath

> Geometry node name: [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/boolean_math.html)<br>
  Blender type: [Boolean Math](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.BooleanMath(boolean0=None, boolean1=None, operation='AND', label=None)
```



## Arguments


### Input sockets

boolean0 : Boolean
- boolean1 : Boolean

### Parameters

operation : str (default = 'AND') in ('AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

boolean : Boolean

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Boolean) [b_and](section:Data socket Boolean/b_and) : Method
- [class_name](section:Data socket Boolean) [b_not](section:Data socket Boolean/b_not) : Method
- [class_name](section:Data socket Boolean) [b_or](section:Data socket Boolean/b_or) : Method
- [class_name](section:Data socket Boolean) [imply](section:Data socket Boolean/imply) : Method
- [class_name](section:Data socket Boolean) [nand](section:Data socket Boolean/nand) : Method
- [class_name](section:Data socket Boolean) [nimply](section:Data socket Boolean/nimply) : Method
- [class_name](section:Data socket Boolean) [nor](section:Data socket Boolean/nor) : Method
- [class_name](section:Data socket Boolean) [xnor](section:Data socket Boolean/xnor) : Method
- [class_name](section:Data socket Boolean) [xor](section:Data socket Boolean/xor) : Method
  
