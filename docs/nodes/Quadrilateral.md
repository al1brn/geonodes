
# Node Quadrilateral

> Geometry node name: [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/quadrilateral.html)<br>
  Blender type: [Quadrilateral](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveQuadrilateral.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Quadrilateral(width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE', label=None, node_color=None)
```



## Arguments


### Input sockets

- width : Float
- height : Float
- bottom_width : Float
- top_width : Float
- offset : Float
- bottom_height : Float
- top_height : Float
- point_1 : Vector
- point_2 : Vector
- point_3 : Vector
- point_4 : Vector

### Parameters

- mode : str (default = 'RECTANGLE') in ('RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- curve : Curve
