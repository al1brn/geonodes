
# Node MapRange

> Geometry node name: [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html)<br>
  Blender type: [Map Range](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.MapRange(value=None, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, vector=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR', label=None, node_color=None)
```



## Arguments


### Input sockets

- value : Float
- from_min : data_type dependant
- from_max : data_type dependant
- to_min : data_type dependant
- to_max : data_type dependant
- steps : data_type dependant
- vector : Vector

### Parameters

- clamp : bool (default = True)
- data_type : str (default = 'FLOAT') in ('FLOAT', 'FLOAT_VECTOR')
- interpolation_type : str (default = 'LINEAR') in ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Data type dependant sockets

- Driving parameter : data_type in ('FLOAT', 'FLOAT_VECTOR')
- Input sockets  : ['from_min', 'from_max', 'to_min', 'to_max', 'steps']
- Output sockets : []   
  
  

## Output sockets

- result : Float
- vector : Vector
