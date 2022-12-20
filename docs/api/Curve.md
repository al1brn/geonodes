# class {class_name}

## Arc *classmethod* {#Arc}

> def Arc(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None):

Node [Arc](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- resolution: Integer
- radius: Float
- start_angle: Float
- sweep_angle: Float
- connect_center: Boolean
- invert_arc: Boolean

### Returns:

  socket 'curve'

## ArcFromPoints *classmethod* {#ArcFromPoints}

> def ArcFromPoints(cls, resolution=None, start=None, middle=None, end=None, offset_angle=None, connect_center=None, invert_arc=None):

Node [Arc](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- resolution: Integer
- start: Vector
- middle: Vector
- end: Vector
- offset_angle: Float
- connect_center: Boolean
- invert_arc: Boolean

### Returns:

- node with sockets ['curve', 'center', 'normal', 'radius']

## Circle *classmethod* {#Circle}

> def Circle(cls, resolution=None, radius=None):

Node [Curve Circle](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- resolution: Integer
- radius: Float

### Returns:

  socket 'curve'

## CircleFromPoints *classmethod* {#CircleFromPoints}

> def CircleFromPoints(cls, resolution=None, point_1=None, point_2=None, point_3=None):

Node [Curve Circle](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- resolution: Integer
- point_1: Vector
- point_2: Vector
- point_3: Vector

### Returns:

- node with sockets ['curve', 'center']

## Line *classmethod* {#Line}

> def Line(cls, start=None, end=None):

Node [Curve Line](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- start: Vector
- end: Vector

### Returns:

  socket 'curve'

## LineDirection *classmethod* {#LineDirection}

> def LineDirection(cls, start=None, direction=None, length=None):

Node [Curve Line](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- start: Vector
- direction: Vector
- length: Float

### Returns:

  socket 'curve'

## QuadraticBezier *classmethod* {#QuadraticBezier}

> def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None):

Node [Quadratic Bezier](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- resolution: Integer
- start: Vector
- middle: Vector
- end: Vector

### Returns:

  socket 'curve'

## Quadrilateral *classmethod* {#Quadrilateral}

> def Quadrilateral(cls, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE'):

Node [Quadrilateral](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- width: Float
- height: Float
- bottom_width: Float
- top_width: Float
- offset: Float
- bottom_height: Float
- top_height: Float
- point_1: Vector
- point_2: Vector
- point_3: Vector
- point_4: Vector
- mode (str): 'RECTANGLE' in [RECTANGLE, PARALLELOGRAM, TRAPEZOID, KITE, POINTS]

### Returns:

  socket 'curve'

## Spiral *classmethod* {#Spiral}

> def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):

Node [Spiral](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- resolution: Integer
- rotations: Float
- start_radius: Float
- end_radius: Float
- height: Float
- reverse: Boolean

### Returns:

  socket 'curve'

## Star *classmethod* {#Star}

> def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):

Node [Star](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- points: Integer
- inner_radius: Float
- outer_radius: Float
- twist: Float

### Returns:

- node with sockets ['curve', 'outer_points']

## bezier_segment *classmethod* {#bezier_segment}

> def bezier_segment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):

Node [Bezier Segment](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- resolution: Integer
- start: Vector
- start_handle: Vector
- end_handle: Vector
- end: Vector
- mode (str): 'POSITION' in [POSITION, OFFSET]

### Returns:

  socket 'curve'

## curve_of_point {#curve_of_point}

> def curve_of_point(self, point_index=None):

Node [Curve of Point](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- point_index: Integer

### Returns:

- tuple ('curve_index', 'index_in_curve')

## deform_on_surface {#deform_on_surface}

> def deform_on_surface(self):

Node [Deform Curves on Surface](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

- node with sockets ['curves']

## domain_size *property* {#domain_size}

> def domain_size(self):

Node [Domain Size](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

## fill {#fill}

> def fill(self, curve=None, mode='TRIANGLES'):

Node [Fill Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- curve: Curve
- mode (str): 'TRIANGLES' in [TRIANGLES, NGONS]

### Returns:

  socket 'mesh' of class Mesh

## fill_ngons {#fill_ngons}

> def fill_ngons(self, curve=None):

Node [Fill Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- curve: Curve

### Returns:

  socket 'mesh' of class Mesh

## fill_triangles {#fill_triangles}

> def fill_triangles(self, curve=None):

Node [Fill Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- curve: Curve

### Returns:

  socket 'mesh' of class Mesh

## fillet {#fillet}

> def fillet(self, count=None, radius=None, limit_radius=None, mode='BEZIER'):

Node [Fillet Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- count: Integer
- radius: Float
- limit_radius: Boolean
- mode (str): 'BEZIER' in [BEZIER, POLY]

### Returns:

- node with sockets ['curve']

## fillet_bezier {#fillet_bezier}

> def fillet_bezier(self, radius=None, limit_radius=None):

Node [Fillet Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- radius: Float
- limit_radius: Boolean

### Returns:

- node with sockets ['curve']

## fillet_poly {#fillet_poly}

> def fillet_poly(self, count=None, radius=None, limit_radius=None):

Node [Fillet Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- count: Integer
- radius: Float
- limit_radius: Boolean

### Returns:

- node with sockets ['curve']

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

## length *property* {#length}

> def length(self):

Node [Curve Length](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'length'

## offset_point {#offset_point}

> def offset_point(self, point_index=None, offset=None):

Node [Offset Point in Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- point_index: Integer
- offset: Integer

### Returns:

- tuple ('is_valid_offset', 'point_index')

## point_count *property* {#point_count}

> def point_count(self):

Node [Domain Size](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'point_count'

## points_of_curve {#points_of_curve}

> def points_of_curve(self, curve_index=None, weights=None, sort_index=None):

Node [Points of Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- curve_index: Integer
- weights: Float
- sort_index: Integer

### Returns:

- tuple ('point_index', 'total')

## resample {#resample}

> def resample(self, selection=None, count=None, length=None, mode='COUNT'):

Node [Resample Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- count: Integer
- length: Float
- mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]

### Returns:

- node with sockets ['curve']

## resample_count {#resample_count}

> def resample_count(self, selection=None, count=None):

Node [Resample Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- count: Integer

### Returns:

- node with sockets ['curve']

## resample_evaluated {#resample_evaluated}

> def resample_evaluated(self, selection=None):

Node [Resample Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean

### Returns:

- node with sockets ['curve']

## resample_length {#resample_length}

> def resample_length(self, selection=None, length=None):

Node [Resample Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- length: Float

### Returns:

- node with sockets ['curve']

## reverse {#reverse}

> def reverse(self, selection=None):

Node [Reverse Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean

### Returns:

- node with sockets ['curve']

## sample {#sample}

> def sample(self, value=None, factor=None, length=None, curve_index=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False):

Node [Sample Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- factor: Float
- length: Float
- curve_index: Integer
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
- mode (str): 'FACTOR' in [FACTOR, LENGTH]
- use_all_curves (bool): False

### Returns:

- node with sockets ['value', 'position', 'tangent', 'normal']

## spline_count *property* {#spline_count}

> def spline_count(self):

Node [Domain Size](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'spline_count'

## subdivide {#subdivide}

> def subdivide(self, cuts=None):

Node [Subdivide Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- cuts: Integer

### Returns:

- node with sockets ['curve']

## to_mesh {#to_mesh}

> def to_mesh(self, profile_curve=None, fill_caps=None):

Node [Curve to Mesh](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- profile_curve: Geometry
- fill_caps: Boolean

### Returns:

  socket 'mesh' of class Mesh

## to_points {#to_points}

> def to_points(self, count=None, length=None, mode='COUNT'):

Node [Curve to Points](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- count: Integer
- length: Float
- mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]

### Returns:

- tuple ('points', 'tangent', 'normal', 'rotation')

## to_points_count {#to_points_count}

> def to_points_count(self, count=None):

Node [Curve to Points](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- count: Integer

### Returns:

- tuple ('points', 'tangent', 'normal', 'rotation')

## to_points_evaluated {#to_points_evaluated}

> def to_points_evaluated(self):

Node [Curve to Points](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

- tuple ('points', 'tangent', 'normal', 'rotation')

## to_points_length {#to_points_length}

> def to_points_length(self, length=None):

Node [Curve to Points](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- length: Float

### Returns:

- tuple ('points', 'tangent', 'normal', 'rotation')

## trim {#trim}

> def trim(self, start=None, end=None, mode='FACTOR'):

Node [Trim Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- mode (str): 'FACTOR' in [FACTOR, LENGTH]

### Returns:

- node with sockets ['curve']

## trim_factor {#trim_factor}

> def trim_factor(self, start=None, end=None, mode='FACTOR'):

Node [Trim Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- start: Float
- end: Float
- mode (str): 'FACTOR' in [FACTOR, LENGTH]

### Returns:

- node with sockets ['curve']

## trim_length {#trim_length}

> def trim_length(self, start=None, end=None, mode='FACTOR'):

Node [Trim Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- start: Float
- end: Float
- mode (str): 'FACTOR' in [FACTOR, LENGTH]

### Returns:

- node with sockets ['curve']

