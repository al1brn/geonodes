
# Node RemoveNamedAttribute

> Geometry node name: [Remove Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html)<br>
  Blender type: [Remove Named Attribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.RemoveNamedAttribute(geometry=None, name=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : Geometry
- name : String

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- geometry : Geometry
