
# Node SampleNearest

> Geometry node name: [Sample Nearest](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html)<br>
  Blender type: [Sample Nearest](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SampleNearest(geometry=None, sample_position=None, domain='POINT', label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : Geometry
- sample_position : Vector

### Parameters

- domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'CORNER')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- index : Integer
