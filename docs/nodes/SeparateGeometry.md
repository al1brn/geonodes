
# Node SeparateGeometry

> Geometry node name: [Separate Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html)<br>
  Blender type: [Separate Geometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SeparateGeometry(geometry=None, selection=None, domain='POINT', label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : Geometry
- selection : Boolean

### Parameters

- domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- selection : Geometry
- inverted : Geometry
