
# Node MergeByDistance

> Geometry node name: [Merge by Distance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html)<br>
  Blender type: [Merge by Distance](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------

```python
from geonodes import nodes
node = nodes.MergeByDistance(geometry=None, selection=None, distance=None, mode='ALL', label=None)
```



## Arguments


### Input sockets

- geometry : Geometry
- selection : Boolean
- distance : Float

### Parameters

- mode : str (default = 'ALL') in ('ALL', 'CONNECTED')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- geometry : Geometry

## Data sockets

> Data socket classes implementing this node.
  
  
- [Geometry](/docs/sockets/Geometry.md).[merge_by_distance](/docs/sockets/Geometry.md#merge_by_distance) : Method
  
