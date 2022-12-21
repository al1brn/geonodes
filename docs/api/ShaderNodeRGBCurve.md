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

## Implementation

#### class [Color](Color.md)

 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16d4fb0a0>>](Color.md#rgb_curves-property)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4fb0d0>>](function.md#rgb_curves)
