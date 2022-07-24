# Light (Modifier)

> Compute the 4D ligthening of a mesh from a 4D object passed in parameter.

**Note:** The light is given as a node output socket. It can be named and used in the shader.

## Sockets

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Geometry    | Modifier input geometry                                               |
| Light       | Object      | A object with a geometry plunged in 4D consired as source of light    |
| Intensity   | Float       | Intensity of the light                                                |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Mesh        | Modifier output geometry                                              |
| Light       | Float       | The enlightment of vertices                                           |

## Code

``` python

with gn.Tree(modifiers.name("Light")) as tree:

    geo = gn.Mesh(tree.ig)
    obj = gn.Object.Input("Light")
    its = gn.Float.Input(1, "Intensity")

    with tree.layout("Light location"):

        pts     = obj.geometry.points
        light_v = pts.statistic(pts.position).mean
        light_w = pts.statistic(pts.get_named_float("w")).mean

    # ---- Incident vector

    with tree.layout("Incident vector"):

        v = geo.verts.position - light_v
        w = geo.verts.get_named_float("w") - light_w

        node = maths.normalize(xyz=v, w=w)
        v    = node.xyz
        w    = node.w

    # ----- Normal

    with tree.layout("Normal vector"):

        nv = geo.verts.get_named_vector("Nxyz")
        nw = geo.verts.get_named_float("Nw")

    # ----- Dot product

    with tree.layout("Dot product of the two vectors"):

        light = its*(nv.dot(v) + nw*w)

    # ----- Done

    tree.og = geo

    light.to_output("Light")

```

