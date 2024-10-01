# Shader Cross Reference

You will find here how nodes are implemented

## Content

- **&** : [&Material Output](shader_cross_reference.md#&material-output)
- **A** : [AOV Output](shader_cross_reference.md#aov-output)
- **B** : [Blackbody](shader_cross_reference.md#blackbody) :black_small_square: [Brightness Contrast](shader_cross_reference.md#brightness-contrast) :black_small_square: [Bump](shader_cross_reference.md#bump)
- **C** : [Color Attribute](shader_cross_reference.md#color-attribute)
- **D** : [Displacement](shader_cross_reference.md#displacement)
- **G** : [Gamma](shader_cross_reference.md#gamma)
- **H** : [Hue Saturation Value](shader_cross_reference.md#hue-saturation-value)
- **I** : [Input](shader_cross_reference.md#input) :black_small_square: [Invert Color](shader_cross_reference.md#invert-color)
- **M** : [Mapping](shader_cross_reference.md#mapping) :black_small_square: [Material Output](shader_cross_reference.md#material-output)
- **N** : [Normal](shader_cross_reference.md#normal) :black_small_square: [Normal Map](shader_cross_reference.md#normal-map)
- **O** : [of curve](shader_cross_reference.md#of-curve) :black_small_square: [of Point](shader_cross_reference.md#of-point) :black_small_square: [Output](shader_cross_reference.md#output)
- **P** : [Point in Curve](shader_cross_reference.md#point-in-curve)
- **R** : [RGB to BW](shader_cross_reference.md#rgb-to-bw)
- **S** : [Shader to RGB](shader_cross_reference.md#shader-to-rgb) :black_small_square: [Size](shader_cross_reference.md#size)
- **T** : [Tangent](shader_cross_reference.md#tangent) :black_small_square: [to Euler](shader_cross_reference.md#to-euler) :black_small_square: [to Rotation](shader_cross_reference.md#to-rotation)
- **U** : [UV Map](shader_cross_reference.md#uv-map)
- **V** : [Value](shader_cross_reference.md#value) :black_small_square: [Vector Displacement](shader_cross_reference.md#vector-displacement) :black_small_square: [Vector Transform](shader_cross_reference.md#vector-transform)
- **W** : [Wavelength](shader_cross_reference.md#wavelength)
- **X** : [XYZ](shader_cross_reference.md#xyz)

#### &Material Output

- [Vector](geono-vector.md#vector) :white_small_square: [out](geono-vector.md#out)

#### AOV Output

- [Color](geono-color.md#color) :white_small_square: [out](geono-color.md#out)
- [Float](geono-float.md#float) :white_small_square: [out](geono-float.md#out)
- [Vector](geono-vector.md#vector) :white_small_square: [out](geono-vector.md#out)

#### Blackbody

- [Color](geono-color.md#color) :white_small_square: [Blackbody](geono-color.md#blackbody)

#### Brightness Contrast

- [Color](geono-color.md#color) :white_small_square: [brightness_contrast](geono-color.md#brightness_contrast)

#### Bump

- [Vector](geono-vector.md#vector) :white_small_square: [bump](geono-vector.md#bump)

#### Color Attribute

- [Color](geono-color.md#color) :white_small_square: [Attribute](geono-color.md#attribute)
- [Color](geono-color.md#color) :white_small_square: [ambient_occlusion](geono-color.md#ambient_occlusion)

#### Displacement

- [Vector](geono-vector.md#vector) :white_small_square: [displacement](geono-vector.md#displacement)

#### Gamma

- [Color](geono-color.md#color) :white_small_square: [gamma](geono-color.md#gamma)

#### Hue Saturation Value

- [Color](geono-color.md#color) :white_small_square: [hue_saturation_value](geono-color.md#hue_saturation_value)

#### Input

- [Tree](geono-tree.md#tree) :white_small_square: [new_input](geono-tree.md#new_input)

#### Invert Color

- [Color](geono-color.md#color) :white_small_square: [invert](geono-color.md#invert)

#### Mapping

- [Vector](geono-vector.md#vector) :white_small_square: [mapping](geono-vector.md#mapping)

#### Material Output

- [Vector](geono-vector.md#vector) :white_small_square: [displacement_out](geono-vector.md#displacement_out)

#### Normal

- [Vector](geono-vector.md#vector) :white_small_square: [normal](geono-vector.md#normal)

#### Normal Map

- [Color](geono-color.md#color) :white_small_square: [normal_map](geono-color.md#normal_map)
- [Vector](geono-vector.md#vector) :white_small_square: [NormalMap](geono-vector.md#normalmap)

#### of curve

- [Spline](geono-spline.md#spline) :white_small_square: [points](geono-spline.md#points)

#### of Point

- [SplinePoint](geono-splinepoint.md#splinepoint) :white_small_square: [curve_index](geono-splinepoint.md#curve_index)
- [SplinePoint](geono-splinepoint.md#splinepoint) :white_small_square: [index_in_curve](geono-splinepoint.md#index_in_curve)

#### Output

- [Tree](geono-tree.md#tree) :white_small_square: [new_output](geono-tree.md#new_output)

#### Point in Curve

- [SplinePoint](geono-splinepoint.md#splinepoint) :white_small_square: [offset_in_curve](geono-splinepoint.md#offset_in_curve)

#### RGB to BW

- [Color](geono-color.md#color) :white_small_square: [to_bw](geono-color.md#to_bw)

#### Shader to RGB

- [Color](geono-color.md#color) :white_small_square: [FromShader](geono-color.md#fromshader)

#### Size

- [Cloud](geono-cloud.md#cloud) :white_small_square: [domain_size](geono-cloud.md#domain_size)
- [Curve](geono-curve.md#curve) :white_small_square: [domain_size](geono-curve.md#domain_size)
- [Instances](geono-instances.md#instances) :white_small_square: [domain_size](geono-instances.md#domain_size)
- [Mesh](geono-mesh.md#mesh) :white_small_square: [domain_size](geono-mesh.md#domain_size)

#### Tangent

- [Vector](geono-vector.md#vector) :white_small_square: [Tangent](geono-vector.md#tangent)

#### to Euler

- [Vector](geono-vector.md#vector) :white_small_square: [FromRotation](geono-vector.md#fromrotation)

#### to Rotation

- [Vector](geono-vector.md#vector) :white_small_square: [to_rotation](geono-vector.md#to_rotation)

#### UV Map

- [Vector](geono-vector.md#vector) :white_small_square: [UVMap](geono-vector.md#uvmap)

#### Value

- [Rotation](geono-rotation.md#rotation) :white_small_square: [Random](geono-rotation.md#random)
- [Vector](geono-vector.md#vector) :white_small_square: [Random](geono-vector.md#random)

#### Vector Displacement

- [Color](geono-color.md#color) :white_small_square: [vector_displacement](geono-color.md#vector_displacement)
- [Vector](geono-vector.md#vector) :white_small_square: [vector_displacement](geono-vector.md#vector_displacement)

#### Vector Transform

- [Vector](geono-vector.md#vector) :white_small_square: [transform](geono-vector.md#transform)

#### Wavelength

- [Color](geono-color.md#color) :white_small_square: [Wavelength](geono-color.md#wavelength)

#### XYZ

- [Rotation](geono-rotation.md#rotation) :white_small_square: [Combine](geono-rotation.md#combine)
- [Rotation](geono-rotation.md#rotation) :white_small_square: [x](geono-rotation.md#x)
- [Rotation](geono-rotation.md#rotation) :white_small_square: [y](geono-rotation.md#y)
- [Rotation](geono-rotation.md#rotation) :white_small_square: [z](geono-rotation.md#z)
- [Vector](geono-vector.md#vector) :white_small_square: [Combine](geono-vector.md#combine)
- [Vector](geono-vector.md#vector) :white_small_square: [x](geono-vector.md#x)
- [Vector](geono-vector.md#vector) :white_small_square: [y](geono-vector.md#y)
- [Vector](geono-vector.md#vector) :white_small_square: [z](geono-vector.md#z)