# Hypersphere (Modifier)

> Create an hypersphere from the input geometry (which should be a sphere).

**Note:** Call the modifier [Build along curve](mod_build_along_curve.md) along the curve generated with [Line](mod_line.md)

## Sockets & attributes

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Mesh        | Modifier input geometry                                               |
| Slices      | Integer     | Number of slices to create along the W axis                           |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Mesh        | Modifier output geometry                                              |

### Named attributes

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| w           | Float       | The fourth dimension                                                  |
| Nxyz        | Vector      | Vector part of the normals                                            |
| Nw          | Float       | Float part of the normals                                             |
| Txyz        | Vector      | Vector part of the tangents                                           |
| Tw          | Float       | Float part of the tangents                                           |


## Code

``` python

with gn.Tree(modifiers.name("Hypersphere")) as tree:

    sphere = gn.Mesh(tree.ig)
    stat   = sphere.verts.statistic(attribute=sphere.verts.position)
    radius = stat.max.x
    slices = gn.Integer.Input(7, "Slices", min_value=1, max_value=1000, description="Number of slices along w axis")

    # The fourth dimension

    with tree.layout("Prepare 4th axis"):

        curve = gn.Curve.Line(start=(0, 0, -radius), end=(0, 0, radius)).resample(count=slices+2)
        curve.points.set_named_float("w", curve.points.position.z)
        curve.points.position = 0
        curve.points.set_named_vector("Txyz", 0)
        curve.points.set_named_float("Tw", 1)

    with tree.layout("Slices radius"):

        n2 = (slices + 1)/2
        z = (curve.points.index - n2)/n2
        curve.points.radius = radius*(gn.sqrt(1 - z*z))

        curve.points[slices+1].delete()
        curve.points[0].delete()

    # Sphere to 4D

    sphere = modifiers.to_4D(geometry=sphere).geometry

    hs = maths.build_along_curve(
        geometry_4d = sphere,
        curve_4d    = curve,
        align_xyz   = (0, 0, 0),
        align_w     = 1,
        use_radius  = True,
    ).geometry

    tree.og = hs


```

