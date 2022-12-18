
# Node SampleUvSurface

> Geometry node name: [Sample UV Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample_uv_surface.html)<br>
  Blender type: [Sample UV Surface](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleUVSurface.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SampleUvSurface(mesh=None, value=None, source_uv_map=None, sample_uv=None, data_type='FLOAT', label=None, node_color=None)
```



## Arguments


### Input sockets

- mesh : Mesh
- value : data_type dependant
- source_uv_map : Vector
- sample_uv : Vector

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
- is_valid : Boolean
