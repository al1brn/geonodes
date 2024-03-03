# The 4D Engine

> Compute 4D shapes Geometry Nodes scripted with **geonodes**.

## Overview

This project implements a 4D Engine to viualize 4D shapes in Blender by projecting them from 4D to 3D.

The architecture of the Engine is the following:
- A set of node groups perform the mathematical computations
- A set of Geometry Nodes modifiers can be stacked to build 4D objects and project them
- The last modifier to stack is "Projection"

> [!Note]
> All modifiers are prefixed by 4D, hence the actual name of the "Projection" modifier is "4D Projection".

For instance, to plunge a standard UV sphere into 4D, simply stack the two nodes:
- ***To 4D***
- ***Projection***

<img src="images/img_03.png" width = "400px"/>

Applied to a sphere, the result of this transformation is:

<img src="images/img_02.png" width = "600px"/>

The projection 4D -> 3D is driven by the Euler rotation of the object named "Projection".

The group "Projection Matrix" reads the Euler transformation of the "Projection" object and
computes the projection matrix from the 3 angles:

``` python
with GeoNodes("Projection Matrix", is_group=True, fake_user=True, prefix=maths) as tree:
    
    abc = tree.ObjectInfo("Projection").rotation
    
    a = abc.x  # Rotation x - w
    b = abc.y  # Rotation y - w
    c = abc.z  # Rotation z - w
    
    # Compute the projection matrix using
    # ...
```

With the architecture, all the 4D objects are projected with the same parameters

## Building the engine

Each group or modifier is build within a dedicated function. For instance, the modifier "Add Normals"
is build in the function `add_normals`. This allows to partially change the engine without having to rebuild the full engine.

``` python
def add_normals():
    
    with GeoNodes("Add normals", fake_user=True, prefix=modifiers) as tree:
        
        mesh  = tree.ig
        
        # The normals
        
        mesh.POINT.store_named_vector("Nxyz", mesh.normal)
        mesh.POINT.store_named_float( "Nw",   0)
            
        tree.og = mesh
```

Building the full engine requires to call all the building functions.

``` python
def gen():
    
    add_normals()
    add_tangents()
    to_4D()
    
    dot_normal()
    projection()
    
    # ...

# Building the engine

if True:
    gen()
    
``` 

## Conventions

The 4 dimensions of a 4-vector are stored in a couple (**Vector**, **Float**).
Input and output sockets use the name `xyz` for the vector and `w` for the float.

For instance, the group "Rotate from hyperplane" needs two 4-vectors as input which are named:
- `xyz` and `w`
- `Hyper xyz` and `Hyper w`
- Output sockets : `xyz` and `w`

<img src="images/img_04.png" width = "400px"/>

The fourth component is stored as **named attribute** `w`.

Meshes normals are saved as **named atributes** `Nxyz` and `Nw`.

Curves tangents are aved as **named atributes** `Txyz` and `Tw`.


## Maths Groups

- Projection
  - **Projection matrix** : build the projection Matrix from the ***Projection*** object
  - **Projection** : project the geometry into 3D. Must be the last modifier of the stack.

- Normalization
  - **Length** : length of a 4-vector
  - **Normalize** : normalize a 4-vector
  - **Normal basis** : build a normal basis from as set of 3 independant 4-vectors
  - **Cross** : cross product like between three 4-vectors, returns a 4-vector normal to the input
  - **Hyperplane** : return a normal basis perpendicular to a 4-vector

- Rotation
  - **Rotate to hyperplane** : rotate a vector to an hyperplane defined by a 4-vector
  - **Rotate from hyperplane** : rotate a vector from an hyperplane defined by a 4-vector
  - **Rotate in hyperplane** : rotate a vector within an hyperplane by either Euler or axis angle
  - **Follow vector** : rotate a vector such as vector A is aligned with vector B
  - **W Plane rotation** : rotate a vector within the w plane
  - **Rotation 2D** : rotate a vecor within a 2D plane defined by two 4-vectors

- Special
  - **Build along curve** : build a 4D shape by duplicating a 3D shape along a 4D curve


### Modifiers trees

- Initiaiization / utilities
  - **To 4D** : plunge a standard curve of mesh into 4D by setting its w component
  - **Add normals** : compute the 4D normals to a mesh surface
  - **Add tangents** : compute the 4D tangents of a curve 

- Projection
  - **Dot normal** : compute the dot product between the normals and the projection direction
  - **Projection** : projection from 4D to 3D

- Rotation
  - **Rotate in hyperplane** : rotate a 4D geometry in hyperplane
  - **Rotation 2D** : 2D rotation of a 4D geometry
  - **W Plane rotation** : rotation in the w plane

- Objects
  - **Axis** : visualize the 4 axis as they are projected
  - **Line** : a simple line
  - **Clifford torus** : Clifford torus
  - **Hypersphere** : hypersphere
  

- Light
  - **Light Set** : make the object emits 4D light
  - **Light Capture** : the object receive 4D light
  
- Miscelleanous
  - **Curve to mesh** : transform a 4D curve into a 4D mesh
  - **Build along curve** : build along curve




## Show case
### A sphere plunged in 4D

<img src="images/hypersphere 1.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />
     
### An hypersphere made of 7 slices

<img src="images/hypersphere 2.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

### Clifford torus

<img src="images/clifford 1.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

### Cones along a circle

<img src="images/cones 1.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />





