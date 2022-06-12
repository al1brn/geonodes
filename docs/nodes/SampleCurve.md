
# Node SampleCurve

> Geometry node name: [Sample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample_curve.html)<br>
  Blender type: [Sample Curve](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleCurve.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------
```python
from geonodes import nodes
node = nodes.SampleCurve(curve=None, factor=None, length=None, mode='LENGTH', label=None)
```



## Arguments


### Input sockets

- curve : Curve
- factor : Float
- length : Float

### Parameters

- mode : str (default = 'LENGTH') in ('FACTOR', 'LENGTH')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- position : Vector
- tangent : Vector
- normal : Vector

## Data sockets

> Data socket classes implementing this node.
  
  
- [Curve](/docs/sockets/Curve.md).[sample](/docs/sockets/Curve.md#sample) : Method
  
