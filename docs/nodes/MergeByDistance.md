
# Node MergeByDistance

> Geometry node name: [Merge by Distance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html)<br>
  Blender type: [Merge by Distance](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.MergeByDistance(geometry=None, selection=None, distance=None, mode='ALL', label=None, node_color=None)
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
- node_color : Geometry node color (default=None)

## Output sockets

- geometry : Geometry
