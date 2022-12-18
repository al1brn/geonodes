
# Node SetMaterial

> Geometry node name: [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)<br>
  Blender type: [Set Material](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SetMaterial(geometry=None, selection=None, material=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : Geometry
- selection : Boolean
- material : Material

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- geometry : Geometry
