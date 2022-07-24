# Hyperplane (Maths)

> Computes the three 4-vectors forming a normal basis of the hyperplane perpendicular to a 4-vector.

## Sockets

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| xyz         | Vector      | Vector part of the 4-vector                                           |
| w           | Float       | Float part of the 4-vector                                            |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| xyz 0       | Vector      | Vector part of first vector of the basis                              |
| w 0         | Float       | Float part of first vector of the basis                               |
| xyz 1       | Vector      | Vector part of second vector of the basis                             |
| w 1         | Float       | Float part of second vector of the basis                              |
| xyz 2       | Vector      | Vector part of third vector of the basis                              |
| w 2         | Float       | Float part of third vector of the basis                               |
| xyz 3       | Vector      | Vector part of fourth vector of the basis                              |
| w 3         | Float       | Float part of fourth vector of the basis                               |

**Note:** The fourth 4-vector (xyz 3, w 3) is the normal 4-vector in the direction of the input vector.

## Code

``` python

    with gn.Tree(maths.name("Hyperplane"), group=True) as tree:
        
        v = gn.Vector.Input((0, 0, 0), "xyz")
        w = gn.Float.Input(1, "w")
        
        # ----- Normalize the entry
        
        node = maths.normalize(xyz=v, w=w)
        v    = node.xyz
        w    = node.w
        
        # ----- Try to build a 3D-base with v and plane (k, l)
        
        node = maths.normal_basis(
            xyz_0 = v,
            w_0   = w,
            xyz_1 = (0, 0, 1),
            w_1   = 0,
            xyz_2 = (0, 0, 0),
            w_2   = 1)
            
        u0 = node.xyz_1
        w0 = node.w_1
        u1 = node.xyz_2
        w1 = node.w_2
        
        error = node.error
        
        # ---------------------------------------------------------------------------
        # If error, it does mean that v is in plane (k, l), hence (i, j) is perp to v
        
        node = maths.cross(
            xyz_0 = v,
            w_0   = w,
            xyz_1 = (1, 0, 0),
            w_1   = 0,
            xyz_2 = (0, 1, 0),
            w_2   = 0,
            )
            
        e_u2 = node.xyz
        e_w2 = node.w
        
        # ---------------------------------------------------------------------------
        # If no error, we have (u0, u1) perp to input vector
        # The third basis vector is perpendicular to these 3 vectors
        
        node = maths.cross(
            xyz_0 = v,
            w_0   = w,
            xyz_1 = u0,
            w_1   = w0,
            xyz_2 = u1,
            w_2   = w1,
            )

        u0 = u0.switch(error, (1, 0, 0))
        w0 = w0.switch(error, 0)
        u1 = u1.switch(error, (0, 1, 0))
        w1 = w1.switch(error, 0)
        u2 = node.xyz.switch(error, e_u2)
        w2 = node.w.switch(error, e_w2)
        
        # ----- Done
        
        u0.to_output("xyz 0")
        w0.to_output("w 0")

        u1.to_output("xyz 1")
        w1.to_output("w 1")
            
        u2.to_output("xyz 2")
        w2.to_output("w 2")
        
        v.to_output("xyz 3")
        w.to_output("w 3")
        
```        
