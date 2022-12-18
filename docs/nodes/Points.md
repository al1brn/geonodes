
# Node Points

> Geometry node name: [Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points.html)<br>
  Blender type: [Points](https://docs.blender.org/api/current/bpy.types.GeometryNodePoints.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Points(count=None, position=None, radius=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- count : Integer
- position : Vector
- radius : Float

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- geometry : Geometry
