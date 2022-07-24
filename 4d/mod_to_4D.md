# To 4D (Modifier)

> Plunge a 3D geometry into a 4D shape by adding a fourth dimension.

**Note:** See [Add normals](mod_add_normals.md) and [Add tangents](mod_add_tangents.md)

## Sockets & attributes

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Mesh        | Modifier input geometry                                               |

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

