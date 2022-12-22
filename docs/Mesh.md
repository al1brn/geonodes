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
- or by using a constructor such as `Cube`, `Line`, `IcoSphere`, `UVSphere`

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

### Material and shading

The example below shows how the set material on a mesh, either by using the `set_material` method of mesh or
by using the `material` property of `faces` domain.

```python
import geonodes as gn

with gn.Tree("Test") as tree:
    
    # ----- Modifier parameters

    # We read the materials given by the user
    mat1 = gn.Material.Input(None, "Base material")
    mat2 = gn.Material.Input(None, "Selection material")
    
    # Let's ask from the starting and ending indices of the face selection
    
    start = gn.Integer.Input(10, "Selection start")
    end   = gn.Integer.Input(20, "Selection end")
    
    # Shading smooth or not
    shade_smooth = gn.Boolean.Input(None,"Shade smooth")
    
    # Let's use an icosphere
    mesh = gn.Mesh.IcoSphere(subdivisions=3)
    
    # ----- Let's go
    
    # Material 1 as base material
    mesh.set_material(mat1)
    
    # Material 2 on a selection of faces
    mesh.faces[start:end].material = mat2
    
    # We smooth (or not)
    mesh.faces.shade_smooth = shade_smooth

    tree.og = mesh
```

## Extrusion

Extrusion uses `extrude` property of extrudable domains: `verts`, `faces` or `edges`. The method returns two [Boolean](Boolean.md)
which can be used to select the newly created faces.

The example below shows how to inset a selection of faces and then extrude the top faces.


```python
import geonodes as gn

with gn.Tree("Test") as tree:
    
    # ----- Modifier parameters
    
    # Let's ask from the starting and ending indices of the faces
    # to extrude
    
    start = gn.Integer.Input(10, "Extrusion start")
    end   = gn.Integer.Input(20, "Extrusion end")
    
    inset = gn.Float.Input(.5, "Inset factor", min_value=0, max_value=1)

    # ----- Let's
    
    # Let's use an icosphere
    mesh = gn.Mesh.IcoSphere(subdivisions=3)
    
    # inset: extrude with offset_scale = 0 followed by a scale
    
    # First inset
    top, side = mesh.faces[start:end].extrude(offset_scale=0)
    
    # First inset
    mesh.faces[top].scale_uniform(inset)
    
    # True extrusion
    mesh.faces[top].extrude()
    
    tree.og = mesh
```

### Boolean

The three possible boolean operations on meshes can be done using the three methods:
- `boolean_union`
- `boolean_intersect`
- `boolean_difference`

```python
import geonodes as gn

with gn.Tree("Test") as tree:
    
    # We will make the boolean with the same cylinder
    cyl, _, _, _ = gn.Mesh.Cylinder(depth=5)
    
    # ----- Union
    
    mesh1 = gn.Mesh.UVSphere(radius=2)
    mesh1.boolean_union(cyl)
    
    mesh1.transform(translation=(5, 0, 0))
    
    # ----- Intersection
    
    mesh2 = gn.Mesh.UVSphere(radius=2)
    mesh2.boolean_intersect(cyl)
    
    # ----- Difference
    
    mesh3 = gn.Mesh.UVSphere(radius=2)
    mesh3.boolean_difference(cyl)
    
    mesh3.transform(translation=(-5, 0, 0))
    
    tree.og = mesh1 + mesh2 + mesh3
```







    
    
    
    


