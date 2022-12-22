# class Mesh

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

# Mesh

**Mesh** is a subclass of [Geometry](Geometry.md).

Use **Mesh** type to access methods specific to meshes.

A **Mesh** has four [domains](domain.md):
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

## Circle <sub>*classmethod*</sub>

```python
def Circle(cls, vertices=None, radius=None, fill_type='NONE'):

```
> Node: [Mesh Circle](GeometryNodeMeshCircle.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_circle.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCircle.html)

#### Args:
- vertices: Integer
- radius: Float
- fill_type (str): 'NONE' in [NONE, NGON, TRIANGLE_FAN]

#### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Cone <sub>*staticmethod*</sub>

```python
def Cone(vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON'):

```
> Node: [Cone](GeometryNodeMeshCone.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cone.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCone.html)

#### Args:
- vertices: Integer
- side_segments: Integer
- fill_segments: Integer
- radius_top: Float
- radius_bottom: Float
- depth: Float
- fill_type (str): 'NGON' in [NONE, NGON, TRIANGLE_FAN]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshCone.webp)

#### Returns:
- tuple ('`mesh`', '`top`', '`bottom`', '`side`')

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Cube <sub>*classmethod*</sub>

```python
def Cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None):

```
> Node: [Cube](GeometryNodeMeshCube.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cube.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCube.html)

#### Args:
- size: Vector
- vertices_x: Integer
- vertices_y: Integer
- vertices_z: Integer

#### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Cylinder <sub>*staticmethod*</sub>

```python
def Cylinder(vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON'):

```
> Node: [Cylinder](GeometryNodeMeshCylinder.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cylinder.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCylinder.html)

#### Args:
- vertices: Integer
- side_segments: Integer
- fill_segments: Integer
- radius: Float
- depth: Float
- fill_type (str): 'NGON' in [NONE, NGON, TRIANGLE_FAN]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshCylinder.webp)

#### Returns:
- tuple ('`mesh`', '`top`', '`bottom`', '`side`')

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Grid <sub>*classmethod*</sub>

```python
def Grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None):

```
> Node: [Grid](GeometryNodeMeshGrid.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/grid.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshGrid.html)

#### Args:
- size_x: Float
- size_y: Float
- vertices_x: Integer
- vertices_y: Integer

#### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## IcoSphere <sub>*classmethod*</sub>

```python
def IcoSphere(cls, radius=None, subdivisions=None):

```
> Node: [Ico Sphere](GeometryNodeMeshIcoSphere.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/icosphere.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshIcoSphere.html)

#### Args:
- radius: Float
- subdivisions: Integer

#### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Line <sub>*classmethod*</sub>

```python
def Line(cls, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET'):

```
> Node: [Mesh Line](GeometryNodeMeshLine.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)

#### Args:
- count: Integer
- resolution: Float
- start_location: Vector
- offset: Vector
- count_mode (str): 'TOTAL' in [TOTAL, RESOLUTION]
- mode (str): 'OFFSET' in [OFFSET, END_POINTS]

#### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## LineEndPoints <sub>*classmethod*</sub>

```python
def LineEndPoints(cls, count=None, start_location=None, end_location=None):

```
> Node: [Mesh Line](GeometryNodeMeshLine.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)

#### Args:
- count: Integer
- start_location: Vector
- end_location: Vector

#### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## LineEndPointsResolution <sub>*classmethod*</sub>

```python
def LineEndPointsResolution(cls, resolution=None, start_location=None, end_location=None):

```
> Node: [Mesh Line](GeometryNodeMeshLine.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)

#### Args:
- resolution: Float
- start_location: Vector
- end_location: Vector

#### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## LineOffset <sub>*classmethod*</sub>

```python
def LineOffset(cls, count=None, start_location=None, offset=None):

```
> Node: [Mesh Line](GeometryNodeMeshLine.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)

#### Args:
- count: Integer
- start_location: Vector
- offset: Vector

#### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## LineOffsetResolution <sub>*classmethod*</sub>

```python
def LineOffsetResolution(cls, resolution=None, start_location=None, offset=None):

```
> Node: [Mesh Line](GeometryNodeMeshLine.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)

#### Args:
- resolution: Float
- start_location: Vector
- offset: Vector

#### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## UVSphere <sub>*classmethod*</sub>

```python
def UVSphere(cls, segments=None, rings=None, radius=None):

```
> Node: [UV Sphere](GeometryNodeMeshUVSphere.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/uv_sphere.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshUVSphere.html)

#### Args:
- segments: Integer
- rings: Integer
- radius: Float

#### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## boolean_difference

