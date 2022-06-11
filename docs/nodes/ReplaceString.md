
# Node ReplaceString

> Geometry node name: [Replace String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/replace_string.html)<br>
  Blender type: [Replace String](https://docs.blender.org/api/current/bpy.types.FunctionNodeReplaceString.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.ReplaceString(string=None, find=None, replace=None, label=None)
```



## Arguments


### Input sockets

- string : String
- find : String
- replace : String

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- string : String

## Data sockets

> Data socket classes implementing this node.
  
  
- [String](/docs/sockets/String.md).[replace](/docs/sockets/String.md#replace) : Method
  
