# Projection Matrix (Maths)

> Return the 4x4 projection matrix from the rotation euler of the object named *Projection*.

**Note:** The fourth row of the projection matrix is the direction of projection.
It is used to compute the orientation of the face.

## Parameters

The projection is performed by rotating the 4-vertices according 3 angles:

1. rotation in the plane XW
2. rotation in the plane YW
3. rotation in the plane ZW

Then, the resulting fourth vector along W axis is ignored.

## Sockets

### Input sockets

None (angles read from the object named *Projection*.

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Row 0 xyz   | Vector      | Vector part of the row 0                                              |
| Row 0 w     | Float       | Float part of the row 0                                               |
| Row 1 xyz   | Vector      | Vector part of the row 1                                              |
| Row 1 w     | Float       | Float part of the row 1                                               |
| Row 2 xyz   | Vector      | Vector part of the row 2                                              |
| Row 2 w     | Float       | Float part of the row 2                                               |
| Dir xyz     | Vector      | Vector part of the row 3 (direction of projection)                    |
| Dir w       | Float       | Float part of the row 3 (direction of projection)                     |

## Code

``` python

with gn.Tree(maths.name("Projection Matrix"), group=True) as tree:

    abc = gn.Object("Projection").rotation

    a = abc.x
    b = abc.y
    c = abc.z

    ca = gn.cos(a)
    sa = gn.sin(a)
    cb = gn.cos(b)
    sb = gn.sin(b)
    cc = gn.cos(c)
    sc = gn.sin(c)

    M = (
            (    ca,  0,    -sa*sc,    -sa*cc),
            (-sa*sb, cb, -ca*sb*sc, -ca*sb*cc),
            (     0,  0,        cc,       -sc),
            ( sa*cb, sb,  ca*cb*sc,  ca*cb*cc),
        )

    gn.Vector(M[0][:3]).to_output("Row 0 xyz")
    gn.Vector(M[0][ 3]).to_output("Row 0 w")
    gn.Vector(M[1][:3]).to_output("Row 1 xyz")
    gn.Vector(M[1][ 3]).to_output("Row 1 w")
    gn.Vector(M[2][:3]).to_output("Row 2 xyz")
    gn.Vector(M[2][ 3]).to_output("Row 2 w")

    gn.Vector(M[3][:3]).to_output("Dir xyz")
    gn.Vector(M[3][ 3]).to_output("Dir w")


```


