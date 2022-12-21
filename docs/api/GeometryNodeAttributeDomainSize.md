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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1639de080>>](Geometry.md#domain_size-property)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1639de140>>](Mesh.md#domain_size-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1639dc4c0>>](Mesh.md#point_count-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1639dd300>>](Mesh.md#face_count-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1639dd8d0>>](Mesh.md#edge_count-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1639ddbd0>>](Mesh.md#corner_count-property)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1639ddf60>>](Curve.md#domain_size-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1639ddba0>>](Curve.md#point_count-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1639dd960>>](Curve.md#spline_count-property)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1639dc100>>](Points.md#domain_size-property)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1639dc0d0>>](Instances.md#domain_size-property)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x1639dc1c0>>](Vertex.md#domain_size)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x1639de6b0>>](Face.md#domain_size)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x1639ddc90>>](Edge.md#domain_size)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x1639dded0>>](Corner.md#domain_size)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x1639dd870>>](Spline.md#domain_size)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x1639ddae0>>](ControlPoint.md#domain_size)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x1639ddea0>>](CloudPoint.md#domain_size)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x1639dc4f0>>](Instance.md#domain_size)
