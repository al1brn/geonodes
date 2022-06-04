
# Class VolumeToMesh

> Geometry node name: _'Volume to Mesh'_<br>Blender type:  **GeometryNodeVolumeToMesh**

## Initialization


```python
from geonodes import nodes
node = nodes.VolumeToMesh(volume=None, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID', label=None)
```


### Arguments


#### Input sockets



- **volume** : _Volume_
- **voxel_size** : _Float_
- **voxel_amount** : _Float_
- **threshold** : _Float_
- **adaptivity** : _Float_



#### Parameters



- **resolution_mode** : _'GRID'_ in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE')



#### Node label



- **label** : Geometry node label



## Output sockets



- **mesh** : _Mesh_



## Data sockets

> Data socket classes implementing this node


- [Volume](../sockets/Volume.md) [to_mesh](../sockets/Volume.md#to_mesh) : Method


