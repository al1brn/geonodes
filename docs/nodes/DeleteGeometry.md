
# Node DeleteGeometry

> Geometry node name: [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)<br>
  Blender type: [Delete Geometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.DeleteGeometry(geometry=None, selection=None, domain='POINT', mode='ALL', label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : Geometry
- selection : Boolean

### Parameters

- domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')
- mode : str (default = 'ALL') in ('ALL', 'EDGE_FACE', 'ONLY_FACE')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- geometry : Geometry
