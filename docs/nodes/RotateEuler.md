
# Node RotateEuler

> Geometry node name: [Rotate Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotate_euler.html)<br>
  Blender type: [Rotate Euler](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.RotateEuler(rotation=None, rotate_by=None, axis=None, angle=None, space='OBJECT', type='EULER', label=None, node_color=None)
```



## Arguments


### Input sockets

- rotation : Vector
- rotate_by : Vector
- axis : Vector
- angle : Float

### Parameters

- space : str (default = 'OBJECT') in ('OBJECT', 'LOCAL')
- type : str (default = 'EULER') in ('AXIS_ANGLE', 'EULER')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- rotation : Vector
