# class Curve

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

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

## Arc <sub>*classmethod*</sub>

```python
def Arc(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None):

```
> Node: [Arc](GeometryNodeCurveArc.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/arc.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html)

#### Args:
- resolution: Integer
- radius: Float
- start_angle: Float
- sweep_angle: Float
- connect_center: Boolean
- invert_arc: Boolean

#### Returns:
- socket `curve`

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## ArcFromPoints <sub>*classmethod*</sub>

```python
def ArcFromPoints(cls, resolution=None, start=None, middle=None, end=None, offset_angle=None, connect_center=None, invert_arc=None):

```
> Node: [Arc](GeometryNodeCurveArc.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/arc.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html)

#### Args:
- resolution: Integer
- start: Vector
- middle: Vector
- end: Vector
- offset_angle: Float
- connect_center: Boolean
- invert_arc: Boolean

#### Returns:
- node with sockets ['curve', 'center', 'normal', 'radius']

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Circle <sub>*classmethod*</sub>

```python
def Circle(cls, resolution=None, radius=None):

```
> Node: [Curve Circle](GeometryNodeCurvePrimitiveCircle.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_circle.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html)

#### Args:
- resolution: Integer
- radius: Float

#### Returns:
- socket `curve`

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## CircleFromPoints <sub>*classmethod*</sub>

```python
def CircleFromPoints(cls, resolution=None, point_1=None, point_2=None, point_3=None):

```
> Node: [Curve Circle](GeometryNodeCurvePrimitiveCircle.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_circle.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html)

#### Args:
- resolution: Integer
- point_1: Vector
- point_2: Vector
- point_3: Vector

#### Returns:
- node with sockets ['curve', 'center']

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Line <sub>*classmethod*</sub>

```python
def Line(cls, start=None, end=None):

```
> Node: [Curve Line](GeometryNodeCurvePrimitiveLine.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_line.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html)

#### Args:
- start: Vector
- end: Vector

#### Returns:
- socket `curve`

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## LineDirection <sub>*classmethod*</sub>

```python
def LineDirection(cls, start=None, direction=None, length=None):

```
> Node: [Curve Line](GeometryNodeCurvePrimitiveLine.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_line.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html)

#### Args:
- start: Vector
- direction: Vector
- length: Float

#### Returns:
- socket `curve`

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## QuadraticBezier <sub>*classmethod*</sub>

```python
def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None):

```
> Node: [Quadratic Bezier](GeometryNodeCurveQuadraticBezier.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/quadratic_bezier.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveQuadraticBezier.html)

#### Args:
- resolution: Integer
- start: Vector
- middle: Vector
- end: Vector

#### Returns:
- socket `curve`

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Quadrilateral <sub>*classmethod*</sub>

```python
def Quadrilateral(cls, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE'):

```
> Node: [Quadrilateral](GeometryNodeCurvePrimitiveQuadrilateral.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/quadrilateral.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveQuadrilateral.html)

#### Args:
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

#### Returns:
- socket `curve`

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Spiral <sub>*classmethod*</sub>

```python
def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):

```
> Node: [Spiral](GeometryNodeCurveSpiral.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_spiral.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSpiral.html)

#### Args:
- resolution: Integer
- rotations: Float
- start_radius: Float
- end_radius: Float
- height: Float
- reverse: Boolean

#### Returns:
- socket `curve`

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Star <sub>*classmethod*</sub>

```python
def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):

```
> Node: [Star](GeometryNodeCurveStar.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/star.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveStar.html)

#### Args:
- points: Integer
- inner_radius: Float
- outer_radius: Float
- twist: Float

#### Returns:
- node with sockets ['curve', 'outer_points']

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## bezier_segment <sub>*classmethod*</sub>

```python
def bezier_segment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):

```
> Node: [Bezier Segment](GeometryNodeCurvePrimitiveBezierSegment.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/bezier_segment.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveBezierSegment.html)

