
# Class CollectionInfo

> Geometry node name: _'Collection Info'_<br>Blender type:  **GeometryNodeCollectionInfo**

## Initialization


```python
from geonodes import nodes
node = nodes.CollectionInfo(collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL', label=None)
```


### Arguments


#### Input sockets



- **collection** : _Collection_
- **separate_children** : _Boolean_
- **reset_children** : _Boolean_



#### Parameters



- **transform_space** : _'ORIGINAL'_ in ('ORIGINAL', 'RELATIVE')



#### Node label



- **label** : Geometry node label



## Output sockets



- **geometry** : _Geometry_



## Data sockets

> Data socket classes implementing this node


- [Collection](./sockets/Collection.md) [info](./sockets/Collection.md#info) : Method


