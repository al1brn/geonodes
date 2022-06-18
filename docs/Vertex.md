
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

'''python
mesh.verts.select().merge()
````

### Arguments

- mode : str (default = 'ALL') in ('ALL', 'CONNECTED')        
- distance : Float
The merge distance



## merge_connected

> Merge connected vertices by distance
  
<blid GeometryNodeMergeByDistance>

'''python
mesh.verts.select().merge_connected()
````

### Arguments

- distance : Float
The merge distance

