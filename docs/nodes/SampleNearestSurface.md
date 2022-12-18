
# Node SampleNearestSurface

> Geometry node name: [Sample Nearest Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample_nearest_surface.html)<br>
  Blender type: [Sample Nearest Surface](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearestSurface.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SampleNearestSurface(mesh=None, value=None, sample_position=None, data_type='FLOAT', label=None, node_color=None)
```



## Arguments


### Input sockets

- mesh : Mesh
- value : data_type dependant
- sample_position : Vector

### Parameters

- data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Data type dependant sockets

- Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : ['value']
- Output sockets : ['value']   
  
  

## Output sockets

- value : data_type dependant
