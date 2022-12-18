
# Node SetCurveTilt

> Geometry node name: [Set Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_tilt.html)<br>
  Blender type: [Set Curve Tilt](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SetCurveTilt(curve=None, selection=None, tilt=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- curve : Curve
- selection : Boolean
- tilt : Float

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- curve : Curve
