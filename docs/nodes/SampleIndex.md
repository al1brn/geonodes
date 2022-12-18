
# Node SampleIndex

> Geometry node name: [Sample Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html)<br>
  Blender type: [Sample Index](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SampleIndex(geometry=None, value=None, index=None, clamp=False, data_type='FLOAT', domain='POINT', label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : Geometry
- value : data_type dependant
- index : Integer

### Parameters

- clamp : bool (default = False)
- data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Data type dependant sockets

- Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : ['value']
- Output sockets : ['value']   
  
  

## Output sockets

- value : data_type dependant
