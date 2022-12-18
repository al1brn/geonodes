
# Node VectorRotate

> Geometry node name: [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html)<br>
  Blender type: [Vector Rotate](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.VectorRotate(vector=None, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE', label=None, node_color=None)
```



## Arguments


### Input sockets

- vector : Vector
- center : Vector
- axis : Vector
- angle : Float
- rotation : Vector

### Parameters

- invert : bool (default = False)
- rotation_type : str (default = 'AXIS_ANGLE') in ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- vector : Vector
