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

 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16e1a3e80>>](Geometry.md#domain_size-property)
#### class [Mesh](Mesh.md)

 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16e1a3e50>>](Mesh.md#domain_size-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16e1a3fd0>>](Mesh.md#point_count-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16e1a3cd0>>](Mesh.md#face_count-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16e1a3e20>>](Mesh.md#edge_count-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16e1a3fa0>>](Mesh.md#corner_count-property)
#### class [Curve](Curve.md)

 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16e1a3ca0>>](Curve.md#domain_size-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16e1a3d00>>](Curve.md#point_count-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16e1a3d90>>](Curve.md#spline_count-property)
#### class [Points](Points.md)

 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16e1a3eb0>>](Points.md#domain_size-property)
#### class [Instances](Instances.md)

 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16e1a3d30>>](Instances.md#domain_size-property)
#### class [Vertex](Vertex.md)

 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x16e1a3dc0>>](Vertex.md#domain_size)
#### class [Face](Face.md)

 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x16d4fbf40>>](Face.md#domain_size)
#### class [Edge](Edge.md)

 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x16d4fbf70>>](Edge.md#domain_size)
#### class [Corner](Corner.md)

 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x16d4fbfa0>>](Corner.md#domain_size)
#### class [Spline](Spline.md)

 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x16d4fbfd0>>](Spline.md#domain_size)
#### class [ControlPoint](ControlPoint.md)

 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x16d4fbdc0>>](ControlPoint.md#domain_size)
#### class [CloudPoint](CloudPoint.md)

 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x16d4fbd90>>](CloudPoint.md#domain_size)
#### class [Instance](Instance.md)

 - [<bound method Generator.fname of <generator.code_gen.Source object at 0x16d4fbd60>>](Instance.md#domain_size)
