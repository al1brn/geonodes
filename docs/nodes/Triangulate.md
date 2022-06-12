
# Node Triangulate

> Geometry node name: [Triangulate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/triangulate.html)<br>
  Blender type: [Triangulate](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------
        
        ```python
        from geonodes import nodes
        node = nodes.Triangulate(mesh=None, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL', label=None)
        ```



## Arguments


### Input sockets

- mesh : Mesh
- selection : Boolean
- minimum_vertices : Integer

### Parameters

- ngon_method : str (default = 'BEAUTY') in ('BEAUTY', 'CLIP')
- quad_method : str (default = 'SHORTEST_DIAGONAL') in ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- mesh : Mesh

## Data sockets

> Data socket classes implementing this node.
  
  
- [Mesh](/docs/sockets/Mesh.md).[triangulate](/docs/sockets/Mesh.md#triangulate) : Method
  
