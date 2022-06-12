
# Node QuadraticBezier

> Geometry node name: [Quadratic Bezier](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/quadratic_bezier.html)<br>
  Blender type: [Quadratic Bezier](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveQuadraticBezier.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------

```python
from geonodes import nodes
node = nodes.QuadraticBezier(resolution=None, start=None, middle=None, end=None, label=None)
```



## Arguments


### Input sockets

- resolution : Integer
- start : Vector
- middle : Vector
- end : Vector

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- curve : Curve

## Data sockets

> Data socket classes implementing this node.
  
  
- [Curve](/docs/sockets/Curve.md).[QuadraticBezier](/docs/sockets/Curve.md#quadraticbezier) : Constructor
  
