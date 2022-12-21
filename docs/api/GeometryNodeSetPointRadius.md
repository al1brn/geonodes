# Node Set Point Radius

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)
- geonodes name: `SetPointRadius`
- bl_idname: `GeometryNodeSetPointRadius`

```python
from geonodes import nodes

node = nodes.SetPointRadius(points=None, selection=None, radius=None)
```

### Args:

#### Input socket arguments:

- **points**: [Points](Points.md)
- **selection**: [Boolean](Boolean.md)
- **radius**: [Float](Float.md)

### Output sockets:

- **points** : [Points](Points.md)

## Implementation

#### [CloudPoint](CloudPoint.md)

 - [radius](CloudPoint.md#radius) ```python nodes.SetPointRadius(points=self.data_socket, selection=self.selection, radius=attr_value````
#### [Points](Points.md)

 - [set_point_radius](Points.md#set_point_radius) ```python nodes.SetPointRadius(points=self, selection=selection, radius=radius````
