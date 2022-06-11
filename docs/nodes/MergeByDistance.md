
# Node MergeByDistance

> Geometry node name: [Merge by Distance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/merge_by_distance.html)<br>
  Blender type: [Merge by Distance](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.MergeByDistance(geometry=None, selection=None, distance=None, label=None)
```



## Arguments


### Input sockets

geometry : Geometry
- selection : Boolean
- distance : Float

### Node label

- label : Geometry node display label (default=None)

## Output sockets

geometry : Geometry

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Geometry) [merge_by_distance](section:Data socket Geometry/merge_by_distance) : Method

