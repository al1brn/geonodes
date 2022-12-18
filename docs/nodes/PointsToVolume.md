
# Node PointsToVolume

> Geometry node name: [Points to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html)<br>
  Blender type: [Points to Volume](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.PointsToVolume(points=None, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT', label=None, node_color=None)
```



## Arguments


### Input sockets

- points : Points
- density : Float
- voxel_size : Float
- voxel_amount : Float
- radius : Float

### Parameters

- resolution_mode : str (default = 'VOXEL_AMOUNT') in ('VOXEL_AMOUNT', 'VOXEL_SIZE')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- volume : Volume
