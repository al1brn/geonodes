
# Node RandomValue

> Geometry node name: [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/random_value.html)<br>
  Blender type: [Random Value](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.RandomValue(min=None, max=None, probability=None, ID=None, seed=None, data_type='FLOAT', label=None)
```



## Arguments


### Input sockets

min : data_type dependant
- max : data_type dependant
- probability : Float
- ID : Integer
- seed : Integer

### Parameters

data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')

### Node label

- label : Geometry node display label (default=None)

## Data type dependant sockets

- Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')
- Input sockets  : ['min', 'max']
- Output sockets : ['value']   
  
  

## Output sockets

value : data_type dependant

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Boolean) [Random](section:Data socket Boolean/Random) : Constructor
- [class_name](section:Data socket Float) [Random](section:Data socket Float/Random) : Constructor
- [class_name](section:Data socket Integer) [Random](section:Data socket Integer/Random) : Constructor
- [class_name](section:Data socket Vector) [Random](section:Data socket Vector/Random) : Constructor
  
