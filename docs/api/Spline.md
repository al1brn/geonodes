# class Spline

## Properties

- [cyclic](#cyclic-property)
- [length](#length-property)
- [material](#material-property)
- [normal](#normal-property)
- [resolution](#resolution-property)
- [type](#type-property)



## Methods

- [domain_size](#domain_size)
- [points](#points)
- [resample](#resample)
- [resample_count](#resample_count)
- [resample_evaluated](#resample_evaluated)
- [resample_length](#resample_length)
- [set_cyclic](#set_cyclic)
- [set_material](#set_material)
- [set_normal](#set_normal)
- [set_resolution](#set_resolution)
- [set_type](#set_type)

## cyclic *property*

{#cyclic}

> def cyclic(self):

Node [Is Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/is_spline_cyclic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineCyclic.html) )

### Returns:

  socket 'cyclic'

## cyclic *etter*

{#cyclic}

> def cyclic(self, attr_value):

Node [Set Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_cyclic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html) )

Node implemented as property setter.

        ###Args:- attr_value: cyclic


## domain_size

{#domain_size}

> def __len__(self):

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

        ### Args:
- geometry: Geometry
- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

### Returns:

- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

## length *property*

{#length}

> def length(self):

Node [Spline Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_length.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineLength.html) )

### Returns:

- tuple ('length', 'point_count')

## material *property*

{#material}

> def material(self):

Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html) )

'material' is a write only property.
Raise an exception if attempt to read.


## material *etter*

{#material}

> def material(self, attr_value):

Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html) )

Node implemented as property setter.

        ###Args:- attr_value: material


## normal *property*

{#normal}

> def normal(self):

Node [Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html) )

### Returns:

  socket 'normal'

## normal *etter*

{#normal}

> def normal(self, attr_value):

Node [Set Curve Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_normal.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveNormal.html) )

Node implemented as property setter.

        ###Args:- attr_value: mode


## points

{#points}

> def points(self, weights=None, sort_index=None):

Node [Points of Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/points_of_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsOfCurve.html) )

        ### Args:
- weights: Float
- sort_index: Integer

### Returns:

- tuple ('point_index', 'total')

## resample

{#resample}

> def resample(self, count=None, length=None, mode='COUNT'):

Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html) )

        ### Args:
- count: Integer
- length: Float
- mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]

### Returns:

- node with sockets ['curve']

## resample_count

{#resample_count}

> def resample_count(self, count=None):

Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html) )

        ### Args:
- count: Integer

### Returns:

- node with sockets ['curve']

## resample_evaluated

{#resample_evaluated}

> def resample_evaluated(self):

Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html) )

### Returns:

- node with sockets ['curve']

## resample_length

{#resample_length}

> def resample_length(self, length=None):

Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html) )

        ### Args:
- length: Float

### Returns:

- node with sockets ['curve']

## resolution *property*

{#resolution}

> def resolution(self):

Node [Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_resolution.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineResolution.html) )

### Returns:

  socket 'resolution'

## resolution *etter*

{#resolution}

> def resolution(self, attr_value):

Node [Set Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_resolution.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html) )

Node implemented as property setter.

        ###Args:- attr_value: resolution


## set_cyclic

{#set_cyclic}

> def set_cyclic(self, cyclic=None):

Node [Set Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_cyclic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html) )

        ### Args:
- cyclic: Boolean

### Returns:

- node with sockets ['geometry']

## set_material

{#set_material}

> def set_material(self, material=None):

Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html) )

        ### Args:
- material: Material

### Returns:

- node with sockets ['geometry']

## set_normal

{#set_normal}

> def set_normal(self, mode='MINIMUM_TWIST'):

Node [Set Curve Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_normal.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveNormal.html) )

        ### Args:
- mode (str): 'MINIMUM_TWIST' in [MINIMUM_TWIST, Z_UP]

### Returns:

- node with sockets ['curve']

## set_resolution

{#set_resolution}

> def set_resolution(self, resolution=None):

Node [Set Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_resolution.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html) )

        ### Args:
- resolution: Integer

### Returns:

- node with sockets ['geometry']

## set_type

{#set_type}

> def set_type(self, spline_type='POLY'):

Node [Set Spline Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html) )

        ### Args:
- spline_type (str): 'POLY' in [CATMULL_ROM, POLY, BEZIER, NURBS]

### Returns:

- node with sockets ['curve']

## type *property*

{#type}

> def type(self):

Node [Set Spline Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html) )

'type' is a write only property.
Raise an exception if attempt to read.


## type *etter*

{#type}

> def type(self, attr_value):

Node [Set Spline Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html) )

Node implemented as property setter.

        ###Args:- attr_value: spline_type


