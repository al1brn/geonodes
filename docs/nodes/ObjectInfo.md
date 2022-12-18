
# Node ObjectInfo

> Geometry node name: [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html)<br>
  Blender type: [Object Info](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.ObjectInfo(object=None, as_instance=None, transform_space='ORIGINAL', label=None, node_color=None)
```



## Arguments


### Input sockets

- object : Object
- as_instance : Boolean

### Parameters

- transform_space : str (default = 'ORIGINAL') in ('ORIGINAL', 'RELATIVE')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- location : Vector
- rotation : Vector
- scale : Vector
- geometry : Geometry
