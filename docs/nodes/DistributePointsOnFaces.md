
# Node DistributePointsOnFaces

> Geometry node name: [Distribute Points on Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html)<br>
  Blender type: [Distribute Points on Faces](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.DistributePointsOnFaces(mesh=None, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM', label=None, node_color=None)
```



## Arguments


### Input sockets

- mesh : Mesh
- selection : Boolean
- distance_min : Float
- density_max : Float
- density : Float
- density_factor : Float
- seed : Integer

### Parameters

- distribute_method : str (default = 'RANDOM') in ('RANDOM', 'POISSON')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- points : Points
- normal : Vector
- rotation : Vector
