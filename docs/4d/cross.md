# Cross (Maths)

> Computes a *cross product-like* operation between three 4-vectors: return a vector perpendicular
> to the hyperplane formed by the three 4-vectors.

## Sockets


### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| xyz 0       | Vector      | Vector part of first vector                                           |
| w 0         | Float       | Float part of first vector                                            |
| xyz 1       | Vector      | Vector part of second vector                                          |
| w 1         | Float       | Float part of second vector                                           |
| xyz 2       | Vector      | Vector part of third vector                                           |
| w 2         | Float       | Float part of third vector                                            |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| xyz         | Vector      | Vector part of the result                                             |
| w           | Float       | Float part of the result                                              |
| Error       | Boolean     | True if the input 4-vectors don't define a 3D space                   |

## Code

> Note that the loop in the code generates 4 times the same nodes, one for each of the 4 axis.

``` python

with gn.Tree(maths.name("Cross"), group=True) as tree:

    # ----- Convert the three input vectors in a normal basis

    gn.Vector.Input((1, 0, 0), "xyz 0")
    gn.Float.Input(0, "w 0")
    gn.Vector.Input((0, 1, 0), "xyz 1")
    gn.Float.Input(0, "w 1")
    gn.Vector.Input((0, 0, 1), "xyz 2")
    gn.Float.Input(0, "w 2")

    node = maths.normal_basis()
    node.plug_node(tree.group_input) # xyz_i, w_i

    u0 = node.xyz_0
    w0 = node.w_0
    u1 = node.xyz_1
    w1 = node.w_1
    u2 = node.xyz_2
    w2 = node.w_2

    error = node.error

    # ----- Test the fourth basis vectors

    n3 = gn.Float(0)
    u3 = gn.Vector(0)
    w3 = gn.Float(0)
    for i in range(4):

        with tree.layout(f"Axis {i}"):

            v4 = [0] * 4
            v4[i] = 1

            u = gn.Vector(v4[:3])
            w = gn.Float(v4[3])

            d0 = u0.dot(u) + w*w0
            d1 = u1.dot(u) + w*w1
            d2 = u2.dot(u) + w*w2
            u -= d0*u0
            w -= d0*w0
            u -= d1*u1
            w -= d1*w1
            u -= d2*u2
            w -= d2*w2

            # Resulting norm

            n = maths.length(xyz=u, w=w).length

            greater = gn.Boolean(n.greater_than(n3))
            u3 = u3.switch(greater, u)
            w3 = w3.switch(greater, w)
            n3 = n3.switch(greater, n)

    # ----- Let's normalize the result

    u3 /= n3
    w3 /= n3

    u3.to_output("xyz")
    w3.to_output("w")
    error.to_output("Error")

```        
