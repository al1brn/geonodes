
# Node Transform

> Geometry node name: [Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/transform.html)<br>
  Blender type: [Transform](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Transform(geometry=None, translation=None, rotation=None, scale=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : Geometry
- translation : Vector
- rotation : Vector
- scale : Vector

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- geometry : Geometry
