
# Node VolumeToMesh

> Geometry node name: [Volume to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/volume_to_mesh.html)<br>
  Blender type: [Volume to Mesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeToMesh.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.VolumeToMesh(volume=None, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID', label=None, node_color=None)
```



## Arguments


### Input sockets

- volume : Volume
- voxel_size : Float
- voxel_amount : Float
- threshold : Float
- adaptivity : Float

### Parameters

- resolution_mode : str (default = 'GRID') in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- mesh : Mesh
