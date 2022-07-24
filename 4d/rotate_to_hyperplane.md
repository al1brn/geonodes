# Rotate to Hyperplane (Maths)

> Peforms a 4-rotation such as the hyperplane peprpendicular to the 4-vector passes in parameter becomes XYZ.

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

with gn.Tree(maths.name("Rotate to hyperplane"), group=True) as tree:

    v = gn.Vector.Input(0, "xyz")
    w = gn.Float.Input(0, "w")

    hv = gn.Vector.Input((0, 0, 0), "Hyper xyz")
    hw = gn.Float.Input(1, "Hyper w")

    node = maths.hyperplane(xyz=hv, w=hw)

    x = node.xyz_0.dot(v) + node.w_0*w
    y = node.xyz_1.dot(v) + node.w_1*w
    z = node.xyz_2.dot(v) + node.w_2*w
    w = node.xyz_3.dot(v) + node.w_3*w

    gn.Vector((x, y, z)).to_output("xyz")
    w.to_output("w")
        
```

 
