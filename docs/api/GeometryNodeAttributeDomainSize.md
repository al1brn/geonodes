# Node Domain Size

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)
- geonodes name: `DomainSize`
- bl_idname: `GeometryNodeAttributeDomainSize`

```python
from geonodes import nodes

node = nodes.DomainSize(geometry=None, component='MESH')
```

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

#### class [Geometry](Geometry.md)

 - [domain_size](Geometry.md#domain_size-property)
#### class [Mesh](Mesh.md)

 - [domain_size](Mesh.md#domain_size-property)
 - [point_count](Mesh.md#point_count-property)
 - [face_count](Mesh.md#face_count-property)
 - [edge_count](Mesh.md#edge_count-property)
 - [corner_count](Mesh.md#corner_count-property)
#### class [Curve](Curve.md)

 - [domain_size](Curve.md#domain_size-property)
 - [point_count](Curve.md#point_count-property)
 - [spline_count](Curve.md#spline_count-property)
#### class [Points](Points.md)

 - [domain_size](Points.md#domain_size-property)
#### class [Instances](Instances.md)

 - [domain_size](Instances.md#domain_size-property)
#### class [Vertex](Vertex.md)

 - [domain_size](Vertex.md#domain_size)
#### class [Face](Face.md)

 - [domain_size](Face.md#domain_size)
#### class [Edge](Edge.md)

 - [domain_size](Edge.md#domain_size)
#### class [Corner](Corner.md)

 - [domain_size](Corner.md#domain_size)
#### class [Spline](Spline.md)

 - [domain_size](Spline.md#domain_size)
#### class [ControlPoint](ControlPoint.md)

 - [domain_size](ControlPoint.md#domain_size)
#### class [CloudPoint](CloudPoint.md)

 - [domain_size](CloudPoint.md#domain_size)
#### class [Instance](Instance.md)

 - [domain_size](Instance.md#domain_size)
