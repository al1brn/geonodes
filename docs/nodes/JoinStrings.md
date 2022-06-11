
# Node JoinStrings

> Geometry node name: [Join Strings](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/join_strings.html)<br>
  Blender type: [Join Strings](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.JoinStrings(*strings, delimiter=None, label=None)
```



## Arguments


### Input sockets

delimiter : String
- strings : *String

### Node label

- label : Geometry node display label (default=None)

## Output sockets

string : String

## Data sockets

> Data socket classes implementing this node.
  
[class_name](/docs/sockets/String.md) [join](/docs/sockets/String.md#join) : Method
- [class_name](/docs/sockets/functions.md) [join_strings](/docs/sockets/functions.md#join_strings) : Function
  
