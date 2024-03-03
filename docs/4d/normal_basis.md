# Normal basis (Maths)

> Computes three 4-vectors forming a normal basis in the 3D space defined by hree input 4-vectors.

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
| xyz 0       | Vector      | Vector part of first vector of the basis                              |
| w 0         | Float       | Float part of first vector of the basis                               |
| xyz 1       | Vector      | Vector part of second vector of the basis                             |
| w 1         | Float       | Float part of second vector of the basis                              |
| xyz 2       | Vector      | Vector part of third vector of the basis                              |
| w 2         | Float       | Float part of third vector of the basis                               |
| Error       | Boolean     | True if the input 4-vectors don't define a 3D space                   |

## Code

``` python

with gn.Tree(maths.name("Normal basis"), group=True) as tree:

    u0 = gn.Vector.Input((1, 0, 0), "xyz 0")
    w0 = gn.Float.Input(0, "w 0")
    u1 = gn.Vector.Input((0, 1, 0), "xyz 1")
    w1 = gn.Float.Input(0, "w 1")
    u2 = gn.Vector.Input((0, 0, 1), "xyz 2")
    w2 = gn.Float.Input(0, "w 2")

    # ----- Let's normalize the first input

    with tree.layout("Normalize entry"):

        node = maths.normalize(xyz=u0, w=w0)
        e0   = node.xyz
        t0   = node.w
        null = gn.Boolean(node.null)

    # ----- (e0, t0) is the first vector
    # Let's suppress this dimension in the second one

    with tree.layout("Make the second vector perp to the first"):

        #d   = e0.dot(u1) + t0*w1
        d   = gen_dot(tree, e0, t0, u1, w1)
        u1 -= e0*d
        w1 -= t0*d

        # ----- Let's normalize

        node = maths.normalize(xyz=u1, w=w1)
        e1   = node.xyz
        t1   = node.w
        null = null.b_or(node.null)

    with tree.layout("Make the third vector perp to the two other ones"):

        # ----- (e0, t0) and (e1, t1) are two basis vectors
        # Let's suppress these dimensions in the third one

        #d = e0.dot(u2) + t0*w2
        d   = gen_dot(tree, e0, t0, u2, w2)
        u2 -= e0*d
        w2 -= t0*d

        #d = e1.dot(u2) + t1*w2
        d   = gen_dot(tree, e1, t1, u2, w2)
        u2 -= e1*d
        w2 -= t1*d

        # ----- Let's normalize

        node = maths.normalize(xyz=u2, w=w2)
        e2   = node.xyz
        t2   = node.w
        null = null.b_or(node.null)

    # ----- We are done :-)

    e0.to_output("xyz 0")
    t0.to_output("w 0")
    e1.to_output("xyz 1")
    t1.to_output("w 1")
    e2.to_output("xyz 2")
    t2.to_output("w 2")

    null.to_output("Error")
        
```
   
   
