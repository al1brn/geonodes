
# Node MeshToPoints

> Geometry node name: [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_points.html)<br>
  Blender type: [Mesh to Points](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------

```python
from geonodes import nodes
node = nodes.MeshToPoints(mesh=None, selection=None, position=None, radius=None, mode='VERTICES', label=None)
```



## Arguments


### Input sockets

- mesh : Mesh
- selection : Boolean
- position : Vector
- radius : Float

### Parameters

- mode : str (default = 'VERTICES') in ('VERTICES', 'EDGES', 'FACES', 'CORNERS')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- points : Points

## Data sockets

> Data socket classes implementing this node.
  
  
- [Mesh](/docs/sockets/Mesh.md).[to_points](/docs/sockets/Mesh.md#to_points) : Method
  
