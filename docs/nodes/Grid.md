
# Node Grid

> Geometry node name: [Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/grid.html)<br>
  Blender type: [Grid](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshGrid.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
        from geonodes import nodes
        node = nodes.Grid(size_x=None, size_y=None, vertices_x=None, vertices_y=None, label=None)
        ```



## Arguments


### Input sockets

- size_x : Float
- size_y : Float
- vertices_x : Integer
- vertices_y : Integer

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- mesh : Mesh

## Data sockets

> Data socket classes implementing this node.
  
  
- [Mesh](/docs/sockets/Mesh.md).[Grid](/docs/sockets/Mesh.md#grid) : Constructor
  
