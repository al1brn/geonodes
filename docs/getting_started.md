# Getting started

## Prerequisites

To use the **geonodes** python module, you are supposed to be familiar with:
- Blender Geometry Nodes
- Python language
- Running python scripts in Blender

Install the version of **geonodes** compatible with the Blender version you use.

## Important

> You can ask yourself what is the name of the method implementing a particular node and what are the name of the node sockets.
> Simply use the `snake_case` version of the names. See [Naming conventions](naming.md) for more details.
> You can also refer to the [API reference](https://al1brn.github.io/geonodes/).

## Importing the module

We suppose that all scripts start with the following import instruction:

``` python
import geonodes as gn
``` 

## My first tree

Execute the following piece of code (node forgetting the module import :-):

``` python
with gn.Tree("Do nothing tree") as tree:

   # og and ig are shortcuts for output_geometry and input_geometry

   tree.og = tree.ig
```

This code simply creates the tree which connects the input geometry to the output geometry.

Add a **Geometry Node** modifier to your Object and, as a parameter, select the node tree named "Do nothing tree" in the list.

And nothing happens as expected !

## My first operation

Let's build something more interesting with our input geometry. We will subdivide it and shade it smooth:

``` python
with gn.Tree("Shading smooth") as tree:

  geo = tree.ig           # Let's get the input geometry (allegedly a mesh)
  
  geo.subdivide()         # Node named 'Subdivide Mesh' (Mesh is implicit and is not used to build the method name)
  geo.set_shade_smooth()  # Node named 'Set Shade Smooth'
  
  tree.og = geo           # or tree.output_geometry = geo
``` 

## Using domains

Operations on geometries are often operations on domains properties. You will write a clearer code by making explicit
on which domain you operate. For instance, shading a mesh is in reality setting a property of the mesh faces.

A better code will be:

``` python
  geo.faces.shade_smooth = True
``` 

This time, the smooth shading is treated as a property of faces. As any property, `shade_smooth` can be set and it can also be get.

In the code below, the variable `smoothed_faces` contains the values `True` or `False` for all the mesh faces,
depending if they are smoothed or not.

``` python
  smoothed_faces = geo.faces.shade_smooth
```

## User inputs

In Geometry Nodes, user parameters are group input sockets.
These inputs can be created with the class constructor `Input` available in all the **geonodes** classes, for instance:

``` python
   object = gn.Object.Input("Other geometry")
   count  = gn.Integer.Input(10, "Count", min_value=2)
   factor = gn.Float.Input(0.5, "Factor", min_value=0, max_value=1, description="Use this value to control the modifier effect")
```

The `input` constructor get a  socket name as parameter. For values such as Integer or Float, it takes the default value as first
parameter. It can also take `min_value`, `max_value` and `description` parameters for better control.

See [API reference](https://al1brn.github.io/geonodes/).

## Tree outputs

As seen above, the resulting geometry can be output with:

``` python
   tree.output_geometry = geo # og alias can be also used
```

To output other values, use the method `to_output` available in all classes:

``` python
   v = mesh.verts.position   # Position of vertices
   v.to_output("Location")   # Location output sockets is created. Its type is Vector 
```

## A more advanced example

Let's create an icosphere, add two materials and set randomly the materials on the faces.
Once done, will extrude the faces with one particular material.

To do that, we need to learn:
- [How to create a geometry](#creating-geometries)
- [Manipulating materials](#adding-materials)
- [How to selectively change properties on domains](#selecting-faces)

### Creating geometries

Geometries are created by calling constructors of geometry classes. These constructors correspond to the menus **Mesh Primitives**
and **Curve Primitives** of the `Add node` menu in Blender.

The names of the constructors are build as CamelCase version of their node names.

``` python
   icosphere = gn.Mesh.IcoSphere()
```

This create the default icosphere. We may want some customization. Looking at the node reference [Ico Sphere Node](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/icosphere.html),
we see that there are two parameters: **Radius** and **Subdivisions**. They are implemented as parameters of the constructors.
As explained in the [naming conventions](naming.md), **geonodes** uses snake_case version of the nodes sockets and nodes parameters names:

``` python
   icosphere = gn.Mesh.IcoSphere(radius=1, subdivisions=3)
```

You may want to give more control on these parameters:

``` python
   radius = gn.Float.Input(1, "Radius", min_value=0.01, max_value=10, description="A reasonable radius for the sphere")
   subs   = gn.Integer.Input(3, description="No limits: I trust you")
   icosphere = gn.Mesh.IcoSphere(radius=radius, subdivisions=subs)
```

We have now an icosphere which can be created with parameters exposed to the user.

### Adding materials

Materials are properties of faces. The syntax will look like `mesh.faces.material = ...`.

A material is instantiated with its name. Let's suppose that we have two existing materials named "Red" and "Blue".
To assign the materials to our icosphere, we write:

``` python
   icosphere.faces.material = gn.Material("Red")
   icosphere.faces.material = gn.Material("Blue")
```

### Selecting faces

The resulting icosphere is blue because the second material was assigned to all faces, overwriting the previous assignment.
But what we want is to have a random selection of faces with a different color.
The faces can be selected by "calling" them with a selection parameter.

``` python
   icosphere.faces( random_selection ).material = gn.Material("Blue")
```

A random selection can be generated using the `Random` constructor of class [Boolean](https://al1brn.github.io/geonodes/sockets/boolean.html):

``` python
   icosphere.faces( gn.Boolean.Random(probability=0.5) ).material = gn.Material("Blue")
```

This time, the blue material will overwrite only 50% of the red faces.

Another way to reach this result is to use the material index:

``` python
   icosphere.faces.material = gn.Material("Red")
   icosphere.faces.material = gn.Material("Blue")
   
   # Two materials have be added
   # All faces have material index set to 1
   # Let's change half of them back to 0
   
   icosphere.faces( gn.Boolean.Random(probability=.5) ).material_index = 0
```

### Extrusion

The `Extrude Mesh` node accepts a domain parameter to define what must be extruded. With **geonodes**, the 3 possibilities
are written:

``` python
   mesh.faces.extrude()
   mesh.edges.extrude()
   mesh.verts.extrude()
```

We want to extrude faces, but only the blue faces:

``` python
   faces = icosphere.faces
   faces(faces.material_index.equal(1)).extrude()
```

**Note:** `material_index.equal(1)` is used rather than `material_index == 1`. This late expression would give a python `bool`
result rather than the expected **geonodes** `Boolean`.

Alternatively, if you are not confident with the material indices, you can use the `material_selection` method:

``` python
   faces(faces.material_selection(gn.Material("Blue"))).extrude()
```

The extrusion itself can be controlled with the extrusion parameters:

``` python
   faces(faces.material_index.equal(1)).extrude(offset_scale=0.3)
```

### The full code


``` python
import geonodes as gn

with gn.Tree("Icosphere tuto") as tree:

   # Good practice: let's start with the tree inputs

   radius = gn.Float.Input(1, "Radius", min_value=0.01, max_value=10, description="A reasonable radius for the sphere")
   subs   = gn.Integer.Input(3, description="No limits: I trust you")
   
   # The icosphere
   
   icosphere = gn.Mesh.IcoSphere(radius=radius, subdivisions=subs)
   
   # The materials
   
   faces = icosphere.faces

   faces.material = gn.Material("Red")
   faces( gn.Boolean.Random(probability=.5) ).material_index = 0

   # Extrude the blue faces
   
   faces(faces.material_index.equal(1)).extrude(offset_scale=0.3)
   
   
```



















