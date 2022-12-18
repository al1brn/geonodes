
# Node ValueToString

> Geometry node name: [Value to String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/value_to_string.html)<br>
  Blender type: [Value to String](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.ValueToString(value=None, decimals=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- value : Float
- decimals : Integer

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- string : String
