
# Node SetSplineResolution

> Geometry node name: [Set Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_resolution.html)<br>
  Blender type: [Set Spline Resolution](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SetSplineResolution(geometry=None, selection=None, resolution=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : Geometry
- selection : Boolean
- resolution : Integer

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- geometry : Geometry

## Data sockets

> Data socket classes implementing this node.
  
  
- [Curve](/docs/sockets/Curve.md).[set_resolution](/docs/sockets/Curve.md#set_resolution) : Method
  
