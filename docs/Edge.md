
# Class Edge

Edge domain


## neighbors_faces

Neighbors (faces count)

Returns:
  Integer
  
- getter: :class:`nodes.EdgeNeighbors`
- setter: read only
  
  

## edge_angle

Edge angle node

Returns:
  Node *EdgeAngle*
  
- getter: :class:`nodes.EdgeAngle`
- setter: read only
  
  

## unsigned_angle

Unsigned angle

Returns:
  Float: Unsigned output socket of *EdgeAngle*
  
- getter: :class:`nodes.EdgeAngle`
- setter: read only
  
  
  

## angle

Signed angle

Returns:
  Float: Signed output socket of *EdgeAngle*
  
- getter: :class:`nodes.EdgeAngle`
- setter: read only
  
  
  

## vertices

EdgeVertices node

Returns:
  Node *EdgeVertices*
  
Output sockets:
- vertex_index_1 : Integer
- vertex_index_2 : Integer
- position_1 : Vector
- position_2 : Vector
  
- getter: :class:`nodes.EdgeVertices`
- setter: read only
  
  
  

## vertex_index

The indices of the vertices composing the edge

Returns:
  (Integer, Integer)
  
- getter: :class:`nodes.EdgeVertices`
- setter: read only
  
  
  

## vertex_position

The position of the vertices composing the edge

Returns:
  (Float, Float)
  
- getter: :class:`nodes.EdgeVertices`
- setter: read only
  
  
  

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


