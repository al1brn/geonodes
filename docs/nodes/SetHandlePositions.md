
# Node SetHandlePositions

> Geometry node name: [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html)<br>
  Blender type: [Set Handle Positions](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SetHandlePositions(curve=None, selection=None, position=None, offset=None, mode='LEFT', label=None, node_color=None)
```



## Arguments


### Input sockets

- curve : Curve
- selection : Boolean
- position : Vector
- offset : Vector

### Parameters

- mode : str (default = 'LEFT') in ('LEFT', 'RIGHT')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- curve : Curve
