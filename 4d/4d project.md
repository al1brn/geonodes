# The 4D project

> Compute 4D shapes Geometry Nodes scripted with **geonodes**.

## Overview

With **geonodes**, python is used to generate tree nodes modifiers performing 4D computations.
The 4D modifiers can be stacked to build more complex objects.

### Maths trees and modifiers

The 4D engine is made of two layers, the second layers using the first one for the actual computation:

- **Maths trees**: Utilities to perform the computation on 4D vertices.
- **Modifiers**: Trees with input and output geometries transforming the shapes.

<img src="images/Param hypersphere.png"
     alt="Markdown Monster icon"
     width="400px"/>

## The nodes trees

### Maths trees

- Projection
  - [Projection matrix](projection_matrix.md)
  - [Projection](projection.md)

- Normalization
  - [Length](length.md)
  - [Normalize](normalize.md)
  - [Normal basis](normal_basis.md)
  - [Cross](cross.md)
  - [Hyperplane](hyperplane.md)

- Rotation
  - [Rotate to hyperplane](rotate_to_hyperplane.md)
  - [Rotate from hyperplane](rotate_from_hyperplane.md)
  - [Rotate in hyperplane](rotate_in_hyperplane.md)
  - [Follow vector](follow_vector.md)
  - [W Plane rotation](w_plane_rotation.md)
  - [Rotation 2D](rotation_2d.md)

- Special
  - [Build along curve](build_along_curve.md)


### Modifiers trees

- Initiaiization / utilities
  - [To 4D](mod_to_4D.md)
  - [Add normals](mod_add_normals.md)
  - [Add tangents](mod_add_tangents.md)

- Projection
  - [Dot normal](mod_dot_normal.md)
  - [Projection](mod_projection.md)

- Rotation
  - [Rotate in hyperplane](mod_rotate_in_hyperplane.md)
  - [Rotation 2D](mod_rotation_2d.md)
  - [W Plane rotation](mod_w_plane_rotation.md)

- Objects
  - [Axis](mod_axis.md)
  - [Line](mod_line.md)
  - [Clifford torus](mod_clifford.md)
  - [Hypersphere](mod_hypersphere.md)

- Special
  - [Light](mod_light.md)
  - [Build along curve](mod_build_along_curve.md)


## A sphere plunged in 4D

<img src="images/hypersphere 1.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />
     
## An hypersphere made of 7 slices

<img src="images/hypersphere 2.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />
     