```python
def boolean_difference(self, *mesh_2, self_intersection=None, hole_tolerant=None):

```
> Node: [Mesh Boolean](GeometryNodeMeshBoolean.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)

#### Args:
- mesh_2: <m>Geometry
- self_intersection: Boolean
- hole_tolerant: Boolean

#### Returns:
- socket `intersecting_edges`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## boolean_intersect

```python
def boolean_intersect(*mesh_2, self_intersection=None, hole_tolerant=None):

```
> Node: [Mesh Boolean](GeometryNodeMeshBoolean.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)

#### Args:
- mesh_2: <m>Geometry
- self_intersection: Boolean
- hole_tolerant: Boolean

#### Returns:
- socket `intersecting_edges`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## boolean_union

```python
def boolean_union(*mesh_2, self_intersection=None, hole_tolerant=None):

```
> Node: [Mesh Boolean](GeometryNodeMeshBoolean.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)

#### Args:
- mesh_2: <m>Geometry
- self_intersection: Boolean
- hole_tolerant: Boolean

#### Returns:
- socket `intersecting_edges`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## corner_count <sub>*property*</sub>

```python
def corner_count(self):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `face_corner_count`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## corners_of_face

```python
def corners_of_face(self, face_index=None, weights=None, sort_index=None):

```
> Node: [Corners of Face](GeometryNodeCornersOfFace.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/corners_of_face.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfFace.html)

#### Args:
- face_index: Integer
- weights: Float
- sort_index: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCornersOfFace.webp)

#### Returns:
- tuple ('`corner_index`', '`total`')

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## corners_of_vertex

```python
def corners_of_vertex(self, vertex_index=None, weights=None, sort_index=None):

```
> Node: [Corners of Vertex](GeometryNodeCornersOfVertex.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/corners_of_vertex.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfVertex.html)

#### Args:
- vertex_index: Integer
- weights: Float
- sort_index: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCornersOfVertex.webp)

#### Returns:
- tuple ('`corner_index`', '`total`')

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## delete_all

```python
def delete_all(self, selection=None, domain='POINT'):

```
> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

#### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## delete_edges

```python
def delete_edges(self, selection=None, domain='POINT'):

```
> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

#### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## delete_faces

```python
def delete_faces(self, selection=None, domain='POINT'):

```
> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

#### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## distribute_points_on_faces

```python
def distribute_points_on_faces(self, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM'):

```
> Node: [Distribute Points on Faces](GeometryNodeDistributePointsOnFaces.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html)

#### Args:
- selection: Boolean
- distance_min: Float
- density_max: Float
- density: Float
- density_factor: Float
- seed: Integer
- distribute_method (str): 'RANDOM' in [RANDOM, POISSON]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDistributePointsOnFaces.webp)

#### Returns:
- tuple ('`points`', '`normal`', '`rotation`')

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## domain_size <sub>*property*</sub>

```python
def domain_size(self):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## dual_mesh

```python
def dual_mesh(self, mesh=None, keep_boundaries=None):

```
> Node: [Dual Mesh](GeometryNodeDualMesh.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/dual_mesh.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDualMesh.html)

#### Args:
- mesh: Mesh
- keep_boundaries: Boolean

#### Returns:
- socket `dual_mesh` of class Mesh

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## edge_count <sub>*property*</sub>

```python
def edge_count(self):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `edge_count`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## edge_paths_to_curves

```python
def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None):

```
> Node: [Edge Paths to Curves](GeometryNodeEdgePathsToCurves.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_curves.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html)

#### Args:
- start_vertices: Boolean
- next_vertex_index: Integer

#### Returns:
- socket `curves` of class Curve

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## edge_paths_to_selection

```python
def edge_paths_to_selection(self, start_vertices=None, next_vertex_index=None):

```
> Node: [Edge Paths to Selection](GeometryNodeEdgePathsToSelection.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_selection.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToSelection.html)

#### Args:
- start_vertices: Boolean
- next_vertex_index: Integer

#### Returns:
- socket `selection`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## edges_of_corner

```python
def edges_of_corner(self, corner_index=None):

```
> Node: [Edges of Corner](GeometryNodeEdgesOfCorner.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_corner.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfCorner.html)

#### Args:
- corner_index: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgesOfCorner.webp)

#### Returns:
- tuple ('`next_edge_index`', '`previous_edge_index`')

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## edges_of_vertex

```python
def edges_of_vertex(self, vertex_index=None, weights=None, sort_index=None):

```
> Node: [Edges of Vertex](GeometryNodeEdgesOfVertex.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_vertex.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfVertex.html)

#### Args:
- vertex_index: Integer
- weights: Float
- sort_index: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgesOfVertex.webp)

#### Returns:
- tuple ('`edge_index`', '`total`')

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## extrude

```python
def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES'):

