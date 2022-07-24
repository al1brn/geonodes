# Line (Modifier)

> Build a 4D line curve. Can by used as curve 4D in [Build along curve](mod_build_along_curve.md).

**Note:** Input geometry is unsued.

## Sockets & attributes

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Mesh        | Modifier input geometry (unused)                                      |
| xyz 0       | Vector      | Vector part starting point                                            |
| w 0         | Float       | Float part of starting point                                          |
| xyz 1       | Vector      | Vector part of ending point                                           |
| w 1         | Float       | Float part of endinf point                                            |
| Count       | Integer     | Number of point in the line                                           |

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

with gn.Tree(modifiers.name("To 4D")) as tree:
        
    geo = tree.ig
    w   = gn.Float.Input(0 , "w")

    # ----- The fourth dimention

    geo.points.set_named_float("w", w)

    # ----- Normals and tangent

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

