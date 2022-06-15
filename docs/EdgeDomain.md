
# Class EdgeDomain

> Field domain FACE
  
Inherits from [Domain](/docs/core/domain.MD)

A property of Mesh



## angle

> Field [EdgeAngle](/docs/nodes/EdgeAngle.md)
  
Blender menu : mesh/edge_angle

  Property
  
  To get the unsigned angle, used the property [unsigned_angle](#unsigned_angle).

### Returns

Float



## unsigned_angle

> Field [EdgeAngle](/docs/nodes/EdgeAngle.md)
  
Blender menu : mesh/edge_angle

  Property
  
  To get the signed angle, used the property [angle](#angle).

### Returns

Float



## neighbors

> Field [EdgeNeighbors](/docs/nodes/EdgeNeighbors.md)
  
Blender menu : mesh/edge_neighbors

  Property

### Returns

Integer



## vertices

> Field [EdgeVertices](/docs/nodes/EdgeVertices.md)
  
Blender menu : mesh/edge_vertices

  Property
  
  Sockets can be access individually via:
  
  - [vertices_index_1](#vertices_index_1)
  - [vertices_index_2](#vertices_index_2)
  - [vertices_position_1](#vertices_position_1)
  - [vertices_position_2](#vertices_position_2)

### Returns

Node with 4 output sockets:
- vertex_index_1
- vertex_index_2
- position_1
- position_2
  
  

## vertices_index_1

> Field [EdgeVertices](/docs/nodes/EdgeVertices.md)
  
Blender menu : mesh/edge_vertices

  Property

### Returns

Integer



## vertices_index_2

> Field [EdgeVertices](/docs/nodes/EdgeVertices.md)
  
Blender menu : mesh/edge_vertices

  Property

### Returns

Integer



## vertices_position_1

> Field [EdgeVertices](/docs/nodes/EdgeVertices.md)
  
Blender menu : mesh/edge_vertices

  Property

### Returns

Integer



## vertices_position_2

> Field [EdgeVertices](/docs/nodes/EdgeVertices.md)
  
Blender menu : mesh/edge_vertices

  Property

### Returns

Integer

