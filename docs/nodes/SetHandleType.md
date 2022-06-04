
# Class SetHandleType

> Geometry node name: _'Set Handle Type'_<br>Blender type:  **GeometryNodeCurveSetHandles**

## Initialization


```python
from geonodes import nodes
node = nodes.SetHandleType(curve=None, selection=None, handle_type='AUTO', mode={'LEFT', 'RIGHT'}, label=None)
```


### Arguments


#### Input sockets



- **curve** : _Curve_
- **selection** : _Boolean_



#### Parameters



- **handle_type** : _'AUTO'_ in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
- **mode** : _{'LEFT', 'RIGHT'}_ set



#### Node label



- **label** : Geometry node label



## Output sockets



- **curve** : _Curve_



## Data sockets

> Data socket classes implementing this node


- [Curve](./sockets/Curve.md) [set_handles](./sockets/Curve.md#set_handles) : Stacked method


