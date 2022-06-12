
# Node UvSphere

> Geometry node name: [UV Sphere](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/uv_sphere.html)<br>
  Blender type: [UV Sphere](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshUVSphere.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------
        
        ```python
        from geonodes import nodes
        node = nodes.UvSphere(segments=None, rings=None, radius=None, label=None)
        ```



## Arguments


### Input sockets

- segments : Integer
- rings : Integer
- radius : Float

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- mesh : Mesh

## Data sockets

> Data socket classes implementing this node.
  
  
- [Mesh](/docs/sockets/Mesh.md).[UVSphere](/docs/sockets/Mesh.md#uvsphere) : Constructor
  
