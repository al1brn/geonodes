
# Node SeparateRgb(legacy)

> Geometry node name: [Separate RGB (Legacy)](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/e.html)<br>
  Blender type: [Separate RGB (Legacy)](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateRGB.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SeparateRgb(legacy)(image=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- image : Color

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- r : Float
- g : Float
- b : Float
