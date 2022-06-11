
# Node GeometryProximity

> Geometry node name: [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/geometry_proximity.html)<br>
  Blender type: [Geometry Proximity](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.GeometryProximity(target=None, source_position=None, target_element='FACES', label=None)
```



## Arguments


### Input sockets

- target : Geometry
- source_position : Vector

### Parameters

- target_element : str (default = 'FACES') in ('POINTS', 'EDGES', 'FACES')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- position : Vector
- distance : Float

## Data sockets

> Data socket classes implementing this node.
  
  
- [Geometry](/docs/sockets/Geometry.md).[proximity](/docs/sockets/Geometry.md#proximity) : Method
  
