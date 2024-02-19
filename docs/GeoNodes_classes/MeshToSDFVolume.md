# class MeshToSDFVolume (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : MeshToSDFVolume
 - bl_idname : GeometryNodeMeshToSDFVolume

Node parameters
 - resolution_mode : 'VOXEL_AMOUNT'

Input sockets
 - mesh : Geometry
 - voxel_size : Float
 - voxel_amount : Float
 - half_band_width : Float

Output sockets
 - volume : Geometry

### Header

``` python
def MeshToSDFVolume(self, mesh=None, voxel_amount=None, half_band_width=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None):
```

## Implementations

o functions : [mesh_to_sdf_volume](/docs/GeoNodes_classes/mesh_to_sdf_volume.md)
o Geometry : [mesh_to_sdf_volume](#mesh_to_sdf_volume) 

