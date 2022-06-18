
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
  
  

## material_selection

> Field [MaterialSelection](/docs/nodes/MaterialSelection.md)
  
Blender menu : **material/material_selection**<br>
<sub>go to [top](#class-face) [index](/docs/index.md)</sub>

  Method

### Arguments

- material : Material or str (material name)

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



