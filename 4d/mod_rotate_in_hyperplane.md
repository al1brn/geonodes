# Rotate in hyperplane (Modifier)

> Rotate a geometry into an hyperplane defined by a 4-vector. See [Rotate in hyperplane](rotate_in_hyperplane.md).

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

with gn.Tree(modifiers.name("Rotate in hyperplane")) as tree:

    geo   = tree.ig

    hv    = gn.Vector.Input((0, 0, 0), "Hyper xyz")
    hw    = gn.Float.Input(1, "Hyper w")
    euler = gn.Vector.Rotation((0, 0, 0), "Euler")
    axis  = gn.Vector.Input((0, 0, 1), "Axis")
    angle = gn.Float.Angle(0, "Angle")

    # ----- All

    with tree.layout("All points rotation"):

        node = maths.rotate_in_hyperplane(
                    xyz  = geo.points.position,
                    w    = geo.points.get_named_float("w"),
                    )
        node.plug_node(tree.group_input)

        geo.points.position = node.xyz
        geo.points.set_named_float("w", node.w)

    mesh  = geo.mesh_component
    curve = geo.curve_component
    cloud = geo.points_component
    inst  = geo.instances_component

    # ----- Mesh

    with tree.layout("Mesh"):

        node = maths.rotate_in_hyperplane(
                    xyz  = mesh.verts.get_named_vector("Nxyz"),
                    w    = mesh.verts.get_named_float("Nw"),
                    )
        node.plug_node(tree.group_input)

        mesh.verts.set_named_vector("Nxyz", node.xyz)
        mesh.verts.set_named_float("Nw", node.w)

    # ----- Curve

    with tree.layout("Curve"):

        node = maths.rotate_in_hyperplane(
                    xyz  = curve.points.get_named_vector("Txyz"),
                    w    = curve.points.get_named_float("Tw"),
                    )
        node.plug_node(tree.group_input)

        curve.points.set_named_vector("Txyz", node.xyz)
        curve.points.set_named_float("Tw", node.w)

    tree.og = mesh + curve + cloud + inst        

```

