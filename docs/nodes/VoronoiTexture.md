
# Node VoronoiTexture

> Geometry node name: [Voronoi Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html)<br>
  Blender type: [Voronoi Texture](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.VoronoiTexture(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D', label=None, node_color=None)
```



## Arguments


### Input sockets

- vector : Vector
- w : Float
- scale : Float
- smoothness : Float
- exponent : Float
- randomness : Float

### Parameters

- distance : str (default = 'EUCLIDEAN') in ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI')
- feature : str (default = 'F1') in ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS')
- voronoi_dimensions : str (default = '3D') in ('1D', '2D', '3D', '4D')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- distance : Float
- color : Color
- position : Vector
- w : Float
- radius : Float
