
# Node Transform

> Geometry node name: [Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/transform.html)<br>
  Blender type: [Transform](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Transform(geometry=None, translation=None, rotation=None, scale=None, label=None)
```



## Arguments


### Input sockets

geometry : Geometry
- translation : Vector
- rotation : Vector
- scale : Vector

### Node label

- label : Geometry node display label (default=None)

## Output sockets

geometry : Geometry

## Data sockets

> Data socket classes implementing this node.
  
[class_name](/docs/sockets/Geometry.md) [transform](/docs/sockets/Geometry.md#transform) : Method

