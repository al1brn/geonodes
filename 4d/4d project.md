# The 4D project

> Compute 4D shapes Geometry Nodes scripted with **geonodes**.

## Overview

With **geonodes**, python is used to generate tree nodes modifiers performing 4D computations.
The 4D modifiers can be stacked to build more complex objects.

### Maths trees and modifiers

The 4D engine is made of two layers, the second layers using the first one for the actual computation:

- **Maths trees**: Nodes tree dealing with 4D vertices
  - *rotation*: rotate vertices according parameters
  - *projection*: projection of vertices from 4D to 3D
  
- **Modifiers**: nodes applied to geometries
  - *rotation*: rotate the geometry in 4D, including faces normals and curves tangents
  - *projection*: project the geometry to 3D space

## A sphere plunged in 4D

<img src="images/hypersphere 1.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />
     
## An hypersphere made of 7 slices

<img src="images/hypersphere 2.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />












