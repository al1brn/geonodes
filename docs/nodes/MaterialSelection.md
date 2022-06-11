
# Node MaterialSelection

> Geometry node name: [Material Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html)<br>
  Blender type: [Material Selection](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.MaterialSelection(material=None, label=None)
```



## Arguments


### Input sockets

material : Material

### Node label

- label : Geometry node display label (default=None)

## Output sockets

selection : Boolean

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Material) [selection](section:Data socket Material/selection) : Method
- [class_name](section:Data socket Mesh) [capture_material_selection](section:Data socket Mesh/capture_material_selection) : Capture attribute
- [class_name](section:Data socket Mesh) [material_selection](section:Data socket Mesh/material_selection) : Attribute
  
