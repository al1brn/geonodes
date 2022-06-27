
# Class CloudPoint

Cloud point : the point domain of cloud of points


## delete

<method GeometryNodeDeleteGeometry>

### Example

```python
cloud.points(...).delete()
```



## merge

> Merge points by distance
  
<blid GeometryNodeMergeByDistance>

### Example

'''python
cloud.points().merge()
````

### Arguments

- distance : Float
The merge distance



## to_vertices

> Convert points to vertices
  
<blid GeometryNodePointsToVertices>

### Returns

Points

### Example

```python
verts = cloud.points.to_vertices()
```



## to_volume

> Convert points to vertices
  
<blid GeometryNodePointsToVertices>

### Parameters

- density : Float
- voxel_size : Float
- voxel_amount : Float
- radius : Float
- resolution_mode : str (default = 'VOXEL_AMOUNT') in ('VOXEL_AMOUNT', 'VOXEL_SIZE')

### Returns

Volume

### Example

```python
volume = cloud.points.to_volume()
```

