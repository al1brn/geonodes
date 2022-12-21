# Node RGB Curves

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/rgb_curves.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBCurve.html)
- geonodes name: `RgbCurves`
- bl_idname: `ShaderNodeRGBCurve`

```python
from geonodes import nodes

node = nodes.RgbCurves(fac=None, color=None)
```

### Args:

#### Input socket arguments:

- **fac**: [Float](Float.md)
- **color**: [Color](Color.md)

### Output sockets:

- **color** : [Color](Color.md)

