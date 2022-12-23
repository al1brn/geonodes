# class Mesh

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

**Mesh** is a subclass of [Geometry](Geometry.md).

Use **Mesh** type to access methods specific to meshes.

A **Mesh** has four [domains](domain.md):
- `verts` of type [Vertex](Vertex.md)
- `edges` of type [Edge](Edge.md)
- `faces` of type [Face](Face.md)
- `corners` of type [Corner](Corner.md)

> see [examples](#examples)

## Properties

- [corner_count](#corner_count-property)
- [domain_size](#domain_size-property)
- [edge_count](#edge_count-property)
- [face_count](#face_count-property)
- [island](#island-property)
- [island_count](#island_count-property)
- [island_index](#island_index-property)
- [point_count](#point_count-property)

## Class methods

- [Circle](#Circle-classmethod)
- [Cube](#Cube-classmethod)
- [Grid](#Grid-classmethod)
- [IcoSphere](#IcoSphere-classmethod)
- [Line](#Line-classmethod)
- [LineEndPoints](#LineEndPoints-classmethod)
- [LineEndPointsResolution](#LineEndPointsResolution-classmethod)
- [LineOffset](#LineOffset-classmethod)
- [LineOffsetResolution](#LineOffsetResolution-classmethod)
- [UVSphere](#UVSphere-classmethod)

## Static methods

- [Cone](#Cone-staticmethod)
- [Cylinder](#Cylinder-staticmethod)

## Methods

- [boolean_difference](#boolean_difference)
- [boolean_intersect](#boolean_intersect)
- [boolean_union](#boolean_union)
- [corners_of_face](#corners_of_face)
- [corners_of_vertex](#corners_of_vertex)
- [delete_all](#delete_all)
- [delete_edges](#delete_edges)
- [delete_faces](#delete_faces)
- [distribute_points_on_faces](#distribute_points_on_faces)
- [dual_mesh](#dual_mesh)
- [edge_paths_to_curves](#edge_paths_to_curves)
- [edge_paths_to_selection](#edge_paths_to_selection)
- [edges_of_corner](#edges_of_corner)
- [edges_of_vertex](#edges_of_vertex)
- [extrude](#extrude)
- [face_is_planar](#face_is_planar)
- [face_of_corner](#face_of_corner)
- [face_set_boundaries](#face_set_boundaries)
- [flip_faces](#flip_faces)
- [instance_on_points](#instance_on_points)
- [is_shade_smooth](#is_shade_smooth)
- [offset_corner_in_face](#offset_corner_in_face)
- [pack_uv_islands](#pack_uv_islands)
- [sample_nearest_surface](#sample_nearest_surface)
- [sample_uv_surface](#sample_uv_surface)
- [scale_elements](#scale_elements)
- [scale_single_axis](#scale_single_axis)
- [scale_uniform](#scale_uniform)
- [set_shade_smooth](#set_shade_smooth)
- [shortest_edge_paths](#shortest_edge_paths)
- [split_edges](#split_edges)
- [subdivide](#subdivide)
- [subdivision_surface](#subdivision_surface)
- [to_curve](#to_curve)
- [to_points](#to_points)
- [to_volume](#to_volume)
- [triangulate](#triangulate)
- [uv_unwrap](#uv_unwrap)
- [vertex_of_corner](#vertex_of_corner)

## Examples

### Initialization

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

### Boolean operations

The three possible boolean operations on meshes can be done using the three methods:
- `boolean_union`
- `boolean_intersect`
- `boolean_difference`

The three methods accept several meshes as arguments.

```python
import geonodes as gn

with gn.Tree("Test") as tree:
    
    # We will perform the boolean operation with a cylinder and a thick plane
    cyl, _, _, _ = gn.Mesh.Cylinder(depth=5)
    plane = gn.Mesh.Cube().transform(scale=(4.1, 4.1, .25))
    
    # ----- Union
    
    mesh1 = gn.Mesh.UVSphere(radius=2)
    mesh1.boolean_union(cyl, plane)
    
    mesh1.transform(translation=(5, 0, 0))
    
    # ----- Intersection
    
    mesh2 = gn.Mesh.UVSphere(radius=2)
    mesh2.boolean_intersect(cyl, plane)
    
    # ----- Difference
    
    mesh3 = gn.Mesh.UVSphere(radius=2)
    mesh3.boolean_difference(cyl, plane)
    
    mesh3.transform(translation=(-5, 0, 0))
    
    # ----- The 3 operations as a result
    
    tree.og = mesh1 + mesh2 + mesh3
```

