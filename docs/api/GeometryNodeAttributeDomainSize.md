# Node *Domain Size*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

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

| Class or method name | Definition |
|----------------------|------------|
| **[CloudPoint](CloudPoint.md)** |
| [count](CloudPoint.md#count) | `@property`<br> `def count(self):` |
| **[ControlPoint](ControlPoint.md)** |
| [count](ControlPoint.md#count) | `@property`<br> `def count(self):` |
| **[Corner](Corner.md)** |
| [count](Corner.md#count) | `@property`<br> `def count(self):` |
| **[Curve](Curve.md)** |
| [domain_size](Curve.md#domain_size) | `@property`<br> `def domain_size(self):` |
| [point_count](Curve.md#point_count) | `@property`<br> `def point_count(self):` |
| [spline_count](Curve.md#spline_count) | `@property`<br> `def spline_count(self):` |
| **[Edge](Edge.md)** |
| [count](Edge.md#count) | `@property`<br> `def count(self):` |
| **[Face](Face.md)** |
| [count](Face.md#count) | `@property`<br> `def count(self):` |
| **[Geometry](Geometry.md)** |
| [domain_size](Geometry.md#domain_size) | `@property`<br> `def domain_size(self, component='MESH'):` |
| **[Instance](Instance.md)** |
| [count](Instance.md#count) | `@property`<br> `def count(self):` |
| **[Instances](Instances.md)** |
| [domain_size](Instances.md#domain_size) | `@property`<br> `def domain_size(self):` |
| **[Mesh](Mesh.md)** |
| [domain_size](Mesh.md#domain_size) | `@property`<br> `def domain_size(self):` |
| [point_count](Mesh.md#point_count) | `@property`<br> `def point_count(self):` |
| [face_count](Mesh.md#face_count) | `@property`<br> `def face_count(self):` |
| [edge_count](Mesh.md#edge_count) | `@property`<br> `def edge_count(self):` |
| [corner_count](Mesh.md#corner_count) | `@property`<br> `def corner_count(self):` |
| **[Points](Points.md)** |
| [domain_size](Points.md#domain_size) | `@property`<br> `def domain_size(self):` |
| **[Spline](Spline.md)** |
| [count](Spline.md#count) | `@property`<br> `def count(self):` |
| **[Vertex](Vertex.md)** |
| [count](Vertex.md#count) | `@property`<br> `def count(self):` |

<sub>Go to [top](#node-Domain-Size) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

