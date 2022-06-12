
# Node ReplaceMaterial

> Geometry node name: [Replace Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html)<br>
  Blender type: [Replace Material](https://docs.blender.org/api/current/bpy.types.GeometryNodeReplaceMaterial.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------
```python
from geonodes import nodes
node = nodes.ReplaceMaterial(geometry=None, old=None, new=None, label=None)
```



## Arguments


### Input sockets

- geometry : Geometry
- old : Material
- new : Material

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- geometry : Geometry

## Data sockets

> Data socket classes implementing this node.
  
  
- [Geometry](/docs/sockets/Geometry.md).[replace_material](/docs/sockets/Geometry.md#replace_material) : Method
  
