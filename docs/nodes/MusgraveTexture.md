
# Node MusgraveTexture

> Geometry node name: [Musgrave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/musgrave.html)<br>
  Blender type: [Musgrave Texture](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMusgrave.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.MusgraveTexture(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM', label=None, node_color=None)
```



## Arguments


### Input sockets

- vector : Vector
- w : Float
- scale : Float
- detail : Float
- dimension : Float
- lacunarity : Float
- offset : Float
- gain : Float

### Parameters

- musgrave_dimensions : str (default = '3D') in ('1D', '2D', '3D', '4D')
- musgrave_type : str (default = 'FBM') in ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- fac : Float
