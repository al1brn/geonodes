# Node Vector Curves

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_curves.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorCurve.html)
- geonodes name: `VectorCurves`
- bl_idname: `ShaderNodeVectorCurve`

```python
from geonodes import nodes

node = nodes.VectorCurves(fac=None, vector=None)
```

### Args:

#### Input socket arguments:

- **fac**: [Float](Float.md)
- **vector**: [Vector](Vector.md)

### Output sockets:

- **vector** : [Vector](Vector.md)

## Implementation

#### class [Vector](Vector.md)

 - [curves](Vector.md#curves)