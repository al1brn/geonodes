
# Node HandleTypeSelection

> Geometry node name: [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/handle_type_selection.html)<br>
  Blender type: [Handle Type Selection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.HandleTypeSelection(handle_type='AUTO', mode={'LEFT', 'RIGHT'}, label=None)
```



## Arguments


### Parameters

handle_type : str (default = 'AUTO') in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
- mode : set (default = {'LEFT', 'RIGHT'})

### Node label

- label : Geometry node display label (default=None)

## Output sockets

selection : Boolean

## Data sockets

> Data socket classes implementing this node.
  
[class_name](/docs/sockets/Spline.md) [capture_handle_type_selection](/docs/sockets/Spline.md#capture_handle_type_selection) : Capture attribute
- [class_name](/docs/sockets/Spline.md) [handle_type_selection](/docs/sockets/Spline.md#handle_type_selection) : Attribute
  
