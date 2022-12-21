# Node Volume Cube

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/volume_cube.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeCube.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeVolumeCube`

```python
from geonodes import nodes

node = nodes.VolumeCube(density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None)
```

#### Input socket arguments:

- density: Float
- background: Float
- min: Vector
- max: Vector
- resolution_x: Integer
- resolution_y: Integer
- resolution_z: Integer

#### Output sockets:

- **volume** : Volume

