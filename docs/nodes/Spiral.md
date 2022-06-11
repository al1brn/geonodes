
# Node Spiral

> Geometry node name: [Spiral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/spiral.html)<br>
  Blender type: [Spiral](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSpiral.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Spiral(resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None, label=None)
```



## Arguments


### Input sockets

resolution : Integer
- rotations : Float
- start_radius : Float
- end_radius : Float
- height : Float
- reverse : Boolean

### Node label

- label : Geometry node display label (default=None)

## Output sockets

curve : Curve

## Data sockets

> Data socket classes implementing this node.
  
[class_name](docs/sockets/Curve.md) [Spiral](docs/sockets/Curve.md#spiral) : Constructor

