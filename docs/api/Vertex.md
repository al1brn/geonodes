# class {class_name}

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

## extrude {#extrude}

> def extrude(self, offset=None, offset_scale=None, individual=None):

Node [Extrude Mesh](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- offset: Vector
- offset_scale: Float
- individual: Boolean

### Returns:

- tuple ('top', 'side')

## instance_on_points {#instance_on_points}

> def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

Node [Instance on Points](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

### Returns:

  socket 'instances' of class Instances

## merge_by_distance {#merge_by_distance}

> def merge_by_distance(self, distance=None, mode='ALL'):

Node [Merge by Distance](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- distance: Float
- mode (str): 'ALL' in [ALL, CONNECTED]

### Returns:

- node with sockets ['geometry']

## neighbors *property* {#neighbors}

> def neighbors(self):

Node [Vertex Neighbors](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

- node with sockets ['vertex_count', 'face_count']

## neighbors_face_count *property* {#neighbors_face_count}

> def neighbors_face_count(self):

Node [Vertex Neighbors](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'face_count'

## neighbors_vertex_count *property* {#neighbors_vertex_count}

> def neighbors_vertex_count(self):

Node [Vertex Neighbors](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'vertex_count'

## to_points {#to_points}

> def to_points(self, position=None, radius=None, mode='VERTICES'):

Node [Mesh to Points](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- position: Vector
- radius: Float
- mode (str): 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]

### Returns:

  socket 'points' of class Points

## to_volume {#to_volume}

> def to_volume(self, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT'):

Node [Mesh to Volume](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- density: Float
- voxel_size: Float
- voxel_amount: Float
- exterior_band_width: Float
- interior_band_width: Float
- fill_volume: Boolean
- resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]

### Returns:

  socket 'volume' of class Volume

