# W Plane Rotation (Maths)

> Rotate a 4-vector in a plane containing the W axis.

## Sockets

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| xyz         | Vector      | Vector part of the 4-vector to rotate                                 |
| w           | Float       | Float part of the 4-vector to rotate                                  |
| Axis        | Integer     | Axis number: 0 for X, 1 for Y, 2 for Z                                |
| Angle       | Float       | Rotation angle                                                        |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| xyz         | Vector      | Vector part of the rotated vector                                     |
| w           | Float       | Float part of the rotated vector                                      |

## Code

``` python

with gn.Tree(maths.name("W plane rotation"), group=True) as tree:

    v     = gn.Vector.Input(0, "xyz")
    w     = gn.Float.Input(0, "w")
    axis  = gn.Integer.Input(0, "Axis", min_value=0, max_value=2)
    angle = gn.Float.Angle(0, "Angle")

    # w is mapped on x
    # select y based on axis value

    with tree.layout("Axis on y component"):

        y = v.y.switch(axis.equal(0), v.x).switch(axis.equal(2), v.z)

    with tree.layout("Rotation around z"): 

        # rotation around z axis

        r = gn.Vector((w, y, 0)).rotate(axis=(0, 0, 1), angle=angle)

    with tree.layout("y result on axis, x result on w"):

        # Returns the result

        gn.Vector((v.x.switch(axis.equal(0), r.y),
                   v.y.switch(axis.equal(1), r.y),
                   v.z.switch(axis.equal(2), r.y)) ).to_output("xyz")

        r.x.to_output("w")

        
```

 
