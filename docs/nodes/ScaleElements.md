
# Class ScaleElements

> Geometry node name: _'Scale Elements'_<br>Blender type:  **GeometryNodeScaleElements**

## Initialization


```python
from geonodes import nodes
node = nodes.ScaleElements(geometry=None, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM', label=None)
```


### Arguments


#### Input sockets



- **geometry** : _Geometry_
- **selection** : _Boolean_
- **scale** : _Float_
- **center** : _Vector_
- **axis** : _Vector_



#### Parameters



- **domain** : _'FACE'_ in ('FACE', 'EDGE')
- **scale_mode** : _'UNIFORM'_ in ('UNIFORM', 'SINGLE_AXIS')



#### Node label



- **label** : Geometry node label



## Output sockets



- **geometry** : _Geometry_



## Data sockets

> Data socket classes implementing this node


- [Geometry](../sockets/Geometry.md) [scale_elements](../sockets/Geometry.md#scale_elements) : Stacked method


