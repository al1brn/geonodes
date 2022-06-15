
# Class PointDomain

> Field domain POINT
  
Inherits from [Domain](/docs/core/domain.MD)

A property of Mesh, Curve, Points


## neighbors

> Field [VertexNeighbors](/docs/nodes/VertexNeighbors.md)
  
Blender menu : **mesh/vertex_neighbors**
<sub>go to [top](#pointdomain) [index](/docs/index.md)</sub>

  Property
  
  Individual sockets can be accessed via properties:
  
  - [neighbors_vertices](#neighbors_vertices)
  - [neighbors_faces](#neighbors_faces)

### Returns

Node with two sockets:
- vertex_count
- face_count
  
  

## neighbors_vertices

> Field [VertexNeighbors](/docs/nodes/VertexNeighbors.md)
  
Blender menu : **mesh/vertex_neighbors**
<sub>go to [top](#pointdomain) [index](/docs/index.md)</sub>

  Property
  
  Return the socket **vertex_count** of property [neighbors](#neighbors)

### Returns

Integer



## neighbors_faces

> Field [VertexNeighbors](/docs/nodes/VertexNeighbors.md)
  
Blender menu : **mesh/vertex_neighbors**
<sub>go to [top](#pointdomain) [index](/docs/index.md)</sub>

  Property
  
  Return the socket **face_count** of property [neighbors](#neighbors)

### Returns

Integer

