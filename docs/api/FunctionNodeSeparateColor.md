# Node Separate Color

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)
- geonodes name: `SeparateColor`
- bl_idname: `FunctionNodeSeparateColor`

```python
from geonodes import nodes

node = nodes.SeparateColor(color=None, mode='RGB')
```

### Args:

#### Input socket arguments:

- **color**: [Color](Color.md)

#### Node parameter arguments:

- **mode** (str): default = 'RGB' in ('RGB', 'HSV', 'HSL')

### Output sockets:

- **red** : [Float](Float.md)
- **green** : [Float](Float.md)
- **blue** : [Float](Float.md)
- **alpha** : [Float](Float.md)

## Implementation

#### Global functions

 - [separate_rgb](A.md#separate_rgb)
 - [separate_hsv](A.md#separate_hsv)
 - [separate_hsl](A.md#separate_hsl)
#### class [Color](Color.md)

 - [rgb](Color.md#rgb-property)
 - [hsv](Color.md#hsv-property)
 - [hsl](Color.md#hsl-property)
 - [alpha](Color.md#alpha-property)
 - [red](Color.md#red-property)
 - [green](Color.md#green-property)
 - [blue](Color.md#blue-property)
 - [hue](Color.md#hue-property)
 - [saturation](Color.md#saturation-property)
 - [value](Color.md#value-property)
 - [lightness](Color.md#lightness-property)
