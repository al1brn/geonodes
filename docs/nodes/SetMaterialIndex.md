
# Node SetMaterialIndex

> Geometry node name: [Set Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html)<br>
  Blender type: [Set Material Index](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SetMaterialIndex(geometry=None, selection=None, material_index=None, label=None)
```



## Arguments


### Input sockets

geometry : Geometry
- selection : Boolean
- material_index : Integer

### Node label

- label : Geometry node display label (default=None)

## Output sockets

geometry : Geometry

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Geometry) [set_material_index](section:Data socket Geometry/set_material_index) : Method

