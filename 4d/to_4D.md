# To 4D

> The first step is to plunge a geometry into the 4th space

## The fourth coordinate

Plunging a shape in the 4D space consists in adding a 4th coordinate named `w`:

``` python

with gn.Tree(modifiers.name("To 4D")) as tree:

    geo = tree.ig
    w   = gn.Float.Input(0 , "w")

    # ----- The fourth dimention

    geo.points.set_named_float("w", w)
        
``` 

## Normals

The normals of mesh faces are now plunged 
