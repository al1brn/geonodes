
# Node ObjectInfo

> Geometry node name: [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/object_info.html)<br>
  Blender type: [Object Info](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.ObjectInfo(object=None, as_instance=None, transform_space='ORIGINAL', label=None)
```



## Arguments


### Input sockets

object : Object
- as_instance : Boolean

### Parameters

transform_space : str (default = 'ORIGINAL') in ('ORIGINAL', 'RELATIVE')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

location : Vector
- rotation : Vector
- scale : Vector
- geometry : Geometry

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Object) [geometry](section:Data socket Object/geometry) : Property
- [class_name](section:Data socket Object) [info](section:Data socket Object/info) : Property
- [class_name](section:Data socket Object) [location](section:Data socket Object/location) : Property
- [class_name](section:Data socket Object) [rotation](section:Data socket Object/rotation) : Property
- [class_name](section:Data socket Object) [scale](section:Data socket Object/scale) : Property
  
