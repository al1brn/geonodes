
# Class Volume

> Inherits from: ***gn.Geometry***


[Index](/docs/index.md)

## Methods



- [**to_mesh**](#to_mesh) : [VolumeToMesh](../nodes/VolumeToMesh.md) mesh (Mesh)



## Methods reference


### to_mesh

> Node: [VolumeToMesh](../nodes/{self.node_name}.md)


[Top](#class-volume) [Index](/docs/index.md)

```python
v = volume.to_mesh(voxel_size, voxel_amount, threshold, adaptivity, resolution_mode)
```


#### Arguments


##### Sockets arguments



- volume : Volume (self)
- voxel_size : Float
- voxel_amount : Float
- threshold : Float
- adaptivity : Float



##### Parameters arguments



- resolution_mode : 'GRID' in [GRID, VOXEL_AMOUNT, VOXEL_SIZE]



#### Node creation


```python
node = nodes.VolumeToMesh(volume=self, voxel_size=voxel_size, voxel_amount=voxel_amount, threshold=threshold, adaptivity=adaptivity, resolution_mode=resolution_mode)
```


#### Returns

    Mesh
