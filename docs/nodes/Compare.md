
# Node Compare

> Geometry node name: [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)<br>
  Blender type: [Compare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Compare(a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', label=None, node_color=None)
```



## Arguments


### Input sockets

- a : data_type dependant
- b : data_type dependant
- c : Float
- angle : Float
- epsilon : Float

### Parameters

- data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
- mode : str (default = 'ELEMENT') in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
- operation : str (default = 'GREATER_THAN') in ('LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Data type dependant sockets

- Driving parameter : data_type in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
- Input sockets  : ['a', 'b']
- Output sockets : []   
  
  

## Output sockets

- result : Boolean
