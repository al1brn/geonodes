
# Class ObjectInfo

> Geometry node name: _'Object Info'_<br>Blender type:  **GeometryNodeObjectInfo**

## Initialization


```python
from geonodes import nodes
node = nodes.ObjectInfo(object=None, as_instance=None, transform_space='ORIGINAL', label=None)
```


### Arguments


#### Input sockets



- **object** : _Object_
- **as_instance** : _Boolean_



#### Parameters



- **transform_space** : _'ORIGINAL'_ in ('ORIGINAL', 'RELATIVE')



#### Node label



- **label** : Geometry node label



## Output sockets



- **location** : _Vector_
- **rotation** : _Vector_
- **scale** : _Vector_
- **geometry** : _Geometry_



## Data sockets

> Data socket classes implementing this node


- [Object](../sockets/Object.md) [info](../sockets/Object.md#info) : Property


