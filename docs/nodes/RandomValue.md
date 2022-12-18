
# Node RandomValue

> Geometry node name: [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)<br>
  Blender type: [Random Value](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.RandomValue(min=None, max=None, probability=None, ID=None, seed=None, data_type='FLOAT', label=None, node_color=None)
```



## Arguments


### Input sockets

- min : data_type dependant
- max : data_type dependant
- probability : Float
- ID : Integer
- seed : Integer

### Parameters

- data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Data type dependant sockets

- Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')
- Input sockets  : ['min', 'max']
- Output sockets : ['value']   
  
  

## Output sockets

- value : data_type dependant
