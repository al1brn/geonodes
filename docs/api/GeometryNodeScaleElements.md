# Node *Scale Elements*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)
- geonodes name: `ScaleElements`
- bl_idname: `GeometryNodeScaleElements`

```python
from geonodes import nodes

node = nodes.ScaleElements(geometry=None, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeScaleElements.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **scale**: [Float](Float.md)
- **center**: [Vector](Vector.md)
- **axis**: [Vector](Vector.md)

#### Node parameter arguments:

- **domain** (str): default = 'FACE' in ('FACE', 'EDGE')
- **scale_mode** (str): default = 'UNIFORM' in ('UNIFORM', 'SINGLE_AXIS')

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Edge](Edge.md)** |
| [scale_uniform](Edge.md#scale_uniform) | `def scale_uniform(self, scale=None, center=None):` |
| [scale_single_axis](Edge.md#scale_single_axis) | `def scale_single_axis(self, scale=None, center=None, axis=None):` |
| **[Face](Face.md)** |
| [scale_uniform](Face.md#scale_uniform) | `def scale_uniform(self, scale=None, center=None):` |
| [scale_single_axis](Face.md#scale_single_axis) | `def scale_single_axis(self, scale=None, center=None, axis=None):` |
| **[Mesh](Mesh.md)** |
| [scale_elements](Mesh.md#scale_elements) | `def scale_elements(self, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM'):` |
| [scale_uniform](Mesh.md#scale_uniform) | `def scale_uniform(self, selection=None, scale=None, center=None, domain='FACE'):` |
| [scale_single_axis](Mesh.md#scale_single_axis) | `def scale_single_axis(self, selection=None, scale=None, center=None, axis=None, domain='FACE'):` |

<sub>Go to [top](#node-Scale-Elements) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

