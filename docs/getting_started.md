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

We suppose that all scripts starts with the following import instruction:

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

  geo = tree.ig            # Let's get the input geometry (allegedly a mesh)
  
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

This time, the smooth shading is treated as a property of faces. As any property, `shade_smooth' can be set and it can also be get.

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
parameter. It can also take `min_value`, `max_value` and `description` parameter for better control.

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


















