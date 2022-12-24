# Node *Face Area*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_area.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceArea.html)
- geonodes name: `FaceArea`
- bl_idname: `GeometryNodeInputMeshFaceArea`

```python
from geonodes import nodes

node = nodes.FaceArea()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshFaceArea.webp)

### Output sockets:

- **area** : [Float](Float.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Face](Face.md)** |
| [area](Face.md#area) | `@property`<br> `def area(self):` |

<sub>Go to [top](#node-Face-Area) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

