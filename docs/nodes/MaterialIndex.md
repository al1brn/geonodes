
# Node MaterialIndex

> Geometry node name: [Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html)<br>
  Blender type: [Material Index](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.MaterialIndex(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

material_index : Integer

## Data sockets

> Data socket classes implementing this node.
  
[class_name](/docs/sockets/Mesh.md) [capture_material_index](/docs/sockets/Mesh.md#capture_material_index) : Capture attribute
- [class_name](/docs/sockets/Mesh.md) [material_index](/docs/sockets/Mesh.md#material_index) : Attribute
  
