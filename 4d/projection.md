# Projection (Maths)

> Project a 4-vector in the 3D space XYZ.

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

## Projection matrix

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

## Projection

The projection matrix is used in the maths projection computation:

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

## Modifier projection

The modifier uses the maths projection to:

- Project the vertices
- Project the faces normals
- Project the curves tangents
- Compute the orientation of the faces

``` python

with gn.Tree(modifiers.name("Projection")) as tree:

    geo = tree.ig

    # ----- All

    with tree.layout("All points projection"):

        v = geo.points.position
        w = geo.points.get_named_float("w")

        geo.points.position = maths.projection(xyz=v, w=w).vector

    # ----- Components

    mesh  = geo.mesh_component
    curve = geo.curve_component
    cloud = geo.points_component
    inst  = geo.instances_component

    with tree.layout("Mesh projection"):

        with tree.layout("Normals projection"):

            v = mesh.verts.get_named_vector("Nxyz")
            w = mesh.verts.get_named_float("Nw")

            N = maths.projection(xyz=v, w=w).vector

            mesh.verts.set_named_vector("N", N)

        with tree.layout("Back face"):

            mproj = maths.projection_matrix()

            node = maths.projection(xyz=0, w=1)
            mesh.verts.set_named_float("orientation", modifiers.dot_normal(geometry=mesh, xyz=mproj.dir_xyz, w=mproj.dir_w).dot)

        mesh = mesh.switch(gn.Boolean.Input(True, "Shade smooth"), mesh.set_shade_smooth())

    with tree.layout("Curve projection"):

        with tree.layout("Tangents projection"):

            v = curve.points.get_named_vector("Txyz")
            w = curve.points.get_named_float("Tw")

            curve.points.set_named_vector("T", maths.projection(xyz=v, w=w).vector)

    tree.og = mesh + curve + cloud + inst

```

                
                
                
