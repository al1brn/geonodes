# Add normals (Modifier)

> Store the normals of a mesh as named attributes.

Normals are stored as vertices named attributes:

- **Nxyz** (Vector): The vector part of the normals
- **Nw** (Float): The float part of the normals

## Sockets

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Mesh        | Modifier input geometry.                                              |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Mesh        | Modifier output geometry                                              |

## Code

``` python

with gn.Tree(modifiers.name("Add normals")) as tree:

    mesh  = gn.Mesh(tree.ig)

    # The normals

    mesh.verts.set_named_vector("Nxyz", mesh.verts.normal)
    mesh.verts.set_named_float( "Nw",   0)

    tree.og = mesh

```
