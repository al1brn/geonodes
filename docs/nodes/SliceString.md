
# Node SliceString

> Geometry node name: [Slice String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/slice_string.html)<br>
  Blender type: [Slice String](https://docs.blender.org/api/current/bpy.types.FunctionNodeSliceString.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SliceString(string=None, position=None, length=None, label=None)
```



## Arguments


### Input sockets

string : String
- position : Integer
- length : Integer

### Node label

- label : Geometry node display label (default=None)

## Output sockets

string : String

## Data sockets

> Data socket classes implementing this node.
  
[String](/docs/sockets/String.md) [slice](/docs/sockets/String.md#slice) : Method

