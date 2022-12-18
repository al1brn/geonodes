
# Node SetSplineCyclic

> Geometry node name: [Set Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_cyclic.html)<br>
  Blender type: [Set Spline Cyclic](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SetSplineCyclic(geometry=None, selection=None, cyclic=None, label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : Geometry
- selection : Boolean
- cyclic : Boolean

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- geometry : Geometry
