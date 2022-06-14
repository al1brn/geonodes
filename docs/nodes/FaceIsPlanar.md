
# Node FaceIsPlanar

> Geometry node name: [Face is Planar](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_is_planar.html)<br>
  Blender type: [Face is Planar](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.FaceIsPlanar(threshold=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- threshold : Float

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- planar : Boolean
