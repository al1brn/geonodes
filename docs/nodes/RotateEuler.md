
# Node RotateEuler

> Geometry node name: [Rotate Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/rotate_euler.html)<br>
  Blender type: [Rotate Euler](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.RotateEuler(rotation=None, rotate_by=None, axis=None, angle=None, space='OBJECT', label=None)
```



## Arguments


### Input sockets

- rotation : Vector
- rotate_by : Vector
- axis : Vector
- angle : Float

### Parameters

- space : str (default = 'OBJECT') in ('OBJECT', 'LOCAL')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- rotation : Vector

## Data sockets

> Data socket classes implementing this node.
  
  
- [Vector](/docs/sockets/Vector.md).[rotate_euler](/docs/sockets/Vector.md#rotate_euler) : Method
  
