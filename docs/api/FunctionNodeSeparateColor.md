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
  ```python
  nodes.SeparateColor(color=color, mode='RGB'  ```

 - [separate_hsv](A.md#separate_hsv)
  ```python
  nodes.SeparateColor(color=color, mode='HSV'  ```

 - [separate_hsl](A.md#separate_hsl)
  ```python
  nodes.SeparateColor(color=color, mode='HSL'  ```

#### [Color](Color.md)

 - [rgb](Color.md#rgb-property)
  ```python
  nodes.SeparateColor(color=self, mode='RGB'  ```

 - [hsv](Color.md#hsv-property)
  ```python
  nodes.SeparateColor(color=self, mode='HSV'  ```

 - [hsl](Color.md#hsl-property)
  ```python
  nodes.SeparateColor(color=self, mode='HSL'  ```

 - [alpha](Color.md#alpha-property)
  ```python
  nodes.SeparateColor(color=self, mode=RGB  ```

 - [red](Color.md#red-property)
  ```python
  nodes.SeparateColor(color=self, mode=RGB  ```

 - [green](Color.md#green-property)
  ```python
  nodes.SeparateColor(color=self, mode=RGB  ```

 - [blue](Color.md#blue-property)
  ```python
  nodes.SeparateColor(color=self, mode=RGB  ```

 - [hue](Color.md#hue-property)
  ```python
  nodes.SeparateColor(color=self, mode=HSV  ```

 - [saturation](Color.md#saturation-property)
  ```python
  nodes.SeparateColor(color=self, mode=HSV  ```

 - [value](Color.md#value-property)
  ```python
  nodes.SeparateColor(color=self, mode=HSV  ```

 - [lightness](Color.md#lightness-property)
  ```python
  nodes.SeparateColor(color=self, mode=HSL  ```

