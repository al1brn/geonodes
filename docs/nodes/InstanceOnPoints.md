
# Class InstanceOnPoints

> Geometry node name: _'Instance on Points'_<br>Blender type:  **GeometryNodeInstanceOnPoints**

## Initialization


```python
from geonodes import nodes
node = nodes.InstanceOnPoints(points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None, label=None)
```


### Arguments


#### Input sockets



- **points** : _Points_
- **selection** : _Boolean_
- **instance** : _Geometry_
- **pick_instance** : _Boolean_
- **instance_index** : _Integer_
- **rotation** : _Vector_
- **scale** : _Vector_



#### Node label



- **label** : Geometry node label



## Output sockets



- **instances** : _Instances_



## Data sockets

> Data socket classes implementing this node


- [Points](../sockets/Points.md) [instance_on_points](../sockets/Points.md#instance_on_points) : Method


