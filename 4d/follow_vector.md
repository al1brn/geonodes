# Follow vector (Maths)

> Rotate a 4-vector to another one.

**Note 1:** This is a planar rotation in the plane defined by the two vectors.

**Note 2:** Called by the modifier *Build along Curve* to orient the base shape along the tangent ofthe curve.

## Sockets

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| xyz         | Vector      | Vector part of the 4-vector to rotate                                 |
| w           | Float       | Float part of the 4-vector to rotate                                  |
| A xyz       | Vector      | Vector part of the first 4-vector                                     |
| A w         | Float       | Float part of the first 4-vector                                      |
| B xyz       | Vector      | Vector part of the second 4-vector                                    |
| B w         | Float       | Float part of the second 4-vector                                     |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| xyz         | Vector      | Vector part of the rotated vector                                     |
| w           | Float       | Float part of the rotated vector                                      |

## Code

``` python

with gn.Tree(maths.name("Follow vector"), group=True) as tree:

    v = gn.Vector.Input(0, "xyz")
    w = gn.Float.Input(0, "w")

    va = gn.Vector.Input(0, "A xyz")
    wa = gn.Float.Input(1, "A w")
    vb = gn.Vector.Input(0, "B xyz")
    wb = gn.Float.Input(1, "B w")

    # ----- Create a normalized basis in the plane (a, b)

    with tree.layout("e0 = Basis first vector aligned on A"):

        xa = maths.length(xyz=va, w=wa).length

        null = xa.less_than(zero)
        e0 = va / xa
        t0 = wa / xa

    with tree.layout("e1 = Basis second vector: B - (B.e0).e0"):

        xb = e0.dot(vb) + t0*wb
        e1 = vb - e0*xb
        t1 = wb - t0*xb
        yb = maths.length(xyz=e1, w=t1).length

        null = null + yb.less_than(zero)
        e1 /= yb
        t1 /= yb

        # If vector are colinear, they can be opposite

        opposite = xb.less_than(0) 

    # ----- Compute the angle, cosine and sine

    with tree.layout("Compute the rotation cosine and sine"):

        ag = gn.arctan2(yb, xb)
        ag.node.label = "Rotation angle"
        ca = gn.cos(ag)
        sa = gn.sin(ag)

    # ----- Component of v on (e0, e1)

    with tree.layout("Components (xv, yv) on (e0, e1)"):

        xv = e0.dot(v) + t0*w
        yv = e1.dot(v) + t1*w

        xv.node.label = "xv"
        yv.node.label = "yv"

    # ----- Part out of the rotation plane

    with tree.layout("Part out of the rotation plane"):

        v3 = v - xv*e0 - yv*e1
        w3 = w - xv*t0 - yv*t1

    # ----- Rotate in the plane

    with tree.layout("Rotated coordinates"):

        fac0 = xv*ca - yv*sa
        fac1 = xv*sa + yv*ca

    # ----- Build the rotated vector

    with tree.layout("Build the resulting vector"):

        rv = v3 + fac0*e0 + fac1*e1
        rw = w3 + fac0*t0 + fac1*t1

    with tree.layout("No rotation if null"):

        rv = rv.switch(null, v.switch(opposite, -v))
        rw = rw.switch(null, w.switch(opposite, -w))

    rv.to_output("xyz")
    rw.to_output("w")
        
```

 
