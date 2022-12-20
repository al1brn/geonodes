# class {class_name}

## angle *property* {#angle}

> def angle(self):

Node [Edge Angle](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

- node with sockets ['unsigned_angle', 'signed_angle']

## delete_all {#delete_all}

> def delete_all(self):

Node [Delete Geometry](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

- node with sockets ['geometry']

## delete_edges {#delete_edges}

> def delete_edges(self):

Node [Delete Geometry](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

- node with sockets ['geometry']

## delete_faces {#delete_faces}

> def delete_faces(self):

Node [Delete Geometry](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

- node with sockets ['geometry']

## domain_size {#domain_size}

> def __len__(self):

Node [Domain Size](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- geometry: Geometry
- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

### Returns:

- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

## edge_paths_to_curves {#edge_paths_to_curves}

> def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None):

Node [Edge Paths to Curves](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- start_vertices: Boolean
- next_vertex_index: Integer

### Returns:

  socket 'curves' of class Curve

## extrude {#extrude}

> def extrude(self, offset=None, offset_scale=None, individual=None):

Node [Extrude Mesh](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- offset: Vector
- offset_scale: Float
- individual: Boolean

### Returns:

- tuple ('top', 'side')

## neighbors *property* {#neighbors}

> def neighbors(self):

Node [Edge Neighbors](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'face_count'

## scale_single_axis {#scale_single_axis}

> def scale_single_axis(self, scale=None, center=None, axis=None):

Node [Scale Elements](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- scale: Float
- center: Vector
- axis: Vector

### Returns:

- node with sockets ['geometry']

## scale_uniform {#scale_uniform}

> def scale_uniform(self, scale=None, center=None):

Node [Scale Elements](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- scale: Float
- center: Vector

### Returns:

- node with sockets ['geometry']

## signed_angle *property* {#signed_angle}

> def signed_angle(self):

Node [Edge Angle](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'signed_angle'

## split {#split}

> def split(self):

Node [Split Edges](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

- node with sockets ['mesh']

## to_curve {#to_curve}

> def to_curve(self):

Node [Mesh to Curve](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'curve' of class Curve

## unsigned_angle *property* {#unsigned_angle}

> def unsigned_angle(self):

Node [Edge Angle](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'unsigned_angle'

## vertices *property* {#vertices}

> def vertices(self):

Node [Edge Vertices](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

- node with sockets ['vertex_index_1', 'vertex_index_2', 'position_1', 'position_2']

## vertices_index *property* {#vertices_index}

> def vertices_index(self):

Node [Edge Vertices](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

- tuple ('vertex_index_1', 'vertex_index_2')

## vertices_position *property* {#vertices_position}

> def vertices_position(self):

Node [Edge Vertices](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

- tuple ('position_1', 'position_2')

