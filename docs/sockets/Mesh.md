
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

## Attribute capture

- [capture_edge_angle](#capture_edge_angle) : Sockets      [unsigned_angle (Float), signed_angle (Float)]
- [capture_edge_neighbors](#capture_edge_neighbors) : face_count (Integer)
- [capture_edge_vertices](#capture_edge_vertices) : Sockets      [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
- [capture_face_area](#capture_face_area) : area (Float)
- [capture_face_is_planar](#capture_face_is_planar) : planar (Boolean)
- [capture_face_neighbors](#capture_face_neighbors) : Sockets      [vertex_count (Integer), face_count (Integer)]
- [capture_island](#capture_island) : Sockets      [island_index (Integer), island_count (Integer)]
- [capture_material_index](#capture_material_index) : material_index (Integer)
- [capture_material_selection](#capture_material_selection) : selection (Boolean)
- [capture_shade_smooth](#capture_shade_smooth) : smooth (Boolean)
- [capture_vertex_neighbors](#capture_vertex_neighbors) : Sockets      [vertex_count (Integer), face_count (Integer)]

## Attributes

- [corner_ID](#corner_id) : Float = capture_ID(domain='CORNER').unsigned_angle
- [corner_index](#corner_index) : Float = capture_index(domain='CORNER').unsigned_angle
- [corner_position](#corner_position) : Float = capture_position(domain='CORNER').unsigned_angle
- [edge_angle](#edge_angle) : Float = capture_edge_angle(domain='EDGE').unsigned_angle
- [edge_neighbors](#edge_neighbors) : Integer = capture_edge_neighbors(domain='EDGE')
- [edge_unsigned_angle](#edge_unsigned_angle) : Float = capture_edge_angle(domain='EDGE').signed_angle
- [edge_vertices_index1](#edge_vertices_index1) : Integer = capture_edge_vertices(domain='EDGE').vertex_index_1
- [edge_vertices_index2](#edge_vertices_index2) : Integer = capture_edge_vertices(domain='EDGE').vertex_index_2
- [edge_vertices_position1](#edge_vertices_position1) : Vector = capture_edge_vertices(domain='EDGE').position_1
- [edge_vertices_position2](#edge_vertices_position2) : Vector = capture_edge_vertices(domain='EDGE').position_2
- [egde_ID](#egde_id) : Float = capture_ID(domain='EDGE').unsigned_angle
- [egde_index](#egde_index) : Float = capture_index(domain='EDGE').unsigned_angle
- [egde_position](#egde_position) : Float = capture_position(domain='EDGE').unsigned_angle
- [face_ID](#face_id) : Float = capture_ID(domain='FACE').unsigned_angle
- [face_area](#face_area) : Float = capture_face_area(domain='FACE')
- [face_index](#face_index) : Float = capture_index(domain='FACE').unsigned_angle
- [face_is_planar](#face_is_planar) : Boolean = capture_face_is_planar(domain='FACE')
- [face_neighbors_face_count](#face_neighbors_face_count) : Integer = capture_face_neighbors(domain='FACE').face_count
- [face_neighbors_vertex_count](#face_neighbors_vertex_count) : Integer = capture_face_neighbors(domain='FACE').vertex_count
- [face_position](#face_position) : Float = capture_position(domain='FACE').unsigned_angle
- [island](#island) : Integer = capture_island(domain='POINT').island_index
- [material_index](#material_index) : Integer = capture_material_index(domain='FACE')
- [material_selection](#material_selection) : Boolean = capture_material_selection(domain='FACE')
- [shade_smooth](#shade_smooth) : Boolean = capture_shade_smooth(domain='FACE')
- [vertex_neighbors_face_count](#vertex_neighbors_face_count) : Integer = capture_vertex_neighbors(domain='POINT').face_count
- [vertex_neighbors_vertex_count](#vertex_neighbors_vertex_count) : Integer = capture_vertex_neighbors(domain='POINT').vertex_count

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


## capture_edge_angle

> Node: [EdgeAngle](/docs/nodes/EdgeAngle.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshEdgeAngle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)
node ref [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) </sub>
                          
```python
v = mesh.capture_edge_angle(self, domain='EDGE', node_label = None, node_color = None)
```

### Arguments

## Parameters
- self
- domain:'EDGE'
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.EdgeAngle(label=node_label, node_color=node_color)
```

### Returns

Sockets [unsigned_angle (Float), signed_angle (Float)]


## capture_edge_neighbors

> Node: [EdgeNeighbors](/docs/nodes/EdgeNeighbors.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshEdgeNeighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeNeighbors.html)
node ref [Edge Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_neighbors.html) </sub>
                          
```python
v = mesh.capture_edge_neighbors(self, domain='EDGE', node_label = None, node_color = None)
```

### Arguments

## Parameters
- self
- domain:'EDGE'
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.EdgeNeighbors(label=node_label, node_color=node_color)
```

### Returns

Integer


## capture_edge_vertices

> Node: [EdgeVertices](/docs/nodes/EdgeVertices.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshEdgeVertices](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)
node ref [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html) </sub>
                          
```python
v = mesh.capture_edge_vertices(self, domain='EDGE', node_label = None, node_color = None)
```

### Arguments

## Parameters
- self
- domain:'EDGE'
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.EdgeVertices(label=node_label, node_color=node_color)
```

### Returns

Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]


## capture_face_area

> Node: [FaceArea](/docs/nodes/FaceArea.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshFaceArea](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceArea.html)
node ref [Face Area](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_area.html) </sub>
                          
```python
v = mesh.capture_face_area(self, domain='FACE', node_label = None, node_color = None)
```

### Arguments

## Parameters
- self
- domain:'FACE'
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.FaceArea(label=node_label, node_color=node_color)
```

### Returns

Float


## capture_face_neighbors

> Node: [FaceNeighbors](/docs/nodes/FaceNeighbors.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshFaceNeighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html)
node ref [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html) </sub>
                          
```python
v = mesh.capture_face_neighbors(self, domain='FACE', node_label = None, node_color = None)
```

### Arguments

## Parameters
- self
- domain:'FACE'
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.FaceNeighbors(label=node_label, node_color=node_color)
```

### Returns

Sockets [vertex_count (Integer), face_count (Integer)]


## capture_island

> Node: [MeshIsland](/docs/nodes/MeshIsland.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshIsland](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)
node ref [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) </sub>
                          
```python
v = mesh.capture_island(self, domain='POINT', node_label = None, node_color = None)
```

### Arguments

## Parameters
- self
- domain:'POINT'
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.MeshIsland(label=node_label, node_color=node_color)
```

### Returns

Sockets [island_index (Integer), island_count (Integer)]


## capture_shade_smooth

> Node: [IsShadeSmooth](/docs/nodes/IsShadeSmooth.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputShadeSmooth](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html)
node ref [Is Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/is_shade_smooth.html) </sub>
                          
```python
v = mesh.capture_shade_smooth(self, domain='FACE', node_label = None, node_color = None)
```

### Arguments

## Parameters
- self
- domain:'FACE'
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.IsShadeSmooth(label=node_label, node_color=node_color)
```

### Returns

Boolean


## capture_vertex_neighbors

> Node: [VertexNeighbors](/docs/nodes/VertexNeighbors.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshVertexNeighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html)
node ref [Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/vertex_neighbors.html) </sub>
                          
```python
v = mesh.capture_vertex_neighbors(self, domain='POINT', node_label = None, node_color = None)
```

### Arguments

## Parameters
- self
- domain:'POINT'
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.VertexNeighbors(label=node_label, node_color=node_color)
```

### Returns

Sockets [vertex_count (Integer), face_count (Integer)]


## capture_material_index

> Node: [MaterialIndex](/docs/nodes/MaterialIndex.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMaterialIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)
node ref [Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html) </sub>
                          
```python
v = mesh.capture_material_index(self, domain='FACE', node_label = None, node_color = None)
```

### Arguments

## Parameters
- self
- domain:'FACE'
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.MaterialIndex(label=node_label, node_color=node_color)
```

### Returns

Integer


## capture_material_selection

> Node: [MaterialSelection](/docs/nodes/MaterialSelection.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeMaterialSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)
node ref [Material Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html) </sub>
                          
```python
v = mesh.capture_material_selection(self, material, domain='FACE', node_label = None, node_color = None)
```

### Arguments

## Sockets
- material : Material## Parameters
- self
- domain:'FACE'
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.MaterialSelection(material=material, label=node_label, node_color=node_color)
```

### Returns

Boolean


## capture_face_is_planar

> Node: [FaceIsPlanar](/docs/nodes/FaceIsPlanar.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshFaceIsPlanar](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html)
node ref [Face is Planar](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_is_planar.html) </sub>
                          
```python
v = mesh.capture_face_is_planar(self, threshold, domain='FACE', node_label = None, node_color = None)
```

### Arguments

## Sockets
- threshold : Float## Parameters
- self
- domain:'FACE'
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.FaceIsPlanar(threshold=threshold, label=node_label, node_color=node_color)
```

### Returns

Boolean


## face_ID

> Node: [EdgeAngle](/docs/nodes/EdgeAngle.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshEdgeAngle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)
node ref [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) </sub>
                          
```python
v = mesh.face_ID(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.EdgeAngle()
```

### Returns

Float


## egde_ID

> Node: [EdgeAngle](/docs/nodes/EdgeAngle.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshEdgeAngle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)
node ref [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) </sub>
                          
```python
v = mesh.egde_ID(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.EdgeAngle()
```

### Returns

Float


## corner_ID

> Node: [EdgeAngle](/docs/nodes/EdgeAngle.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshEdgeAngle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)
node ref [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) </sub>
                          
```python
v = mesh.corner_ID(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.EdgeAngle()
```

### Returns

Float


## face_index

> Node: [EdgeAngle](/docs/nodes/EdgeAngle.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshEdgeAngle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)
node ref [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) </sub>
                          
```python
v = mesh.face_index(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.EdgeAngle()
```

### Returns

Float


## egde_index

> Node: [EdgeAngle](/docs/nodes/EdgeAngle.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshEdgeAngle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)
node ref [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) </sub>
                          
```python
v = mesh.egde_index(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.EdgeAngle()
```

### Returns

Float


## corner_index

> Node: [EdgeAngle](/docs/nodes/EdgeAngle.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshEdgeAngle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)
node ref [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) </sub>
                          
```python
v = mesh.corner_index(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.EdgeAngle()
```

### Returns

Float


## face_position

> Node: [EdgeAngle](/docs/nodes/EdgeAngle.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshEdgeAngle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)
node ref [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) </sub>
                          
```python
v = mesh.face_position(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.EdgeAngle()
```

### Returns

Float


## egde_position

> Node: [EdgeAngle](/docs/nodes/EdgeAngle.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshEdgeAngle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)
node ref [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) </sub>
                          
```python
v = mesh.egde_position(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.EdgeAngle()
```

### Returns

Float


## corner_position

> Node: [EdgeAngle](/docs/nodes/EdgeAngle.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshEdgeAngle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)
node ref [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) </sub>
                          
```python
v = mesh.corner_position(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.EdgeAngle()
```

### Returns

Float


## edge_angle

> Node: [EdgeAngle](/docs/nodes/EdgeAngle.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshEdgeAngle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)
node ref [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) </sub>
                          
```python
v = mesh.edge_angle(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.EdgeAngle()
```

### Returns

Float


## edge_unsigned_angle

> Node: [EdgeAngle](/docs/nodes/EdgeAngle.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshEdgeAngle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)
node ref [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) </sub>
                          
```python
v = mesh.edge_unsigned_angle(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.EdgeAngle()
```

### Returns

Float


## edge_neighbors

> Node: [EdgeNeighbors](/docs/nodes/EdgeNeighbors.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshEdgeNeighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeNeighbors.html)
node ref [Edge Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_neighbors.html) </sub>
                          
```python
v = mesh.edge_neighbors(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.EdgeNeighbors()
```

### Returns

Integer


## edge_vertices_index1

> Node: [EdgeVertices](/docs/nodes/EdgeVertices.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshEdgeVertices](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)
node ref [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html) </sub>
                          
```python
v = mesh.edge_vertices_index1(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.EdgeVertices()
```

### Returns

Integer


## edge_vertices_index2

> Node: [EdgeVertices](/docs/nodes/EdgeVertices.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshEdgeVertices](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)
node ref [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html) </sub>
                          
```python
v = mesh.edge_vertices_index2(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.EdgeVertices()
```

### Returns

Integer


## edge_vertices_position1

> Node: [EdgeVertices](/docs/nodes/EdgeVertices.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshEdgeVertices](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)
node ref [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html) </sub>
                          
```python
v = mesh.edge_vertices_position1(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.EdgeVertices()
```

### Returns

Vector


## edge_vertices_position2

> Node: [EdgeVertices](/docs/nodes/EdgeVertices.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshEdgeVertices](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)
node ref [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html) </sub>
                          
```python
v = mesh.edge_vertices_position2(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.EdgeVertices()
```

### Returns

Vector


## face_area

> Node: [FaceArea](/docs/nodes/FaceArea.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshFaceArea](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceArea.html)
node ref [Face Area](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_area.html) </sub>
                          
```python
v = mesh.face_area(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.FaceArea()
```

### Returns

Float


## face_neighbors_vertex_count

> Node: [FaceNeighbors](/docs/nodes/FaceNeighbors.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshFaceNeighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html)
node ref [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html) </sub>
                          
```python
v = mesh.face_neighbors_vertex_count(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.FaceNeighbors()
```

### Returns

Integer


## face_neighbors_face_count

> Node: [FaceNeighbors](/docs/nodes/FaceNeighbors.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshFaceNeighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html)
node ref [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html) </sub>
                          
```python
v = mesh.face_neighbors_face_count(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.FaceNeighbors()
```

### Returns

Integer


## island

> Node: [MeshIsland](/docs/nodes/MeshIsland.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshIsland](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)
node ref [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) </sub>
                          
```python
v = mesh.island(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.MeshIsland()
```

### Returns

Integer


## shade_smooth

> Node: [IsShadeSmooth](/docs/nodes/IsShadeSmooth.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputShadeSmooth](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html)
node ref [Is Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/is_shade_smooth.html) </sub>
                          
```python
v = mesh.shade_smooth(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.IsShadeSmooth()
```

### Returns

Boolean


## vertex_neighbors_vertex_count

> Node: [VertexNeighbors](/docs/nodes/VertexNeighbors.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshVertexNeighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html)
node ref [Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/vertex_neighbors.html) </sub>
                          
```python
v = mesh.vertex_neighbors_vertex_count(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.VertexNeighbors()
```

### Returns

Integer


## vertex_neighbors_face_count

> Node: [VertexNeighbors](/docs/nodes/VertexNeighbors.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshVertexNeighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html)
node ref [Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/vertex_neighbors.html) </sub>
                          
```python
v = mesh.vertex_neighbors_face_count(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.VertexNeighbors()
```

### Returns

Integer


## material_index

> Node: [MaterialIndex](/docs/nodes/MaterialIndex.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMaterialIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)
node ref [Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html) </sub>
                          
```python
v = mesh.material_index(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.MaterialIndex()
```

### Returns

Integer


## material_selection

> Node: [MaterialSelection](/docs/nodes/MaterialSelection.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeMaterialSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)
node ref [Material Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html) </sub>
                          
```python
v = mesh.material_selection(self, material)
```

### Arguments

## Sockets
- material : Material## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.MaterialSelection(material=material)
```

### Returns

Boolean


## face_is_planar

> Node: [FaceIsPlanar](/docs/nodes/FaceIsPlanar.md)
  
<sub>go to: [top](#data-socket-mesh) [index](/docs/index.md)
blender ref [GeometryNodeInputMeshFaceIsPlanar](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html)
node ref [Face is Planar](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_is_planar.html) </sub>
                          
```python
v = mesh.face_is_planar(self, threshold)
```

### Arguments

## Sockets
- threshold : Float## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.FaceIsPlanar(threshold=threshold)
```

### Returns

Boolean


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

