
# Node AttributeRemove

> Geometry node name: [Attribute Remove](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/attribute_remove.html)<br>
  Blender type: [Attribute Remove](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeRemove.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.AttributeRemove(*attribute, geometry=None, label=None)
```



## Arguments


### Input sockets

geometry : Geometry
- attribute : *String

### Node label

- label : Geometry node display label (default=None)

## Output sockets

geometry : Geometry

## Data sockets

> Data socket classes implementing this node.
  
[class_name](docs/sockets/Geometry.md) [attribute_remove](docs/sockets/Geometry.md#attribute_remove) : Method

