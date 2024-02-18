# Getting started

## Prerequisites

To use the **geonodes** python module, you are supposed to be familiar with:
- Blender Geometry and Shader nodes
- Python language
- Running python scripts in Blender

Install the version of **geonodes** compatible with the Blender version you use.

## Important

> You can ask yourself what is the name of the method implementing a particular node and what are the name of the node sockets.
> Simply use the `snake_case` version of the names.
> You can also refer to the [API reference](index.md) or use `geonodes.print_doc(tree.xxxx)` method to dynamically print help into the console.


## Importing the module

We suppose that all scripts start with the following import instruction:

``` python
import geonodes as gn

or

from geonodes import GeoNodes, Shader, Simulation, Repeat, print_doc
``` 

See [Scripting nodes overview](/README.md#scripting-nodes-overview) for a quick overview of ***geonodes*** features.

## Playing with an icosphere

![Result](images/ico_tuto.png)




``` python
from geonodes import GeoNodes

with GeoNodes("Icosphere tuto") as tree:

   # Good practice: let's start with the tree inputs

   radius = tree.float_input("Radius", 1., min_value=0.01, max_value=10, description="A reasonable radius for the sphere")
   subs   = tree.integer_input("Subdivisions", 3, min_value=1, max_value=6, description="Ico Sphere d-subdivisions. Don't be too ambitious")
   
   # The icosphere
   
   ico = tree.IcoSphere(radius=radius, subdivisions=subs).mesh
   
   # The materials
   
   ico.set_material("Base Material")
   ico[tree.random_boolean(probability=.5)].set_material("Sel Material")
   
   # Extrude the select faces
   
   ico = ico[tree.material_index().equal(2)].extrude_mesh(offset_scale=0.3)
   
   tree.og = ico
```

![Result](images/ico_tuto.png)





















