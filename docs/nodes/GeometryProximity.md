
# Node GeometryProximity

> Geometry node name: [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html)<br>
  Blender type: [Geometry Proximity](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.GeometryProximity(target=None, source_position=None, target_element='FACES', label=None, node_color=None)
```



## Arguments


### Input sockets

- target : Geometry
- source_position : Vector

### Parameters

- target_element : str (default = 'FACES') in ('POINTS', 'EDGES', 'FACES')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- position : Vector
- distance : Float
