
# Node SetPosition

> Geometry node name: [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html)<br>
  Blender type: [Set Position](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SetPosition(geometry=None, selection=None, position=None, offset=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : Geometry
- selection : Boolean
- position : Vector
- offset : Vector

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- geometry : Geometry
