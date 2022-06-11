
# Node StringLength

> Geometry node name: [String Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/string_length.html)<br>
  Blender type: [String Length](https://docs.blender.org/api/current/bpy.types.FunctionNodeStringLength.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.StringLength(string=None, label=None)
```



## Arguments


### Input sockets

string : String

### Node label

- label : Geometry node display label (default=None)

## Output sockets

length : Integer

## Data sockets

> Data socket classes implementing this node.
  
[String](/docs/sockets/String.md).[length](/docs/sockets/String.md#length) : Property

