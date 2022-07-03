
# Node MaterialSelection

> Geometry node name: [Material Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html)<br>
  Blender type: [Material Selection](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.MaterialSelection(material=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- material : Material

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- selection : Boolean

## Data sockets

> Data socket classes implementing this node.
  
  
- [Material](/docs/sockets/Material.md).[selection](/docs/sockets/Material.md#selection) : Method
  
