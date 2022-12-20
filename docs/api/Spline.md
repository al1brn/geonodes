# class {class_name}

## cyclic *property* {#cyclic}

> def cyclic(self):

Node [Is Spline Cyclic](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'cyclic'

## cyclic *etter* {#cyclic}

> def cyclic(self, attr_value):

Node [Set Spline Cyclic](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property setter.

        ###Args:- attr_value: cyclic


## domain_size {#domain_size}

> def __len__(self):

Node [Domain Size](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- geometry: Geometry
- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

### Returns:

- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

## length *property* {#length}

> def length(self):

Node [Spline Length](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

- tuple ('length', 'point_count')

## material *property* {#material}

> def material(self):

Node [Set Material](node.blender_ref) ( [api](node.blender_python_ref) )

'material' is a write only property.
Raise an exception if attempt to read.


## material *etter* {#material}

> def material(self, attr_value):

Node [Set Material](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property setter.

        ###Args:- attr_value: material


## normal *property* {#normal}

> def normal(self):

Node [Normal](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'normal'

## normal *etter* {#normal}

> def normal(self, attr_value):

Node [Set Curve Normal](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property setter.

        ###Args:- attr_value: mode


## points {#points}

> def points(self, weights=None, sort_index=None):

Node [Points of Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- weights: Float
- sort_index: Integer

### Returns:

- tuple ('point_index', 'total')

## resample {#resample}

> def resample(self, count=None, length=None, mode='COUNT'):

Node [Resample Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- count: Integer
- length: Float
- mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]

### Returns:

- node with sockets ['curve']

## resample_count {#resample_count}

> def resample_count(self, count=None):

Node [Resample Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- count: Integer

### Returns:

- node with sockets ['curve']

## resample_evaluated {#resample_evaluated}

> def resample_evaluated(self):

Node [Resample Curve](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

- node with sockets ['curve']

## resample_length {#resample_length}

> def resample_length(self, length=None):

Node [Resample Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- length: Float

### Returns:

- node with sockets ['curve']

## resolution *property* {#resolution}

> def resolution(self):

Node [Spline Resolution](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'resolution'

## resolution *etter* {#resolution}

> def resolution(self, attr_value):

Node [Set Spline Resolution](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property setter.

        ###Args:- attr_value: resolution


## set_cyclic {#set_cyclic}

> def set_cyclic(self, cyclic=None):

Node [Set Spline Cyclic](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- cyclic: Boolean

### Returns:

- node with sockets ['geometry']

## set_material {#set_material}

> def set_material(self, material=None):

Node [Set Material](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- material: Material

### Returns:

- node with sockets ['geometry']

## set_normal {#set_normal}

> def set_normal(self, mode='MINIMUM_TWIST'):

Node [Set Curve Normal](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- mode (str): 'MINIMUM_TWIST' in [MINIMUM_TWIST, Z_UP]

### Returns:

- node with sockets ['curve']

## set_resolution {#set_resolution}

> def set_resolution(self, resolution=None):

Node [Set Spline Resolution](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- resolution: Integer

### Returns:

- node with sockets ['geometry']

## set_type {#set_type}

> def set_type(self, spline_type='POLY'):

Node [Set Spline Type](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- spline_type (str): 'POLY' in [CATMULL_ROM, POLY, BEZIER, NURBS]

### Returns:

- node with sockets ['curve']

## type *property* {#type}

> def type(self):

Node [Set Spline Type](node.blender_ref) ( [api](node.blender_python_ref) )

'type' is a write only property.
Raise an exception if attempt to read.


## type *etter* {#type}

> def type(self, attr_value):

Node [Set Spline Type](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property setter.

        ###Args:- attr_value: spline_type


