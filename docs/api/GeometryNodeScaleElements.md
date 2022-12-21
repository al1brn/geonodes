# Node Scale Elements

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeScaleElements`

```python
from geonodes import nodes

node = nodes.ScaleElements(geometry=None, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM')
```

#### Input socket arguments:

- geometry: Geometry
- selection: Boolean
- scale: Float
- center: Vector
- axis: Vector

#### Node parameter arguments:

- domain (str): Node parameter, default = 'FACE' in ('FACE', 'EDGE')
- scale_mode (str): Node parameter, default = 'UNIFORM' in ('UNIFORM', 'SINGLE_AXIS')

#### Output sockets:

- **geometry** : Geometry

