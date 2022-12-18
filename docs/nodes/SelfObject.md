
# Node SelfObject

> Geometry node name: [Self Object](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/self_object.html)<br>
  Blender type: [Self Object](https://docs.blender.org/api/current/bpy.types.GeometryNodeSelfObject.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SelfObject(label=None, node_color=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- self_object : Object
