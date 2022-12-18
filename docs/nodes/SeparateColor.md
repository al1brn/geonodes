
# Node SeparateColor

> Geometry node name: [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html)<br>
  Blender type: [Separate Color](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SeparateColor(color=None, mode='RGB', label=None, node_color=None)
```



## Arguments


### Input sockets

- color : Color

### Parameters

- mode : str (default = 'RGB') in ('RGB', 'HSV', 'HSL')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- red : Float
- green : Float
- blue : Float
- alpha : Float
