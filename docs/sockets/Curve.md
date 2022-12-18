
# Data socket Curve

> Inherits from gn.Geometry
  
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

## Properties

- [domain_size](#domain_size) : Sockets      [point_count (Integer), spline_count (Integer)]
- [point_count](#point_count) : point_count (Integer) = domain_size.point_count
- [spline_count](#spline_count) : spline_count (Integer) = domain_size.spline_count

## Methods

- [deform_on_surface](#deform_on_surface) : curves (Curve)
- [duplicate_splines](#duplicate_splines) : Sockets      [geometry (Geometry), duplicate_index (Integer)]
- [fill](#fill) : mesh (Mesh)
- [fillet](#fillet) : curve (Curve)
- [length](#length) : length (Float)
- [resample](#resample) : curve (Curve)
- [reverse](#reverse) : curve (Curve)
- [sample](#sample) : Sockets      [value (Boolean), position (Vector), tangent (Vector), normal (Vector)]
- [set_cyclic](#set_cyclic) : geometry (Geometry)
- [set_handle_positions](#set_handle_positions) : curve (Curve)
- [set_handles](#set_handles) : curve (Curve)
- [set_radius](#set_radius) : curve (Curve)
- [set_resolution](#set_resolution) : geometry (Geometry)
- [set_spline_type](#set_spline_type) : curve (Curve)
- [set_tilt](#set_tilt) : curve (Curve)
- [subdivide](#subdivide) : curve (Curve)
- [to_mesh](#to_mesh) : mesh (Mesh)
- [to_points](#to_points) : Sockets      [points (Points), tangent (Vector), normal (Vector), rotation (Vector)]
- [trim](#trim) : curve (Curve)

## BezierSegment

Geometry node [*Bezier Segment*].


  Args:
    resolution: Integer
    start: Vector
    start_handle: Vector
    end_handle: Vector
    end: Vector
    mode (str): 'POSITION' in [POSITION, OFFSET]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Curve
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.BezierSegment`
  
  
  .. blid:: GeometryNodeCurvePrimitiveBezierSegment
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.BezierSegment(resolution=resolution, start=start, start_handle=start_handle, end_handle=end_handle, end=end, mode=mode, label=node_label, node_color=node_color)
    

## Circle

Geometry node [*Curve Circle*].


  Args:
    resolution: Integer
    point_1: Vector
    point_2: Vector
    point_3: Vector
    radius: Float
    mode (str): 'RADIUS' in [POINTS, RADIUS]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [curve (Curve), center (Vector)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.CurveCircle`
  
  
  .. blid:: GeometryNodeCurvePrimitiveCircle
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.CurveCircle(resolution=resolution, point_1=point_1, point_2=point_2, point_3=point_3, radius=radius, mode=mode, label=node_label, node_color=node_color)
    

## Line

Geometry node [*Curve Line*].


  Args:
    start: Vector
    end: Vector
    direction: Vector
    length: Float
    mode (str): 'POINTS' in [POINTS, DIRECTION]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Curve
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.CurveLine`
  
  
  .. blid:: GeometryNodeCurvePrimitiveLine
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.CurveLine(start=start, end=end, direction=direction, length=length, mode=mode, label=node_label, node_color=node_color)
    

## Quadrilateral

Geometry node [*Quadrilateral*].


  Args:
    width: Float
    height: Float
    bottom_width: Float
    top_width: Float
    offset: Float
    bottom_height: Float
    top_height: Float
    point_1: Vector
    point_2: Vector
    point_3: Vector
    point_4: Vector
    mode (str): 'RECTANGLE' in [RECTANGLE, PARALLELOGRAM, TRAPEZOID, KITE, POINTS]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Curve
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Quadrilateral`
  
  
  .. blid:: GeometryNodeCurvePrimitiveQuadrilateral
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Quadrilateral(width=width, height=height, bottom_width=bottom_width, top_width=top_width, offset=offset, bottom_height=bottom_height, top_height=top_height, point_1=point_1, point_2=point_2, point_3=point_3, point_4=point_4, mode=mode, label=node_label, node_color=node_color)
    

## QuadraticBezier

Geometry node [*Quadratic Bezier*].


  Args:
    resolution: Integer
    start: Vector
    middle: Vector
    end: Vector
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Curve
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.QuadraticBezier`
  
  
  .. blid:: GeometryNodeCurveQuadraticBezier
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.QuadraticBezier(resolution=resolution, start=start, middle=middle, end=end, label=node_label, node_color=node_color)
    

## Star

Geometry node [*Star*].


  Args:
    points: Integer
    inner_radius: Float
    outer_radius: Float
    twist: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [curve (Curve), outer_points (Boolean)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Star`
  
  
  .. blid:: GeometryNodeCurveStar
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Star(points=points, inner_radius=inner_radius, outer_radius=outer_radius, twist=twist, label=node_label, node_color=node_color)
    

## Spiral

Geometry node [*Spiral*].


  Args:
    resolution: Integer
    rotations: Float
    start_radius: Float
    end_radius: Float
    height: Float
    reverse: Boolean
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Curve
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Spiral`
  
  
  .. blid:: GeometryNodeCurveSpiral
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Spiral(resolution=resolution, rotations=rotations, start_radius=start_radius, end_radius=end_radius, height=height, reverse=reverse, label=node_label, node_color=node_color)
    

## ArcFromRadius

Geometry node [*Arc*].


  Args:
    resolution: Integer
    radius: Float
    start_angle: Float
    sweep_angle: Float
    connect_center: Boolean
    invert_arc: Boolean
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Curve
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Arc`
  
  - mode = 'RADIUS'
    
  .. blid:: GeometryNodeCurveArc
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Arc(resolution=resolution, radius=radius, start_angle=start_angle, sweep_angle=sweep_angle, connect_center=connect_center, invert_arc=invert_arc, mode='RADIUS', label=node_label, node_color=node_color)
    

## ArcFromPoints

Geometry node [*Arc*].


  Args:
    resolution: Integer
    start: Vector
    middle: Vector
    end: Vector
    offset_angle: Float
    connect_center: Boolean
    invert_arc: Boolean
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [curve (Curve), center (Vector), normal (Vector), radius (Float)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Arc`
  
  - mode = 'POINTS'
    
  .. blid:: GeometryNodeCurveArc
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Arc(resolution=resolution, start=start, middle=middle, end=end, offset_angle=offset_angle, connect_center=connect_center, invert_arc=invert_arc, mode='POINTS', label=node_label, node_color=node_color)
    

## domain_size

Geometry node [*Domain Size*].



  Returns:
    Sockets [point_count (Integer), spline_count (Integer)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.DomainSize`
  
  - component = 'CURVE'
    
  .. blid:: GeometryNodeAttributeDomainSize
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.DomainSize(geometry=self, component='CURVE', label=f"{self.node_chain_label}.domain_size")
    

## point_count

Geometry node [*Domain Size*].



  Returns:
    Sockets [point_count (Integer), spline_count (Integer)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.DomainSize`
  
  - component = 'CURVE'
    
  .. blid:: GeometryNodeAttributeDomainSize
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.DomainSize(geometry=self, component='CURVE', label=f"{self.node_chain_label}.point_count")
    

## spline_count

Geometry node [*Domain Size*].



  Returns:
    Sockets [point_count (Integer), spline_count (Integer)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.DomainSize`
  
  - component = 'CURVE'
    
  .. blid:: GeometryNodeAttributeDomainSize
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.DomainSize(geometry=self, component='CURVE', label=f"{self.node_chain_label}.spline_count")
    

## set_cyclic

Geometry node [*Set Spline Cyclic*].


  Args:
    selection: Boolean
    cyclic: Boolean
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SetSplineCyclic`
  
  
  .. blid:: GeometryNodeSetSplineCyclic
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SetSplineCyclic(geometry=self, selection=selection, cyclic=cyclic, label=node_label, node_color=node_color)
    

## set_resolution

Geometry node [*Set Spline Resolution*].


  Args:
    selection: Boolean
    resolution: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SetSplineResolution`
  
  
  .. blid:: GeometryNodeSetSplineResolution
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SetSplineResolution(geometry=self, selection=selection, resolution=resolution, label=node_label, node_color=node_color)
    

## set_handles

Geometry node [*Set Handle Type*].


  Args:
    selection: Boolean
    handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
    mode (set): {'RIGHT', 'LEFT'}
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Curve
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SetHandleType`
  
  
  .. blid:: GeometryNodeCurveSetHandles
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SetHandleType(curve=self, selection=selection, handle_type=handle_type, mode=mode, label=node_label, node_color=node_color)
    

## set_spline_type

Geometry node [*Set Spline Type*].


  Args:
    selection: Boolean
    spline_type (str): 'POLY' in [CATMULL_ROM, POLY, BEZIER, NURBS]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Curve
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SetSplineType`
  
  
  .. blid:: GeometryNodeCurveSplineType
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SetSplineType(curve=self, selection=selection, spline_type=spline_type, label=node_label, node_color=node_color)
    

## fillet

Geometry node [*Fillet Curve*].


  Args:
    count: Integer
    radius: Float
    limit_radius: Boolean
    mode (str): 'BEZIER' in [BEZIER, POLY]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Curve
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.FilletCurve`
  
  
  .. blid:: GeometryNodeFilletCurve
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.FilletCurve(curve=self, count=count, radius=radius, limit_radius=limit_radius, mode=mode, label=node_label, node_color=node_color)
    

## resample

Geometry node [*Resample Curve*].


  Args:
    selection: Boolean
    count: Integer
    length: Float
    mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Curve
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.ResampleCurve`
  
  
  .. blid:: GeometryNodeResampleCurve
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.ResampleCurve(curve=self, selection=selection, count=count, length=length, mode=mode, label=node_label, node_color=node_color)
    

## reverse

Geometry node [*Reverse Curve*].


  Args:
    selection: Boolean
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Curve
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.ReverseCurve`
  
  
  .. blid:: GeometryNodeReverseCurve
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.ReverseCurve(curve=self, selection=selection, label=node_label, node_color=node_color)
    

## set_handle_positions

Geometry node [*Set Handle Positions*].


  Args:
    selection: Boolean
    position: Vector
    offset: Vector
    mode (str): 'LEFT' in [LEFT, RIGHT]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Curve
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SetHandlePositions`
  
  
  .. blid:: GeometryNodeSetCurveHandlePositions
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SetHandlePositions(curve=self, selection=selection, position=position, offset=offset, mode=mode, label=node_label, node_color=node_color)
    

## set_radius

Geometry node [*Set Curve Radius*].


  Args:
    selection: Boolean
    radius: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Curve
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SetCurveRadius`
  
  
  .. blid:: GeometryNodeSetCurveRadius
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SetCurveRadius(curve=self, selection=selection, radius=radius, label=node_label, node_color=node_color)
    

## set_tilt

Geometry node [*Set Curve Tilt*].


  Args:
    selection: Boolean
    tilt: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Curve
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SetCurveTilt`
  
  
  .. blid:: GeometryNodeSetCurveTilt
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SetCurveTilt(curve=self, selection=selection, tilt=tilt, label=node_label, node_color=node_color)
    

## subdivide

Geometry node [*Subdivide Curve*].


  Args:
    cuts: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Curve
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SubdivideCurve`
  
  
  .. blid:: GeometryNodeSubdivideCurve
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SubdivideCurve(curve=self, cuts=cuts, label=node_label, node_color=node_color)
    

## trim

Geometry node [*Trim Curve*].


  Args:
    start0: Float
    end0: Float
    start1: Float
    end1: Float
    mode (str): 'FACTOR' in [FACTOR, LENGTH]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Curve
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.TrimCurve`
  
  
  .. blid:: GeometryNodeTrimCurve
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.TrimCurve(curve=self, start0=start0, end0=end0, start1=start1, end1=end1, mode=mode, label=node_label, node_color=node_color)
    

## deform_on_surface

Geometry node [*Deform Curves on Surface*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Curve
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.DeformCurvesOnSurface`
  
  
  .. blid:: GeometryNodeDeformCurvesOnSurface
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.DeformCurvesOnSurface(curves=self, label=node_label, node_color=node_color)
    

## duplicate_splines

Geometry node [*Duplicate Elements*].


  Args:
    selection: Boolean
    amount: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [geometry (Geometry), duplicate_index (Integer)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.DuplicateElements`
  
  - domain = 'SPLINE'
    
  .. blid:: GeometryNodeDuplicateElements
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='SPLINE', label=node_label, node_color=node_color)
    

## fill

Geometry node [*Fill Curve*].


  Args:
    mode (str): 'TRIANGLES' in [TRIANGLES, NGONS]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Mesh
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.FillCurve`
  
  
  .. blid:: GeometryNodeFillCurve
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.FillCurve(curve=self, mode=mode, label=node_label, node_color=node_color)
    

## to_mesh

Geometry node [*Curve to Mesh*].


  Args:
    profile_curve: Geometry
    fill_caps: Boolean
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Mesh
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.CurveToMesh`
  
  
  .. blid:: GeometryNodeCurveToMesh
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.CurveToMesh(curve=self, profile_curve=profile_curve, fill_caps=fill_caps, label=node_label, node_color=node_color)
    

## to_points

Geometry node [*Curve to Points*].


  Args:
    count: Integer
    length: Float
    mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [points (Points), tangent (Vector), normal (Vector), rotation (Vector)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.CurveToPoints`
  
  
  .. blid:: GeometryNodeCurveToPoints
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.CurveToPoints(curve=self, count=count, length=length, mode=mode, label=node_label, node_color=node_color)
    

## sample

Geometry node [*Sample Curve*].


  Args:
    value: Boolean
    factor: Float
    length: Float
    curve_index: Integer
    mode (str): 'FACTOR' in [FACTOR, LENGTH]
    use_all_curves (bool): False
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [value (Boolean), position (Vector), tangent (Vector), normal (Vector)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SampleCurve`
  
  - data_type = None
    
  .. blid:: GeometryNodeSampleCurve
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SampleCurve(curves=self, value=value, factor=factor, length=length, curve_index=curve_index, data_type=None, mode=mode, use_all_curves=use_all_curves, label=node_label, node_color=node_color)
    

## length

Geometry node [*Curve Length*].


  Args:
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Float
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.CurveLength`
  
  
  .. blid:: GeometryNodeCurveLength
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.CurveLength(curve=self, label=node_label, node_color=node_color)
    
