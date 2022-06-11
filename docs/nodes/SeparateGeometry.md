
# Node SeparateGeometry

> Geometry node name: [Separate Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/separate_geometry.html)<br>
  Blender type: [Separate Geometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SeparateGeometry(geometry=None, selection=None, domain='POINT', label=None)
```



## Arguments


### Input sockets

geometry : Geometry
- selection : Boolean

### Parameters

domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

selection : Geometry
- inverted : Geometry

## Data sockets

> Data socket classes implementing this node.
  
[Geometry](/docs/sockets/Geometry.md) [components](/docs/sockets/Geometry.md#components) : Method

