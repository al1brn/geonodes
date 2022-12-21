# Node Remove Named Attribute

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)
- geonodes name: `RemoveNamedAttribute`
- bl_idname: `GeometryNodeRemoveAttribute`

```python
from geonodes import nodes

node = nodes.RemoveNamedAttribute(geometry=None, name=None)
```

#### Input socket arguments:

- geometry: [Geometry](Geometry.md)
- name: [String](String.md)

#### Output sockets:

- **geometry** : [Geometry](Geometry.md)

