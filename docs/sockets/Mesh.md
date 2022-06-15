
# Data socket Mesh

> Inherits from gn.Geometry
  
<sub>go to [index](/docs/index.md)</sub>



## Constructors

- [Circle](#circle) : mesh (Mesh)
- [Cone](#cone) : Sockets      [mesh (Mesh), top (Boolean), bottom (Boolean), side (Boolean)]
- [Cube](#cube) : mesh (Mesh)
- [Cylinder](#cylinder) : Sockets      [mesh (Mesh), top (Boolean), side (Boolean), bottom (Boolean)]
- [Grid](#grid) : mesh (Mesh)
- [IcoSphere](#icosphere) : mesh (Mesh)
- [Line](#line) : mesh (Mesh)
- [UVSphere](#uvsphere) : mesh (Mesh)

## Methods

- [difference](#difference) : mesh (Mesh)
- [distribute_points_on_faces](#distribute_points_on_faces) : Sockets      [points (Points), normal (Vector), rotation (Vector)]
- [dual](#dual) : dual_mesh (Geometry)
- [duplicate_edges](#duplicate_edges) : Sockets      [geometry (Geometry), duplicate_index (Integer)]
- [duplicate_faces](#duplicate_faces) : Sockets      [geometry (Geometry), duplicate_index (Integer)]
- [extrude](#extrude) : Sockets      [mesh (Mesh), top (Boolean), side (Boolean)]
- [flip_faces](#flip_faces) : mesh (Mesh)
- [intersect](#intersect) : mesh (Mesh)
- [split_edges](#split_edges) : mesh (Mesh)
- [subdivide](#subdivide) : mesh (Mesh)
- [subdivision_surface](#subdivision_surface) : mesh (Mesh)
- [to_curve](#to_curve) : curve (Curve)
- [to_points](#to_points) : points (Points)
- [triangulate](#triangulate) : mesh (Mesh)
- [union](#union) : mesh (Mesh)

## Circle

> Node: [MeshCircle](/docs/nodes/MeshCircle.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeMeshCircle](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCircle.html)
node ref [Mesh Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_circle.html) </sub>
                          
```python
v = Mesh.Circle(vertices, radius, fill_type, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vertices : Integer
- radius : Float## Parameters
- fill_type : 'NONE' in [NONE, NGON, TRIANGLE_FAN]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.MeshCircle(vertices=vertices, radius=radius, fill_type=fill_type, label=node_label, node_color=node_color)
```

### Returns

Mesh


## Cone

> Node: [Cone](/docs/nodes/Cone.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeMeshCone](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCone.html)
node ref [Cone](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cone.html) </sub>
                          
```python
v = Mesh.Cone(vertices, side_segments, fill_segments, radius_top, radius_bottom, depth, fill_type, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vertices : Integer
- side_segments : Integer
- fill_segments : Integer
- radius_top : Float
- radius_bottom : Float
- depth : Float## Parameters
- fill_type : 'NGON' in [NONE, NGON, TRIANGLE_FAN]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.Cone(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius_top=radius_top, radius_bottom=radius_bottom, depth=depth, fill_type=fill_type, label=node_label, node_color=node_color)
```

### Returns

Sockets [mesh (Mesh), top (Boolean), bottom (Boolean), side (Boolean)]


## Cube

> Node: [Cube](/docs/nodes/Cube.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeMeshCube](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCube.html)
node ref [Cube](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cube.html) </sub>
                          
```python
v = Mesh.Cube(size, vertices_x, vertices_y, vertices_z, node_label = None, node_color = None)
```

### Arguments

## Sockets
- size : Vector
- vertices_x : Integer
- vertices_y : Integer
- vertices_z : Integer## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.Cube(size=size, vertices_x=vertices_x, vertices_y=vertices_y, vertices_z=vertices_z, label=node_label, node_color=node_color)
```

### Returns

Mesh


## Cylinder

> Node: [Cylinder](/docs/nodes/Cylinder.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeMeshCylinder](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCylinder.html)
node ref [Cylinder](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cylinder.html) </sub>
                          
```python
v = Mesh.Cylinder(vertices, side_segments, fill_segments, radius, depth, fill_type, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vertices : Integer
- side_segments : Integer
- fill_segments : Integer
- radius : Float
- depth : Float## Parameters
- fill_type : 'NGON' in [NONE, NGON, TRIANGLE_FAN]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.Cylinder(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius=radius, depth=depth, fill_type=fill_type, label=node_label, node_color=node_color)
```

### Returns

Sockets [mesh (Mesh), top (Boolean), side (Boolean), bottom (Boolean)]


## Grid

> Node: [Grid](/docs/nodes/Grid.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeMeshGrid](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshGrid.html)
node ref [Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/grid.html) </sub>
                          
```python
v = Mesh.Grid(size_x, size_y, vertices_x, vertices_y, node_label = None, node_color = None)
```

### Arguments

## Sockets
- size_x : Float
- size_y : Float
- vertices_x : Integer
- vertices_y : Integer## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.Grid(size_x=size_x, size_y=size_y, vertices_x=vertices_x, vertices_y=vertices_y, label=node_label, node_color=node_color)
```

### Returns

Mesh


## IcoSphere

> Node: [IcoSphere](/docs/nodes/IcoSphere.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeMeshIcoSphere](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshIcoSphere.html)
node ref [Ico Sphere](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/icosphere.html) </sub>
                          
```python
v = Mesh.IcoSphere(radius, subdivisions, node_label = None, node_color = None)
```

### Arguments

## Sockets
- radius : Float
- subdivisions : Integer## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.IcoSphere(radius=radius, subdivisions=subdivisions, label=node_label, node_color=node_color)
```

### Returns

Mesh


## Line

> Node: [MeshLine](/docs/nodes/MeshLine.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeMeshLine](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)
node ref [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) </sub>
                          
```python
v = Mesh.Line(count, start_location, offset, count_mode, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- count : Integer
- start_location : Vector
- offset : Vector## Parameters
- count_mode : 'TOTAL' in [TOTAL, RESOLUTION]
- mode : 'OFFSET' in [OFFSET, END_POINTS]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.MeshLine(count=count, start_location=start_location, offset=offset, count_mode=count_mode, mode=mode, label=node_label, node_color=node_color)
```

### Returns

Mesh


## UVSphere

> Node: [UvSphere](/docs/nodes/UvSphere.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeMeshUVSphere](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshUVSphere.html)
node ref [UV Sphere](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/uv_sphere.html) </sub>
                          
```python
v = Mesh.UVSphere(segments, rings, radius, node_label = None, node_color = None)
```

### Arguments

## Sockets
- segments : Integer
- rings : Integer
- radius : Float## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.UvSphere(segments=segments, rings=rings, radius=radius, label=node_label, node_color=node_color)
```

### Returns

Mesh


## intersect

> Node: [MeshBoolean](/docs/nodes/MeshBoolean.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeMeshBoolean](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)
node ref [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) </sub>
                          
```python
v = mesh.intersect(mesh_2_1, mesh_2_2, mesh_2_3, self_intersection, hole_tolerant, node_label = None, node_color = None)
```

### Arguments

## Sockets
- mesh_2 : *Geometry (self)
- self_intersection : Boolean
- hole_tolerant : Boolean## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'INTERSECT'

### Node creation

```python
from geondes import nodes
nodes.MeshBoolean(self, *mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='INTERSECT', label=node_label, node_color=node_color)
```

### Returns

Mesh


## union

> Node: [MeshBoolean](/docs/nodes/MeshBoolean.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeMeshBoolean](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)
node ref [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) </sub>
                          
```python
v = mesh.union(mesh_2_1, mesh_2_2, mesh_2_3, self_intersection, hole_tolerant, node_label = None, node_color = None)
```

### Arguments

## Sockets
- mesh_2 : *Geometry (self)
- self_intersection : Boolean
- hole_tolerant : Boolean## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'UNION'

### Node creation

```python
from geondes import nodes
nodes.MeshBoolean(self, *mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='UNION', label=node_label, node_color=node_color)
```

### Returns

Mesh


## difference

> Node: [MeshBoolean](/docs/nodes/MeshBoolean.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeMeshBoolean](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)
node ref [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) </sub>
                          
```python
v = mesh.difference(mesh_2_1, mesh_2_2, mesh_2_3, self_intersection, hole_tolerant, node_label = None, node_color = None)
```

### Arguments

## Sockets
- mesh_1 : Geometry (self)
- mesh_2 : *Geometry
- self_intersection : Boolean
- hole_tolerant : Boolean## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'DIFFERENCE'

### Node creation

```python
from geondes import nodes
nodes.MeshBoolean(*mesh_2, mesh_1=self, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='DIFFERENCE', label=node_label, node_color=node_color)
```

### Returns

Mesh


## split_edges

> Node: [SplitEdges](/docs/nodes/SplitEdges.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeSplitEdges](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html)
node ref [Split Edges](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/split_edges.html) </sub>
                          
```python
v = mesh.split_edges(selection, node_label = None, node_color = None)
```

### Arguments

## Sockets
- mesh : Mesh (self)
- selection : Boolean## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.SplitEdges(mesh=self, selection=selection, label=node_label, node_color=node_color)
```

### Returns

Mesh


## subdivide

> Node: [SubdivideMesh](/docs/nodes/SubdivideMesh.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeSubdivideMesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideMesh.html)
node ref [Subdivide Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivide_mesh.html) </sub>
                          
```python
v = mesh.subdivide(level, node_label = None, node_color = None)
```

### Arguments

## Sockets
- mesh : Mesh (self)
- level : Integer## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.SubdivideMesh(mesh=self, level=level, label=node_label, node_color=node_color)
```

### Returns

Mesh


## subdivision_surface

> Node: [SubdivisionSurface](/docs/nodes/SubdivisionSurface.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeSubdivisionSurface](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivisionSurface.html)
node ref [Subdivision Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivision_surface.html) </sub>
                          
```python
v = mesh.subdivision_surface(level, crease, boundary_smooth, uv_smooth, node_label = None, node_color = None)
```

### Arguments

## Sockets
- mesh : Mesh (self)
- level : Integer
- crease : Float## Parameters
- boundary_smooth : 'ALL' in [PRESERVE_CORNERS, ALL]
- uv_smooth : 'PRESERVE_BOUNDARIES' in [NONE, PRESERVE_CORNERS, PRESERVE_CORNERS_AND_JUNCTIONS, PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE, PRESERVE_BOUNDARIES, SMOOTH_ALL]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.SubdivisionSurface(mesh=self, level=level, crease=crease, boundary_smooth=boundary_smooth, uv_smooth=uv_smooth, label=node_label, node_color=node_color)
```

### Returns

Mesh


## triangulate

> Node: [Triangulate](/docs/nodes/Triangulate.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeTriangulate](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html)
node ref [Triangulate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/triangulate.html) </sub>
                          
```python
v = mesh.triangulate(selection, minimum_vertices, ngon_method, quad_method, node_label = None, node_color = None)
```

### Arguments

## Sockets
- mesh : Mesh (self)
- selection : Boolean
- minimum_vertices : Integer## Parameters
- ngon_method : 'BEAUTY' in [BEAUTY, CLIP]
- quad_method : 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.Triangulate(mesh=self, selection=selection, minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method, label=node_label, node_color=node_color)
```

### Returns

Mesh


## dual

> Node: [DualMesh](/docs/nodes/DualMesh.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeDualMesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeDualMesh.html)
node ref [Dual Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/dual_mesh.html) </sub>
                          
```python
v = mesh.dual(keep_boundaries, node_label = None, node_color = None)
```

### Arguments

## Sockets
- mesh : Mesh (self)
- keep_boundaries : Boolean## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.DualMesh(mesh=self, keep_boundaries=keep_boundaries, label=node_label, node_color=node_color)
```

### Returns

Geometry


## flip_faces

> Node: [FlipFaces](/docs/nodes/FlipFaces.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeFlipFaces](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html)
node ref [Flip Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/flip_faces.html) </sub>
                          
```python
v = mesh.flip_faces(selection, node_label = None, node_color = None)
```

### Arguments

## Sockets
- mesh : Mesh (self)
- selection : Boolean## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.FlipFaces(mesh=self, selection=selection, label=node_label, node_color=node_color)
```

### Returns

Mesh


## duplicate_edges

> Node: [DuplicateElements](/docs/nodes/DuplicateElements.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeDuplicateElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)
node ref [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) </sub>
                          
```python
v = mesh.duplicate_edges(selection, amount, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- selection : Boolean
- amount : Integer## Parameters
- node_label : None
- node_color : None## Fixed parameters
- domain : 'EDGE'

### Node creation

```python
from geondes import nodes
nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='EDGE', label=node_label, node_color=node_color)
```

### Returns

Sockets [geometry (Geometry), duplicate_index (Integer)]


## duplicate_faces

> Node: [DuplicateElements](/docs/nodes/DuplicateElements.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeDuplicateElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)
node ref [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) </sub>
                          
```python
v = mesh.duplicate_faces(selection, amount, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- selection : Boolean
- amount : Integer## Parameters
- node_label : None
- node_color : None## Fixed parameters
- domain : 'FACE'

### Node creation

```python
from geondes import nodes
nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='FACE', label=node_label, node_color=node_color)
```

### Returns

Sockets [geometry (Geometry), duplicate_index (Integer)]


## extrude

> Node: [ExtrudeMesh](/docs/nodes/ExtrudeMesh.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeExtrudeMesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)
node ref [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html) </sub>
                          
```python
v = mesh.extrude(selection, offset, offset_scale, individual, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- mesh : Mesh (self)
- selection : Boolean
- offset : Vector
- offset_scale : Float
- individual : Boolean## Parameters
- mode : 'FACES' in [VERTICES, EDGES, FACES]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.ExtrudeMesh(mesh=self, selection=selection, offset=offset, offset_scale=offset_scale, individual=individual, mode=mode, label=node_label, node_color=node_color)
```

### Returns

Sockets [mesh (Mesh), top (Boolean), side (Boolean)]


## to_curve

> Node: [MeshToCurve](/docs/nodes/MeshToCurve.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeMeshToCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html)
node ref [Mesh to Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_curve.html) </sub>
                          
```python
v = mesh.to_curve(selection, node_label = None, node_color = None)
```

### Arguments

## Sockets
- mesh : Mesh (self)
- selection : Boolean## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.MeshToCurve(mesh=self, selection=selection, label=node_label, node_color=node_color)
```

### Returns

Curve


## to_points

> Node: [MeshToPoints](/docs/nodes/MeshToPoints.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeMeshToPoints](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html)
node ref [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_points.html) </sub>
                          
```python
v = mesh.to_points(selection, position, radius, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- mesh : Mesh (self)
- selection : Boolean
- position : Vector
- radius : Float## Parameters
- mode : 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.MeshToPoints(mesh=self, selection=selection, position=position, radius=radius, mode=mode, label=node_label, node_color=node_color)
```

### Returns

Points


## distribute_points_on_faces

> Node: [DistributePointsOnFaces](/docs/nodes/DistributePointsOnFaces.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeDistributePointsOnFaces](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html)
node ref [Distribute Points on Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html) </sub>
                          
```python
v = mesh.distribute_points_on_faces(selection, distance_min, density_max, density, density_factor, seed, distribute_method, node_label = None, node_color = None)
```

### Arguments

## Sockets
- mesh : Mesh (self)
- selection : Boolean
- distance_min : Float
- density_max : Float
- density : Float
- density_factor : Float
- seed : Integer## Parameters
- distribute_method : 'RANDOM' in [RANDOM, POISSON]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.DistributePointsOnFaces(mesh=self, selection=selection, distance_min=distance_min, density_max=density_max, density=density, density_factor=density_factor, seed=seed, distribute_method=distribute_method, label=node_label, node_color=node_color)
```

### Returns

Sockets [points (Points), normal (Vector), rotation (Vector)]

