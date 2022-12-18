
# Node FloatToInteger

> Geometry node name: [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html)<br>
  Blender type: [Float to Integer](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.FloatToInteger(float=None, rounding_mode='ROUND', label=None, node_color=None)
```



## Arguments


### Input sockets

- float : Float

### Parameters

- rounding_mode : str (default = 'ROUND') in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- integer : Integer
