# class {class_name}

## Points *classmethod* {#Points}

> def Points(cls, count=None, position=None, radius=None):

Node [Points](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- count: Integer
- position: Vector
- radius: Float

### Returns:

  socket 'geometry'

## domain_size *property* {#domain_size}

> def domain_size(self):

Node [Domain Size](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'point_count'

## instance_on_points {#instance_on_points}

> def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

Node [Instance on Points](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

### Returns:

  socket 'instances'

## set_point_radius {#set_point_radius}

> def set_point_radius(self, selection=None, radius=None):

Node [Set Point Radius](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- radius: Float

### Returns:

- node with sockets ['points']

## to_vertices {#to_vertices}

> def to_vertices(self, points=None, selection=None):

Node [Points to Vertices](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- points: Points
- selection: Boolean

### Returns:

  socket 'mesh' of class Mesh

## to_volume {#to_volume}

> def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):

Node [Points to Volume](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- density: Float
- voxel_size: Float
- voxel_amount: Float
- radius: Float
- resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]

### Returns:

  socket 'volume' of class Volume

## to_volume_amount {#to_volume_amount}

> def to_volume_amount(self, density=None, voxel_amount=None, radius=None):

Node [Points to Volume](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- density: Float
- voxel_amount: Float
- radius: Float

### Returns:

  socket 'volume' of class Volume

## to_volume_size {#to_volume_size}

> def to_volume_size(self, density=None, voxel_size=None, radius=None):

Node [Points to Volume](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- density: Float
- voxel_size: Float
- radius: Float

### Returns:

  socket 'volume' of class Volume

