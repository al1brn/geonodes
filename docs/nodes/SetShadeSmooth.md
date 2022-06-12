
# Node SetShadeSmooth

> Geometry node name: [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html)<br>
  Blender type: [Set Shade Smooth](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------
```python
from geonodes import nodes
node = nodes.SetShadeSmooth(geometry=None, selection=None, shade_smooth=None, label=None)
```



## Arguments


### Input sockets

- geometry : Geometry
- selection : Boolean
- shade_smooth : Boolean

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- geometry : Geometry

## Data sockets

> Data socket classes implementing this node.
  
  
- [Geometry](/docs/sockets/Geometry.md).[set_shade_smooth](/docs/sockets/Geometry.md#set_shade_smooth) : Method
  
