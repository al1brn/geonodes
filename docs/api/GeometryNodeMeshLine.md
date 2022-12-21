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
  nodes.MeshLine(count=count, resolution=resolution, start_location=start_location, offset=offset, count_mode=count_mode, mode=mode  ```

 - [LineEndPoints](Mesh.md#LineEndPoints-classmethod)
  ```python
  nodes.MeshLine(count=count, resolution=None, start_location=start_location, offset=end_location, count_mode='TOTAL', mode=END_POINTS  ```

 - [LineOffset](Mesh.md#LineOffset-classmethod)
  ```python
  nodes.MeshLine(count=count, resolution=None, start_location=start_location, offset=offset, count_mode='TOTAL', mode=OFFSET  ```

 - [LineEndPointsResolution](Mesh.md#LineEndPointsResolution-classmethod)
  ```python
  nodes.MeshLine(count=None, resolution=resolution, start_location=start_location, offset=end_location, count_mode='RESOLUTION', mode=END_POINTS  ```

 - [LineOffsetResolution](Mesh.md#LineOffsetResolution-classmethod)
  ```python
  nodes.MeshLine(count=None, resolution=resolution, start_location=start_location, offset=offset, count_mode='RESOLUTION', mode=OFFSET  ```

