
# Node ColorRamp

> Geometry node name: [ColorRamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/color_ramp.html)<br>
  Blender type: [ColorRamp](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.ColorRamp(fac=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- fac : Float

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- color : Color
- alpha : Float
