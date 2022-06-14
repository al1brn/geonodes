
# Node DuplicateElements

> Geometry node name: [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html)<br>
  Blender type: [Duplicate Elements](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.DuplicateElements(geometry=None, selection=None, amount=None, domain='POINT', label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : Geometry
- selection : Boolean
- amount : Integer

### Parameters

- domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'SPLINE', 'INSTANCE')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- geometry : Geometry
- duplicate_index : Integer
