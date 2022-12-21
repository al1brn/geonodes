# Node Distribute Points on Faces

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html)
- geonodes name: `DistributePointsOnFaces`
- bl_idname: `GeometryNodeDistributePointsOnFaces`

```python
from geonodes import nodes

node = nodes.DistributePointsOnFaces(mesh=None, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM')
```

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **selection**: [Boolean](Boolean.md)
- **distance_min**: [Float](Float.md)
- **density_max**: [Float](Float.md)
- **density**: [Float](Float.md)
- **density_factor**: [Float](Float.md)
- **seed**: [Integer](Integer.md)

#### Node parameter arguments:

- **distribute_method** (str): default = 'RANDOM' in ('RANDOM', 'POISSON')

### Output sockets:

- **points** : [Points](Points.md)
- **normal** : [Vector](Vector.md)
- **rotation** : [Vector](Vector.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x1683b2c20>>](Mesh.md#distribute_points_on_faces)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomMethod object at 0x1683b2bc0>>](Face.md#distribute_points_random)
 - [<bound method Generator.fname of <generator.code_gen.DomMethod object at 0x1683b0070>>](Face.md#distribute_points_poisson)