```
> Node: [Extrude Mesh](GeometryNodeExtrudeMesh.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)

#### Args:
- selection: Boolean
- offset: Vector
- offset_scale: Float
- individual: Boolean
- mode (str): 'FACES' in [VERTICES, EDGES, FACES]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeExtrudeMesh.webp)

#### Returns:
- tuple ('`top`', '`side`')

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## face_count <sub>*property*</sub>

```python
def face_count(self):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `face_count`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## face_is_planar

```python
def face_is_planar(self, threshold=None):

```
> Node: [Face is Planar](GeometryNodeInputMeshFaceIsPlanar.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_is_planar.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html)

#### Args:
- threshold: Float

#### Returns:
- socket `planar`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## face_of_corner

```python
def face_of_corner(self, corner_index=None):

```
> Node: [Face of Corner](GeometryNodeFaceOfCorner.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/face_of_corner.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFaceOfCorner.html)

#### Args:
- corner_index: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFaceOfCorner.webp)

#### Returns:
- tuple ('`face_index`', '`index_in_face`')

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## face_set_boundaries

```python
def face_set_boundaries(self, face_set=None):

```
> Node: [Face Set Boundaries](GeometryNodeMeshFaceSetBoundaries.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_set_boundaries.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html)

#### Args:
- face_set: Integer

#### Returns:
- socket `boundary_edges`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## flip_faces

```python
def flip_faces(self, selection=None):

```
> Node: [Flip Faces](GeometryNodeFlipFaces.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/flip_faces.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html)

#### Args:
- selection: Boolean

#### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## instance_on_points

```python
def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

```
> Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

#### Args:
- selection: Boolean
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

#### Returns:
- socket `instances`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## is_shade_smooth

```python
def is_shade_smooth(self):

```
> Node: [Is Shade Smooth](GeometryNodeInputShadeSmooth.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/is_shade_smooth.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html)

#### Returns:
- socket `smooth`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## island <sub>*property*</sub>

```python
def island(self):

```
> Node: [Mesh Island](GeometryNodeInputMeshIsland.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)

#### Returns:
- node with sockets ['island_index', 'island_count']

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## island_count <sub>*property*</sub>

```python
def island_count(self):

```
> Node: [Mesh Island](GeometryNodeInputMeshIsland.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)

#### Returns:
- socket `island_count`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## island_index <sub>*property*</sub>

```python
def island_index(self):

```
> Node: [Mesh Island](GeometryNodeInputMeshIsland.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)

#### Returns:
- socket `island_index`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## offset_corner_in_face

```python
def offset_corner_in_face(self, corner_index=None, offset=None):

```
> Node: [Offset Corner in Face](GeometryNodeOffsetCornerInFace.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/offset_corner_in_face.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetCornerInFace.html)

#### Args:
- corner_index: Integer
- offset: Integer

#### Returns:
- socket `corner_index`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## pack_uv_islands

```python
def pack_uv_islands(self, uv=None, selection=None, margin=None, rotate=None):

```
> Node: [Pack UV Islands](GeometryNodeUVPackIslands.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/pack_uv_islands.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html)

#### Args:
- uv: Vector
- selection: Boolean
- margin: Float
- rotate: Boolean

#### Returns:
- socket `uv`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## point_count <sub>*property*</sub>

```python
def point_count(self):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `point_count`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## sample_nearest_surface

```python
def sample_nearest_surface(self, value=None, sample_position=None):

```
> Node: [Sample Nearest Surface](GeometryNodeSampleNearestSurface.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample_nearest_surface.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearestSurface.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- sample_position: Vector

#### Returns:
- socket `value`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## sample_uv_surface

```python
def sample_uv_surface(self, value=None, source_uv_map=None, sample_uv=None):

