
# Class FaceDomain

> Field domain FACE
  
Inherits from [Domain](/docs/core/domain.MD)

A property of Mesh


## area

> Field [FaceArea](/docs/nodes/FaceArea.md)
  
Blender menu : **mesh/face_area**
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Property

### Returns

Float



## neighbors

> Field [FaceNeighbors](/docs/nodes/FaceNeighbors.md)
  
Blender menu : **mesh/face_neighbors**
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Property
  
  Individual sockets can be accessed via properties:
  
  - [neighbors_vertices](#neighbors_vertices)
  - [neighbors_faces](#neighbors_faces)

### Returns

Node with two sockets:
- vertex_count
- face_count
  
  

## neighbors_vertices

> Field [FaceNeighbors](/docs/nodes/FaceNeighbors.md)
  
Blender menu : **mesh/face_neighbors**
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Property
  
  Return the socket **vertex_count** of property [neighbors](#neighbors)

### Returns

Integer



## neighbors_faces

> Field [FaceNeighbors](/docs/nodes/FaceNeighbors.md)
  
Blender menu : **mesh/face_neighbors**
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Property
  
  Return the socket **face_count** of property [neighbors](#neighbors)

### Returns

Integer



## is_shade_smooth

> Field [IsShadeSmooth](/docs/nodes/IsShadeSmooth.md)
  
Blender menu : **mesh/is_shade_smooth**
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Property

### Returns

Float



## island

> Field [MeshIsland](/docs/nodes/MeshIsland.md)
  
Blender menu : **mesh/mesh_island**
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Property
  
  Individual sockets can be accessed via properties:
  
  - [neighbors_vertices](#neighbors_vertices)
  - [neighbors_faces](#neighbors_faces)

### Returns

Node with two sockets:
- vertex_count
- face_count
  
  

## island_vertices

> Field [MeshIsland](/docs/nodes/MeshIsland.md)
  
Blender menu : **mesh/mesh_island**
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Property
  
  Return the socket **vertex_count** of property [island](#island)

### Returns

Integer



## island_faces

> Field [MeshIsland](/docs/nodes/MeshIsland.md)
  
Blender menu : **mesh/mesh_island**
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Property
  
  Return the socket **face_count** of property [island](#island)

### Returns

Integer



## material_index

> Field [MaterialIndex](/docs/nodes/MaterialIndex.md)
  
Blender menu : **material/material_index**
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Property

### Returns

Integer



## material_selection

> Field [MaterialSelection](/docs/nodes/MaterialSelection.md)
  
Blender menu : **material/material_selection**
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Method

### Arguments

- material : Material

### Returns

Boolean



## face_is_planar

> Field [FaceIsPlanar](/docs/nodes/FaceIsPlanar.md)
  
Blender menu : **mesh/face_is_planar**
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Method

### Arguments

- threshold : Float

### Returns

Boolean

