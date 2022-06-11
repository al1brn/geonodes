
# Node CurveToMesh

> Geometry node name: [Curve to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/curve_to_mesh.html)<br>
  Blender type: [Curve to Mesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToMesh.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.CurveToMesh(curve=None, profile_curve=None, fill_caps=None, label=None)
```



## Arguments


### Input sockets

curve : Curve
- profile_curve : Geometry
- fill_caps : Boolean

### Node label

- label : Geometry node display label (default=None)

## Output sockets

mesh : Mesh

## Data sockets

> Data socket classes implementing this node.
  
[Curve](/docs/sockets/Curve.md) [to_mesh](/docs/sockets/Curve.md#to_mesh) : Method

