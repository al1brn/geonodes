
# Node UvUnwrap

> Geometry node name: [UV Unwrap](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/uv_unwrap.html)<br>
  Blender type: [UV Unwrap](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVUnwrap.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.UvUnwrap(selection=None, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED', label=None, node_color=None)
```



## Arguments


### Input sockets

- selection : Boolean
- seam : Boolean
- margin : Float
- fill_holes : Boolean

### Parameters

- method : str (default = 'ANGLE_BASED') in ('ANGLE_BASED', 'CONFORMAL')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- uv : Vector
