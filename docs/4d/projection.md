# Projection (Maths)

> Project a 4-vector in the 3D space XYZ.

**Note 1:** The projection must be the last modifier of a 4D project.

**Note 2:** The projection calls the [Projection Matrix](projection_matrix.md).

## Sockets

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| xyz         | Vector      | Vector part of the 4-vector                                           |
| w           | Float       | Float part of the 4-vector                                            |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Vector      | Vector      | The projected 3-vector                                                |

## Code

``` python

with gn.Tree(maths.name("Projection"), group=True) as tree:

    v = gn.Vector.Input(0, "xyz")
    w = gn.Float.Input(0, "w")

    mproj = maths.projection_matrix()

    mv0 = mproj.row_0_xyz
    mw0 = mproj.row_0_w
    mv1 = mproj.row_1_xyz
    mw1 = mproj.row_1_w
    mv2 = mproj.row_2_xyz
    mw2 = mproj.row_2_w

    x = mv0.dot(v) + mw0*w
    y = mv1.dot(v) + mw1*w
    z = mv2.dot(v) + mw2*w

    gn.Vector((x, y, z)).to_output("Vector")

``` 
          
                
                
