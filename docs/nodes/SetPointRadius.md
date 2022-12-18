
# Node SetPointRadius

> Geometry node name: [Set Point Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html)<br>
  Blender type: [Set Point Radius](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SetPointRadius(points=None, selection=None, radius=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- points : Points
- selection : Boolean
- radius : Float

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- points : Points
