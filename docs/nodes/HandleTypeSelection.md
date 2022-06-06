
# Class HandleTypeSelection

> Geometry node name: _'Handle Type Selection'_<br>Blender type:  **GeometryNodeCurveHandleTypeSelection**


[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.HandleTypeSelection(handle_type='AUTO', mode={'LEFT', 'RIGHT'}, label=None)
```


### Arguments


#### Parameters



- **handle_type** : _'AUTO'_ in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
- **mode** : _{'LEFT', 'RIGHT'}_ set



#### Node label



- **label** : Geometry node label



## Output sockets



- **selection** : _Boolean_



## Data sockets

> Data socket classes implementing this node




- [Spline](../sockets/Spline.md) [capture_handle_type_selection](../sockets/Spline.md#capture_handle_type_selection) : Capture attribute
- [Spline](../sockets/Spline.md) [handle_type_selection](../sockets/Spline.md#handle_type_selection) : Attribute


