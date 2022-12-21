# Node 'Object Info'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)
- geonodes name: `ObjectInfo`
- bl_idname: `GeometryNodeObjectInfo`

```python
from geonodes import nodes

node = nodes.ObjectInfo(object=None, as_instance=None, transform_space='ORIGINAL')
```

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

### [Object](Object.md)

| Name | Definition |
|------|------------|
 | [info](Object.md#info) | `def info(self, object=None, as_instance=None, transform_space='ORIGINAL'):` |
 | [location](Object.md#location) | `def location(self, object=None, as_instance=None, transform_space='ORIGINAL'):` |
 | [rotation](Object.md#rotation) | `def rotation(self, object=None, as_instance=None, transform_space='ORIGINAL'):` |
 | [scale](Object.md#scale) | `def scale(self, object=None, as_instance=None, transform_space='ORIGINAL'):` |
 | [geometry](Object.md#geometry) | `def geometry(self, object=None, as_instance=None, transform_space='ORIGINAL'):` |

<sub>Go to [top](#node-{wnode.bnode.name}) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

