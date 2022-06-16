
# Class FaceDomain

> Field domain FACE
  
Inherits from [Domain](/docs/core/domain.MD)

A property of Mesh


## area

> Field [FaceArea](/docs/nodes/FaceArea.md)
  
Blender menu : **mesh/face_area**<br>
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Property

### Returns

Float



## neighbors

> Field [FaceNeighbors](/docs/nodes/FaceNeighbors.md)
  
Blender menu : **mesh/face_neighbors**<br>
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
  
Blender menu : **mesh/face_neighbors**<br>
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Property
  
  Return the socket **vertex_count** of property [neighbors](#neighbors)

### Returns

Integer



## neighbors_faces

> Field [FaceNeighbors](/docs/nodes/FaceNeighbors.md)
  
Blender menu : **mesh/face_neighbors**<br>
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Property
  
  Return the socket **face_count** of property [neighbors](#neighbors)

### Returns

Integer



## is_shade_smooth

> Field [IsShadeSmooth](/docs/nodes/IsShadeSmooth.md)
  
Blender menu : **mesh/is_shade_smooth**<br>
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Property

### Returns

Float



## island

> Field [MeshIsland](/docs/nodes/MeshIsland.md)
  
Blender menu : **mesh/mesh_island**<br>
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
  
Blender menu : **mesh/mesh_island**<br>
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Property
  
  Return the socket **vertex_count** of property [island](#island)

### Returns

Integer



## island_faces

> Field [MeshIsland](/docs/nodes/MeshIsland.md)
  
Blender menu : **mesh/mesh_island**<br>
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Property
  
  Return the socket **face_count** of property [island](#island)

### Returns

Integer



## material_index

> Field [MaterialIndex](/docs/nodes/MaterialIndex.md)
  
Blender menu : **material/material_index**<br>
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Property

### Returns

Integer



## material_selection

> Field [MaterialSelection](/docs/nodes/MaterialSelection.md)
  
Blender menu : **material/material_selection**<br>
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Method

### Arguments

- material : Material

### Returns

Boolean



## face_is_planar

> Field [FaceIsPlanar](/docs/nodes/FaceIsPlanar.md)
  
Blender menu : **mesh/face_is_planar**<br>
<sub>go to [top](#class-facedomain) [index](/docs/index.md)</sub>

  Method

### Arguments

- threshold : Float

### Returns

Boolean



## distribute_points

<method GeometryNodeDistributePointsOnFaces>

### Call

```python
node = mesh.face.distribute_points(selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM', label=None, node_color=None)
```

### Arguments


### Input sockets

- mesh : Mesh
- selection : Boolean
- distance_min : Float
- density_max : Float
- density : Float
- density_factor : Float
- seed : Integer

### Parameters

- distribute_method : str (default = 'RANDOM') in ('RANDOM', 'POISSON')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

### Returns

Node with 3 sockets:
- points : Points
- normal : Vector
- rotation : Vector
  
  
  

## extrude

<method GeometryNodeExtrudeMesh>

call [Mesh.extrude](/docs/sockets/Mesh.md#extrude) with mode = 'FACES'
                            
```python
node = mesh.faces.extrude()
```



