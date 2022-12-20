# class Curve

## Properties

- [domain_size](#domain_size-property)
- [length](#length-property)
- [point_count](#point_count-property)
- [spline_count](#spline_count-property)

## Class methods

- [Arc](#Arc-classmethod)
- [ArcFromPoints](#ArcFromPoints-classmethod)
- [Circle](#Circle-classmethod)
- [CircleFromPoints](#CircleFromPoints-classmethod)
- [Line](#Line-classmethod)
- [LineDirection](#LineDirection-classmethod)
- [QuadraticBezier](#QuadraticBezier-classmethod)
- [Quadrilateral](#Quadrilateral-classmethod)
- [Spiral](#Spiral-classmethod)
- [Star](#Star-classmethod)
- [bezier_segment](#bezier_segment-classmethod)


## Methods

- [curve_of_point](#curve_of_point)
- [deform_on_surface](#deform_on_surface)
- [fill](#fill)
- [fill_ngons](#fill_ngons)
- [fill_triangles](#fill_triangles)
- [fillet](#fillet)
- [fillet_bezier](#fillet_bezier)
- [fillet_poly](#fillet_poly)
- [instance_on_points](#instance_on_points)
- [offset_point](#offset_point)
- [points_of_curve](#points_of_curve)
- [resample](#resample)
- [resample_count](#resample_count)
- [resample_evaluated](#resample_evaluated)
- [resample_length](#resample_length)
- [reverse](#reverse)
- [sample](#sample)
- [subdivide](#subdivide)
- [to_mesh](#to_mesh)
- [to_points](#to_points)
- [to_points_count](#to_points_count)
- [to_points_evaluated](#to_points_evaluated)
- [to_points_length](#to_points_length)
- [trim](#trim)
- [trim_factor](#trim_factor)
- [trim_length](#trim_length)

## Arc <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def Arc(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Arc](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/arc.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- resolution: Integer
<sub>Go to [top](#class-Curve)</sub>- radius: Float
<sub>Go to [top](#class-Curve)</sub>- start_angle: Float
<sub>Go to [top](#class-Curve)</sub>- sweep_angle: Float
<sub>Go to [top](#class-Curve)</sub>- connect_center: Boolean
<sub>Go to [top](#class-Curve)</sub>- invert_arc: Boolean
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>  socket 'curve'<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## ArcFromPoints <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def ArcFromPoints(cls, resolution=None, start=None, middle=None, end=None, offset_angle=None, connect_center=None, invert_arc=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Arc](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/arc.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- resolution: Integer
<sub>Go to [top](#class-Curve)</sub>- start: Vector
<sub>Go to [top](#class-Curve)</sub>- middle: Vector
<sub>Go to [top](#class-Curve)</sub>- end: Vector
<sub>Go to [top](#class-Curve)</sub>- offset_angle: Float
<sub>Go to [top](#class-Curve)</sub>- connect_center: Boolean
<sub>Go to [top](#class-Curve)</sub>- invert_arc: Boolean
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- node with sockets ['curve', 'center', 'normal', 'radius']
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## Circle <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def Circle(cls, resolution=None, radius=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Curve Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_circle.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- resolution: Integer
<sub>Go to [top](#class-Curve)</sub>- radius: Float
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>  socket 'curve'<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## CircleFromPoints <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def CircleFromPoints(cls, resolution=None, point_1=None, point_2=None, point_3=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Curve Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_circle.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- resolution: Integer
<sub>Go to [top](#class-Curve)</sub>- point_1: Vector
<sub>Go to [top](#class-Curve)</sub>- point_2: Vector
<sub>Go to [top](#class-Curve)</sub>- point_3: Vector
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- node with sockets ['curve', 'center']
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## Line <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def Line(cls, start=None, end=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Curve Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_line.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- start: Vector
<sub>Go to [top](#class-Curve)</sub>- end: Vector
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>  socket 'curve'<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## LineDirection <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def LineDirection(cls, start=None, direction=None, length=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Curve Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_line.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- start: Vector
<sub>Go to [top](#class-Curve)</sub>- direction: Vector
<sub>Go to [top](#class-Curve)</sub>- length: Float
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>  socket 'curve'<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## QuadraticBezier <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Quadratic Bezier](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/quadratic_bezier.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveQuadraticBezier.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- resolution: Integer
<sub>Go to [top](#class-Curve)</sub>- start: Vector
<sub>Go to [top](#class-Curve)</sub>- middle: Vector
<sub>Go to [top](#class-Curve)</sub>- end: Vector
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>  socket 'curve'<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## Quadrilateral <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def Quadrilateral(cls, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE'):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/quadrilateral.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveQuadrilateral.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- width: Float
<sub>Go to [top](#class-Curve)</sub>- height: Float
<sub>Go to [top](#class-Curve)</sub>- bottom_width: Float
<sub>Go to [top](#class-Curve)</sub>- top_width: Float
<sub>Go to [top](#class-Curve)</sub>- offset: Float
<sub>Go to [top](#class-Curve)</sub>- bottom_height: Float
<sub>Go to [top](#class-Curve)</sub>- top_height: Float
<sub>Go to [top](#class-Curve)</sub>- point_1: Vector
<sub>Go to [top](#class-Curve)</sub>- point_2: Vector
<sub>Go to [top](#class-Curve)</sub>- point_3: Vector
<sub>Go to [top](#class-Curve)</sub>- point_4: Vector
<sub>Go to [top](#class-Curve)</sub>- mode (str): 'RECTANGLE' in [RECTANGLE, PARALLELOGRAM, TRAPEZOID, KITE, POINTS]
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>  socket 'curve'<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## Spiral <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Spiral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_spiral.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSpiral.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- resolution: Integer
<sub>Go to [top](#class-Curve)</sub>- rotations: Float
<sub>Go to [top](#class-Curve)</sub>- start_radius: Float
<sub>Go to [top](#class-Curve)</sub>- end_radius: Float
<sub>Go to [top](#class-Curve)</sub>- height: Float
<sub>Go to [top](#class-Curve)</sub>- reverse: Boolean
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>  socket 'curve'<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## Star <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Star](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/star.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveStar.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- points: Integer
<sub>Go to [top](#class-Curve)</sub>- inner_radius: Float
<sub>Go to [top](#class-Curve)</sub>- outer_radius: Float
<sub>Go to [top](#class-Curve)</sub>- twist: Float
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- node with sockets ['curve', 'outer_points']
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## bezier_segment <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def bezier_segment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Bezier Segment](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/bezier_segment.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveBezierSegment.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- resolution: Integer
<sub>Go to [top](#class-Curve)</sub>- start: Vector
<sub>Go to [top](#class-Curve)</sub>- start_handle: Vector
<sub>Go to [top](#class-Curve)</sub>- end_handle: Vector
<sub>Go to [top](#class-Curve)</sub>- end: Vector
<sub>Go to [top](#class-Curve)</sub>- mode (str): 'POSITION' in [POSITION, OFFSET]
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>  socket 'curve'<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## curve_of_point

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def curve_of_point(self, point_index=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Curve of Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/curve_of_point.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- point_index: Integer
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- tuple ('curve_index', 'index_in_curve')
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## deform_on_surface

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def deform_on_surface(self):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Deform Curves on Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/deform_curves_on_surface.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeformCurvesOnSurface.html) )

<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- node with sockets ['curves']
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## domain_size <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def domain_size(self):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

<sub>Go to [top](#class-Curve)</sub>Node implemented as property.

<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## fill

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def fill(self, curve=None, mode='TRIANGLES'):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Fill Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- curve: Curve
<sub>Go to [top](#class-Curve)</sub>- mode (str): 'TRIANGLES' in [TRIANGLES, NGONS]
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>  socket 'mesh'<sub>Go to [top](#class-Curve)</sub> of class Mesh
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## fill_ngons

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def fill_ngons(self, curve=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Fill Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- curve: Curve
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>  socket 'mesh'<sub>Go to [top](#class-Curve)</sub> of class Mesh
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## fill_triangles

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def fill_triangles(self, curve=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Fill Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- curve: Curve
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>  socket 'mesh'<sub>Go to [top](#class-Curve)</sub> of class Mesh
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## fillet

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def fillet(self, count=None, radius=None, limit_radius=None, mode='BEZIER'):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Fillet Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- count: Integer
<sub>Go to [top](#class-Curve)</sub>- radius: Float
<sub>Go to [top](#class-Curve)</sub>- limit_radius: Boolean
<sub>Go to [top](#class-Curve)</sub>- mode (str): 'BEZIER' in [BEZIER, POLY]
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- node with sockets ['curve']
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## fillet_bezier

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def fillet_bezier(self, radius=None, limit_radius=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Fillet Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- radius: Float
<sub>Go to [top](#class-Curve)</sub>- limit_radius: Boolean
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- node with sockets ['curve']
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## fillet_poly

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def fillet_poly(self, count=None, radius=None, limit_radius=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Fillet Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- count: Integer
<sub>Go to [top](#class-Curve)</sub>- radius: Float
<sub>Go to [top](#class-Curve)</sub>- limit_radius: Boolean
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- node with sockets ['curve']
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## instance_on_points

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- selection: Boolean
<sub>Go to [top](#class-Curve)</sub>- instance: Geometry
<sub>Go to [top](#class-Curve)</sub>- pick_instance: Boolean
<sub>Go to [top](#class-Curve)</sub>- instance_index: Integer
<sub>Go to [top](#class-Curve)</sub>- rotation: Vector
<sub>Go to [top](#class-Curve)</sub>- scale: Vector
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>  socket 'instances'<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## length <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def length(self):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Curve Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_length.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveLength.html) )

<sub>Go to [top](#class-Curve)</sub>Node implemented as property.

<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>  socket 'length'<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## offset_point

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def offset_point(self, point_index=None, offset=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Offset Point in Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/offset_point_in_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetPointInCurve.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- point_index: Integer
<sub>Go to [top](#class-Curve)</sub>- offset: Integer
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- tuple ('is_valid_offset', 'point_index')
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## point_count <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def point_count(self):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

<sub>Go to [top](#class-Curve)</sub>Node implemented as property.

<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>  socket 'point_count'<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## points_of_curve

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def points_of_curve(self, curve_index=None, weights=None, sort_index=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Points of Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/points_of_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsOfCurve.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- curve_index: Integer
<sub>Go to [top](#class-Curve)</sub>- weights: Float
<sub>Go to [top](#class-Curve)</sub>- sort_index: Integer
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- tuple ('point_index', 'total')
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## resample

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def resample(self, selection=None, count=None, length=None, mode='COUNT'):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- selection: Boolean
<sub>Go to [top](#class-Curve)</sub>- count: Integer
<sub>Go to [top](#class-Curve)</sub>- length: Float
<sub>Go to [top](#class-Curve)</sub>- mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- node with sockets ['curve']
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## resample_count

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def resample_count(self, selection=None, count=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- selection: Boolean
<sub>Go to [top](#class-Curve)</sub>- count: Integer
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- node with sockets ['curve']
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## resample_evaluated

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def resample_evaluated(self, selection=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- selection: Boolean
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- node with sockets ['curve']
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## resample_length

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def resample_length(self, selection=None, length=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- selection: Boolean
<sub>Go to [top](#class-Curve)</sub>- length: Float
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- node with sockets ['curve']
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## reverse

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def reverse(self, selection=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Reverse Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/reverse_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeReverseCurve.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- selection: Boolean
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- node with sockets ['curve']
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## sample

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def sample(self, value=None, factor=None, length=None, curve_index=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Sample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleCurve.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
<sub>Go to [top](#class-Curve)</sub>- factor: Float
<sub>Go to [top](#class-Curve)</sub>- length: Float
<sub>Go to [top](#class-Curve)</sub>- curve_index: Integer
<sub>Go to [top](#class-Curve)</sub>- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
<sub>Go to [top](#class-Curve)</sub>- mode (str): 'FACTOR' in [FACTOR, LENGTH]
<sub>Go to [top](#class-Curve)</sub>- use_all_curves (bool): False
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- node with sockets ['value', 'position', 'tangent', 'normal']
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## spline_count <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def spline_count(self):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

<sub>Go to [top](#class-Curve)</sub>Node implemented as property.

<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>  socket 'spline_count'<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## subdivide

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def subdivide(self, cuts=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Subdivide Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/subdivide_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideCurve.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- cuts: Integer
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- node with sockets ['curve']
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## to_mesh

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def to_mesh(self, profile_curve=None, fill_caps=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Curve to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_mesh.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToMesh.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- profile_curve: Geometry
<sub>Go to [top](#class-Curve)</sub>- fill_caps: Boolean
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>  socket 'mesh'<sub>Go to [top](#class-Curve)</sub> of class Mesh
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## to_points

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def to_points(self, count=None, length=None, mode='COUNT'):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- count: Integer
<sub>Go to [top](#class-Curve)</sub>- length: Float
<sub>Go to [top](#class-Curve)</sub>- mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- tuple ('points', 'tangent', 'normal', 'rotation')
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## to_points_count

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def to_points_count(self, count=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- count: Integer
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- tuple ('points', 'tangent', 'normal', 'rotation')
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## to_points_evaluated

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def to_points_evaluated(self):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html) )

<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- tuple ('points', 'tangent', 'normal', 'rotation')
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## to_points_length

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def to_points_length(self, length=None):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- length: Float
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- tuple ('points', 'tangent', 'normal', 'rotation')
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## trim

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def trim(self, start=None, end=None, mode='FACTOR'):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Trim Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- mode (str): 'FACTOR' in [FACTOR, LENGTH]
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- node with sockets ['curve']
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## trim_factor

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def trim_factor(self, start=None, end=None, mode='FACTOR'):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Trim Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- start: Float
<sub>Go to [top](#class-Curve)</sub>- end: Float
<sub>Go to [top](#class-Curve)</sub>- mode (str): 'FACTOR' in [FACTOR, LENGTH]
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- node with sockets ['curve']
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>## trim_length

<sub>Go to [top](#class-Curve)</sub>```python
<sub>Go to [top](#class-Curve)</sub>def trim_length(self, start=None, end=None, mode='FACTOR'):

<sub>Go to [top](#class-Curve)</sub>```
<sub>Go to [top](#class-Curve)</sub>Node [Trim Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html) )

<sub>Go to [top](#class-Curve)</sub>### Args:
<sub>Go to [top](#class-Curve)</sub>- start: Float
<sub>Go to [top](#class-Curve)</sub>- end: Float
<sub>Go to [top](#class-Curve)</sub>- mode (str): 'FACTOR' in [FACTOR, LENGTH]
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>### Returns:

<sub>Go to [top](#class-Curve)</sub>- node with sockets ['curve']
<sub>Go to [top](#class-Curve)</sub>
<sub>Go to [top](#class-Curve)</sub>