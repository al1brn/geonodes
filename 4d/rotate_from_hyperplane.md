# Rotate from Hyperplane (Maths)

> Peforms a 4-rotation such as XYZ becomes the hyperplane peprpendicular to the 4-vector passed.

**Note:** Performs the invert of *Rotate to Hyperplane*

## Sockets

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| xyz         | Vector      | Vector part of the 4-vector to rotate                                 |
| w           | Float       | Float part of the 4-vector to rotate                                  |
| Hyper xyz   | Vector      | Vector part of the 4-vector defining the hyperplane                   |
| Hyper w     | Float       | Float part of the 4-vector defining the hyperplane                    |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| xyz         | Vector      | Vector part of the rotated vector                                     |
| w           | Float       | Float part of the rotated vector                                      |

## Code

``` python

with gn.Tree(maths.name("Rotate from hyperplane"), group=True) as tree:

    v = gn.Vector.Input(0, "xyz")
    w = gn.Float.Input(0, "w")

    hv = gn.Vector.Input((0, 0, 0), "Hyper xyz")
    hw = gn.Float.Input(1, "Hyper w")

    node = maths.hyperplane(xyz=hv, w=hw)

    rv = node.xyz_0*v.x + node.xyz_1*v.y + node.xyz_2*v.z + node.xyz_3*w
    rw = node.w_0*v.x   + node.w_1*v.y   + node.w_2*v.z   + node.w_3*w

    rv.to_output("xyz")
    rw.to_output("w")

        
```

 
