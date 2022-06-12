
# Node SubdivideCurve

> Geometry node name: [Subdivide Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/subdivide_curve.html)<br>
  Blender type: [Subdivide Curve](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideCurve.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------
```python
from geonodes import nodes
node = nodes.SubdivideCurve(curve=None, cuts=None, label=None)
```



## Arguments


### Input sockets

- curve : Curve
- cuts : Integer

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- curve : Curve

## Data sockets

> Data socket classes implementing this node.
  
  
- [Curve](/docs/sockets/Curve.md).[subdivide](/docs/sockets/Curve.md#subdivide) : Method
  
