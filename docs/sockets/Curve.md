
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


