
# Node CombineRgb

> Geometry node name: [Combine RGB](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_rgb.html)<br>
  Blender type: [Combine RGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineRGB.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.CombineRgb(r=None, g=None, b=None, label=None, node_color=None)
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
