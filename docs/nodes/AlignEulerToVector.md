
# Node AlignEulerToVector

> Geometry node name: [Align Euler to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/align_euler_to_vector.html)<br>
  Blender type: [Align Euler to Vector](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.AlignEulerToVector(rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO', label=None, node_color=None)
```



## Arguments


### Input sockets

- rotation : Vector
- factor : Float
- vector : Vector

### Parameters

- axis : str (default = 'X') in ('X', 'Y', 'Z')
- pivot_axis : str (default = 'AUTO') in ('AUTO', 'X', 'Y', 'Z')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- rotation : Vector
