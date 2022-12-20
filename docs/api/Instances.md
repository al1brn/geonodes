# class {class_name}

## InstanceOnPoints *classmethod* {#InstanceOnPoints}

> def InstanceOnPoints(cls, points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

Node [Instance on Points](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- points: Points
- selection: Boolean
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

### Returns:

  socket 'instances'

## domain_size *property* {#domain_size}

> def domain_size(self):

Node [Domain Size](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'instance_count'

## on_points {#on_points}

> def on_points(self, points=None, selection=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

Node [Instance on Points](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- points: Points
- selection: Boolean
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

### Returns:

  socket 'instances'

## realize {#realize}

> def realize(self, geometry=None, legacy_behavior=False):

Node [Realize Instances](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- geometry: Geometry
- legacy_behavior (bool): False

### Returns:

  socket 'geometry'

## rotate {#rotate}

> def rotate(self, selection=None, rotation=None, pivot_point=None, local_space=None):

Node [Rotate Instances](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
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

> def set_scale(self, selection=None, scale=None, center=None, local_space=None):

Node [Scale Instances](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- scale: Vector
- center: Vector
- local_space: Boolean

### Returns:

- node with sockets ['instances']

## to_points {#to_points}

> def to_points(self, selection=None, position=None, radius=None):

Node [Instances to Points](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- position: Vector
- radius: Float

### Returns:

  socket 'points' of class Points

## translate {#translate}

> def translate(self, selection=None, translation=None, local_space=None):

Node [Translate Instances](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- translation: Vector
- local_space: Boolean

### Returns:

- node with sockets ['instances']

