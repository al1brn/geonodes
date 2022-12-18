
# Node GeometryToInstance

> Geometry node name: [Geometry to Instance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html)<br>
  Blender type: [Geometry to Instance](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.GeometryToInstance(*geometry, label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : <m> Geometry

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- instances : Instances
