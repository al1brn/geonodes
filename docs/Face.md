
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



## neighbors_vertices

Fields


## area

> Field [FaceArea](/docs/nodes/FaceArea.md)
  
Blender menu : **mesh/face_area**<br>
<sub>go to [top](#class-face) [index](/docs/index.md)</sub>

  Property

### Returns

Float



## is_planar

> Field [FaceIsPlanar](/docs/nodes/FaceIsPlanar.md)
  
Blender menu : **mesh/face_is_planar**<br>
<sub>go to [top](#class-face) [index](/docs/index.md)</sub>

  Method

### Arguments

- threshold : Float

### Returns

Boolean




## material_index

> Field [SetMaterialIndex](/docs/nodes/SetMaterialIndex.md)
  
Blender menu : **material/set_material_index**<br>
<sub>go to [top](#class-face) [index](/docs/index.md)</sub>

  Property setter
  
  

## set_material

> Set a material on the faces
  
<blid GeometryNodeSetMaterial>

### Arguments

- material : material of material name

### Example

```python
mesh.faces.set_material(...)
```



## material_selection

> Field [MaterialSelection](/docs/nodes/MaterialSelection.md)
  
Blender menu : **material/material_selection**<br>
<sub>go to [top](#class-face) [index](/docs/index.md)</sub>

  Method

### Arguments

- material : Material or str (material name)

### Returns

Boolean



## flip

> Flip faces
  
<blid GeometryNodeFlipFaces>

### Example

```python
mesh.faces.flip()
```




## triangulate

> Triangulate faces
  
<blid GeometryNodeTriangulate>

### Arguments

- minimum_vertices : Integer
- ngon_method : str (default = 'BEAUTY') in ('BEAUTY', 'CLIP')
- quad_method : str (default = 'SHORTEST_DIAGONAL') in ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL')

### Example

```python
mesh.faces(...).triangulate(...)
```



## distribute_points

> Distribute points on faces
  
<blid GeometryNodeDistributePointsOnFaces>

### Arguments

- distance_min : Float
- density_max : Float
- density : Float
- density_factor : Float
- seed : Integer
- distribute_method : str (default = 'RANDOM') in ('RANDOM', 'POISSON')

### Returns

Node with 3 sockets:
- points : Points
- normal : Vector
- rotation : Vector

### Example

```python
node = mesh.faces.distribute_points(...)
cloud = node.points
normal = node.normal
rotation = node.rotation
        
```



