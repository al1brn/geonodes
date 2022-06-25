
# Class Edge

Edge domain


## neighbors_faces

> Field [EdgeNeighbors](/docs/nodes/EdgeNeighbors.md)
  
Blender menu : **mesh/edge_neighbors**<br>
<sub>go to [top](#class-edge) [index](/docs/index.md)</sub>

  Property

### Returns

Integer




## unsigned_angle

> Field [EdgeAngle](/docs/nodes/EdgeAngle.md)
  
Blender menu : **mesh/edge_angle**<br>
<sub>go to [top](#class-edge) [index](/docs/index.md)</sub>

  Property
  
  To get the signed angle, used the property [angle](#angle).

### Returns

Float



## angle

> Field [EdgeAngle](/docs/nodes/EdgeAngle.md)
  
Blender menu : **mesh/edge_angle**<br>
<sub>go to [top](#class-edge) [index](/docs/index.md)</sub>

  Property
  
  To get the unsigned angle, used the property [unsigned_angle](#unsigned_angle).

### Returns

Float



## vertices_index_1

> Field [EdgeVertices](/docs/nodes/EdgeVertices.md)
  
Blender menu : **mesh/edge_vertices**<br>
<sub>go to [top](#class-edge) [index](/docs/index.md)</sub>

  Property
  
  Sockets can be access individually via:
  
  - [vertices_index_1](#vertices_index_1)
  - [vertices_index_2](#vertices_index_2)
  - [vertices_position_1](#vertices_position_1)
  - [vertices_position_2](#vertices_position_2)

### Returns

Integer



## vertices_index_2

> Field [EdgeVertices](/docs/nodes/EdgeVertices.md)
  
Blender menu : **mesh/edge_vertices**<br>
<sub>go to [top](#class-edge) [index](/docs/index.md)</sub>

  Property
  
  Sockets can be access individually via:
  
  - [vertices_index_1](#vertices_index_1)
  - [vertices_index_2](#vertices_index_2)
  - [vertices_position_1](#vertices_position_1)
  - [vertices_position_2](#vertices_position_2)

### Returns

Integer



## vertices_position_1

> Field [EdgeVertices](/docs/nodes/EdgeVertices.md)
  
Blender menu : **mesh/edge_vertices**<br>
<sub>go to [top](#class-edge) [index](/docs/index.md)</sub>

  Property
  
  Sockets can be access individually via:
  
  - [vertices_index_1](#vertices_index_1)
  - [vertices_index_2](#vertices_index_2)
  - [vertices_position_1](#vertices_position_1)
  - [vertices_position_2](#vertices_position_2)

### Returns

Integer



## vertices_position_2

> Field [EdgeVertices](/docs/nodes/EdgeVertices.md)
  
Blender menu : **mesh/edge_vertices**<br>
<sub>go to [top](#class-edge) [index](/docs/index.md)</sub>

  Property
  
  Sockets can be access individually via:
  
  - [vertices_index_1](#vertices_index_1)
  - [vertices_index_2](#vertices_index_2)
  - [vertices_position_1](#vertices_position_1)
  - [vertices_position_2](#vertices_position_2)

### Returns

Integer



## to_curve

> Convert edges to curve
  
<blid GeometryNodeMeshToCurve>

### Example

```python
mesh.edges.to_curve(...)
```




## split

> Split edges
  
<blid GeometryNodeSplitEdges>

### Example

```python
mesh.edges.split()
```


