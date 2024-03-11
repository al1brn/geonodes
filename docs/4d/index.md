# The 4D Engine

> Compute 4D shapes Geometry Nodes scripted with **geonodes**.

<p align="center">
    <img src="images/Hypercube.gif" width = "600px"/>
</p>

> Source code of this project can be found in `geonodes.nodes.fourd.py` file.
> It shows how scripting nodes can simplify calcul intensive projects.


## Overview

This project implements a 4D Engine to viualize 4D shapes in Blender by projecting them from 4D to 3D.

The architecture of the Engine is the following:
- A set of node groups perform the mathematical computations
- A set of Geometry Nodes modifiers can be stacked to build 4D objects and project them
- The last modifier to stack is "Projection"

> [!Note]
> This module makes an extensive use of prefix to provide some sorting in the numerous modiers.

For instance, to plunge a standard UV sphere into 4D, simply stack the two nodes:
- ***4D Plunge 3D Geometry*** : add a fourth component to the geometry
- ***4D Projection*** : projection de 4D shape into 3D

The node ***4D Projection*** generally terminates the stack of 4D modfiers.
In the exemple below, the modifier ***4D Rotation 4D*** is added to rotate the figure in front of the camera.

<img src="images/4D_img_01.png" width = "400px"/>

Applied to a sphere, the result of this transformation is:

<img src="images/4D_img_02.png" width = "600px"/>

The projection 4D -> 3D is driven by the Euler rotation of two objects named "Projection" and "Projection2":
- "Projection" : each Euler angle is the angle between each axis and the fourth W axis : X: XW, Y: YW, Z: ZW
- "Projection2" :  each Euler angle is the secondary rotation : X: YZ, Y: XZ, Z: XY

> [!Note]
> With the architecture, all the 4D objects are projected with the same parameters

## Building the engine

The modifiers are build by calling **build4D** method of the **geonodes** module:

``` python
import geonodes as gn

gn.build4D()
```

> [!Note]
> Once the modifiers are created, python is not needed anymore to play with the modifiers.
> Moddifiers can be adder either manually or with **geonodes** to create custom shapes.

## Conventions

The 4 dimensions of a 4-vector are stored in a couple (**Vector**, **Float**).
Input and output sockets are suffixed by:
- `V` for the vector part
- `w` for the float part

In the exemple below, the nodes group ***M Projection*** accepts a 4-vector as input and returns a 4-vector.

<img src="images/4D_img_03.png" width = "600px"/>

The `V` part is the geometry position, and the `w` fourth component is stored as named attribute "w".

## V4 Class

Computing needs to perform operations on 4-Vectors: dot product, normalization, addition, scale...
To make source code as clear as possible the 4D engine uses a specific class which is basically a couple (Vector, Float):

``` python
class V4:
    def __init__(self, V, w):
        
        # Get the current tree
        tree = GeoNodes.current_tree()
        
        # The arguments can be either a socket or a value
        if hasattr(V, 'bsocket'):
            self.V = V
        else:
            self.V = tree.Vector(V)
            
        if hasattr(w, 'bsocket'):
            self.w = w
        else:
            self.w = tree.value(w)
``` 


This class implement the basic operations, for instance dot product and addition (note the use of a layout
to group the created node in a color specific layout and make the result quite readable):

``` python
class V4:

    # ...

    def dot(self, other):
        with GeoNodes.current_tree().layout("Dot 4", V4_COL):
            return self.V.dot(other.V) + self.w*other.w
            
    # ...
    
    def __add__(self, other):
        with GeoNodes.current_tree().layout("V4 Add", V4_COL):
            return V4(self.V + other.V, self.w + other.w)
```

The `V4` class also implements initialization and outputing functions to ease its use.
For instance, the `Position`constructor loads the position and the "w" named attribute.
If can read these information directly from the geometry or sample it:

``` python
class V4:
    @classmethod
    def Position(cls, geo, sample_index=None):
        with GeoNodes.current_tree().layout("Get Position V4", V4_COL):
            if sample_index is None:
                return cls(geo.position, geo.named_float("w"))
            else:
                return cls(
                    geo.POINT.sample_index_vector(geo.position,         index=sample_index), 
                    geo.POINT.sample_index_float( geo.named_float("w"), index=sample_index))
```

A `V4` class can then be used to change to 4D coordinates of a shape:

