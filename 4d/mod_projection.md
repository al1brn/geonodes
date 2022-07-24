# Projection (Modifier)

> Project a 4D geometry into the 3D XYZ space. See [Projection (Maths)](projection.md).

## Sockets & attributes

### Input sockets

| Name         | Type        | Description                                                           |
| ------------ | ----------- | --------------------------------------------------------------------- |
| Geometry     | Geometry    | Modifier input geometry                                               |
| Shade smooth | Boolean     | Shade smooth or not the result                                        |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Mesh        | Modifier output geometry                                              |

### Named attributes

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| N           | Vector      | Projected normals                                                     |
| Orientation | Float       | Dot product of the normals with the direction of projection           |

## Code

``` python

with gn.Tree(modifiers.name("Projection")) as tree:

    geo          = tree.ig
    shade_smooth = gn.Boolean.Input(True, "Shade smooth")


    # ----- All

    with tree.layout("All points projection"):

        v = geo.points.position
        w = geo.points.get_named_float("w")

        geo.points.position = maths.projection(xyz=v, w=w).vector

    # ----- Components

    mesh  = geo.mesh_component
    curve = geo.curve_component
    cloud = geo.points_component
    inst  = geo.instances_component

    with tree.layout("Mesh projection"):

        with tree.layout("Normals projection"):

            v = mesh.verts.get_named_vector("Nxyz")
            w = mesh.verts.get_named_float("Nw")

            N = maths.projection(xyz=v, w=w).vector

            mesh.verts.set_named_vector("N", N)

        with tree.layout("Back face"):

            mproj = maths.projection_matrix()

            node = maths.projection(xyz=0, w=1)
            mesh.verts.set_named_float("orientation", modifiers.dot_normal(geometry=mesh, xyz=mproj.dir_xyz, w=mproj.dir_w).dot)

        mesh = mesh.switch(shade_smooth, mesh.set_shade_smooth())

    with tree.layout("Curve projection"):

        with tree.layout("Tangents projection"):

            v = curve.points.get_named_vector("Txyz")
            w = curve.points.get_named_float("Tw")

            curve.points.set_named_vector("T", maths.projection(xyz=v, w=w).vector)

    tree.og = mesh + curve + cloud + inst



```
