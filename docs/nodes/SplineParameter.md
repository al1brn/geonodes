
# Node SplineParameter

> Geometry node name: [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html)<br>
  Blender type: [Spline Parameter](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------

```python
from geonodes import nodes
node = nodes.SplineParameter(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

- factor : Float
- length : Float
- index : Integer

## Data sockets

> Data socket classes implementing this node.
  
  
- [Spline](/docs/sockets/Spline.md).[capture_parameter](/docs/sockets/Spline.md#capture_parameter) : Capture attribute
- [Spline](/docs/sockets/Spline.md).[factor](/docs/sockets/Spline.md#factor) : Attribute
- [Spline](/docs/sockets/Spline.md).[parameter_index](/docs/sockets/Spline.md#parameter_index) : Attribute
- [Spline](/docs/sockets/Spline.md).[parameter_length](/docs/sockets/Spline.md#parameter_length) : Attribute
  
