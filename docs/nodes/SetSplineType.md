
# Node SetSplineType

> Geometry node name: [Set Spline Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html)<br>
  Blender type: [Set Spline Type](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------

```python
from geonodes import nodes
node = nodes.SetSplineType(curve=None, selection=None, spline_type='POLY', label=None)
```



## Arguments


### Input sockets

- curve : Curve
- selection : Boolean

### Parameters

- spline_type : str (default = 'POLY') in ('BEZIER', 'NURBS', 'POLY')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- curve : Curve

## Data sockets

> Data socket classes implementing this node.
  
  
- [Curve](/docs/sockets/Curve.md).[set_spline_type](/docs/sockets/Curve.md#set_spline_type) : Method
  
