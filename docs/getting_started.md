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
import geonodes as gn

with gn.Tree("Icosphere tuto") as tree:

   # Good practice: let's start with the tree inputs

   radius = gn.Float.Input(1, "Radius", min_value=0.01, max_value=10, description="A reasonable radius for the sphere")
   subs   = gn.Integer.Input(3, description="No limits: I trust you")
   
   mat_base = gn.Material.Input(None, "Base")
   mat_sel  = gn.Material.Input(None, "Selected")
   
   
   # The icosphere
   
   icosphere = gn.Mesh.IcoSphere(radius=radius, subdivisions=subs).mesh
   
   # The materials
   
   faces = icosphere.faces
   
   faces.material = mat_base
   faces[ gn.Boolean.Random(probability=.5) ].material = mat_sel
   
   # Extrude the select faces
   
   faces[faces.material_index.equal(2)].extrude(offset_scale=0.3)
   
   tree.og = icosphere
```

![Result](images/ico_tuto.png)





















