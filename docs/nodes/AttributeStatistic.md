
# Node AttributeStatistic

> Geometry node name: [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)<br>
  Blender type: [Attribute Statistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.AttributeStatistic(geometry=None, selection=None, attribute=None, data_type='FLOAT', domain='POINT', label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : Geometry
- selection : Boolean
- attribute : data_type dependant

### Parameters

- data_type : str (default = 'FLOAT') in ('FLOAT', 'FLOAT_VECTOR')
- domain : str (default = 'POINT') in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Data type dependant sockets

- Driving parameter : data_type in ('FLOAT', 'FLOAT_VECTOR')
- Input sockets  : ['attribute']
- Output sockets : ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']   
  
  

## Output sockets

- mean : data_type dependant
- median : data_type dependant
- sum : data_type dependant
- min : data_type dependant
- max : data_type dependant
- range : data_type dependant
- standard_deviation : data_type dependant
- variance : data_type dependant
