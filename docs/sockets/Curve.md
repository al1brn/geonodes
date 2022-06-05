
# Class Curve

> Inherits from: ***Spline***

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



- [length](#length) : length (Float)
- [sample](#sample) : Sockets      [position (Vector), tangent (Vector), normal (Vector)]
- [to_mesh](#to_mesh) : mesh (Mesh)
- [to_points](#to_points) : Sockets      [points (Points), tangent (Vector), normal (Vector), rotation (Vector)]



## Stacked methods



- [fill](#fill) : Curve
- [fillet](#fillet) : Curve
- [resample](#resample) : Curve
- [reverse](#reverse) : Curve
- [set_handle_positions](#set_handle_positions) : Curve
- [set_handles](#set_handles) : Curve
- [set_radius](#set_radius) : Curve
- [set_spline_type](#set_spline_type) : Curve
- [set_tilt](#set_tilt) : Curve
- [subdivide](#subdivide) : Curve
- [trim](#trim) : Curve



## Methods reference


### ArcFromPoints

> Node: [Arc](../nodes/{self.node_name}.md)

```python
v = Curve.ArcFromPoints(resolution, start, middle, end, offset_angle, connect_center, invert_arc)
```


#### Arguments


##### Sockets arguments



- resolution : Integer
- start : Vector
- middle : Vector
- end : Vector
- offset_angle : Float
- connect_center : Boolean
- invert_arc : Boolean



##### Fixed parameters



- mode : 'POINTS'



#### Node creation


```python
node = nodes.Arc(resolution=resolution, start=start, middle=middle, end=end, offset_angle=offset_angle, connect_center=connect_center, invert_arc=invert_arc, mode='POINTS')
```


#### Returns

    Sockets [curve (Curve), center (Vector), normal (Vector), radius (Float)]

### ArcFromRadius

> Node: [Arc](../nodes/{self.node_name}.md)

```python
v = Curve.ArcFromRadius(resolution, radius, start_angle, sweep_angle, connect_center, invert_arc)
```


#### Arguments


##### Sockets arguments



- resolution : Integer
- radius : Float
- start_angle : Float
- sweep_angle : Float
- connect_center : Boolean
- invert_arc : Boolean



##### Fixed parameters



- mode : 'RADIUS'



#### Node creation


```python
node = nodes.Arc(resolution=resolution, radius=radius, start_angle=start_angle, sweep_angle=sweep_angle, connect_center=connect_center, invert_arc=invert_arc, mode='RADIUS')
```


#### Returns

    Curve

### BezierSegment

> Node: [BezierSegment](../nodes/{self.node_name}.md)

```python
v = Curve.BezierSegment(resolution, start, start_handle, end_handle, end, mode)
```


#### Arguments


##### Sockets arguments



- resolution : Integer
- start : Vector
- start_handle : Vector
- end_handle : Vector
- end : Vector



##### Parameters arguments



- mode : 'POSITION' in [POSITION, OFFSET]



#### Node creation


```python
node = nodes.BezierSegment(resolution=resolution, start=start, start_handle=start_handle, end_handle=end_handle, end=end, mode=mode)
```


#### Returns

    Curve

### Circle

> Node: [CurveCircle](../nodes/{self.node_name}.md)

```python
v = Curve.Circle(resolution, point_1, point_2, point_3, radius, mode)
```


#### Arguments


##### Sockets arguments



- resolution : Integer
- point_1 : Vector
- point_2 : Vector
- point_3 : Vector
- radius : Float



##### Parameters arguments



- mode : 'RADIUS' in [POINTS, RADIUS]



#### Node creation


```python
node = nodes.CurveCircle(resolution=resolution, point_1=point_1, point_2=point_2, point_3=point_3, radius=radius, mode=mode)
```


#### Returns

    Sockets [curve (Curve), center (Vector)]

### Line

> Node: [CurveLine](../nodes/{self.node_name}.md)

```python
v = Curve.Line(start, end, direction, length, mode)
```


#### Arguments


##### Sockets arguments



- start : Vector
- end : Vector
- direction : Vector
- length : Float



##### Parameters arguments



- mode : 'POINTS' in [POINTS, DIRECTION]



#### Node creation


```python
node = nodes.CurveLine(start=start, end=end, direction=direction, length=length, mode=mode)
```


#### Returns

    Curve

### QuadraticBezier

> Node: [QuadraticBezier](../nodes/{self.node_name}.md)

```python
v = Curve.QuadraticBezier(resolution, start, middle, end)
```


#### Arguments


##### Sockets arguments



- resolution : Integer
- start : Vector
- middle : Vector
- end : Vector



#### Node creation


```python
node = nodes.QuadraticBezier(resolution=resolution, start=start, middle=middle, end=end)
```


#### Returns

    Curve

### Quadrilateral

> Node: [Quadrilateral](../nodes/{self.node_name}.md)

```python
v = Curve.Quadrilateral(width, height, bottom_width, top_width, offset, bottom_height, top_height, point_1, point_2, point_3, point_4, mode)
```


#### Arguments


##### Sockets arguments



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



##### Parameters arguments



- mode : 'RECTANGLE' in [RECTANGLE, PARALLELOGRAM, TRAPEZOID, KITE, POINTS]



#### Node creation


```python
node = nodes.Quadrilateral(width=width, height=height, bottom_width=bottom_width, top_width=top_width, offset=offset, bottom_height=bottom_height, top_height=top_height, point_1=point_1, point_2=point_2, point_3=point_3, point_4=point_4, mode=mode)
```


#### Returns

    Curve

### Spiral

> Node: [Spiral](../nodes/{self.node_name}.md)

```python
v = Curve.Spiral(resolution, rotations, start_radius, end_radius, height, reverse)
```


#### Arguments


##### Sockets arguments



- resolution : Integer
- rotations : Float
- start_radius : Float
- end_radius : Float
- height : Float
- reverse : Boolean



#### Node creation


```python
node = nodes.Spiral(resolution=resolution, rotations=rotations, start_radius=start_radius, end_radius=end_radius, height=height, reverse=reverse)
```


#### Returns

    Curve

### Star

> Node: [Star](../nodes/{self.node_name}.md)

```python
v = Curve.Star(points, inner_radius, outer_radius, twist)
```


#### Arguments


##### Sockets arguments



- points : Integer
- inner_radius : Float
- outer_radius : Float
- twist : Float



#### Node creation


```python
node = nodes.Star(points=points, inner_radius=inner_radius, outer_radius=outer_radius, twist=twist)
```


#### Returns

    Sockets [curve (Curve), outer_points (Boolean)]

### fill

> Node: [FillCurve](../nodes/{self.node_name}.md)

```python
curve.fill(mode)
```


#### Arguments


##### Sockets arguments



- curve : Curve (self)



##### Parameters arguments



- mode : 'TRIANGLES' in [TRIANGLES, NGONS]



#### Node creation


```python
node = nodes.FillCurve(curve=self, mode=mode)
```


#### Returns

    self

### fillet

> Node: [FilletCurve](../nodes/{self.node_name}.md)

```python
curve.fillet(count, radius, limit_radius, mode)
```


#### Arguments


##### Sockets arguments



- curve : Curve (self)
- count : Integer
- radius : Float
- limit_radius : Boolean



##### Parameters arguments



- mode : 'BEZIER' in [BEZIER, POLY]



#### Node creation


```python
node = nodes.FilletCurve(curve=self, count=count, radius=radius, limit_radius=limit_radius, mode=mode)
```


#### Returns

    self

### length

> Node: [CurveLength](../nodes/{self.node_name}.md)

```python
v = curve.length()
```


#### Arguments


##### Sockets arguments



- curve : Curve (self)



#### Node creation


```python
node = nodes.CurveLength(curve=self)
```


#### Returns

    Float

### resample

> Node: [ResampleCurve](../nodes/{self.node_name}.md)

```python
curve.resample(selection, count, length, mode)
```


#### Arguments


##### Sockets arguments



- curve : Curve (self)
- selection : Boolean
- count : Integer
- length : Float



##### Parameters arguments



- mode : 'COUNT' in [EVALUATED, COUNT, LENGTH]



#### Node creation


```python
node = nodes.ResampleCurve(curve=self, selection=selection, count=count, length=length, mode=mode)
```


#### Returns

    self

### reverse

> Node: [ReverseCurve](../nodes/{self.node_name}.md)

```python
curve.reverse(selection)
```


#### Arguments


##### Sockets arguments



- curve : Curve (self)
- selection : Boolean



#### Node creation


```python
node = nodes.ReverseCurve(curve=self, selection=selection)
```


#### Returns

    self

### sample

> Node: [SampleCurve](../nodes/{self.node_name}.md)

```python
v = curve.sample(factor, length, mode)
```


#### Arguments


##### Sockets arguments



- curve : Curve (self)
- factor : Float
- length : Float



##### Parameters arguments



- mode : 'LENGTH' in [FACTOR, LENGTH]



#### Node creation


```python
node = nodes.SampleCurve(curve=self, factor=factor, length=length, mode=mode)
```


#### Returns

    Sockets [position (Vector), tangent (Vector), normal (Vector)]

### set_handle_positions

> Node: [SetHandlePositions](../nodes/{self.node_name}.md)

```python
curve.set_handle_positions(selection, position, offset, mode)
```


#### Arguments


##### Sockets arguments



- curve : Curve (self)
- selection : Boolean
- position : Vector
- offset : Vector



##### Parameters arguments



- mode : 'LEFT' in [LEFT, RIGHT]



#### Node creation


```python
node = nodes.SetHandlePositions(curve=self, selection=selection, position=position, offset=offset, mode=mode)
```


#### Returns

    self

### set_handles

> Node: [SetHandleType](../nodes/{self.node_name}.md)

```python
curve.set_handles(selection, handle_type, mode)
```


#### Arguments


##### Sockets arguments



- curve : Curve (self)
- selection : Boolean



##### Parameters arguments



- handle_type : 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode : {'RIGHT', 'LEFT'}



#### Node creation


```python
node = nodes.SetHandleType(curve=self, selection=selection, handle_type=handle_type, mode=mode)
```


#### Returns

    self

### set_radius

> Node: [SetCurveRadius](../nodes/{self.node_name}.md)

```python
curve.set_radius(selection, radius)
```


#### Arguments


##### Sockets arguments



- curve : Curve (self)
- selection : Boolean
- radius : Float



#### Node creation


```python
node = nodes.SetCurveRadius(curve=self, selection=selection, radius=radius)
```


#### Returns

    self

### set_spline_type

> Node: [SetSplineType](../nodes/{self.node_name}.md)

```python
curve.set_spline_type(selection, spline_type)
```


#### Arguments


##### Sockets arguments



- curve : Curve (self)
- selection : Boolean



##### Parameters arguments



- spline_type : 'POLY' in [BEZIER, NURBS, POLY]



#### Node creation


```python
node = nodes.SetSplineType(curve=self, selection=selection, spline_type=spline_type)
```


#### Returns

    self

### set_tilt

> Node: [SetCurveTilt](../nodes/{self.node_name}.md)

```python
curve.set_tilt(selection, tilt)
```


#### Arguments


##### Sockets arguments



- curve : Curve (self)
- selection : Boolean
- tilt : Float



#### Node creation


```python
node = nodes.SetCurveTilt(curve=self, selection=selection, tilt=tilt)
```


#### Returns

    self

### subdivide

> Node: [SubdivideCurve](../nodes/{self.node_name}.md)

```python
curve.subdivide(cuts)
```


#### Arguments


##### Sockets arguments



- curve : Curve (self)
- cuts : Integer



#### Node creation


```python
node = nodes.SubdivideCurve(curve=self, cuts=cuts)
```


#### Returns

    self

### to_mesh

> Node: [CurveToMesh](../nodes/{self.node_name}.md)

```python
v = curve.to_mesh(profile_curve, fill_caps)
```


#### Arguments


##### Sockets arguments



- curve : Curve (self)
- profile_curve : Geometry
- fill_caps : Boolean



#### Node creation


```python
node = nodes.CurveToMesh(curve=self, profile_curve=profile_curve, fill_caps=fill_caps)
```


#### Returns

    Mesh

### to_points

> Node: [CurveToPoints](../nodes/{self.node_name}.md)

```python
v = curve.to_points(count, length, mode)
```


#### Arguments


##### Sockets arguments



- curve : Curve (self)
- count : Integer
- length : Float



##### Parameters arguments



- mode : 'COUNT' in [EVALUATED, COUNT, LENGTH]



#### Node creation


```python
node = nodes.CurveToPoints(curve=self, count=count, length=length, mode=mode)
```


#### Returns

    Sockets [points (Points), tangent (Vector), normal (Vector), rotation (Vector)]

### trim

> Node: [TrimCurve](../nodes/{self.node_name}.md)

```python
curve.trim(start0, end0, start1, end1, mode)
```


#### Arguments


##### Sockets arguments



- curve : Curve (self)
- start0 : Float
- end0 : Float
- start1 : Float
- end1 : Float



##### Parameters arguments



- mode : 'FACTOR' in [FACTOR, LENGTH]



#### Node creation


```python
node = nodes.TrimCurve(curve=self, start0=start0, end0=end0, start1=start1, end1=end1, mode=mode)
```


#### Returns

    self
