# fractal

[Source Code](../demos/fractal.py)

> [!CAUTION]
> This module is still work in progress

This module provides several independant features:
- Random normal: normal law implementation for values and vectors
- Camera culling: culls points, edges and faces which are not visible in the field of view of the camera
- Multi resolution: surfaces with a resolution depending on the distance to the camera
- Fractals: diving into fractals

All the modifiers can be generated using demo function.
Specific modifiers can be generated using specic functions:
- random_normal : random modifiers
- camera_culling : camera culling modifiers
- multires_surface : multi resolution modifiers
- sierpinski : sierpinski fractal
- romanesco : other fractals



> [!NOTE]
> Modifiers:
> - Random Normal Value
> - Random Normal Vector
> - Random Shake Vectors
> - Camera Projection
> - Camera Point Culling
> - Camrea Edge Culling
> - Camera Face Culling
> - Sierpinski Triangle
> - Multires Surface
> - Multires Faces
> - DEMO Multires Faces
> - Fractal Cloud Iterator
> - Fractal Mesh Iterator
> - Fractal Cone Iterator
> - Logarithmic Spiral
> - Romanesco Cabbage (In progress)

``` python
from geonodes.demos import fractal

fractal.demo()
```

## Content

- [camera_culling](fractal.md#camera_culling)
- [face_fractals](fractal.md#face_fractals)
- [romanesco](fractal.md#romanesco)

## Functions



----------
### camera_culling()

> function

``` python
camera_culling()
```

Camera culling

Removes geometry which is not visible from the camera.

The camera is defined by the following arguments
- Aspect Ratio (Float) : width / height
- Focal Length (Float) : expressed in mm
- Margin (Float) : margin extended the visibility area

Relative
========

> Group

Transform position in space relative to camera and project the points on the sensor



Point Culling
=============

> Mesh, Cloud or Curve Modifier

Delete the points which are not visible.

Delete all the points which are not visible (calling "Position Culling").



Face Culling
=============

> Mesh Modifier

Delete the faces which are not visible.

To determine if a face is visible, it is subdivided and if all the points are not visible, the face is not visible



Edge Culling
=============

> Mesh Modifier

Delete the edges which are not visible.

> [!NODE]
> This particular modifier is relevant only for meshes made only of edges

#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [fractal](fractal.md#fractal) :black_small_square: [Content](fractal.md#content) :black_small_square: [Functions](fractal.md#functions)</sub>

----------
### face_fractals()

> function

``` python
face_fractals()
```

Fractals built by replacing a face by several ones

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [fractal](fractal.md#fractal) :black_small_square: [Content](fractal.md#content) :black_small_square: [Functions](fractal.md#functions)</sub>

----------
### romanesco()

> function

``` python
romanesco()
```

Some fractals such as Romanesco Cabbage

These 3D fractals replace a single point by other points.
Each point has a radius allowing to cull points outside the camera and to
limit the fractal depth.

A point has the following attributes:
- radius (Float) : size
- Up (Vector) : upwards direction

A fractal iteration replaces each point by other points applying the fractal specific shrink factor.

Deform Shape
============

Deforms the point to be less annoying

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [fractal](fractal.md#fractal) :black_small_square: [Content](fractal.md#content) :black_small_square: [Functions](fractal.md#functions)</sub>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [fractal](fractal.md#fractal) :black_small_square: [Content](fractal.md#content) :black_small_square: [fractal](fractal.md#fractal)</sub>