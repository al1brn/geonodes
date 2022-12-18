
# Node SeparateComponents

> Geometry node name: [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html)<br>
  Blender type: [Separate Components](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SeparateComponents(geometry=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : Geometry

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- mesh : Mesh
- point_cloud : Geometry
- curve : Curve
- volume : Volume
- instances : Instances
