
# Class Volume

> Inherits from: ***Geometry***

## Methods



- to_mesh : mesh (Mesh)



## Methods


### to_mesh

> Node: [VolumeToMesh](../nodes/{self.node_name}.md)

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



#### Returns

    Mesh
