# Build along curve (Maths)

> Duplicates a geometry along a given curve.

**Note 1:** Both the geometry to duplicate and the curve must be 4D geometries.

**Note 2:** The geometry is duplicated as many times there are points in the curve.

**Note 3:** The geometry is oriented along the curve using [Follow vector](follow_vector.md) with the curve tangent.

**Note 4:** See [Hypersphere](hypersphere.md) for an example of use.

## Sockets

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry 4D | Geometry    | Geometry to duplicate along the curve                                 |
| Curve 4D    | Curve       | The curve used as backbone to duplicate the geometry                  |
| Align xyz   | Vector      | Vector part of the 4-vector to align with the curve tangent           |
| Align w     | Float       | Float part of the 4-vector to align with the curve tangent            |
| Use radius  | Boolean     | If True, scale the geometry using the curve radius as scale           |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Geometry    | The resulting geometry                                                |

## Code

``` python

with gn.Tree(maths.name("Build along curve"), group=True) as tree:

    geo        = gn.Geometry.Input("Geometry 4D")
    curve      = gn.Curve.Input("Curve 4D")
    align_v    = gn.Vector.Input((0, 0, 1), "Align xyz")
    align_w    = gn.Float.Input(0, "Align w")
    use_radius = gn.Boolean.Input(False, "Use radius")

    # Instantiate along the curve

    instances = gn.Points(curve).instance_on_points(instance=geo)

    # Instances 4D coordinates

    with tree.layout("Instances curve w coordinate"):

        insts = instances.insts
        #v     = insts.position
        w     = curve.points.index_transfer(curve.points.get_named_float("w"))
        insts.set_named_float("curve w", w)

        # ----- Scale with radius

        scale = curve.points.index_transfer(gn.Float(1).switch(use_radius, curve.points.radius))
        insts.scale(scale=scale)


    with tree.layout("Store curve tangent and point location for further rotation"):

        insts = instances.insts

        insts.set_named_vector("pivot xyz", insts.position)
        insts.set_named_float("pivot w", w)

        Txyz = curve.points.index_transfer(curve.points.get_named_vector("Txyz"))
        Tw   = curve.points.index_transfer(curve.points.get_named_float("Tw"))

        insts.set_named_vector("curve Txyz", Txyz)
        insts.set_named_float("curve Tw", Tw)

    # ----- Realize instances

    geo = instances.realize()

    with tree.layout("Set the vertices in 4D space"):

        # ----- w coordinate

        geo.points.set_named_float("w", geo.points.get_named_float("w") + geo.points.get_named_float("curve w"))
        geo.remove_named_attribute("curve w")

        # ----- Rotation

        v = geo.points.position
        w = geo.points.get_named_attribute("w")

        pv = geo.points.get_named_vector("pivot xyz")
        pw = geo.points.get_named_float("pivot w")

        rv = geo.points.get_named_vector("curve Txyz")
        rw = geo.points.get_named_float("curve Tw")

        # ----- Points location

        with tree.layout("Points location"):

            node = maths.follow_vector(
                xyz   = v - pv,
                w     = w - pw,
                a_xyz = align_v,
                a_w   = align_w,
                b_xyz = rv,
                b_w   = rw,
                )

            geo.points.position = pv + node.xyz
            geo.points.set_named_float("w", pw + node.w)

        mesh  = geo.mesh_component
        curve = geo.curve_component
        cloud = geo.points_component
        inst  = geo.instances_component

        # ----- Normals

        with tree.layout("Normals"):

            node = maths.follow_vector(
                xyz   = mesh.verts.get_named_vector("Nxyz"),
                w     = mesh.verts.get_named_float("Nw"),
                a_xyz = align_v,
                a_w   = align_w,
                b_xyz = rv,
                b_w   = rw,
                )

            mesh.verts.set_named_vector("Nxyz", node.xyz)
            mesh.verts.set_named_float("Nw",     node.w)


        # ----- Curves tangents

        with tree.layout("Curves tangents"):

            node = maths.follow_vector(
                xyz   = curve.points.get_named_vector("Txyz"),
                w     = curve.points.get_named_float("Tw"),
                a_xyz = align_v,
                a_w   = align_w,
                b_xyz = rv,
                b_w   = rw,
                )

            curve.points.set_named_vector("Txyz", node.xyz)
            curve.points.set_named_float("Tw",    node.w)

        # ----- Remove the named attributes

        geo.remove_named_attribute("pivot xyz")
        geo.remove_named_attribute("pivot w")
        geo.remove_named_attribute("curve Txyz")
        geo.remove_named_attribute("curve Tw")


    tree.og = mesh + curve + cloud + inst

```


