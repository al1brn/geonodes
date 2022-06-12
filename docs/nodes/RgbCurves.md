
# Node RgbCurves

> Geometry node name: [RGB Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/rgb_curves.html)<br>
  Blender type: [RGB Curves](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBCurve.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------
```python
from geonodes import nodes
node = nodes.RgbCurves(fac=None, color=None, label=None)
```



## Arguments


### Input sockets

- fac : Float
- color : Color

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- color : Color

## Data sockets

> Data socket classes implementing this node.
  
  
- [Color](/docs/sockets/Color.md).[curves](/docs/sockets/Color.md#curves) : Method
  
