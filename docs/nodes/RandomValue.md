
# Node RandomValue

> Geometry node name: [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)<br>
  Blender type: [Random Value](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------

```python
from geonodes import nodes
node = nodes.RandomValue(min=None, max=None, probability=None, ID=None, seed=None, data_type='FLOAT', label=None)
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

## Data type dependant sockets

- Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')
- Input sockets  : ['min', 'max']
- Output sockets : ['value']   
  
  

## Output sockets

- value : data_type dependant

## Data sockets

> Data socket classes implementing this node.
  
  
- [Boolean](/docs/sockets/Boolean.md).[Random](/docs/sockets/Boolean.md#random) : Constructor
- [Float](/docs/sockets/Float.md).[Random](/docs/sockets/Float.md#random) : Constructor
- [Integer](/docs/sockets/Integer.md).[Random](/docs/sockets/Integer.md#random) : Constructor
- [Vector](/docs/sockets/Vector.md).[Random](/docs/sockets/Vector.md#random) : Constructor
  
