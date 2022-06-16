
# Node HandleTypeSelection

> Geometry node name: [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html)<br>
  Blender type: [Handle Type Selection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.HandleTypeSelection(handle_type='AUTO', mode={'LEFT', 'RIGHT'}, label=None, node_color=None)
```



## Arguments


### Parameters

- handle_type : str (default = 'AUTO') in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
- mode : set (default = {'LEFT', 'RIGHT'})

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- selection : Boolean

## Data sockets

> Data socket classes implementing this node.
  
  
- [CurveDomain](/docs/CurveDomain.md).[handle_type_selection](/docs/CurveDomain.md#handle_type_selection) : Fields
- [CurveDomain](/docs/CurveDomain.md).[left_handle_align](/docs/CurveDomain.md#left_handle_align) : Fields
- [CurveDomain](/docs/CurveDomain.md).[left_handle_auto](/docs/CurveDomain.md#left_handle_auto) : Fields
- [CurveDomain](/docs/CurveDomain.md).[left_handle_free](/docs/CurveDomain.md#left_handle_free) : Fields
- [CurveDomain](/docs/CurveDomain.md).[left_handle_selection](/docs/CurveDomain.md#left_handle_selection) : Fields
- [CurveDomain](/docs/CurveDomain.md).[left_handle_vector](/docs/CurveDomain.md#left_handle_vector) : Fields
- [CurveDomain](/docs/CurveDomain.md).[right_handle_align](/docs/CurveDomain.md#right_handle_align) : Fields
- [CurveDomain](/docs/CurveDomain.md).[right_handle_auto](/docs/CurveDomain.md#right_handle_auto) : Fields
- [CurveDomain](/docs/CurveDomain.md).[right_handle_free](/docs/CurveDomain.md#right_handle_free) : Fields
- [CurveDomain](/docs/CurveDomain.md).[right_handle_selection](/docs/CurveDomain.md#right_handle_selection) : Fields
- [CurveDomain](/docs/CurveDomain.md).[right_handle_vector](/docs/CurveDomain.md#right_handle_vector) : Fields
  
