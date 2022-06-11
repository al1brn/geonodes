
# Node SetMaterial

> Geometry node name: [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)<br>
  Blender type: [Set Material](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SetMaterial(geometry=None, selection=None, material=None, label=None)
```



## Arguments


### Input sockets

geometry : Geometry
- selection : Boolean
- material : Material

### Node label

- label : Geometry node display label (default=None)

## Output sockets

geometry : Geometry

## Data sockets

> Data socket classes implementing this node.
  
[Geometry](/docs/sockets/Geometry.md) [set_material](/docs/sockets/Geometry.md#set_material) : Method

