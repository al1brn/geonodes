
# Node Material

> Geometry node name: [Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/material.html)<br>
  Blender type: [Material](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterial.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Material(label=None, node_color=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- material : Material
