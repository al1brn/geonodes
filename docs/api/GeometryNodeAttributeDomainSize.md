# Node 'Domain Size'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)
- geonodes name: `DomainSize`
- bl_idname: `GeometryNodeAttributeDomainSize`

```python
from geonodes import nodes

node = nodes.DomainSize(geometry=None, component='MESH')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeDomainSize.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)

#### Node parameter arguments:

- **component** (str): default = 'MESH' in ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES')

### Output sockets:

- **point_count** : [Integer](Integer.md)
- **edge_count** : [Integer](Integer.md)
- **face_count** : [Integer](Integer.md)
- **face_corner_count** : [Integer](Integer.md)
- **spline_count** : [Integer](Integer.md)
- **instance_count** : [Integer](Integer.md)

## Implementation

### [CloudPoint](CloudPoint.md)

| Name | Definition |
|------|------------|
 | [domain_size](CloudPoint.md#domain_size) | `def __len__(self):` |

### [ControlPoint](ControlPoint.md)

| Name | Definition |
|------|------------|
 | [domain_size](ControlPoint.md#domain_size) | `def __len__(self):` |

### [Corner](Corner.md)

| Name | Definition |
|------|------------|
 | [domain_size](Corner.md#domain_size) | `def __len__(self):` |

### [Curve](Curve.md)

| Name | Definition |
|------|------------|
 | [domain_size](Curve.md#domain_size-property) | `def domain_size(self):` |
 | [point_count](Curve.md#point_count-property) | `def point_count(self):` |
 | [spline_count](Curve.md#spline_count-property) | `def spline_count(self):` |

### [Edge](Edge.md)

| Name | Definition |
|------|------------|
 | [domain_size](Edge.md#domain_size) | `def __len__(self):` |

### [Face](Face.md)

| Name | Definition |
|------|------------|
 | [domain_size](Face.md#domain_size) | `def __len__(self):` |

### [Geometry](Geometry.md)

| Name | Definition |
|------|------------|
 | [domain_size](Geometry.md#domain_size-property) | `def domain_size(self, component='MESH'):` |

### [Instance](Instance.md)

| Name | Definition |
|------|------------|
 | [domain_size](Instance.md#domain_size) | `def __len__(self):` |

### [Instances](Instances.md)

| Name | Definition |
|------|------------|
 | [domain_size](Instances.md#domain_size-property) | `def domain_size(self):` |

### [Mesh](Mesh.md)

| Name | Definition |
|------|------------|
 | [domain_size](Mesh.md#domain_size-property) | `def domain_size(self):` |
 | [point_count](Mesh.md#point_count-property) | `def point_count(self):` |
 | [face_count](Mesh.md#face_count-property) | `def face_count(self):` |
 | [edge_count](Mesh.md#edge_count-property) | `def edge_count(self):` |
 | [corner_count](Mesh.md#corner_count-property) | `def corner_count(self):` |

### [Points](Points.md)

| Name | Definition |
|------|------------|
 | [domain_size](Points.md#domain_size-property) | `def domain_size(self):` |

### [Spline](Spline.md)

| Name | Definition |
|------|------------|
 | [domain_size](Spline.md#domain_size) | `def __len__(self):` |

### [Vertex](Vertex.md)

| Name | Definition |
|------|------------|
 | [domain_size](Vertex.md#domain_size) | `def __len__(self):` |

<sub>Go to [top](#node-Domain-Size) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

