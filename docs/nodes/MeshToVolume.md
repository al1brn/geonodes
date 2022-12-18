
# Node MeshToVolume

> Geometry node name: [Mesh to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_volume.html)<br>
  Blender type: [Mesh to Volume](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToVolume.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.MeshToVolume(mesh=None, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT', label=None, node_color=None)
```



## Arguments


### Input sockets

- mesh : Mesh
- density : Float
- voxel_size : Float
- voxel_amount : Float
- exterior_band_width : Float
- interior_band_width : Float
- fill_volume : Boolean

### Parameters

- resolution_mode : str (default = 'VOXEL_AMOUNT') in ('VOXEL_AMOUNT', 'VOXEL_SIZE')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- volume : Volume
