
# Data socket Curve

> Inherits from gn.Spline
  
<sub>go to [index](/docs/index.md)</sub>



## Constructors

- [ArcFromRadius](#arcfromradius) : curve (Curve)
- [BezierSegment](#beziersegment) : curve (Curve)
- [Circle](#circle) : Sockets      [curve (Curve), center (Vector)]
- [Line](#line) : curve (Curve)
- [QuadraticBezier](#quadraticbezier) : curve (Curve)
- [Quadrilateral](#quadrilateral) : curve (Curve)
- [Spiral](#spiral) : curve (Curve)
- [Star](#star) : Sockets      [curve (Curve), outer_points (Boolean)]

## Static methods

- [ArcFromPoints](#arcfrompoints) : Sockets      [curve (Curve), center (Vector), normal (Vector), radius (Float)]

## Methods

- [fill](#fill) : mesh (Mesh)
- [fillet](#fillet) : curve (Curve)
- [length](#length) : length (Float)
- [resample](#resample) : curve (Curve)
- [reverse](#reverse) : curve (Curve)
- [sample](#sample) : Sockets      [position (Vector), tangent (Vector), normal (Vector)]
- [set_handle_positions](#set_handle_positions) : curve (Curve)
- [set_handles](#set_handles) : curve (Curve)
- [set_radius](#set_radius) : curve (Curve)
- [set_spline_type](#set_spline_type) : curve (Curve)
- [set_tilt](#set_tilt) : curve (Curve)
- [subdivide](#subdivide) : curve (Curve)
- [to_mesh](#to_mesh) : mesh (Mesh)
- [to_points](#to_points) : Sockets      [points (Points), tangent (Vector), normal (Vector), rotation (Vector)]
- [trim](#trim) : curve (Curve)

## BezierSegment

> Node: [BezierSegment](/docs/nodes/BezierSegment.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeCurvePrimitiveBezierSegment](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveBezierSegment.html)
node ref [Bezier Segment](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/bezier_segment.html) </sub>
                          
```python
v = Curve.BezierSegment(resolution, start, start_handle, end_handle, end, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- resolution : Integer
- start : Vector
- start_handle : Vector
- end_handle : Vector
- end : Vector## Parameters
- mode : 'POSITION' in [POSITION, OFFSET]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.BezierSegment(resolution=resolution, start=start, start_handle=start_handle, end_handle=end_handle, end=end, mode=mode, label=node_label, node_color=node_color)
```

### Returns

Curve


## Circle

> Node: [CurveCircle](/docs/nodes/CurveCircle.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeCurvePrimitiveCircle](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html)
node ref [Curve Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_circle.html) </sub>
                          
```python
v = Curve.Circle(resolution, point_1, point_2, point_3, radius, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- resolution : Integer
- point_1 : Vector
- point_2 : Vector
- point_3 : Vector
- radius : Float## Parameters
- mode : 'RADIUS' in [POINTS, RADIUS]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.CurveCircle(resolution=resolution, point_1=point_1, point_2=point_2, point_3=point_3, radius=radius, mode=mode, label=node_label, node_color=node_color)
```

### Returns

Sockets [curve (Curve), center (Vector)]


## Line

> Node: [CurveLine](/docs/nodes/CurveLine.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeCurvePrimitiveLine](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html)
node ref [Curve Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_line.html) </sub>
                          
```python
v = Curve.Line(start, end, direction, length, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- start : Vector
- end : Vector
- direction : Vector
- length : Float## Parameters
- mode : 'POINTS' in [POINTS, DIRECTION]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.CurveLine(start=start, end=end, direction=direction, length=length, mode=mode, label=node_label, node_color=node_color)
```

### Returns

Curve


## Quadrilateral

> Node: [Quadrilateral](/docs/nodes/Quadrilateral.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeCurvePrimitiveQuadrilateral](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveQuadrilateral.html)
node ref [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/quadrilateral.html) </sub>
                          
```python
v = Curve.Quadrilateral(width, height, bottom_width, top_width, offset, bottom_height, top_height, point_1, point_2, point_3, point_4, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
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
- point_4 : Vector## Parameters
- mode : 'RECTANGLE' in [RECTANGLE, PARALLELOGRAM, TRAPEZOID, KITE, POINTS]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.Quadrilateral(width=width, height=height, bottom_width=bottom_width, top_width=top_width, offset=offset, bottom_height=bottom_height, top_height=top_height, point_1=point_1, point_2=point_2, point_3=point_3, point_4=point_4, mode=mode, label=node_label, node_color=node_color)
```

### Returns

Curve


## QuadraticBezier

> Node: [QuadraticBezier](/docs/nodes/QuadraticBezier.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeCurveQuadraticBezier](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveQuadraticBezier.html)
node ref [Quadratic Bezier](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/quadratic_bezier.html) </sub>
                          
```python
v = Curve.QuadraticBezier(resolution, start, middle, end, node_label = None, node_color = None)
```

### Arguments

## Sockets
- resolution : Integer
- start : Vector
- middle : Vector
- end : Vector## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.QuadraticBezier(resolution=resolution, start=start, middle=middle, end=end, label=node_label, node_color=node_color)
```

### Returns

Curve


## Star

> Node: [Star](/docs/nodes/Star.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeCurveStar](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveStar.html)
node ref [Star](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/star.html) </sub>
                          
```python
v = Curve.Star(points, inner_radius, outer_radius, twist, node_label = None, node_color = None)
```

### Arguments

## Sockets
- points : Integer
- inner_radius : Float
- outer_radius : Float
- twist : Float## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.Star(points=points, inner_radius=inner_radius, outer_radius=outer_radius, twist=twist, label=node_label, node_color=node_color)
```

### Returns

Sockets [curve (Curve), outer_points (Boolean)]


## Spiral

> Node: [Spiral](/docs/nodes/Spiral.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeCurveSpiral](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSpiral.html)
node ref [Spiral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_spiral.html) </sub>
                          
```python
v = Curve.Spiral(resolution, rotations, start_radius, end_radius, height, reverse, node_label = None, node_color = None)
```

### Arguments

## Sockets
- resolution : Integer
- rotations : Float
- start_radius : Float
- end_radius : Float
- height : Float
- reverse : Boolean## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.Spiral(resolution=resolution, rotations=rotations, start_radius=start_radius, end_radius=end_radius, height=height, reverse=reverse, label=node_label, node_color=node_color)
```

### Returns

Curve


## ArcFromRadius

> Node: [Arc](/docs/nodes/Arc.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeCurveArc](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html)
node ref [Arc](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/arc.html) </sub>
                          
```python
v = Curve.ArcFromRadius(resolution, radius, start_angle, sweep_angle, connect_center, invert_arc, node_label = None, node_color = None)
```

### Arguments

## Sockets
- resolution : Integer
- radius : Float
- start_angle : Float
- sweep_angle : Float
- connect_center : Boolean
- invert_arc : Boolean## Parameters
- node_label : None
- node_color : None## Fixed parameters
- mode : 'RADIUS'

### Node creation

```python
from geondes import nodes
nodes.Arc(resolution=resolution, radius=radius, start_angle=start_angle, sweep_angle=sweep_angle, connect_center=connect_center, invert_arc=invert_arc, mode='RADIUS', label=node_label, node_color=node_color)
```

### Returns

Curve


## ArcFromPoints

> Node: [Arc](/docs/nodes/Arc.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeCurveArc](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html)
node ref [Arc](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/arc.html) </sub>
                          
```python
v = Curve.ArcFromPoints(resolution, start, middle, end, offset_angle, connect_center, invert_arc, node_label = None, node_color = None)
```

### Arguments

## Sockets
- resolution : Integer
- start : Vector
- middle : Vector
- end : Vector
- offset_angle : Float
- connect_center : Boolean
- invert_arc : Boolean## Parameters
- node_label : None
- node_color : None## Fixed parameters
- mode : 'POINTS'

### Node creation

```python
from geondes import nodes
nodes.Arc(resolution=resolution, start=start, middle=middle, end=end, offset_angle=offset_angle, connect_center=connect_center, invert_arc=invert_arc, mode='POINTS', label=node_label, node_color=node_color)
```

### Returns

Sockets [curve (Curve), center (Vector), normal (Vector), radius (Float)]


## set_handles

> Node: [SetHandleType](/docs/nodes/SetHandleType.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeCurveSetHandles](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)
node ref [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_type.html) </sub>
                          
```python
v = curve.set_handles(selection, handle_type, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- curve : Curve (self)
- selection : Boolean## Parameters
- handle_type : 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode : {'LEFT', 'RIGHT'}
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.SetHandleType(curve=self, selection=selection, handle_type=handle_type, mode=mode, label=node_label, node_color=node_color)
```

### Returns

Curve


## set_spline_type

> Node: [SetSplineType](/docs/nodes/SetSplineType.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeCurveSplineType](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)
node ref [Set Spline Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html) </sub>
                          
```python
v = curve.set_spline_type(selection, spline_type, node_label = None, node_color = None)
```

### Arguments

## Sockets
- curve : Curve (self)
- selection : Boolean## Parameters
- spline_type : 'POLY' in [BEZIER, NURBS, POLY]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.SetSplineType(curve=self, selection=selection, spline_type=spline_type, label=node_label, node_color=node_color)
```

### Returns

Curve


## fill

> Node: [FillCurve](/docs/nodes/FillCurve.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeFillCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)
node ref [Fill Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html) </sub>
                          
```python
v = curve.fill(mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- curve : Curve (self)## Parameters
- mode : 'TRIANGLES' in [TRIANGLES, NGONS]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.FillCurve(curve=self, mode=mode, label=node_label, node_color=node_color)
```

### Returns

Mesh


## fillet

> Node: [FilletCurve](/docs/nodes/FilletCurve.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeFilletCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)
node ref [Fillet Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html) </sub>
                          
```python
v = curve.fillet(count, radius, limit_radius, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- curve : Curve (self)
- count : Integer
- radius : Float
- limit_radius : Boolean## Parameters
- mode : 'BEZIER' in [BEZIER, POLY]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.FilletCurve(curve=self, count=count, radius=radius, limit_radius=limit_radius, mode=mode, label=node_label, node_color=node_color)
```

### Returns

Curve


## resample

> Node: [ResampleCurve](/docs/nodes/ResampleCurve.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeResampleCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)
node ref [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) </sub>
                          
```python
v = curve.resample(selection, count, length, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- curve : Curve (self)
- selection : Boolean
- count : Integer
- length : Float## Parameters
- mode : 'COUNT' in [EVALUATED, COUNT, LENGTH]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.ResampleCurve(curve=self, selection=selection, count=count, length=length, mode=mode, label=node_label, node_color=node_color)
```

### Returns

Curve


## reverse

> Node: [ReverseCurve](/docs/nodes/ReverseCurve.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeReverseCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeReverseCurve.html)
node ref [Reverse Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/reverse_curve.html) </sub>
                          
```python
v = curve.reverse(selection, node_label = None, node_color = None)
```

### Arguments

## Sockets
- curve : Curve (self)
- selection : Boolean## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.ReverseCurve(curve=self, selection=selection, label=node_label, node_color=node_color)
```

### Returns

Curve


## set_handle_positions

> Node: [SetHandlePositions](/docs/nodes/SetHandlePositions.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeSetCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)
node ref [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) </sub>
                          
```python
v = curve.set_handle_positions(selection, position, offset, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- curve : Curve (self)
- selection : Boolean
- position : Vector
- offset : Vector## Parameters
- mode : 'LEFT' in [LEFT, RIGHT]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.SetHandlePositions(curve=self, selection=selection, position=position, offset=offset, mode=mode, label=node_label, node_color=node_color)
```

### Returns

Curve


## set_radius

> Node: [SetCurveRadius](/docs/nodes/SetCurveRadius.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeSetCurveRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html)
node ref [Set Curve Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_radius.html) </sub>
                          
```python
v = curve.set_radius(selection, radius, node_label = None, node_color = None)
```

### Arguments

## Sockets
- curve : Curve (self)
- selection : Boolean
- radius : Float## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.SetCurveRadius(curve=self, selection=selection, radius=radius, label=node_label, node_color=node_color)
```

### Returns

Curve


## set_tilt

> Node: [SetCurveTilt](/docs/nodes/SetCurveTilt.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeSetCurveTilt](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)
node ref [Set Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_tilt.html) </sub>
                          
```python
v = curve.set_tilt(selection, tilt, node_label = None, node_color = None)
```

### Arguments

## Sockets
- curve : Curve (self)
- selection : Boolean
- tilt : Float## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.SetCurveTilt(curve=self, selection=selection, tilt=tilt, label=node_label, node_color=node_color)
```

### Returns

Curve


## subdivide

> Node: [SubdivideCurve](/docs/nodes/SubdivideCurve.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeSubdivideCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideCurve.html)
node ref [Subdivide Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/subdivide_curve.html) </sub>
                          
```python
v = curve.subdivide(cuts, node_label = None, node_color = None)
```

### Arguments

## Sockets
- curve : Curve (self)
- cuts : Integer## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.SubdivideCurve(curve=self, cuts=cuts, label=node_label, node_color=node_color)
```

### Returns

Curve


## trim

> Node: [TrimCurve](/docs/nodes/TrimCurve.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeTrimCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)
node ref [Trim Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html) </sub>
                          
```python
v = curve.trim(start0, end0, start1, end1, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- curve : Curve (self)
- start0 : Float
- end0 : Float
- start1 : Float
- end1 : Float## Parameters
- mode : 'FACTOR' in [FACTOR, LENGTH]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.TrimCurve(curve=self, start0=start0, end0=end0, start1=start1, end1=end1, mode=mode, label=node_label, node_color=node_color)
```

### Returns

Curve


## to_mesh

> Node: [CurveToMesh](/docs/nodes/CurveToMesh.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeCurveToMesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToMesh.html)
node ref [Curve to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_mesh.html) </sub>
                          
```python
v = curve.to_mesh(profile_curve, fill_caps, node_label = None, node_color = None)
```

### Arguments

## Sockets
- curve : Curve (self)
- profile_curve : Geometry
- fill_caps : Boolean## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.CurveToMesh(curve=self, profile_curve=profile_curve, fill_caps=fill_caps, label=node_label, node_color=node_color)
```

### Returns

Mesh


## to_points

> Node: [CurveToPoints](/docs/nodes/CurveToPoints.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeCurveToPoints](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)
node ref [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) </sub>
                          
```python
v = curve.to_points(count, length, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- curve : Curve (self)
- count : Integer
- length : Float## Parameters
- mode : 'COUNT' in [EVALUATED, COUNT, LENGTH]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.CurveToPoints(curve=self, count=count, length=length, mode=mode, label=node_label, node_color=node_color)
```

### Returns

Sockets [points (Points), tangent (Vector), normal (Vector), rotation (Vector)]


## sample

> Node: [SampleCurve](/docs/nodes/SampleCurve.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeSampleCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleCurve.html)
node ref [Sample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample_curve.html) </sub>
                          
```python
v = curve.sample(factor, length, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- curve : Curve (self)
- factor : Float
- length : Float## Parameters
- mode : 'LENGTH' in [FACTOR, LENGTH]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.SampleCurve(curve=self, factor=factor, length=length, mode=mode, label=node_label, node_color=node_color)
```

### Returns

Sockets [position (Vector), tangent (Vector), normal (Vector)]


## length

> Node: [CurveLength](/docs/nodes/CurveLength.md)
  
<sub>go to: [top](#data-socket-curve) [index](/docs/index.md)
blender ref [GeometryNodeCurveLength](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveLength.html)
node ref [Curve Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_length.html) </sub>
                          
```python
v = curve.length(node_label = None, node_color = None)
```

### Arguments

## Sockets
- curve : Curve (self)## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.CurveLength(curve=self, label=node_label, node_color=node_color)
```

### Returns

Float

