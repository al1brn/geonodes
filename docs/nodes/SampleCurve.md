
# Node SampleCurve

> Geometry node name: [Sample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample_curve.html)<br>
  Blender type: [Sample Curve](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleCurve.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SampleCurve(curves=None, value=None, factor=None, length=None, curve_index=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False, label=None, node_color=None)
```



## Arguments


### Input sockets

- curves : Curve
- value : data_type dependant
- factor : Float
- length : Float
- curve_index : Integer

### Parameters

- data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- mode : str (default = 'FACTOR') in ('FACTOR', 'LENGTH')
- use_all_curves : bool (default = False)

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Data type dependant sockets

- Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : ['value']
- Output sockets : ['value']   
  
  

## Output sockets

- value : data_type dependant
- position : Vector
- tangent : Vector
- normal : Vector
