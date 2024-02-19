# class VolumeToMesh (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : VolumeToMesh
 - bl_idname : GeometryNodeVolumeToMesh

Node parameters
 - resolution_mode : 'GRID'

Input sockets
 - volume : Geometry
 - voxel_size : Float
 - voxel_amount : Float
 - threshold : Float
 - adaptivity : Float

Output sockets
 - mesh : Geometry

### Header

``` python
def VolumeToMesh(self, volume=None, threshold=None, adaptivity=None, voxel_amount=None, voxel_size=None, resolution_mode='GRID', node_label=None, node_color=None):
```

## Implementations

o functions : [volume_to_mesh](/docs/classes/volume_to_mesh.md)
o Geometry : [volume_to_mesh](/docs/classes/volume_to_mesh.md) 

