# Dot normal

> Utility that compute the dot product between a 4-vector and the normals.

## Sockets

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Mesh        | Modifier input geometry                                               |
| xyz         | Vector      | Vector part of the 4-vector                                           |
| w           | Float       | Float part of the 4-vector                                            |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Mesh        | Modifier output geometry                                              |
| Dot         | Float       | The dot product                                                       |


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
