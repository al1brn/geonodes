# Node Resample Curve

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)
- geonodes name: `ResampleCurve`
- bl_idname: `GeometryNodeResampleCurve`

```python
from geonodes import nodes

node = nodes.ResampleCurve(curve=None, selection=None, count=None, length=None, mode='COUNT')
```

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)
- **selection**: [Boolean](Boolean.md)
- **count**: [Integer](Integer.md)
- **length**: [Float](Float.md)

#### Node parameter arguments:

- **mode** (str): default = 'COUNT' in ('EVALUATED', 'COUNT', 'LENGTH')

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

#### [Curve](Curve.md)

 - [resample](Curve.md#resample)
  ```python
  def resample(self, selection=None, count=None, length=None, mode='COUNT')
  ```

 - [resample_count](Curve.md#resample_count)
  ```python
  def resample_count(self, selection=None, count=None)
  ```

 - [resample_length](Curve.md#resample_length)
  ```python
  def resample_length(self, selection=None, length=None)
  ```

 - [resample_evaluated](Curve.md#resample_evaluated)
  ```python
  def resample_evaluated(self, selection=None)
  ```

#### [Spline](Spline.md)

 - [resample](Spline.md#resample)
  ```python
  def resample(self, count=None, length=None, mode='COUNT')
  ```

 - [resample_count](Spline.md#resample_count)
  ```python
  def resample_count(self, count=None)
  ```

 - [resample_length](Spline.md#resample_length)
  ```python
  def resample_length(self, length=None)
  ```

 - [resample_evaluated](Spline.md#resample_evaluated)
  ```python
  def resample_evaluated(self)
  ```

