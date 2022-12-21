# Node Set Material

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)
- geonodes name: `SetMaterial`
- bl_idname: `GeometryNodeSetMaterial`

```python
from geonodes import nodes

node = nodes.SetMaterial(geometry=None, selection=None, material=None)
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **material**: [Material](Material.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

#### [Face](Face.md)

 - [set_material](Face.md#set_material)
  ```python
  nodes.SetMaterial(geometry=self.data_socket, selection=self.selection, material=material  ```

 - [material](Face.md#material-property)
  ```python
  nodes.SetMaterial(geometry=geometry, selection=selection, material=material  ```

 - [material](Face.md#material)
  ```python
  nodes.SetMaterial(geometry=self.data_socket, selection=self.selection, material=attr_value  ```

#### [Geometry](Geometry.md)

 - [set_material](Geometry.md#set_material)
  ```python
  nodes.SetMaterial(geometry=self, selection=selection, material=material  ```

#### [Spline](Spline.md)

 - [set_material](Spline.md#set_material)
  ```python
  nodes.SetMaterial(geometry=self.data_socket, selection=self.selection, material=material  ```

 - [material](Spline.md#material-property)
  ```python
  nodes.SetMaterial(geometry=geometry, selection=selection, material=material  ```

 - [material](Spline.md#material)
  ```python
  nodes.SetMaterial(geometry=self.data_socket, selection=self.selection, material=attr_value  ```

