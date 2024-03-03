# Add normals (Modifier)

> Store the normals of a mesh as named attributes.

## Sockets & attributes

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Mesh        | Modifier input geometry                                              |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Mesh        | Modifier output geometry                                              |

### Named attributes

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Nxyz        | Vector      | Vector part of the normals                                            |
| Nw          | Float       | Float part of the normals                                             |



## Code

``` python

with gn.Tree(modifiers.name("Add normals")) as tree:

    mesh  = gn.Mesh(tree.ig)

    # The normals

    mesh.verts.set_named_vector("Nxyz", mesh.verts.normal)
    mesh.verts.set_named_float( "Nw",   0)

    tree.og = mesh

```
