# W Plane Rotation (Modifier)

> Rotate a geometry into a plane containing the W axis. See [W Plane Rotation (Maths)](w_plane_rotation.md).

## Sockets & attributes

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Geometry    | Modifier input geometry                                               |
| Axis        | Integer     | Axis number: 0 for X, 1 for Y, 2 for Z                                |
| Angle       | Float       | Rotation angle                                                        |

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

with gn.Tree(modifiers.name("W Plane Rotation")) as tree:

    geo   = tree.ig
    axis  = gn.Integer.Input(0, "Axis", min_value=0, max_value=2) 
    angle = gn.Float.Angle(0, "Angle")

    # ----- All

    with tree.layout("All points rotation"):

        node = maths.w_plane_rotation(
                    xyz  = geo.points.position,
                    w    = geo.points.get_named_float("w"), 
                    axis = axis, angle=angle)

        geo.points.position = node.xyz
        geo.points.set_named_float("w", node.w)

    mesh  = geo.mesh_component
    curve = geo.curve_component
    cloud = geo.points_component
    inst  = geo.instances_component

    # ----- Mesh

    with tree.layout("Mesh"):

        node = maths.w_plane_rotation(
                    xyz   = mesh.verts.get_named_vector("Nxyz"),
                    w     = mesh.verts.get_named_float("Nw"), 
                    axis  = axis, angle=angle)

        mesh.verts.set_named_vector("Nxyz", node.xyz)
        mesh.verts.set_named_float("Nw", node.w)

    # ----- Curve

    with tree.layout("Curve"):

        node = maths.w_plane_rotation(
                    xyz   = curve.points.get_named_vector("Txyz"),
                    w     = curve.points.get_named_float("Tw"), 
                    axis  = axis, angle=angle)

        curve.points.set_named_vector("Txyz", node.xyz)
        curve.points.set_named_float("Tw", node.w)

    tree.og = mesh + curve + cloud + inst
        


```

