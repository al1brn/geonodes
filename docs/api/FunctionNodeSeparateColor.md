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
  def separate_rgb(color=None)
  ```

 - [separate_hsv](A.md#separate_hsv)
  ```python
  def separate_hsv(color=None)
  ```

 - [separate_hsl](A.md#separate_hsl)
  ```python
  def separate_hsl(color=None)
  ```

#### [Color](Color.md)

 - [rgb](Color.md#rgb-property)
  ```python
  def rgb(self)
  ```

 - [hsv](Color.md#hsv-property)
  ```python
  def hsv(self)
  ```

 - [hsl](Color.md#hsl-property)
  ```python
  def hsl(self)
  ```

 - [alpha](Color.md#alpha-property)
  ```python
  def alpha(self)
  ```

 - [red](Color.md#red-property)
  ```python
  def red(self)
  ```

 - [green](Color.md#green-property)
  ```python
  def green(self)
  ```

 - [blue](Color.md#blue-property)
  ```python
  def blue(self)
  ```

 - [hue](Color.md#hue-property)
  ```python
  def hue(self)
  ```

 - [saturation](Color.md#saturation-property)
  ```python
  def saturation(self)
  ```

 - [value](Color.md#value-property)
  ```python
  def value(self)
  ```

 - [lightness](Color.md#lightness-property)
  ```python
  def lightness(self)
  ```

