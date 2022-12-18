
# Node Clamp

> Geometry node name: [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html)<br>
  Blender type: [Clamp](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Clamp(value=None, min=None, max=None, clamp_type='MINMAX', label=None, node_color=None)
```



## Arguments


### Input sockets

- value : Float
- min : Float
- max : Float

### Parameters

- clamp_type : str (default = 'MINMAX') in ('MINMAX', 'RANGE')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- result : Float
