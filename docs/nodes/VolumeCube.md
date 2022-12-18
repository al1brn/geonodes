
# Node VolumeCube

> Geometry node name: [Volume Cube](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/volume_cube.html)<br>
  Blender type: [Volume Cube](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeCube.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.VolumeCube(density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- density : Float
- background : Float
- min : Vector
- max : Vector
- resolution_x : Integer
- resolution_y : Integer
- resolution_z : Integer

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- volume : Volume
