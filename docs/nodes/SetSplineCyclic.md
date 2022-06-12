
# Node SetSplineCyclic

> Geometry node name: [Set Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_cyclic.html)<br>
  Blender type: [Set Spline Cyclic](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------
```python
from geonodes import nodes
node = nodes.SetSplineCyclic(geometry=None, selection=None, cyclic=None, label=None)
```



## Arguments


### Input sockets

- geometry : Geometry
- selection : Boolean
- cyclic : Boolean

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- geometry : Geometry

## Data sockets

> Data socket classes implementing this node.
  
  
- [Spline](/docs/sockets/Spline.md).[set_cyclic](/docs/sockets/Spline.md#set_cyclic) : Method
  
