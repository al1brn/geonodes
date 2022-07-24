# Add tangents (Modifier)

> Store the tangents of a curve as named attributes.

Tangents are stored as points named attributes:

- **Txyz** (Vector): The vector part of the tangents
- **Tw** (Float): The float part of the tangents

## Sockets

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Curve       | Modifier input geometry.                                              |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Curve       | Modifier output geometry                                              |

## Code

``` python

with gn.Tree(modifiers.name("Add tangents")) as tree:

    curve  = gn.Curve(tree.ig)
    points = curve.points

    # The tangents

    points.set_named_vector("Txyz", points.tangent)
    points.set_named_float( "Tw",   0)

    tree.og = curve

```
