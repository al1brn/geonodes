
# Node ReplaceMaterial

> Geometry node name: [Replace Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html)<br>
  Blender type: [Replace Material](https://docs.blender.org/api/current/bpy.types.GeometryNodeReplaceMaterial.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.ReplaceMaterial(geometry=None, old=None, new=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : Geometry
- old : Material
- new : Material

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- geometry : Geometry
