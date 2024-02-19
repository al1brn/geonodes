# class MeshToVolume (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : MeshToVolume
 - bl_idname : GeometryNodeMeshToVolume

Node parameters
 - resolution_mode : 'VOXEL_AMOUNT'

Input sockets
 - mesh : Geometry
 - density : Float
 - voxel_size : Float
 - voxel_amount : Float
 - interior_band_width : Float

Output sockets
 - volume : Geometry

### Header

``` python
def MeshToVolume(self, mesh=None, density=None, voxel_amount=None, interior_band_width=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None):
```

## Implementations

o functions : [mesh_to_volume](/docs/GeoNodes_classes/mesh_to_volume.md)
o Geometry : [mesh_to_volume](/docs/GeoNodes_classes/mesh_to_volume.md) 

