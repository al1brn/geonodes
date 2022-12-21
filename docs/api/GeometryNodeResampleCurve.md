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
  nodes.ResampleCurve(curve=self, selection=selection, count=count, length=length, mode=mode  ```

 - [resample_count](Curve.md#resample_count)
  ```python
  nodes.ResampleCurve(curve=self, selection=selection, count=count, length=0.1, mode='COUNT'  ```

 - [resample_length](Curve.md#resample_length)
  ```python
  nodes.ResampleCurve(curve=self, selection=selection, count=10, length=length, mode='LENGTH'  ```

 - [resample_evaluated](Curve.md#resample_evaluated)
  ```python
  nodes.ResampleCurve(curve=self, selection=selection, count=10, length=0.1, mode='EVALUATED'  ```

#### [Spline](Spline.md)

 - [resample](Spline.md#resample)
  ```python
  nodes.ResampleCurve(curve=self.data_socket, selection=self.selection, count=count, length=length, mode=mode  ```

 - [resample_count](Spline.md#resample_count)
  ```python
  nodes.ResampleCurve(curve=self.data_socket, selection=self.selection, count=count, length=0.1, mode='COUNT'  ```

 - [resample_length](Spline.md#resample_length)
  ```python
  nodes.ResampleCurve(curve=self.data_socket, selection=self.selection, count=10, length=length, mode='LENGTH'  ```

 - [resample_evaluated](Spline.md#resample_evaluated)
  ```python
  nodes.ResampleCurve(curve=self.data_socket, selection=self.selection, count=10, length=0.1, mode='EVALUATED'  ```