```
> Node: [Sample UV Surface](GeometryNodeSampleUVSurface.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample_uv_surface.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleUVSurface.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- source_uv_map: Vector
- sample_uv: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleUVSurface.webp)

#### Returns:
- tuple ('`value`', '`is_valid`')

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## scale_elements

```python
def scale_elements(self, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM'):

```
> Node: [Scale Elements](GeometryNodeScaleElements.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

#### Args:
- selection: Boolean
- scale: Float
- center: Vector
- axis: Vector
- domain (str): 'FACE' in [FACE, EDGE]
- scale_mode (str): 'UNIFORM' in [UNIFORM, SINGLE_AXIS]

#### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## scale_single_axis

```python
def scale_single_axis(self, selection=None, scale=None, center=None, axis=None, domain='FACE'):

```
> Node: [Scale Elements](GeometryNodeScaleElements.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

#### Args:
- selection: Boolean
- scale: Float
- center: Vector
- axis: Vector
- domain (str): 'FACE' in [FACE, EDGE]

#### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## scale_uniform

```python
def scale_uniform(self, selection=None, scale=None, center=None, domain='FACE'):

```
> Node: [Scale Elements](GeometryNodeScaleElements.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

#### Args:
- selection: Boolean
- scale: Float
- center: Vector
- domain (str): 'FACE' in [FACE, EDGE]

#### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_shade_smooth

```python
def set_shade_smooth(self, selection=None, shade_smooth=None):

```
> Node: [Set Shade Smooth](GeometryNodeSetShadeSmooth.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html)

#### Args:
- selection: Boolean
- shade_smooth: Boolean

#### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## shortest_edge_paths

```python
def shortest_edge_paths(self, end_vertex=None, edge_cost=None):

```
> Node: [Shortest Edge Paths](GeometryNodeInputShortestEdgePaths.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/shortest_edge_paths.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShortestEdgePaths.html)

#### Args:
- end_vertex: Boolean
- edge_cost: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputShortestEdgePaths.webp)

#### Returns:
- tuple ('`next_vertex_index`', '`total_cost`')

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## split_edges

```python
def split_edges(self, selection=None):

```
> Node: [Split Edges](GeometryNodeSplitEdges.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/split_edges.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html)

#### Args:
- selection: Boolean

#### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## subdivide

```python
def subdivide(self, level=None):

```
> Node: [Subdivide Mesh](GeometryNodeSubdivideMesh.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivide_mesh.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideMesh.html)

#### Args:
- level: Integer

#### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## subdivision_surface

```python
def subdivision_surface(self, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES'):

```
> Node: [Subdivision Surface](GeometryNodeSubdivisionSurface.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivision_surface.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivisionSurface.html)

#### Args:
- level: Integer
- edge_crease: Float
- vertex_crease: Float
- boundary_smooth (str): 'ALL' in [PRESERVE_CORNERS, ALL]
- uv_smooth (str): 'PRESERVE_BOUNDARIES' in [NONE, PRESERVE_CORNERS, PRESERVE_CORNERS_AND_JUNCTIONS, PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE, PRESERVE_BOUNDARIES, SMOOTH_ALL]

#### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_curve

```python
def to_curve(self, selection=None):

```
> Node: [Mesh to Curve](GeometryNodeMeshToCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html)

#### Args:
- selection: Boolean

#### Returns:
- socket `curve` of class Curve

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_points

```python
def to_points(self, selection=None, position=None, radius=None, mode='VERTICES'):

```
> Node: [Mesh to Points](GeometryNodeMeshToPoints.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_points.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html)

#### Args:
- selection: Boolean
- position: Vector
- radius: Float
- mode (str): 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]

#### Returns:
- socket `points` of class Points

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_volume

```python
def to_volume(self, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT'):

```
> Node: [Mesh to Volume](GeometryNodeMeshToVolume.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_volume.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToVolume.html)

#### Args:
- density: Float
- voxel_size: Float
- voxel_amount: Float
- exterior_band_width: Float
- interior_band_width: Float
- fill_volume: Boolean
- resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]

#### Returns:
- socket `volume` of class Volume

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## triangulate

```python
def triangulate(self, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):

```
> Node: [Triangulate](GeometryNodeTriangulate.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/triangulate.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html)

#### Args:
- selection: Boolean
- minimum_vertices: Integer
- ngon_method (str): 'BEAUTY' in [BEAUTY, CLIP]
- quad_method (str): 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]

#### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## uv_unwrap

```python
def uv_unwrap(self, selection=None, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED'):

```
> Node: [UV Unwrap](GeometryNodeUVUnwrap.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/uv_unwrap.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVUnwrap.html)

#### Args:
- selection: Boolean
- seam: Boolean
- margin: Float
- fill_holes: Boolean
- method (str): 'ANGLE_BASED' in [ANGLE_BASED, CONFORMAL]

#### Returns:
- socket `uv`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## vertex_of_corner

```python
def vertex_of_corner(self, corner_index=None):

```
> Node: [Vertex of Corner](GeometryNodeVertexOfCorner.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/vertex_of_corner.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeVertexOfCorner.html)

#### Args:
- corner_index: Integer

#### Returns:
- socket `vertex_index`

<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

# Mesh

**Mesh** is a subclass of [Geometry](Geometry.md).

Use **Mesh** type to access methods specific to meshes.

A **Mesh** has four [domains](domain.md):
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







    
    
    
    


