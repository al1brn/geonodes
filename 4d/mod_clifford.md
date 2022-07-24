# Clifford torus (Modifier)

> Build a Clifford torus..

**Note 1:** The input geometry is unused.

**Note 2:** An UVMap is built.

## Sockets & attributes

### Input sockets

| Name         | Type        | Description                                                           |
| ------------ | ----------- | --------------------------------------------------------------------- |
| Geometry     | Geometry    | Modifier input geometry (unused)                                      |
| Segments     | Integer     | Number of segments                                                    |
| Rings        | Integer     | Number of rings                                                       |
| Major radius | Float       | Major radius                                                          |
| Minor radius | Float       | Minor radius                                                          |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Mesh        | Modifier output geometry                                              |

### Named attributes

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| w           | Float       | The fourth dimension                                                  |
| Txyz        | Vector      | Vector part of the tangents                                           |
| Tw          | Float       | Float part of the tangents                                           |


## Code

``` python

with gn.Tree(modifiers.name("Clifford torus")) as tree:

    segms = gn.Integer.Input(32,  "Segments",     min_value=3)
    rings = gn.Integer.Input(16,  "Rings",        min_value=4)
    R     = gn.Float.Input(1.,   "Major radius", min_value=0.01)
    r     = gn.Float.Input(0.25, "Minor radius", min_value=0.0025)

    with tree.layout("Base torus"):

        major = gn.Curve.Circle(resolution=rings, radius=R).curve
        minor = gn.Curve.Circle(resolution=segms, radius=r).curve

        u = major.points.parameter_factor
        v = minor.points.parameter_factor

        gn.Vector((u, v, 0)).to_output("UVMap")


        torus = major.to_mesh(profile_curve=minor)

    with tree.layout("New coordinates of the vertices"):

        verts = torus.verts

        maj_ag = (verts.index / segms).floor()/rings * (2*gn.pi)
        min_ag = (verts.index % segms)/segms * (2*gn.pi)

        x = R*maj_ag.cos()
        y = r*min_ag.cos()
        z = r*min_ag.sin()
        w = R*maj_ag.sin()

        v = gn.Vector((x, y, z))

        verts.position = v
        verts.set_named_float("w", w)

    # Normals are computed on vertices

    with tree.layout("Normals"):

        n = (x*x + y*y + z*z + w*w).sqrt()

        verts.set_named_vector(name="Nxyz", value=gn.Vector((x/n, y/n, z/n)))
        verts.set_named_float(name="Nw", value=w/n)

    torus.set_material(material=gn.Material.Input("Material"))


    tree.og = torus

```

