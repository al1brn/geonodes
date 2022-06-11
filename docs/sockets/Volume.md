
# Data socket Volume

> Inherits from gn.Geometry
  
<sub>go to [index](/docs/index.md)</sub>



## Methods

- [to_mesh](#to_mesh) : [VolumeToMesh](section:nodes/VolumeToMesh), mesh (Mesh)

## to_mesh

> Node: [VolumeToMesh](section:nodes/VolumeToMesh)
  
<sub>go to: [top](#data-socket-volume) [index](/docs/index.md)
blender ref [GeometryNodeVolumeToMesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeToMesh.html)
node ref [Volume to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/volume_to_mesh.html) </sub>

```python
v = volume.to_mesh(voxel_size, voxel_amount, threshold, adaptivity, resolution_mode)
```

### Arguments


#### Sockets

- volume : Volume (self)
- voxel_size : Float
- voxel_amount : Float
- threshold : Float
- adaptivity : Float

#### Parameters

- resolution_mode : 'GRID' in [GRID, VOXEL_AMOUNT, VOXEL_SIZE]

### Node creation

```python
nodes.VolumeToMesh(volume=self, voxel_size=voxel_size, voxel_amount=voxel_amount, threshold=threshold, adaptivity=adaptivity, resolution_mode=resolution_mode)
```

### Returns

Mesh

