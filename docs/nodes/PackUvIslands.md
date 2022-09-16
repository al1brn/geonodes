
# Node PackUvIslands

> Geometry node name: [Pack UV Islands](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/pack_uv_islands.html)<br>
  Blender type: [Pack UV Islands](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.PackUvIslands(uv=None, selection=None, margin=None, rotate=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- uv : Vector
- selection : Boolean
- margin : Float
- rotate : Boolean

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- uv : Vector
