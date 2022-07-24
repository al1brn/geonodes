# Projection

> Projection consists in transforming 4D vertices in 3D vertices.

## Maths projection

The projection is performed by rotating the 4-vertices according 3 angles:

1. rotation in the plane XW
2. rotation in the plane YW
3. rotation in the plane ZW

Then, the resulting fourth vector along W axis is ignored.

``` python

  # Compute the full rotation matrix
  # a, b and c are the 3 rotation angle
  
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

```

The fourth vector of the rotation matrix is the direction of projection, it will be used to compute the orientation of the faces.
This fourth vector will be returned as *direction*.

The *Projection* modifier can be used on several object. To share the same parameters for all the projected objects,
we use the rotation euler of the Blender object named `Projection`.

```Python

    abc = gn.Object("Projection").rotation

    a = abc.x
    b = abc.y
    c = abc.z

```

The full code is given here after:

```python

def projection_matrix():
    
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

