
# Node SetCurveRadius

> Geometry node name: [Set Curve Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_curve_radius.html)<br>
  Blender type: [Set Curve Radius](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SetCurveRadius(curve=None, selection=None, radius=None, label=None)
```



## Arguments


### Input sockets

- curve : Curve
- selection : Boolean
- radius : Float

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- curve : Curve

## Data sockets

> Data socket classes implementing this node.
  
  
- [Curve](/docs/sockets/Curve.md).[set_radius](/docs/sockets/Curve.md#set_radius) : Method
  
