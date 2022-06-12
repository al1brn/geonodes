
# Node VectorCurves

> Geometry node name: [Vector Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_curves.html)<br>
  Blender type: [Vector Curves](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorCurve.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------```python
from geonodes import nodes
node = nodes.VectorCurves(fac=None, vector=None, label=None)
```



## Arguments


### Input sockets

- fac : Float
- vector : Vector

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- vector : Vector

## Data sockets

> Data socket classes implementing this node.
  
  
- [Vector](/docs/sockets/Vector.md).[curves](/docs/sockets/Vector.md#curves) : Method
  
