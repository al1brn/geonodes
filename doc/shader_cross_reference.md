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

- [Vector](vector.md#vector) :white_small_square: [out](vector.md#out)

#### AOV Output

- [Color](color.md#color) :white_small_square: [out](color.md#out)
- [Float](float.md#float) :white_small_square: [out](float.md#out)
- [Vector](vector.md#vector) :white_small_square: [out](vector.md#out)

#### Blackbody

- [Color](color.md#color) :white_small_square: [Blackbody](color.md#blackbody)

#### Brightness Contrast

- [Color](color.md#color) :white_small_square: [brightness_contrast](color.md#brightness_contrast)

#### Bump

- [Vector](vector.md#vector) :white_small_square: [bump](vector.md#bump)

#### Color Attribute

- [Color](color.md#color) :white_small_square: [Attribute](color.md#attribute)
- [Color](color.md#color) :white_small_square: [ambient_occlusion](color.md#ambient_occlusion)

#### Displacement

- [Vector](vector.md#vector) :white_small_square: [displacement](vector.md#displacement)

#### Gamma

- [Color](color.md#color) :white_small_square: [gamma](color.md#gamma)

#### Hue Saturation Value

- [Color](color.md#color) :white_small_square: [hue_saturation_value](color.md#hue_saturation_value)

#### Input

- [Tree](tree.md#tree) :white_small_square: [new_input](tree.md#new_input)

#### Invert Color

- [Color](color.md#color) :white_small_square: [invert](color.md#invert)

#### Mapping

- [Vector](vector.md#vector) :white_small_square: [mapping](vector.md#mapping)

#### Material Output

- [Vector](vector.md#vector) :white_small_square: [displacement_out](vector.md#displacement_out)

#### Normal

- [Vector](vector.md#vector) :white_small_square: [normal](vector.md#normal)

#### Normal Map

- [Color](color.md#color) :white_small_square: [normal_map](color.md#normal_map)
- [Vector](vector.md#vector) :white_small_square: [NormalMap](vector.md#normalmap)

#### of curve

- [Spline](spline.md#spline) :white_small_square: [points](spline.md#points)

#### of Point

- [SplinePoint](splinepoint.md#splinepoint) :white_small_square: [curve_index](splinepoint.md#curve_index)
- [SplinePoint](splinepoint.md#splinepoint) :white_small_square: [index_in_curve](splinepoint.md#index_in_curve)

#### Output

- [Tree](tree.md#tree) :white_small_square: [new_output](tree.md#new_output)

#### Point in Curve

- [SplinePoint](splinepoint.md#splinepoint) :white_small_square: [offset_in_curve](splinepoint.md#offset_in_curve)

#### RGB to BW

- [Color](color.md#color) :white_small_square: [to_bw](color.md#to_bw)

#### Shader to RGB

- [Color](color.md#color) :white_small_square: [FromShader](color.md#fromshader)

#### Size

- [Cloud](cloud.md#cloud) :white_small_square: [domain_size](cloud.md#domain_size)
- [Curve](curve.md#curve) :white_small_square: [domain_size](curve.md#domain_size)
- [Instances](instances.md#instances) :white_small_square: [domain_size](instances.md#domain_size)
- [Mesh](mesh.md#mesh) :white_small_square: [domain_size](mesh.md#domain_size)

#### Tangent

- [Vector](vector.md#vector) :white_small_square: [Tangent](vector.md#tangent)

#### to Euler

- [Vector](vector.md#vector) :white_small_square: [FromRotation](vector.md#fromrotation)

#### to Rotation

- [Vector](vector.md#vector) :white_small_square: [to_rotation](vector.md#to_rotation)

#### UV Map

- [Vector](vector.md#vector) :white_small_square: [UVMap](vector.md#uvmap)

#### Value

- [Rotation](rotation.md#rotation) :white_small_square: [Random](rotation.md#random)
- [Vector](vector.md#vector) :white_small_square: [Random](vector.md#random)

#### Vector Displacement

- [Color](color.md#color) :white_small_square: [vector_displacement](color.md#vector_displacement)
- [Vector](vector.md#vector) :white_small_square: [vector_displacement](vector.md#vector_displacement)

#### Vector Transform

- [Vector](vector.md#vector) :white_small_square: [transform](vector.md#transform)

#### Wavelength

- [Color](color.md#color) :white_small_square: [Wavelength](color.md#wavelength)

#### XYZ

- [Rotation](rotation.md#rotation) :white_small_square: [Combine](rotation.md#combine)
- [Rotation](rotation.md#rotation) :white_small_square: [x](rotation.md#x)
- [Rotation](rotation.md#rotation) :white_small_square: [y](rotation.md#y)
- [Rotation](rotation.md#rotation) :white_small_square: [z](rotation.md#z)
- [Vector](vector.md#vector) :white_small_square: [Combine](vector.md#combine)
- [Vector](vector.md#vector) :white_small_square: [x](vector.md#x)
- [Vector](vector.md#vector) :white_small_square: [y](vector.md#y)
- [Vector](vector.md#vector) :white_small_square: [z](vector.md#z)