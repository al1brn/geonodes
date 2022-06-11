
# Node SetID

> Geometry node name: [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_id.html)<br>
  Blender type: [Set ID](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SetID(geometry=None, selection=None, ID=None, label=None)
```



## Arguments


### Input sockets

geometry : Geometry
- selection : Boolean
- ID : Integer

### Node label

- label : Geometry node display label (default=None)

## Output sockets

geometry : Geometry

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Geometry) [set_ID](section:Data socket Geometry/set_ID) : Method

