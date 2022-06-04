
# Class SetHandlePositions

> Geometry node name: _'Set Handle Positions'_<br>Blender type:  **GeometryNodeSetCurveHandlePositions**

## Initialization


```python
from geonodes import nodes
node = nodes.SetHandlePositions(curve=None, selection=None, position=None, offset=None, mode='LEFT', label=None)
```


### Arguments


#### Input sockets



- **curve** : _Curve_
- **selection** : _Boolean_
- **position** : _Vector_
- **offset** : _Vector_



#### Parameters



- **mode** : _'LEFT'_ in ('LEFT', 'RIGHT')



#### Node label



- **label** : Geometry node label



## Output sockets



- **curve** : _Curve_



## Data sockets

> Data socket classes implementing this node


- [Curve](aaa). [set_handle_positions](bbb) : Stacked method


