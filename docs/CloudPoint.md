
# Class CloudPoint

Cloud point : the point domain of cloud of points


## delete

<method GeometryNodeDeleteGeometry>

mode : str (default = 'ALL') in ('ALL', 'EDGE_FACE', 'ONLY_FACE')        
        
```python
cloud.points.select(...).delete()
```



## merge

> Merge points by distance
  
<blid GeometryNodeMergeByDistance>

'''python
cloud.points.select().merge()
````

### Arguments

- distance : Float
The merge distance

