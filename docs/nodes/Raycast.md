
# Node Raycast

> Geometry node name: [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/raycast.html)<br>
  Blender type: [Raycast](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.Raycast(target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED', label=None)
```



## Arguments


### Input sockets

target_geometry : Geometry
- attribute : data_type dependant
- source_position : Vector
- ray_direction : Vector
- ray_length : Float

### Parameters

data_type : str (default = 'FLOAT') in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- mapping : str (default = 'INTERPOLATED') in ('INTERPOLATED', 'NEAREST')

### Node label

- label : Geometry node display label (default=None)

## Data type dependant sockets

- Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : ['attribute']
- Output sockets : ['attribute']   
  
  

## Output sockets

is_hit : Boolean
- hit_position : Vector
- hit_normal : Vector
- hit_distance : Float
- attribute : data_type dependant

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Boolean) [raycast](section:Data socket Boolean/raycast) : Method
- [class_name](section:Data socket Color) [raycast](section:Data socket Color/raycast) : Method
- [class_name](section:Data socket Float) [raycast](section:Data socket Float/raycast) : Method
- [class_name](section:Data socket Integer) [raycast](section:Data socket Integer/raycast) : Method
- [class_name](section:Data socket Vector) [raycast](section:Data socket Vector/raycast) : Method
  
