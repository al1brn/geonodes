# Mesh

Mesh is a subclass of [Geometry](Geometry.md).

Use Mesh type to access methods specific to meshes.

A Mesh has four [domains](domain.md):
- `verts` of type [Vertex](Vertex.md)
- `edges` of type [Edge](Edge.md)
- `faces` of type [Face](Face.md)
- `corners` of type [Corner](Corner.md)

## Initialization

A Mesh can be initialized:
- by typecasting another geometry
- or by using a constructor

```python
import geonodes as gn

with gn.Tree("Test") as tree:

    # Typecasting the tree input geometry
    
    mesh = gn.Mesh(tree.ig)
    
    # We create a cube
    
    cube = gn.Mesh.Cube()
    cube.set_position(offset=(0, 0, 2))
    
    # We return the two meshes
    
    tree.og = mesh + cube
```

## Examples

### Vertices position

The vertices position is given by the property `position` of domain `verts`: `mesh.verts.position`.
To change the position of a selection of vertices, use the list syntax on the `verts` property: `mesh.verts[selection]`.

```python
import geonodes as gn

with gn.Tree("Test") as tree:
    
    sphere = gn.Mesh.IcoSphere(radius=2, subdivisions=3)
    
    # Offset position
    sphere.verts[(sphere.verts.index % 5).equal(0)].position += (0, 0, 1)
    
    # Absolute position
    v = sphere.verts.position
    v.z = -3
    sphere.verts[10:20].position = v
    
    tree.og = sphere
```



    
    
    
    


