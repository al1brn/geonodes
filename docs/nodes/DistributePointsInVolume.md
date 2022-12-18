
# Node DistributePointsInVolume

> Geometry node name: [Distribute Points in Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_in_volume.html)<br>
  Blender type: [Distribute Points in Volume](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.DistributePointsInVolume(volume=None, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM', label=None, node_color=None)
```



## Arguments


### Input sockets

- volume : Volume
- density : Float
- seed : Integer
- spacing : Vector
- threshold : Float

### Parameters

- mode : str (default = 'DENSITY_RANDOM') in ('DENSITY_RANDOM', 'DENSITY_GRID')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- points : Points
