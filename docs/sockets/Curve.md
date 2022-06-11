
# Data socket Curve

> Inherits from gn.Spline
  
<sub>go to [index](docs/index.md)</sub>



## Constructors

- [ArcFromRadius](#arcfromradius) : [Arc](section:nodes/Arc), curve (Curve)
- [BezierSegment](#beziersegment) : [BezierSegment](section:nodes/BezierSegment), curve (Curve)
- [Circle](#circle) : [CurveCircle](section:nodes/CurveCircle), Sockets      [curve (Curve), center (Vector)]
- [Line](#line) : [CurveLine](section:nodes/CurveLine), curve (Curve)
- [QuadraticBezier](#quadraticbezier) : [QuadraticBezier](section:nodes/QuadraticBezier), curve (Curve)
- [Quadrilateral](#quadrilateral) : [Quadrilateral](section:nodes/Quadrilateral), curve (Curve)
- [Spiral](#spiral) : [Spiral](section:nodes/Spiral), curve (Curve)
- [Star](#star) : [Star](section:nodes/Star), Sockets      [curve (Curve), outer_points (Boolean)]

## Static methods

- [ArcFromPoints](#arcfrompoints) : [Arc](section:nodes/Arc), Sockets      [curve (Curve), center (Vector), normal (Vector), radius (Float)]

## Methods

- [fill](#fill) : [FillCurve](section:nodes/FillCurve), mesh (Mesh)
- [fillet](#fillet) : [FilletCurve](section:nodes/FilletCurve), curve (Curve)
- [length](#length) : [CurveLength](section:nodes/CurveLength), length (Float)
- [resample](#resample) : [ResampleCurve](section:nodes/ResampleCurve), curve (Curve)
- [reverse](#reverse) : [ReverseCurve](section:nodes/ReverseCurve), curve (Curve)
- [sample](#sample) : [SampleCurve](section:nodes/SampleCurve), Sockets      [position (Vector), tangent (Vector), normal (Vector)]
- [set_handle_positions](#set_handle_positions) : [SetHandlePositions](section:nodes/SetHandlePositions), curve (Curve)
- [set_handles](#set_handles) : [SetHandleType](section:nodes/SetHandleType), curve (Curve)
- [set_radius](#set_radius) : [SetCurveRadius](section:nodes/SetCurveRadius), curve (Curve)
- [set_spline_type](#set_spline_type) : [SetSplineType](section:nodes/SetSplineType), curve (Curve)
- [set_tilt](#set_tilt) : [SetCurveTilt](section:nodes/SetCurveTilt), curve (Curve)
- [subdivide](#subdivide) : [SubdivideCurve](section:nodes/SubdivideCurve), curve (Curve)
- [to_mesh](#to_mesh) : [CurveToMesh](section:nodes/CurveToMesh), mesh (Mesh)
- [to_points](#to_points) : [CurveToPoints](section:nodes/CurveToPoints), Sockets      [points (Points), tangent (Vector), normal (Vector), rotation (Vector)]
- [trim](#trim) : [TrimCurve](section:nodes/TrimCurve), curve (Curve)

## BezierSegment

> Node: [BezierSegment](section:nodes/BezierSegment)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeCurvePrimitiveBezierSegment](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveBezierSegment.html)
node ref [Bezier Segment](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/bezier_segment.html) </sub>

```python
v = Curve.BezierSegment(resolution, start, start_handle, end_handle, end, mode)
```

### Arguments


#### Sockets

- resolution : Integer
- start : Vector
- start_handle : Vector
- end_handle : Vector
- end : Vector

#### Parameters

- mode : 'POSITION' in [POSITION, OFFSET]

### Node creation

```python
nodes.BezierSegment(resolution=resolution, start=start, start_handle=start_handle, end_handle=end_handle, end=end, mode=mode)
```

### Returns

Curve


## Circle

> Node: [CurveCircle](section:nodes/CurveCircle)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeCurvePrimitiveCircle](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html)
node ref [Curve Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/curve_circle.html) </sub>

```python
v = Curve.Circle(resolution, point_1, point_2, point_3, radius, mode)
```

### Arguments


#### Sockets

- resolution : Integer
- point_1 : Vector
- point_2 : Vector
- point_3 : Vector
- radius : Float

#### Parameters

- mode : 'RADIUS' in [POINTS, RADIUS]

### Node creation

```python
nodes.CurveCircle(resolution=resolution, point_1=point_1, point_2=point_2, point_3=point_3, radius=radius, mode=mode)
```

### Returns

Sockets [curve (Curve), center (Vector)]


## Line

> Node: [CurveLine](section:nodes/CurveLine)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeCurvePrimitiveLine](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html)
node ref [Curve Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/curve_line.html) </sub>

```python
v = Curve.Line(start, end, direction, length, mode)
```

### Arguments


#### Sockets

- start : Vector
- end : Vector
- direction : Vector
- length : Float

#### Parameters

- mode : 'POINTS' in [POINTS, DIRECTION]

### Node creation

```python
nodes.CurveLine(start=start, end=end, direction=direction, length=length, mode=mode)
```

### Returns

Curve


## Quadrilateral

> Node: [Quadrilateral](section:nodes/Quadrilateral)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeCurvePrimitiveQuadrilateral](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveQuadrilateral.html)
node ref [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/quadrilateral.html) </sub>

```python
v = Curve.Quadrilateral(width, height, bottom_width, top_width, offset, bottom_height, top_height, point_1, point_2, point_3, point_4, mode)
```

### Arguments


#### Sockets

- width : Float
- height : Float
- bottom_width : Float
- top_width : Float
- offset : Float
- bottom_height : Float
- top_height : Float
- point_1 : Vector
- point_2 : Vector
- point_3 : Vector
- point_4 : Vector

#### Parameters

- mode : 'RECTANGLE' in [RECTANGLE, PARALLELOGRAM, TRAPEZOID, KITE, POINTS]

### Node creation

```python
nodes.Quadrilateral(width=width, height=height, bottom_width=bottom_width, top_width=top_width, offset=offset, bottom_height=bottom_height, top_height=top_height, point_1=point_1, point_2=point_2, point_3=point_3, point_4=point_4, mode=mode)
```

### Returns

Curve


## QuadraticBezier

> Node: [QuadraticBezier](section:nodes/QuadraticBezier)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeCurveQuadraticBezier](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveQuadraticBezier.html)
node ref [Quadratic Bezier](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/quadratic_bezier.html) </sub>

```python
v = Curve.QuadraticBezier(resolution, start, middle, end)
```

### Arguments


#### Sockets

- resolution : Integer
- start : Vector
- middle : Vector
- end : Vector

### Node creation

```python
nodes.QuadraticBezier(resolution=resolution, start=start, middle=middle, end=end)
```

### Returns

Curve


## Star

> Node: [Star](section:nodes/Star)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeCurveStar](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveStar.html)
node ref [Star](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/star.html) </sub>

```python
v = Curve.Star(points, inner_radius, outer_radius, twist)
```

### Arguments


#### Sockets

- points : Integer
- inner_radius : Float
- outer_radius : Float
- twist : Float

### Node creation

```python
nodes.Star(points=points, inner_radius=inner_radius, outer_radius=outer_radius, twist=twist)
```

### Returns

Sockets [curve (Curve), outer_points (Boolean)]


## Spiral

> Node: [Spiral](section:nodes/Spiral)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeCurveSpiral](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSpiral.html)
node ref [Spiral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/spiral.html) </sub>

```python
v = Curve.Spiral(resolution, rotations, start_radius, end_radius, height, reverse)
```

### Arguments


#### Sockets

- resolution : Integer
- rotations : Float
- start_radius : Float
- end_radius : Float
- height : Float
- reverse : Boolean

### Node creation

```python
nodes.Spiral(resolution=resolution, rotations=rotations, start_radius=start_radius, end_radius=end_radius, height=height, reverse=reverse)
```

### Returns

Curve


## ArcFromRadius

> Node: [Arc](section:nodes/Arc)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeCurveArc](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html)
node ref [Arc](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/arc.html) </sub>

```python
v = Curve.ArcFromRadius(resolution, radius, start_angle, sweep_angle, connect_center, invert_arc)
```

### Arguments


#### Sockets

- resolution : Integer
- radius : Float
- start_angle : Float
- sweep_angle : Float
- connect_center : Boolean
- invert_arc : Boolean

#### Fixed parameters

- mode : 'RADIUS'

### Node creation

```python
nodes.Arc(resolution=resolution, radius=radius, start_angle=start_angle, sweep_angle=sweep_angle, connect_center=connect_center, invert_arc=invert_arc, mode='RADIUS')
```

### Returns

Curve


## ArcFromPoints

> Node: [Arc](section:nodes/Arc)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeCurveArc](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html)
node ref [Arc](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/arc.html) </sub>

```python
v = Curve.ArcFromPoints(resolution, start, middle, end, offset_angle, connect_center, invert_arc)
```

### Arguments


#### Sockets

- resolution : Integer
- start : Vector
- middle : Vector
- end : Vector
- offset_angle : Float
- connect_center : Boolean
- invert_arc : Boolean

#### Fixed parameters

- mode : 'POINTS'

### Node creation

```python
nodes.Arc(resolution=resolution, start=start, middle=middle, end=end, offset_angle=offset_angle, connect_center=connect_center, invert_arc=invert_arc, mode='POINTS')
```

### Returns

Sockets [curve (Curve), center (Vector), normal (Vector), radius (Float)]


## set_handles

> Node: [SetHandleType](section:nodes/SetHandleType)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeCurveSetHandles](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)
node ref [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_handle_type.html) </sub>

```python
v = curve.set_handles(selection, handle_type, mode)
```

### Arguments


#### Sockets

- curve : Curve (self)
- selection : Boolean

#### Parameters

- handle_type : 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode : {'LEFT', 'RIGHT'}

### Node creation

```python
nodes.SetHandleType(curve=self, selection=selection, handle_type=handle_type, mode=mode)
```

### Returns

Curve


## set_spline_type

> Node: [SetSplineType](section:nodes/SetSplineType)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeCurveSplineType](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)
node ref [Set Spline Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_spline_type.html) </sub>

```python
v = curve.set_spline_type(selection, spline_type)
```

### Arguments


#### Sockets

- curve : Curve (self)
- selection : Boolean

#### Parameters

- spline_type : 'POLY' in [BEZIER, NURBS, POLY]

### Node creation

```python
nodes.SetSplineType(curve=self, selection=selection, spline_type=spline_type)
```

### Returns

Curve


## fill

> Node: [FillCurve](section:nodes/FillCurve)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeFillCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)
node ref [Fill Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/fill_curve.html) </sub>

```python
v = curve.fill(mode)
```

### Arguments


#### Sockets

- curve : Curve (self)

#### Parameters

- mode : 'TRIANGLES' in [TRIANGLES, NGONS]

### Node creation

```python
nodes.FillCurve(curve=self, mode=mode)
```

### Returns

Mesh


## fillet

> Node: [FilletCurve](section:nodes/FilletCurve)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeFilletCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)
node ref [Fillet Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/fillet_curve.html) </sub>

```python
v = curve.fillet(count, radius, limit_radius, mode)
```

### Arguments


#### Sockets

- curve : Curve (self)
- count : Integer
- radius : Float
- limit_radius : Boolean

#### Parameters

- mode : 'BEZIER' in [BEZIER, POLY]

### Node creation

```python
nodes.FilletCurve(curve=self, count=count, radius=radius, limit_radius=limit_radius, mode=mode)
```

### Returns

Curve


## resample

> Node: [ResampleCurve](section:nodes/ResampleCurve)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeResampleCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)
node ref [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/resample_curve.html) </sub>

```python
v = curve.resample(selection, count, length, mode)
```

### Arguments


#### Sockets

- curve : Curve (self)
- selection : Boolean
- count : Integer
- length : Float

#### Parameters

- mode : 'COUNT' in [EVALUATED, COUNT, LENGTH]

### Node creation

```python
nodes.ResampleCurve(curve=self, selection=selection, count=count, length=length, mode=mode)
```

### Returns

Curve


## reverse

> Node: [ReverseCurve](section:nodes/ReverseCurve)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeReverseCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeReverseCurve.html)
node ref [Reverse Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/reverse_curve.html) </sub>

```python
v = curve.reverse(selection)
```

### Arguments


#### Sockets

- curve : Curve (self)
- selection : Boolean

### Node creation

```python
nodes.ReverseCurve(curve=self, selection=selection)
```

### Returns

Curve


## set_handle_positions

> Node: [SetHandlePositions](section:nodes/SetHandlePositions)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeSetCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)
node ref [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_handle_positions.html) </sub>

```python
v = curve.set_handle_positions(selection, position, offset, mode)
```

### Arguments


#### Sockets

- curve : Curve (self)
- selection : Boolean
- position : Vector
- offset : Vector

#### Parameters

- mode : 'LEFT' in [LEFT, RIGHT]

### Node creation

```python
nodes.SetHandlePositions(curve=self, selection=selection, position=position, offset=offset, mode=mode)
```

### Returns

Curve


## set_radius

> Node: [SetCurveRadius](section:nodes/SetCurveRadius)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeSetCurveRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html)
node ref [Set Curve Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_curve_radius.html) </sub>

```python
v = curve.set_radius(selection, radius)
```

### Arguments


#### Sockets

- curve : Curve (self)
- selection : Boolean
- radius : Float

### Node creation

```python
nodes.SetCurveRadius(curve=self, selection=selection, radius=radius)
```

### Returns

Curve


## set_tilt

> Node: [SetCurveTilt](section:nodes/SetCurveTilt)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeSetCurveTilt](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)
node ref [Set Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_curve_tilt.html) </sub>

```python
v = curve.set_tilt(selection, tilt)
```

### Arguments


#### Sockets

- curve : Curve (self)
- selection : Boolean
- tilt : Float

### Node creation

```python
nodes.SetCurveTilt(curve=self, selection=selection, tilt=tilt)
```

### Returns

Curve


## subdivide

> Node: [SubdivideCurve](section:nodes/SubdivideCurve)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeSubdivideCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideCurve.html)
node ref [Subdivide Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/subdivide_curve.html) </sub>

```python
v = curve.subdivide(cuts)
```

### Arguments


#### Sockets

- curve : Curve (self)
- cuts : Integer

### Node creation

```python
nodes.SubdivideCurve(curve=self, cuts=cuts)
```

### Returns

Curve


## trim

> Node: [TrimCurve](section:nodes/TrimCurve)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeTrimCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)
node ref [Trim Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/trim_curve.html) </sub>

```python
v = curve.trim(start0, end0, start1, end1, mode)
```

### Arguments


#### Sockets

- curve : Curve (self)
- start0 : Float
- end0 : Float
- start1 : Float
- end1 : Float

#### Parameters

- mode : 'FACTOR' in [FACTOR, LENGTH]

### Node creation

```python
nodes.TrimCurve(curve=self, start0=start0, end0=end0, start1=start1, end1=end1, mode=mode)
```

### Returns

Curve


## to_mesh

> Node: [CurveToMesh](section:nodes/CurveToMesh)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeCurveToMesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToMesh.html)
node ref [Curve to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/curve_to_mesh.html) </sub>

```python
v = curve.to_mesh(profile_curve, fill_caps)
```

### Arguments


#### Sockets

- curve : Curve (self)
- profile_curve : Geometry
- fill_caps : Boolean

### Node creation

```python
nodes.CurveToMesh(curve=self, profile_curve=profile_curve, fill_caps=fill_caps)
```

### Returns

Mesh


## to_points

> Node: [CurveToPoints](section:nodes/CurveToPoints)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeCurveToPoints](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)
node ref [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/curve_to_points.html) </sub>

```python
v = curve.to_points(count, length, mode)
```

### Arguments


#### Sockets

- curve : Curve (self)
- count : Integer
- length : Float

#### Parameters

- mode : 'COUNT' in [EVALUATED, COUNT, LENGTH]

### Node creation

```python
nodes.CurveToPoints(curve=self, count=count, length=length, mode=mode)
```

### Returns

Sockets [points (Points), tangent (Vector), normal (Vector), rotation (Vector)]


## sample

> Node: [SampleCurve](section:nodes/SampleCurve)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeSampleCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleCurve.html)
node ref [Sample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/sample_curve.html) </sub>

```python
v = curve.sample(factor, length, mode)
```

### Arguments


#### Sockets

- curve : Curve (self)
- factor : Float
- length : Float

#### Parameters

- mode : 'LENGTH' in [FACTOR, LENGTH]

### Node creation

```python
nodes.SampleCurve(curve=self, factor=factor, length=length, mode=mode)
```

### Returns

Sockets [position (Vector), tangent (Vector), normal (Vector)]


## length

> Node: [CurveLength](section:nodes/CurveLength)
  
<sub>go to: [top](#data-socket-curve) [index](docs/index.md)
blender ref [GeometryNodeCurveLength](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveLength.html)
node ref [Curve Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/curve_length.html) </sub>

```python
v = curve.length()
```

### Arguments


#### Sockets

- curve : Curve (self)

### Node creation

```python
nodes.CurveLength(curve=self)
```

### Returns

Float

