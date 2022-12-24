# Node *Distribute Points on Faces*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html)
- geonodes name: `DistributePointsOnFaces`
- bl_idname: `GeometryNodeDistributePointsOnFaces`

```python
from geonodes import nodes

node = nodes.DistributePointsOnFaces(mesh=None, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDistributePointsOnFaces.webp)

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

| Class or method name | Definition |
|----------------------|------------|
| **[Face](Face.md)** |
| [distribute_points_random](Face.md#distribute_points_random) | `def distribute_points_random(self, density=None, seed=None):` |
| [distribute_points_poisson](Face.md#distribute_points_poisson) | `def distribute_points_poisson(self, distance_min=None, density_max=None, density_factor=None, seed=None):` |
| **[Mesh](Mesh.md)** |
| [distribute_points_on_faces](Mesh.md#distribute_points_on_faces) | `def distribute_points_on_faces(self, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM'):` |

<sub>Go to [top](#node-Distribute-Points-on-Faces) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