#### Args:
- resolution: Integer
- start: Vector
- start_handle: Vector
- end_handle: Vector
- end: Vector
- mode (str): 'POSITION' in [POSITION, OFFSET]

#### Returns:
- socket `curve`

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## curve_of_point

```python
def curve_of_point(self, point_index=None):

```
> Node: [Curve of Point](GeometryNodeCurveOfPoint.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/curve_of_point.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html)

#### Args:
- point_index: Integer

#### Returns:
- tuple ('`curve_index`', '`index_in_curve`')
  [Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveOfPoint.webp)

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## deform_on_surface

```python
def deform_on_surface(self):

```
> Node: [Deform Curves on Surface](GeometryNodeDeformCurvesOnSurface.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/deform_curves_on_surface.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeformCurvesOnSurface.html)

#### Returns:
- self

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## domain_size <sub>*property*</sub>

```python
def domain_size(self):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## fill

```python
def fill(self, curve=None, mode='TRIANGLES'):

```
> Node: [Fill Curve](GeometryNodeFillCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)

#### Args:
- curve: Curve
- mode (str): 'TRIANGLES' in [TRIANGLES, NGONS]

#### Returns:
- socket `mesh` of class Mesh

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## fill_ngons

```python
def fill_ngons(self, curve=None):

```
> Node: [Fill Curve](GeometryNodeFillCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)

#### Args:
- curve: Curve

#### Returns:
- socket `mesh` of class Mesh

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## fill_triangles

```python
def fill_triangles(self, curve=None):

```
> Node: [Fill Curve](GeometryNodeFillCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)

#### Args:
- curve: Curve

#### Returns:
- socket `mesh` of class Mesh

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## fillet

```python
def fillet(self, count=None, radius=None, limit_radius=None, mode='BEZIER'):

```
> Node: [Fillet Curve](GeometryNodeFilletCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)

#### Args:
- count: Integer
- radius: Float
- limit_radius: Boolean
- mode (str): 'BEZIER' in [BEZIER, POLY]

#### Returns:
- self

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## fillet_bezier

```python
def fillet_bezier(self, radius=None, limit_radius=None):

```
> Node: [Fillet Curve](GeometryNodeFilletCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)

#### Args:
- radius: Float
- limit_radius: Boolean

#### Returns:
- self

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## fillet_poly

```python
def fillet_poly(self, count=None, radius=None, limit_radius=None):

```
> Node: [Fillet Curve](GeometryNodeFilletCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)

#### Args:
- count: Integer
- radius: Float
- limit_radius: Boolean

#### Returns:
- self

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## instance_on_points

```python
def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

```
> Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

#### Args:
- selection: Boolean
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

#### Returns:
- socket `instances`

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## length <sub>*property*</sub>

```python
def length(self):

```
> Node: [Curve Length](GeometryNodeCurveLength.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_length.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveLength.html)

#### Returns:
- socket `length`

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## offset_point

```python
def offset_point(self, point_index=None, offset=None):

```
> Node: [Offset Point in Curve](GeometryNodeOffsetPointInCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/offset_point_in_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetPointInCurve.html)

#### Args:
- point_index: Integer
- offset: Integer

#### Returns:
- tuple ('`is_valid_offset`', '`point_index`')
  [Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeOffsetPointInCurve.webp)

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## point_count <sub>*property*</sub>

```python
def point_count(self):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `point_count`

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## points_of_curve

```python
def points_of_curve(self, curve_index=None, weights=None, sort_index=None):

```
> Node: [Points of Curve](GeometryNodePointsOfCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/points_of_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsOfCurve.html)

#### Args:
- curve_index: Integer
- weights: Float
- sort_index: Integer

#### Returns:
- tuple ('`point_index`', '`total`')
  [Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePointsOfCurve.webp)

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## resample

```python
def resample(self, selection=None, count=None, length=None, mode='COUNT'):

```
> Node: [Resample Curve](GeometryNodeResampleCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

#### Args:
- selection: Boolean
- count: Integer
- length: Float
- mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]

