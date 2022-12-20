# class Curve

## Properties

- [(domain_size](domain_size-property)
- [(length](length-property)
- [(point_count](point_count-property)
- [(spline_count](spline_count-property)

## Class methods

- [(Arc](Arc-classmethod)
- [(ArcFromPoints](ArcFromPoints-classmethod)
- [(Circle](Circle-classmethod)
- [(CircleFromPoints](CircleFromPoints-classmethod)
- [(Line](Line-classmethod)
- [(LineDirection](LineDirection-classmethod)
- [(QuadraticBezier](QuadraticBezier-classmethod)
- [(Quadrilateral](Quadrilateral-classmethod)
- [(Spiral](Spiral-classmethod)
- [(Star](Star-classmethod)
- [(bezier_segment](bezier_segment-classmethod)


## Methods

- [(curve_of_point](curve_of_point)
- [(deform_on_surface](deform_on_surface)
- [(fill](fill)
- [(fill_ngons](fill_ngons)
- [(fill_triangles](fill_triangles)
- [(fillet](fillet)
- [(fillet_bezier](fillet_bezier)
- [(fillet_poly](fillet_poly)
- [(instance_on_points](instance_on_points)
- [(offset_point](offset_point)
- [(points_of_curve](points_of_curve)
- [(resample](resample)
- [(resample_count](resample_count)
- [(resample_evaluated](resample_evaluated)
- [(resample_length](resample_length)
- [(reverse](reverse)
- [(sample](sample)
- [(subdivide](subdivide)
- [(to_mesh](to_mesh)
- [(to_points](to_points)
- [(to_points_count](to_points_count)
- [(to_points_evaluated](to_points_evaluated)
- [(to_points_length](to_points_length)
- [(trim](trim)
- [(trim_factor](trim_factor)
- [(trim_length](trim_length)

## Arc *classmethod*

{#Arc}

> def Arc(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None):

Node [Arc](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/arc.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html) )

        ### Args:
- resolution: Integer
- radius: Float
- start_angle: Float
- sweep_angle: Float
- connect_center: Boolean
- invert_arc: Boolean

### Returns:

  socket 'curve'

## ArcFromPoints *classmethod*

{#ArcFromPoints}

> def ArcFromPoints(cls, resolution=None, start=None, middle=None, end=None, offset_angle=None, connect_center=None, invert_arc=None):

Node [Arc](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/arc.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html) )

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

## Circle *classmethod*

{#Circle}

> def Circle(cls, resolution=None, radius=None):

Node [Curve Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_circle.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html) )

        ### Args:
- resolution: Integer
- radius: Float

### Returns:

  socket 'curve'

## CircleFromPoints *classmethod*

{#CircleFromPoints}

> def CircleFromPoints(cls, resolution=None, point_1=None, point_2=None, point_3=None):

Node [Curve Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_circle.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html) )

        ### Args:
- resolution: Integer
- point_1: Vector
- point_2: Vector
- point_3: Vector

### Returns:

- node with sockets ['curve', 'center']

## Line *classmethod*

{#Line}

> def Line(cls, start=None, end=None):

Node [Curve Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_line.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html) )

        ### Args:
- start: Vector
- end: Vector

### Returns:

  socket 'curve'

## LineDirection *classmethod*

{#LineDirection}

> def LineDirection(cls, start=None, direction=None, length=None):

Node [Curve Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_line.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html) )

        ### Args:
- start: Vector
- direction: Vector
- length: Float

### Returns:

  socket 'curve'

## QuadraticBezier *classmethod*

{#QuadraticBezier}

> def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None):

Node [Quadratic Bezier](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/quadratic_bezier.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveQuadraticBezier.html) )

        ### Args:
- resolution: Integer
- start: Vector
- middle: Vector
- end: Vector

### Returns:

  socket 'curve'

## Quadrilateral *classmethod*

{#Quadrilateral}

> def Quadrilateral(cls, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE'):

Node [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/quadrilateral.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveQuadrilateral.html) )

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

## Spiral *classmethod*

{#Spiral}

> def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):

Node [Spiral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_spiral.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSpiral.html) )

        ### Args:
- resolution: Integer
- rotations: Float
- start_radius: Float
- end_radius: Float
- height: Float
- reverse: Boolean

### Returns:

  socket 'curve'

## Star *classmethod*

{#Star}

> def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):

Node [Star](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/star.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveStar.html) )

        ### Args:
- points: Integer
- inner_radius: Float
- outer_radius: Float
- twist: Float

### Returns:

- node with sockets ['curve', 'outer_points']

## bezier_segment *classmethod*

{#bezier_segment}

> def bezier_segment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):

Node [Bezier Segment](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/bezier_segment.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveBezierSegment.html) )

        ### Args:
- resolution: Integer
- start: Vector
- start_handle: Vector
- end_handle: Vector
- end: Vector
- mode (str): 'POSITION' in [POSITION, OFFSET]

### Returns:

  socket 'curve'

## curve_of_point

{#curve_of_point}

> def curve_of_point(self, point_index=None):

Node [Curve of Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/curve_of_point.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html) )

        ### Args:
- point_index: Integer

### Returns:

- tuple ('curve_index', 'index_in_curve')

## deform_on_surface

{#deform_on_surface}

> def deform_on_surface(self):

Node [Deform Curves on Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/deform_curves_on_surface.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeformCurvesOnSurface.html) )

### Returns:

- node with sockets ['curves']

## domain_size *property*

{#domain_size}

> def domain_size(self):

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

Node implemented as property.

### Returns:

- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

## fill

{#fill}

> def fill(self, curve=None, mode='TRIANGLES'):

Node [Fill Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html) )

        ### Args:
- curve: Curve
- mode (str): 'TRIANGLES' in [TRIANGLES, NGONS]

### Returns:

  socket 'mesh' of class Mesh

## fill_ngons

{#fill_ngons}

> def fill_ngons(self, curve=None):

Node [Fill Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html) )

        ### Args:
- curve: Curve

### Returns:

  socket 'mesh' of class Mesh

## fill_triangles

{#fill_triangles}

> def fill_triangles(self, curve=None):

Node [Fill Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html) )

        ### Args:
- curve: Curve

### Returns:

  socket 'mesh' of class Mesh

## fillet

{#fillet}

> def fillet(self, count=None, radius=None, limit_radius=None, mode='BEZIER'):

Node [Fillet Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html) )

        ### Args:
- count: Integer
- radius: Float
- limit_radius: Boolean
- mode (str): 'BEZIER' in [BEZIER, POLY]

### Returns:

- node with sockets ['curve']

## fillet_bezier

{#fillet_bezier}

> def fillet_bezier(self, radius=None, limit_radius=None):

Node [Fillet Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html) )

        ### Args:
- radius: Float
- limit_radius: Boolean

### Returns:

- node with sockets ['curve']

## fillet_poly

{#fillet_poly}

> def fillet_poly(self, count=None, radius=None, limit_radius=None):

Node [Fillet Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html) )

        ### Args:
- count: Integer
- radius: Float
- limit_radius: Boolean

### Returns:

- node with sockets ['curve']

## instance_on_points

{#instance_on_points}

> def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html) )

        ### Args:
- selection: Boolean
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

### Returns:

  socket 'instances'

## length *property*

{#length}

> def length(self):

Node [Curve Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_length.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveLength.html) )

Node implemented as property.

### Returns:

  socket 'length'

## offset_point

{#offset_point}

> def offset_point(self, point_index=None, offset=None):

Node [Offset Point in Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/offset_point_in_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetPointInCurve.html) )

        ### Args:
- point_index: Integer
- offset: Integer

### Returns:

- tuple ('is_valid_offset', 'point_index')

## point_count *property*

{#point_count}

> def point_count(self):

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

Node implemented as property.

### Returns:

  socket 'point_count'

## points_of_curve

{#points_of_curve}

> def points_of_curve(self, curve_index=None, weights=None, sort_index=None):

Node [Points of Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/points_of_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsOfCurve.html) )

        ### Args:
- curve_index: Integer
- weights: Float
- sort_index: Integer

### Returns:

- tuple ('point_index', 'total')

## resample

{#resample}

> def resample(self, selection=None, count=None, length=None, mode='COUNT'):

Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html) )

        ### Args:
- selection: Boolean
- count: Integer
- length: Float
- mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]

### Returns:

- node with sockets ['curve']

## resample_count

{#resample_count}

> def resample_count(self, selection=None, count=None):

Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html) )

        ### Args:
- selection: Boolean
- count: Integer

### Returns:

- node with sockets ['curve']

## resample_evaluated

{#resample_evaluated}

> def resample_evaluated(self, selection=None):

Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html) )

        ### Args:
- selection: Boolean

### Returns:

- node with sockets ['curve']

## resample_length

{#resample_length}

> def resample_length(self, selection=None, length=None):

Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html) )

        ### Args:
- selection: Boolean
- length: Float

### Returns:

- node with sockets ['curve']

## reverse

{#reverse}

> def reverse(self, selection=None):

Node [Reverse Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/reverse_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeReverseCurve.html) )

        ### Args:
- selection: Boolean

### Returns:

- node with sockets ['curve']

## sample

{#sample}

> def sample(self, value=None, factor=None, length=None, curve_index=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False):

Node [Sample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleCurve.html) )

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

## spline_count *property*

{#spline_count}

> def spline_count(self):

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

Node implemented as property.

### Returns:

  socket 'spline_count'

## subdivide

{#subdivide}

> def subdivide(self, cuts=None):

Node [Subdivide Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/subdivide_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideCurve.html) )

        ### Args:
- cuts: Integer

### Returns:

- node with sockets ['curve']

## to_mesh

{#to_mesh}

> def to_mesh(self, profile_curve=None, fill_caps=None):

Node [Curve to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_mesh.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToMesh.html) )

        ### Args:
- profile_curve: Geometry
- fill_caps: Boolean

### Returns:

  socket 'mesh' of class Mesh

## to_points

{#to_points}

> def to_points(self, count=None, length=None, mode='COUNT'):

Node [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html) )

        ### Args:
- count: Integer
- length: Float
- mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]

### Returns:

- tuple ('points', 'tangent', 'normal', 'rotation')

## to_points_count

{#to_points_count}

> def to_points_count(self, count=None):

Node [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html) )

        ### Args:
- count: Integer

### Returns:

- tuple ('points', 'tangent', 'normal', 'rotation')

## to_points_evaluated

{#to_points_evaluated}

> def to_points_evaluated(self):

Node [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html) )

### Returns:

- tuple ('points', 'tangent', 'normal', 'rotation')

## to_points_length

{#to_points_length}

> def to_points_length(self, length=None):

Node [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html) )

        ### Args:
- length: Float

### Returns:

- tuple ('points', 'tangent', 'normal', 'rotation')

## trim

{#trim}

> def trim(self, start=None, end=None, mode='FACTOR'):

Node [Trim Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html) )

        ### Args:
- mode (str): 'FACTOR' in [FACTOR, LENGTH]

### Returns:

- node with sockets ['curve']

## trim_factor

{#trim_factor}

> def trim_factor(self, start=None, end=None, mode='FACTOR'):

Node [Trim Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html) )

        ### Args:
- start: Float
- end: Float
- mode (str): 'FACTOR' in [FACTOR, LENGTH]

### Returns:

- node with sockets ['curve']

## trim_length

{#trim_length}

> def trim_length(self, start=None, end=None, mode='FACTOR'):

Node [Trim Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html) )

        ### Args:
- start: Float
- end: Float
- mode (str): 'FACTOR' in [FACTOR, LENGTH]

### Returns:

- node with sockets ['curve']

