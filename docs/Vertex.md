
# Class Vertex

vertex: the point domain of meshes


## neighbors_vertices

> Neighbors vertices
<blid GeometryNodeInputMeshVertexNeighbors>



## neighbors_faces

> Neighbors faces
<blid GeometryNodeInputMeshVertexNeighbors>



## merge

> Merge vertices by distance
  
<blid GeometryNodeMergeByDistance>

### Arguments

- mode : str (default = 'ALL') in ('ALL', 'CONNECTED')        
- distance : Float
The merge distance

### Example

'''python
mesh.verts().merge()
````



## merge_connected

> Merge connected vertices by distance
  
<blid GeometryNodeMergeByDistance>

### Arguments

- distance : Float
The merge distance

### Example

'''python
mesh.verts().merge_connected()
````

