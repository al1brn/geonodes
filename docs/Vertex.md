
# Class Vertex

vertex: the point domain of meshes


## neighbors

Neighbors node

Returns:
  Node *VertexNeighbors*
  
- getter: :class:`nodes.VertexNeighbors`
- setter: read only
  
  

## neighbors_vertices

Neighbors vertices attribute

Returns:
  Integer: The output socket *vertices* of the *VertexNeighbors* node.
  
- getter: :class:`nodes.VertexNeighbors`
- setter: read only
  
  
  

## neighbors_faces

Neighbors faces attribute

Returns:
  Integer: The output socket *faces* of the *VertexNeighbors* node.
  
- getter: :class:`nodes.VertexNeighbors`
- setter: read only
  
  
  

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

