
# Node SetCurveTilt

> Geometry node name: [Set Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_curve_tilt.html)<br>
  Blender type: [Set Curve Tilt](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SetCurveTilt(curve=None, selection=None, tilt=None, label=None)
```



## Arguments


### Input sockets

curve : Curve
- selection : Boolean
- tilt : Float

### Node label

- label : Geometry node display label (default=None)

## Output sockets

curve : Curve

## Data sockets

> Data socket classes implementing this node.
  
[class_name](/docs/sockets/Curve.md) [set_tilt](/docs/sockets/Curve.md#set_tilt) : Method