``` python
class V4:
    def set_position(self, geo):
        # Need to sample w before setting the position because w can be computed
        # from the position (for instance after a rotation)
        # Changing the position would change w before it is written
        with GeoNodes.current_tree().layout("Set Position V4", V4_COL):
            w = geo.POINT.sample_index_float(self.w, index=geo.index)
            geo.position = self.V
            return geo.store_named_float("w", w)
```

Thanks to the `V4` class, one can generate nodes by simply scripting python operation on 4-vectors.
The piece of code below shows how to use `V4` class.
- The `Input` constructor creates two input sockets suffixed by 'V' and 'w' (`"I V"` and `"I w"` for the first vector for instance)
- `normalized` returns a normalized version of the 4-vector. Here, it also returns an error if the vector is null
- In the layout frame, operations are performed on the 4-vectors using standard python syntax
  (just take care place `V4` instance first when operating with a value factor)

``` python
    with GeoNodes("Normalize 3-Basis", is_group=True, fake_user=True, prefix=g_maths) as tree:
        
        u0 = V4.Input(tree, "I", (1., 0., 0., 0.))
        u1 = V4.Input(tree, "J", (0., 1., 0., 0.))
        u2 = V4.Input(tree, "K", (0., 0., 1., 0.))
        
        # ----- Let's normalize the first vector
        
        e0, err = u0.normalized(True)
            
        # Let's suppress this dimension in the second one
        
        with tree.layout("Make the second vector perp to the first"):
            
            # u1 minus e0 part

            d = e0.dot(u1)
            u1 -= e0*d

            # Let's normalize
            
            e1, er = u1.normalized(True)
            err += er
            
        # ...
```

The image below shows the generated nodes:

<img src="images/4D_img_05.png" width = "600px"/>


## Engine modifiers

### 4D Modifiers

***4D Modifiers*** perform basic operations on geometries:

- ***Axis Viewer*** : shows the 4 axis. Note that the axis are directly projected, there is no need
  to stack ***4D Projection*** after this modifier.
- ***Plunge 3D Geometry*** : add a `w` coordinate to a standard 3D geometry. The 4-Geometry can be then
 transformed using other modifiers
- ***4D Projection*** : project a 4D geometry into 3D
- ***4D Translation*** : translate geometry using a 4-Vector
- ***4D Scale*** : scale the geometry in the fourth dimensions
- ***4D Rotation 4D*** : rotation with 6 possible angles
- ***4D Rotation 2D*** : rotation in a plane defined with the parameters
- ***4D Align Vector*** : rotation that aligns a vector along another one

> [!Important]
> After the modifier ***4D Projection***, the geometry is not a 4-Geometry anymore

### Curves modifiers

***Curves modifiers*** work on curves.

- ***C W from curve*** : works as ***Plunge 3D Geometry*** but read the `w` coordinate from the `z` coordinate
  of another curve
- ***C Line*** : a line segment
- ***C Parametric Curve*** : a simple 4-curve generator with parameters to play with
- ***C Curve to Mesh*** : instantiate 3D-Mesh along the 4D-Curve. The 3D meshes are aligned either
  along its `Z` or `W` axis
- ***C Curve to Mesh with Spheres*** : same as ***C Curve to Mesh*** using UV Sphere as profile.
- ***C Mesh to Curve*** : use the edges of a mesh to create curves. Faces can be removed or kept.
- ***C Curves Profile*** : create tubes around the curves to make them visible. **To be used after projection**.

> [!Note]
> The modifier ***C Curves Profile*** must be used after the projection since its creates 3D geometry around the edges.

### Surface modifiers

***Surface Modifiers*** work on surfaces.

- ***S Extrude*** : Extrude a surface a in given direction
- ***S Hypercube*** : create an hypercube (or tesseract)
- ***S Hypersphere*** : create an hypersphere
- ***S Torus*** : parametrable torus
- ***S Clifford Torus*** : Clifford Torus
- ***S Klein Torus*** : Klein Torus
- ***S 5-Cell Polytope*** : 5-cell polytope
- ***S 16-Cell Polytope*** : 16-cell polytope

## Showcase

### Hypersphere

<p align="center">
    <img src="images/4D_hypersphere.png" width = "600px"/>
</p>

### Clifford Torus

<p align="center">
    <img src="images/4D_Clifford.png" width = "600px"/>
</p>

### Klein Torus

<p align="center">
    <img src="images/4D_Klein.png" width = "600px"/>
</p>

### 5-Cell Polytope

<p align="center">
    <img src="images/4D_5-Cell.png" width = "600px"/>
</p>

### 16-Cell Polytope

<p align="center">
    <img src="images/4D_16-Cell.png" width = "600px"/>
</p>










