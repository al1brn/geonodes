# Axis (Modifier)

> Build the projected four axis.

**Note:** Used to easily visualize the space axis.

## Sockets

### Input sockets

| Name         | Type        | Description                                                           |
| ------------ | ----------- | --------------------------------------------------------------------- |
| Geometry     | Geometry    | Modifier input geometry (unused)                                      |
| Negative     | Float       | Distance to start the axis from                                       |
| Positive     | Float       | Distance where to end the axis                                        |
| Radius       | Float       | Axis radius                                                           |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Mesh        | Modifier output geometry                                              |

## Code

``` python

with gn.Tree(modifiers.name("Axis")) as tree:

    neg = gn.Float.Input(-1, "Negative", max_value=0.)
    pos = gn.Float.Input( 3, "Positive", min_value=0.)
    radius = gn.Float.Input(0.05, "Radius")

    lines  = gn.Curve.Line() * 4
    lines.points[0].position = gn.Vector((neg, 0, 0))
    lines.points[1].position = gn.Vector((pos, 0, 0))
    lines.points[2].position = gn.Vector((0, neg, 0))
    lines.points[3].position = gn.Vector((0, pos, 0))
    lines.points[4].position = gn.Vector((0, 0, neg))
    lines.points[5].position = gn.Vector((0, 0, pos))        
    lines.points[6].position = gn.Vector((0, 0, 0))
    lines.points[7].position = gn.Vector((0, 0, 0))

    # Use tilt as w

    lines.points[6].tilt = neg
    lines.points[7].tilt = pos

    tree.view(lines, lines.points.tilt)

    # Projection

    #lines.points.position = tree.call("G4D Coordinates projection", xyz=lines.points.position, w=lines.points.tilt).vector
    lines.points.position = maths.projection(xyz=lines.points.position, w=lines.points.tilt).vector

    # Reset tilt

    lines.points.tilt = 0

    # Some thickness

    mesh = lines.to_mesh(profile_curve=gn.Curve.Circle(resolution=12, radius=radius).curve, fill_caps=True)

    # The arrows

    cones = gn.Mesh.Cone(vertices=12, depth=3).mesh.duplicate(8, realize=False)
    cones.insts.scale(scale=radius*6)
    cones.insts.position = lines.points.position.index_transfer()

    # Delete one on two: 4 cones remaining

    cones.insts((cones.insts.index % 2).equal(0)).delete()

    # Lines to edges to get the directions

    edges = lines.to_mesh()

    # The 4 edges give fours direction

    p0, p1 = edges.edges.vertex_position
    #p0 = p0.index_transfer()
    #p1 = p1.index_transfer()

    rot = gn.Vector((0, 0, 1)).align_to_vector(axis='Z', vector=p1-p0)
    rot = edges.edges.transfer_attribute(attribute=rot, mapping='INDEX')

    cones.rotate(rotation=rot)
    mesh = gn.Mesh(mesh + cones.realize())

    mati = mesh.faces.island_index % 4 

    mesh.faces(mati.equal(0)).set_material(material="Red")
    mesh.faces(mati.equal(1)).set_material(material="Green")
    mesh.faces(mati.equal(2)).set_material(material="Blue")
    mesh.faces(mati.equal(3)).set_material(material="Black")

    mesh.set_shade_smooth()
    tree.og = mesh 

```

