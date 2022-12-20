# class {class_name}

## domain_size {#domain_size}

> def __len__(self):

Node [Domain Size](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- geometry: Geometry
- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

### Returns:

- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

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

## radius *property* {#radius}

> def radius(self):

Node [Radius](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'radius'

## radius *etter* {#radius}

> def radius(self, attr_value):

Node [Set Point Radius](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property setter.

        ###Args:- attr_value: radius


## to_vertices {#to_vertices}

> def to_vertices(self, points=None):

Node [Points to Vertices](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- points: Points

### Returns:

  socket 'mesh' of class Mesh

