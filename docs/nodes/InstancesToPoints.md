
# Node InstancesToPoints

> Geometry node name: [Instances to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html)<br>
  Blender type: [Instances to Points](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstancesToPoints.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.InstancesToPoints(instances=None, selection=None, position=None, radius=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- instances : Instances
- selection : Boolean
- position : Vector
- radius : Float

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- points : Points
