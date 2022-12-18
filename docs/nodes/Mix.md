
# Node Mix

> Geometry node name: [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)<br>
  Blender type: [Mix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Mix(factor=None, a=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM', label=None, node_color=None)
```



## Arguments


### Input sockets

- factor : data_type dependant
- a : data_type dependant
- b : data_type dependant

### Parameters

- blend_type : str (default = 'MIX') in ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE')
- clamp_factor : bool (default = True)
- clamp_result : bool (default = False)
- data_type : str (default = 'FLOAT') in ('FLOAT', 'VECTOR', 'RGBA')
- factor_mode : str (default = 'UNIFORM') in ('UNIFORM', 'NON_UNIFORM')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Data type dependant sockets

- Driving parameter : data_type in ('FLOAT', 'VECTOR', 'RGBA')
- Input sockets  : ['factor', 'a', 'b']
- Output sockets : ['result']   
  
  

## Output sockets

- result : data_type dependant
