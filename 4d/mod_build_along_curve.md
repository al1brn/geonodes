# Build along curve (Modifier)

> Duplicates a geometry along a given curve. See [Build along curve (Maths)](build_along_curve.md).

**Note 1:** The curve is passed as object. The object must have been plunged into 4D **but not projected**.

**Note 2:** See an example of use with [Hypersphere](mod_hypersphere.md).

## Sockets

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Geometry    | Modifier input geometry                                               |
| Curve       | Object      | Curve object to deuplicate the geometry along                         |
| Align xyz   | Vector      | Vector part of the 4-vector to align with the curve tangent           |
| Align w     | Float       | Float part of the 4-vector to align with the curve tangent            |
| Use radius  | Boolean     | If True, scale the geometry using the curve radius as scale           |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Geometry    | The resulting geometry                                                |

## Code

``` python

with gn.Tree(modifiers.name("Build along curve")) as tree:

    geo        = tree.ig
    curve      = gn.Object.Input("Curve").geometry
    align_v    = gn.Vector.Input((0, 0, 1), "Align xyz")
    align_w    = gn.Float.Input(0, "Align w")
    use_radius = gn.Boolean.Input(False, "Use radius")

    node = maths.build_along_curve(
        geometry_4d = geo,
        curve_4d    = curve,
        align_xyz   = align_v,
        align_w     = align_w,
        use_radius  = use_radius)

    tree.og = node.geometry

```




