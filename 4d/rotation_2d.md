# Rotation 2D (Maths)

> Rotate a 4-vector in a plane defined by two 4-vectors

## Sockets

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| xyz         | Vector      | Vector part of the 4-vector to rotate                                 |
| w           | Float       | Float part of the 4-vector to rotate                                  |
| xyz 0       | Vector      | Vector part of the first 4-vector defining the plane                  |
| w 0         | Float       | Float part of the first 4-vector defining the plane                   |
| xyz 1       | Vector      | Vector part of the second 4-vector defining the plane                 |
| w 1         | Float       | Float part of the second 4-vector defining the plane                  |
| Angle       | Float       | Rotation angle                                                        |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| xyz         | Vector      | Vector part of the rotated vector                                     |
| w           | Float       | Float part of the rotated vector                                      |

## Code

``` python

with gn.Tree(maths.name("Rotation 2D"), group=True) as tree:

    with tree.layout("Normalize vector 0"):

        v0 = gn.Vector.Input(0, "xyz 0")
        w0 = gn.Float.Input(1, "w 0")

        n = gn.sqrt(v0.x*v0.x + v0.y*v0.y + v0.z*v0.z + w0*w0)
        v0 = v0/n
        w0 = w0/n

    with tree.layout("Build second vector orthogonally"):

        v1 = gn.Vector.Input((1, 0, 0), "xyz 1")
        w1 = gn.Float.Input(0, "w 1")

        d = v0.dot(v1) + w0*w1

        v1 = v1 - v0*d
        w1 = w1 - w0*d

    with tree.layout("Normalize second vector"):

        n = gn.sqrt(v1.x*v1.x + v1.y*v1.y + v1.z*v1.z + w1*w1)
        v1 = v1/n
        w1 = w1/n

    with tree.layout("Rotation V0 towards V1"):

        a = gn.Float.Angle(0, "Angle", description="Rotation angle in plane (V0, V1)")

        v = gn.Vector.Input(0, "xyz")
        w = gn.Float.Input(0, "w")

        # ----- Components in plane (V0, V1)

        x = v0.dot(v) + w0*w
        y = v1.dot(v) + w1*w

        # ----- Rotation

        c = a.cos() - 1
        s = a.sin()

        # ----- Rotated components

        xp =  c*x - s*y
        yp =  s*x + c*y

        # ----- Resulting vector
        # V = V - P01 components + P01 rotated components

        rv = v + xp*v0 + yp*v1
        rw = w + xp*w0 + yp*w1

    rv.to_output("xyz")
    rw.to_output("w")
        
```

 
