
# Node InstanceOnPoints

> Geometry node name: [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html)<br>
  Blender type: [Instance on Points](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------
```python
from geonodes import nodes
node = nodes.InstanceOnPoints(points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None, label=None)
```



## Arguments


### Input sockets

- points : Points
- selection : Boolean
- instance : Geometry
- pick_instance : Boolean
- instance_index : Integer
- rotation : Vector
- scale : Vector

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- instances : Instances

## Data sockets

> Data socket classes implementing this node.
  
  
- [Points](/docs/sockets/Points.md).[instance_on_points](/docs/sockets/Points.md#instance_on_points) : Method
  
