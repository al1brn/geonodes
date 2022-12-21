# Node Voronoi Texture

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)
- geonodes name: `VoronoiTexture`
- bl_idname: `ShaderNodeTexVoronoi`

```python
from geonodes import nodes

node = nodes.VoronoiTexture(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D')
```

### Args:

#### Input socket arguments:

- **vector**: [Vector](Vector.md)
- **w**: [Float](Float.md)
- **scale**: [Float](Float.md)
- **smoothness**: [Float](Float.md)
- **exponent**: [Float](Float.md)
- **randomness**: [Float](Float.md)

#### Node parameter arguments:

- **distance** (str): default = 'EUCLIDEAN' in ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI')
- **feature** (str): default = 'F1' in ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS')
- **voronoi_dimensions** (str): default = '3D' in ('1D', '2D', '3D', '4D')

### Output sockets:

- **distance** : [Float](Float.md)
- **color** : [Color](Color.md)
- **position** : [Vector](Vector.md)
- **w** : [Float](Float.md)
- **radius** : [Float](Float.md)

## Implementation

#### class [Texture](Texture.md)

 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x16e37a4a0>>](Texture.md#voronoi-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x16e37a140>>](Texture.md#voronoi_1D-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x16e37bf70>>](Texture.md#voronoi_2D-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x16e37ab60>>](Texture.md#voronoi_3D-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x16e37a290>>](Texture.md#voronoi_4D-staticmethod)
