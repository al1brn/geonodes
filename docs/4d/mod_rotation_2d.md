# Rotation 2D (Modifier)

> Rotate a geometry into a plane defined by two 4-vectors. See [Rotation 2D (Maths)](rotation_2d.md).

## Sockets & attributes

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Geometry    | Modifier input geometry                                               |
| xyz 0       | Vector      | Vector part of the first 4-vector defining the plane                  |
| w 0         | Float       | Float part of the first 4-vector defining the plane                   |
| xyz 1       | Vector      | Vector part of the second 4-vector defining the plane                 |
| w 1         | Float       | Float part of the second 4-vector defining the plane                  |
| Angle       | Float       | Rotation angle                                                        |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Geometry    | Modifier output geometry                                              |

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

with gn.Tree(modifiers.name("Rotation 2D")) as tree:

    geo   = tree.ig

    v0    = gn.Vector.Input(0, "xyz 0")
    w0    = gn.Float.Input(0, "w 0")
    v1    = gn.Vector.Input(0, "xyz 1")
    w1    = gn.Float.Input(0, "w 1")
    angle = gn.Float.Angle(0, "Angle")

    # ----- All

    with tree.layout("All points rotation"):

        node = maths.rotation_2D(
                    xyz  = geo.points.position,
                    w    = geo.points.get_named_float("w"))

        node.plug_node(tree.group_input)

        geo.points.position = node.xyz
        geo.points.set_named_float("w", node.w)

    mesh  = geo.mesh_component
    curve = geo.curve_component
    cloud = geo.points_component
    inst  = geo.instances_component

    # ----- Mesh

    with tree.layout("Mesh"):

        node = maths.rotation_2D(
                    xyz   = mesh.verts.get_named_vector("Nxyz"),
                    w     = mesh.verts.get_named_float("Nw"))
        node.plug_node(tree.group_input)

        mesh.verts.set_named_vector("Nxyz", node.xyz)
        mesh.verts.set_named_float("Nw", node.w)

    # ----- Curve

    with tree.layout("Curve"):

        node = maths.rotation_2D(
                    xyz   = curve.points.get_named_vector("Txyz"),
                    w     = curve.points.get_named_float("Tw"))
        node.plug_node(tree.group_input)

        curve.points.set_named_vector("Txyz", node.xyz)
        curve.points.set_named_float("Tw", node.w)

    tree.og = mesh + curve + cloud + inst

```