#### Returns:
- self

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## resample_count

```python
def resample_count(self, selection=None, count=None):

```
> Node: [Resample Curve](GeometryNodeResampleCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

#### Args:
- selection: Boolean
- count: Integer

#### Returns:
- self

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## resample_evaluated

```python
def resample_evaluated(self, selection=None):

```
> Node: [Resample Curve](GeometryNodeResampleCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

#### Args:
- selection: Boolean

#### Returns:
- self

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## resample_length

```python
def resample_length(self, selection=None, length=None):

```
> Node: [Resample Curve](GeometryNodeResampleCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

#### Args:
- selection: Boolean
- length: Float

#### Returns:
- self

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## reverse

```python
def reverse(self, selection=None):

```
> Node: [Reverse Curve](GeometryNodeReverseCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/reverse_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeReverseCurve.html)

#### Args:
- selection: Boolean

#### Returns:
- self

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## sample

```python
def sample(self, value=None, factor=None, length=None, curve_index=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False):

```
> Node: [Sample Curve](GeometryNodeSampleCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleCurve.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- factor: Float
- length: Float
- curve_index: Integer
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
- mode (str): 'FACTOR' in [FACTOR, LENGTH]
- use_all_curves (bool): False

#### Returns:
- self

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## spline_count <sub>*property*</sub>

```python
def spline_count(self):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `spline_count`

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## subdivide

```python
def subdivide(self, cuts=None):

```
> Node: [Subdivide Curve](GeometryNodeSubdivideCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/subdivide_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideCurve.html)

#### Args:
- cuts: Integer

#### Returns:
- self

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_mesh

```python
def to_mesh(self, profile_curve=None, fill_caps=None):

```
> Node: [Curve to Mesh](GeometryNodeCurveToMesh.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_mesh.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToMesh.html)

#### Args:
- profile_curve: Geometry
- fill_caps: Boolean

#### Returns:
- socket `mesh` of class Mesh

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_points

```python
def to_points(self, count=None, length=None, mode='COUNT'):

```
> Node: [Curve to Points](GeometryNodeCurveToPoints.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)

#### Args:
- count: Integer
- length: Float
- mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]

#### Returns:
- tuple ('`points`', '`tangent`', '`normal`', '`rotation`')
  [Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveToPoints.webp)

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_points_count

```python
def to_points_count(self, count=None):

```
> Node: [Curve to Points](GeometryNodeCurveToPoints.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)

#### Args:
- count: Integer

#### Returns:
- tuple ('`points`', '`tangent`', '`normal`', '`rotation`')
  [Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveToPoints.webp)

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_points_evaluated

```python
def to_points_evaluated(self):

```
> Node: [Curve to Points](GeometryNodeCurveToPoints.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)

#### Returns:
- tuple ('`points`', '`tangent`', '`normal`', '`rotation`')
  [Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveToPoints.webp)

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_points_length

```python
def to_points_length(self, length=None):

```
> Node: [Curve to Points](GeometryNodeCurveToPoints.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)

#### Args:
- length: Float

#### Returns:
- tuple ('`points`', '`tangent`', '`normal`', '`rotation`')
  [Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveToPoints.webp)

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## trim

```python
def trim(self, start=None, end=None, mode='FACTOR'):

```
> Node: [Trim Curve](GeometryNodeTrimCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)

#### Args:
- mode (str): 'FACTOR' in [FACTOR, LENGTH]

#### Returns:
- self

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## trim_factor

```python
def trim_factor(self, start=None, end=None):

```
> Node: [Trim Curve](GeometryNodeTrimCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)

#### Args:
- start: Float
- end: Float

#### Returns:
- self

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## trim_length

```python
def trim_length(self, start=None, end=None):

```
> Node: [Trim Curve](GeometryNodeTrimCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)

#### Args:
- start: Float
- end: Float

#### Returns:
- self

<sub>Go to [top](#class-Curve) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

