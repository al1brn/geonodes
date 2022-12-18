
# Node SetHandleType

> Geometry node name: [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_type.html)<br>
  Blender type: [Set Handle Type](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SetHandleType(curve=None, selection=None, handle_type='AUTO', mode={'RIGHT', 'LEFT'}, label=None, node_color=None)
```



## Arguments


### Input sockets

- curve : Curve
- selection : Boolean

### Parameters

- handle_type : str (default = 'AUTO') in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
- mode : set (default = {'RIGHT', 'LEFT'})

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- curve : Curve
