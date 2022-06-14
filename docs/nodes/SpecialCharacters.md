
# Node SpecialCharacters

> Geometry node name: [Special Characters](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/special_characters.html)<br>
  Blender type: [Special Characters](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputSpecialCharacters.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SpecialCharacters(label=None, node_color=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- line_break : String
- tab : String
