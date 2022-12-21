# Node Scale Elements

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)
- geonodes name: `ScaleElements`
- bl_idname: `GeometryNodeScaleElements`

```python
from geonodes import nodes

node = nodes.ScaleElements(geometry=None, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM')
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **scale**: [Float](Float.md)
- **center**: [Vector](Vector.md)
- **axis**: [Vector](Vector.md)

#### Node parameter arguments:

- **domain** (str): default = 'FACE' in ('FACE', 'EDGE')
- **scale_mode** (str): default = 'UNIFORM' in ('UNIFORM', 'SINGLE_AXIS')

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

#### [Edge](Edge.md)

 - [scale_uniform](Edge.md#scale_uniform)
  ```python
  nodes.ScaleElements(geometry=self.data_socket, selection=self.selection, scale=scale, center=center, axis=None, domain=self.domain, scale_mode='UNIFORM'  ```

 - [scale_single_axis](Edge.md#scale_single_axis)
  ```python
  nodes.ScaleElements(geometry=self.data_socket, selection=self.selection, scale=scale, center=center, axis=axis, domain=self.domain, scale_mode='SINGLE_AXIS'  ```

#### [Face](Face.md)

 - [scale_uniform](Face.md#scale_uniform)
  ```python
  nodes.ScaleElements(geometry=self.data_socket, selection=self.selection, scale=scale, center=center, axis=None, domain=self.domain, scale_mode='UNIFORM'  ```

 - [scale_single_axis](Face.md#scale_single_axis)
  ```python
  nodes.ScaleElements(geometry=self.data_socket, selection=self.selection, scale=scale, center=center, axis=axis, domain=self.domain, scale_mode='SINGLE_AXIS'  ```

#### [Mesh](Mesh.md)

 - [scale_elements](Mesh.md#scale_elements)
  ```python
  nodes.ScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=axis, domain=domain, scale_mode=scale_mode  ```

 - [scale_uniform](Mesh.md#scale_uniform)
  ```python
  nodes.ScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=None, domain=domain, scale_mode='UNIFORM'  ```

 - [scale_single_axis](Mesh.md#scale_single_axis)
  ```python
  nodes.ScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=axis, domain=domain, scale_mode='SINGLE_AXIS'  ```

