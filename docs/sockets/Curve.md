
# Class Curve

> Inherits from: ***Spline***

## Constructors



- ArcFromRadius : curve (Curve)
- BezierSegment : curve (Curve)
- Circle : Sockets      [curve (Curve), center (Vector)]
- Line : curve (Curve)
- QuadraticBezier : curve (Curve)
- Quadrilateral : curve (Curve)
- Spiral : curve (Curve)
- Star : Sockets      [curve (Curve), outer_points (Boolean)]



## Static methods



- ArcFromPoints : Sockets      [curve (Curve), center (Vector), normal (Vector), radius (Float)]



## Methods



- length : length (Float)
- sample : Sockets      [position (Vector), tangent (Vector), normal (Vector)]
- to_mesh : mesh (Mesh)
- to_points : Sockets      [points (Points), tangent (Vector), normal (Vector), rotation (Vector)]



## Stacked methods



- fill : Curve
- fillet : Curve
- resample : Curve
- reverse : Curve
- set_handle_positions : Curve
- set_handles : Curve
- set_radius : Curve
- set_spline_type : Curve
- set_tilt : Curve
- subdivide : Curve
- trim : Curve



## Methods


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



#### Returns

    self
