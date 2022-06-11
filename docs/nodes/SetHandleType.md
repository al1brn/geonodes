
# Node SetHandleType

> Geometry node name: [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_handle_type.html)<br>
  Blender type: [Set Handle Type](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SetHandleType(curve=None, selection=None, handle_type='AUTO', mode={'LEFT', 'RIGHT'}, label=None)
```



## Arguments


### Input sockets

curve : Curve
- selection : Boolean

### Parameters

handle_type : str (default = 'AUTO') in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
- mode : set (default = {'LEFT', 'RIGHT'})

### Node label

- label : Geometry node display label (default=None)

## Output sockets

curve : Curve

## Data sockets

> Data socket classes implementing this node.
  
[Curve](/docs/sockets/Curve.md).[set_handles](/docs/sockets/Curve.md#set_handles) : Method

