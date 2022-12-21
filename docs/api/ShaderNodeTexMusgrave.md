# Node Musgrave Texture

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/musgrave.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMusgrave.html)
- geonodes name: `MusgraveTexture`
- bl_idname: `ShaderNodeTexMusgrave`

```python
from geonodes import nodes

node = nodes.MusgraveTexture(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM')
```

#### Input socket arguments:

- vector: Vector
- w: Float
- scale: Float
- detail: Float
- dimension: Float
- lacunarity: Float
- offset: Float
- gain: Float

#### Node parameter arguments:

- musgrave_dimensions (str): Node parameter, default = '3D' in ('1D', '2D', '3D', '4D')
- musgrave_type (str): Node parameter, default = 'FBM' in ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN')

#### Output sockets:

- **fac** : Float

