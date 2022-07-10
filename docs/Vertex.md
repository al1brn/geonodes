
# Class Vertex

vertex: the point domain of meshes


## neighbors

Neighbors

Returns:
  Node *VertexNeighbors*
  
- getter: :class:`~geonodes.nodes.nodes.VertexNeighbors`
- setter: read only
  
  

## neighbors_vertices

Neighbors vertices attribute

Returns:
  Integer: The output socket *vertices* of the *VertexNeighbors* node.
  
- getter: :class:`~geonodes.nodes.nodes.VertexNeighbors`
- setter: read only
  
  
  

## neighbors_faces

Neighbors faces attribute

Returns:
  Integer: The output socket *faces* of the *VertexNeighbors* node.
  
- getter: :class:`~geonodes.nodes.nodes.VertexNeighbors`
- setter: read only
  
  
  

## merge

Merge vertices by distance.

Node :class:`~geonodes.nodes.nodes.MergeByDistance`

Args:
  distance (Float): The merge distance
  mode (str): str (default = 'ALL') in ('ALL', 'CONNECTED')        
  
Returns:
  self
  
.. code-block:: python

  mesh.verts().merge()
  
  

## merge_connected

Merge connected vertices by distance.

call :func:`merge` with mode = 'CONNECTED'

Args:
  distance (Float): The merge distance
  
Returns:
  self
  
.. code-block:: python

  mesh.verts().merge_connected()
  
  