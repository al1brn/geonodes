# class {class_name}

## domain_size {#domain_size}

> def __len__(self):

Node [Domain Size](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- geometry: Geometry
- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

### Returns:

- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

## rotate {#rotate}

> def rotate(self, rotation=None, pivot_point=None, local_space=None):

Node [Rotate Instances](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- rotation: Vector
- pivot_point: Vector
- local_space: Boolean

### Returns:

- node with sockets ['instances']

## rotation *property* {#rotation}

> def rotation(self):

Node [Instance Rotation](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'rotation'

## scale *property* {#scale}

> def scale(self):

Node [Instance Scale](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'scale'

## set_scale {#set_scale}

> def set_scale(self, scale=None, center=None, local_space=None):

Node [Scale Instances](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- scale: Vector
- center: Vector
- local_space: Boolean

### Returns:

- node with sockets ['instances']

## to_points {#to_points}

> def to_points(self, position=None, radius=None):

Node [Instances to Points](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- position: Vector
- radius: Float

### Returns:

  socket 'points' of class Points

## translate {#translate}

> def translate(self, translation=None, local_space=None):

Node [Translate Instances](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- translation: Vector
- local_space: Boolean

### Returns:

- node with sockets ['instances']

