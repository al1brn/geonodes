# Global setup

## Groups

Around 30 nodes trees are generated with **geonodes**.

To keep the things clean are ordered, we use of the *goenodes.Groups* class:

``` python

import geonodes as gn

modifiers = gn.Groups("4D")
maths     = gn.Groups("Maths 4D")

```

A *Groups* class manages a prefix which is added to the node trees name.
In **geonodes**, it can then be used to call a node has a python function.

The following code shows how building and then using a utility nodes tree.

``` python

import geonodes as gn

# Utility nodes tree

with gn.Tree("Maths 4D Do something", group=True) as tree:

  # Return 1 ;-)
  
  gn.Float(1).to_output("One")
  
# We need this utility somewhere

with gn.Tree("Maths 4D Do something else", group=True) as tree:

  node = gn.Group("Maths 4D Do something")
  my_one = node.one

```

In the following code, we use the *Groups* class to ease this naming process.
Note that the python names are the snake_case version of the trees and sockets names.
The result of these two pieces of code are exactly the same.

``` python

import geonodes as gn

# Utility nodes tree

with gn.Tree(maths.name("Do something"), group=True) as tree:

  # Return 1 ;-)
  
  gn.Float(1).to_output("One")
  
# We need this utility somewhere

with gn.Tree(maths.name("Do something else"), group=True) as tree:

  node = maths.do_something()
  my_one = node.one

```

## 4D vertices

The 4D vertices are implemented by a **Vector** and a **Float**.
The vertices of a geometry gives the vector part. The fourth coordinate is stored in the named attribute `w`.

The following piece of code shows how the fourth dimensions is added to plunge the geometry into 4D space using the
`w` parameter passed as input of the modifier.

``` python

def to_4D():
    
    with gn.Tree(modifiers.name("To 4D")) as tree:
        
        geo = tree.ig
        w   = gn.Float.Input(0 , "w")
        
        # ----- The fourth dimention
        
        geo.points.set_named_float("w")
        
```

With modifiers, the naming convention is the following:

- **Vector part**: xyz
- **Float part**: w



## Normals and tangents

When plunged into 4D, the tangents (curves) and normals (mesghes) are stored as named attribute to be transformed together with
the vertices.

The following code shows how the tangents and normals are initialized with the **To 4D** modifier:

``` python

        # Continuation of To 4D modifier

        mesh  = geo.mesh_component
        curve = geo.curve_component
        cloud = geo.points_component
        inst  = geo.instances_component

        # ---- Mesh normals
        
        mesh = modifiers.add_normals(geometry=mesh).geometry
        
        # ---- Curve tangents
        
        curve = modifiers.add_tangents(geometry=curve).geometry
            
        # ---- Result
        
        tree.og = mesh + curve + cloud + inst

```






  
 



