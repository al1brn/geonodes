# Dot normal

> Utility that compute the dot product between a 4-vector and the normals.

## Sockets & attributes

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Mesh        | Modifier input geometry                                               |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Mesh        | Modifier output geometry                                              |
| Dot         | Float       | The dot product                                                       |

### Named attributes

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Orientation | Vector      | Vector part of the normals                                            |
| Nw          | Float       | Float part of the normals                                             |



## Code

``` python

with gn.Tree(modifiers.name("Dot normal")) as tree:

    mesh  = gn.Mesh(tree.ig)

    Vxyz  = gn.Vector.Input(0, "xyz")
    Vw    = gn.Float.Input(1,  "w")

    v = mesh.verts.get_named_vector("Nxyz")
    w = mesh.verts.get_named_float("Nw")

    (v.dot(Vxyz) + w*Vw).to_output("Dot")

    tree.og = mesh
    
```  
