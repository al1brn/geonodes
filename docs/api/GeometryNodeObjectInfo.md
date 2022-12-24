# Node *Object Info*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)
- geonodes name: `ObjectInfo`
- bl_idname: `GeometryNodeObjectInfo`

```python
from geonodes import nodes

node = nodes.ObjectInfo(object=None, as_instance=None, transform_space='ORIGINAL')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeObjectInfo.webp)

### Args:

#### Input socket arguments:

- **object**: [Object](Object.md)
- **as_instance**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **transform_space** (str): default = 'ORIGINAL' in ('ORIGINAL', 'RELATIVE')

### Output sockets:

- **location** : [Vector](Vector.md)
- **rotation** : [Vector](Vector.md)
- **scale** : [Vector](Vector.md)
- **geometry** : [Geometry](Geometry.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Object](Object.md)** |
| [info](Object.md#info) | `def info(self, as_instance=None, transform_space='ORIGINAL'):` |
| [location](Object.md#location) | `def location(self, as_instance=None, transform_space='ORIGINAL'):` |
| [rotation](Object.md#rotation) | `def rotation(self, as_instance=None, transform_space='ORIGINAL'):` |
| [scale](Object.md#scale) | `def scale(self, as_instance=None, transform_space='ORIGINAL'):` |
| [geometry](Object.md#geometry) | `def geometry(self, as_instance=None, transform_space='ORIGINAL'):` |

<sub>Go to [top](#node-Object-Info) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

