# Rotate in Hyperplane (Maths)

> Peforms a 3-rotation within the hyperplane defined by a 4-vector.

**Note 1:** This node uses *Rotate to Hyperplane* and *Rotate from Hyperplane*. The 3-rotation is performend between
these two calls.

**Note 2:** The 3-rotation can be defined either by an Euler or by a couple (Axis, Angle). If both are defined, Euler
is performed first.

## Sockets

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| xyz         | Vector      | Vector part of the 4-vector to rotate                                 |
| w           | Float       | Float part of the 4-vector to rotate                                  |
| Hyper xyz   | Vector      | Vector part of the 4-vector defining the hyperplane                   |
| Hyper w     | Float       | Float part of the 4-vector defining the hyperplane                    |
| Euler       | Euler       | Euler XYZ 3-rotation to perform                                       |
| Axis        | Vector      | 3-vector for (axis, angle) rotation                                   |
| Angle       | Float       | Angle for (axis, angle) rotation                                      |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| xyz         | Vector      | Vector part of the rotated vector                                     |
| w           | Float       | Float part of the rotated vector                                      |

## Code

``` python

with gn.Tree(maths.name("Rotate in hyperplane"), group=True):

    v = gn.Vector.Input(0, "xyz")
    w = gn.Float.Input(0, "w")

    hv    = gn.Vector.Input((0, 0, 0), "Hyper xyz")
    hw    = gn.Float.Input(1, "Hyper w")
    euler = gn.Vector.Rotation((0, 0, 0), "Euler")
    axis  = gn.Vector.Input((0, 0, 1), "Axis")
    angle = gn.Float.Angle(0, "Angle")

    to_hp = maths.rotate_to_hyperplane(
        xyz       = v,
        w         = w,
        hyper_xyz = hv,
        hyper_w   = hw,
    )

    v = to_hp.xyz
    w = to_hp.w

    v = v.rotate(rotation=euler, rotation_type='EULER_XYZ')
    v = v.rotate(axis=axis, angle=angle, rotation_type='AXIS_ANGLE')

    from_hp = maths.rotate_from_hyperplane(
        xyz       = v,
        w         = w,
        hyper_xyz = hv,
        hyper_w   = hw,
    )

    from_hp.xyz.to_output("xyz")
    from_hp.w.to_output("w")
        
```

 
