
# Node CombineRgb(legacy)

> Geometry node name: [Combine RGB (Legacy)](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/o.html)<br>
  Blender type: [Combine RGB (Legacy)](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineRGB.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.CombineRgb(legacy)(r=None, g=None, b=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- r : Float
- g : Float
- b : Float

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- image : Color
