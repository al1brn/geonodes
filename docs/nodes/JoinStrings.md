
# Node JoinStrings

> Geometry node name: [Join Strings](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/join_strings.html)<br>
  Blender type: [Join Strings](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.JoinStrings(*strings, delimiter=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- delimiter : String
- strings : <m> String

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- string : String
