# Node Mesh Line

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)
- geonodes name: `MeshLine`
- bl_idname: `GeometryNodeMeshLine`

```python
from geonodes import nodes

node = nodes.MeshLine(count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET')
```

### Args:

#### Input socket arguments:

- **count**: [Integer](Integer.md)
- **resolution**: [Float](Float.md)
- **start_location**: [Vector](Vector.md)
- **offset**: [Vector](Vector.md)

#### Node parameter arguments:

- **count_mode** (str): default = 'TOTAL' in ('TOTAL', 'RESOLUTION')
- **mode** (str): default = 'OFFSET' in ('OFFSET', 'END_POINTS')

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

#### [Mesh](Mesh.md)

 - [Line](Mesh.md#Line-classmethod)
  ```python
  def Line(cls, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET')
  ```

 - [LineEndPoints](Mesh.md#LineEndPoints-classmethod)
  ```python
  def LineEndPoints(cls, count=None, start_location=None, end_location=None)
  ```

 - [LineOffset](Mesh.md#LineOffset-classmethod)
  ```python
  def LineOffset(cls, count=None, start_location=None, offset=None)
  ```

 - [LineEndPointsResolution](Mesh.md#LineEndPointsResolution-classmethod)
  ```python
  def LineEndPointsResolution(cls, resolution=None, start_location=None, end_location=None)
  ```

 - [LineOffsetResolution](Mesh.md#LineOffsetResolution-classmethod)
  ```python
  def LineOffsetResolution(cls, resolution=None, start_location=None, offset=None)
  ```

