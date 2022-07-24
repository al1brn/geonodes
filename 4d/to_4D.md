# To 4D

> The first step is to plunge a geometry into the 4th dimension.

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

The normals of mesh faces are now plunged into 4D. We also must add a fourth dimension.
But we can't anymore rely on the `Normal` attribute of the mesh to keep the vector part of the normal
because the mesh can be deformed in 4D later one.

> It is why the vector part is saved as a named attribute.

The following modifier plunge the normal into 4D:

``` python

with gn.Tree(modifiers.name("Add normals")) as tree:

    mesh  = gn.Mesh(tree.ig)

    # The normals

    mesh.verts.set_named_vector("Nxyz", mesh.verts.normal)
    mesh.verts.set_named_float( "Nw",   0)

    tree.og = mesh

``` 

## Tangents

Similarily, curves tangents must be plunged as normals:

``` python

# ----------------------------------------------------------------------------------------------------
# Add the tangents to a curve

with gn.Tree(modifiers.name("Add tangents")) as tree:

    curve  = gn.Curve(tree.ig)
    points = curve.points

    # The tangents

    points.set_named_vector("Txyz", points.tangent)
    points.set_named_float( "Tw",   0)

    tree.og = curve

```

## To 4D modifier

The full modifier is given below:

``` python

with gn.Tree(modifiers.name("Add tangents")) as tree:
        
    curve  = gn.Curve(tree.ig)
    points = curve.points

    # The tangents

    points.set_named_vector("Txyz", points.tangent)
    points.set_named_float( "Tw",   0)

    tree.og = curve

```

