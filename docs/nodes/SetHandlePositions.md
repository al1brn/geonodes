
# Node SetHandlePositions

> Geometry node name: [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_handle_positions.html)<br>
  Blender type: [Set Handle Positions](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SetHandlePositions(curve=None, selection=None, position=None, offset=None, mode='LEFT', label=None)
```



## Arguments


### Input sockets

curve : Curve
- selection : Boolean
- position : Vector
- offset : Vector

### Parameters

mode : str (default = 'LEFT') in ('LEFT', 'RIGHT')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

curve : Curve

## Data sockets

> Data socket classes implementing this node.
  
[class_name](/docs/sockets/Curve.md) [set_handle_positions](/docs/sockets/Curve.md#set_handle_positions) : Method

