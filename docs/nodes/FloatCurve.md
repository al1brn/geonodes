
# Node FloatCurve

> Geometry node name: [Float Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_curve.html)<br>
  Blender type: [Float Curve](https://docs.blender.org/api/current/bpy.types.ShaderNodeFloatCurve.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------
```python
from geonodes import nodes
node = nodes.FloatCurve(factor=None, value=None, label=None)
```



## Arguments


### Input sockets

- factor : Float
- value : Float

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- value : Float

## Data sockets

> Data socket classes implementing this node.
  
  
- [Float](/docs/sockets/Float.md).[curve](/docs/sockets/Float.md#curve) : Method
  
