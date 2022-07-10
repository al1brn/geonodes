
# Class Face

Face domain


## transfer_attribute_interpolated

<method GeometryNodeAttributeTransfer>

for other mapping, use transfer_attribute



## transfer_boolean_interpolated

<method GeometryNodeAttributeTransfer>

for other mapping, use transfer_attribute



## transfer_integer_interpolated

<method GeometryNodeAttributeTransfer>

for other mapping, use transfer_attribute



## transfer_float_interpolated

<method GeometryNodeAttributeTransfer>

for other mapping, use transfer_attribute



## transfer_vector_interpolated

<method GeometryNodeAttributeTransfer>

for other mapping, use transfer_attribute



## transfer_color_interpolated

<method GeometryNodeAttributeTransfer>

for other mapping, use transfer_attribute



## neighbors

Neighbors node

Returns:
  Node FaceNeighbors
  
- getter: :class:`~geonodes.nodes.nodes.FaceNeighbors`
- setter: read only
  
  

## neighbors_vertices

Neighbors vertices attribute

Returns:
  Integer: the output socket *vertices* of the *FaceNeighbors* node.
  
- getter: :class:`~geonodes.nodes.nodes.FaceNeighbors`
- setter: read only
  
  
  

## neighbors_faces

Neighbors faces attribute

Returns:
  Integer: The output socket *faces* of the *FaceNeighbors* node.
  
- getter: :class:`~geonodes.nodes.nodes.FaceNeighbors`
- setter: read only
  
  
  

## area

Area attribute

Returns:
  Float
  
- getter: :class:`~geonodes.nodes.nodes.FaceArea`
- setter: read only
  
  
  
  

## is_planar

Attribute is_planar

Args:
  threshold: Float
  
Returns:
  Boolean
  
- getter: :class:`~geonodes.nodes.nodes.FaceIsPlanar`
- setter: read only
  
  
  

## set_material

Material attribute

Args:
  material (str or bpy.types.Material): The material to set
  
- setter: :class:`~geonodes.nodes.nodes.SetMaterial`
  
  
  

## material_selection

Material selection attribule

Args:
  material (str or bpy.types.Material): The material to select
  
Returns:
  Boolean
  
- getter: :class:`~geonodes.nodes.nodes.MaterialSelection`
  
  
  

## flip

Flip faces.

Node :class:`~geonodes.nodes.nodes.FlipFaces`

Returns:
  self
  
.. code-block:: python

  mesh.faces.flip()
  
  

## triangulate

Triangulate faces.

Node :class:`~geonodes.nodes.nodes.Triangulate`

Args:
  minimum_vertices : Integer
  ngon_method (str): (default = 'BEAUTY') in ('BEAUTY', 'CLIP')
  quad_method (str): (default = 'SHORTEST_DIAGONAL') in ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL')
  
Returns:
  self
  
.. code-block:: python

  mesh.faces(...).triangulate(...)
  
  

## distribute_points

Distribute points on faces.

Node :class:`~geonodes.nodes.nodes.DistributePointsOnFaces`

Args:
  distance_min : Float
  density_max : Float
  density : Float
  density_factor : Float
  seed : Integer
  distribute_method (str): (default = 'RANDOM') in ('RANDOM', 'POISSON')
  
Returns:
  Node with 3 sockets:
  
  - points : Points
  - normal : Vector
  - rotation : Vector
    
.. code-block:: python

  node = mesh.faces.distribute_points(...)
  cloud = node.points
  normal = node.normal
  rotation = node.rotation
  
  
  