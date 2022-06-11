
# Node GeometryToInstance

> Geometry node name: [Geometry to Instance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/geometry_to_instance.html)<br>
  Blender type: [Geometry to Instance](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.GeometryToInstance(*geometry, label=None)
```



## Arguments


### Input sockets

geometry : *Geometry

### Node label

- label : Geometry node display label (default=None)

## Output sockets

instances : Instances

## Data sockets

> Data socket classes implementing this node.
  
[class_name](/docs/sockets/Geometry.md) [to_instance](/docs/sockets/Geometry.md#to_instance) : Method

