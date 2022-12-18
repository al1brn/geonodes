
# Node BooleanMath

> Geometry node name: [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html)<br>
  Blender type: [Boolean Math](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.BooleanMath(boolean0=None, boolean1=None, operation='AND', label=None, node_color=None)
```



## Arguments


### Input sockets

- boolean0 : Boolean
- boolean1 : Boolean

### Parameters

- operation : str (default = 'AND') in ('AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- boolean : Boolean
