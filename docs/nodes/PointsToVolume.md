
# Class PointsToVolume

> Geometry node name: _'Points to Volume'_<br>Blender type:  **GeometryNodePointsToVolume**

## Initialization


```python
from geonodes import nodes
node = nodes.PointsToVolume(points=None, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT', label=None)
```


### Arguments


#### Input sockets



- **points** : _Points_
- **density** : _Float_
- **voxel_size** : _Float_
- **voxel_amount** : _Float_
- **radius** : _Float_



#### Parameters



- **resolution_mode** : _'VOXEL_AMOUNT'_ in ('VOXEL_AMOUNT', 'VOXEL_SIZE')



#### Node label



- **label** : Geometry node label



## Output sockets



- **volume** : _Volume_



## Data sockets

> Data socket classes implementing this node


- [Points](aaa). [to_volume](bbb) : Method


