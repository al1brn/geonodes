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

## cyclic <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def cyclic(self):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Is Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/is_spline_cyclic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineCyclic.html) )

<sub>Go to [top](#class-Spline)</sub>

### Returns:

<sub>Go to [top](#class-Spline)</sub>

  socket 'cyclic'<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## cyclic <span style="color:blue">*etter*</span>

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def cyclic(self, attr_value):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Set Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_cyclic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html) )

<sub>Go to [top](#class-Spline)</sub>

Node implemented as property setter.

<sub>Go to [top](#class-Spline)</sub>

        ###Args:<sub>Go to [top](#class-Spline)</sub>

- attr_value: cyclic
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## domain_size

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def __len__(self):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

<sub>Go to [top](#class-Spline)</sub>

### Args:
<sub>Go to [top](#class-Spline)</sub>

- geometry: Geometry
<sub>Go to [top](#class-Spline)</sub>

- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

### Returns:

<sub>Go to [top](#class-Spline)</sub>

- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## length <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def length(self):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Spline Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_length.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineLength.html) )

<sub>Go to [top](#class-Spline)</sub>

### Returns:

<sub>Go to [top](#class-Spline)</sub>

- tuple ('length', 'point_count')
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## material <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def material(self):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html) )

<sub>Go to [top](#class-Spline)</sub>

'material' is a write only property.
Raise an exception if attempt to read.

<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## material <span style="color:blue">*etter*</span>

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def material(self, attr_value):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html) )

<sub>Go to [top](#class-Spline)</sub>

Node implemented as property setter.

<sub>Go to [top](#class-Spline)</sub>

        ###Args:<sub>Go to [top](#class-Spline)</sub>

- attr_value: material
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## normal <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def normal(self):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html) )

<sub>Go to [top](#class-Spline)</sub>

### Returns:

<sub>Go to [top](#class-Spline)</sub>

  socket 'normal'<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## normal <span style="color:blue">*etter*</span>

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def normal(self, attr_value):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Set Curve Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_normal.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveNormal.html) )

<sub>Go to [top](#class-Spline)</sub>

Node implemented as property setter.

<sub>Go to [top](#class-Spline)</sub>

        ###Args:<sub>Go to [top](#class-Spline)</sub>

- attr_value: mode
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## points

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def points(self, weights=None, sort_index=None):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Points of Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/points_of_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsOfCurve.html) )

<sub>Go to [top](#class-Spline)</sub>

### Args:
<sub>Go to [top](#class-Spline)</sub>

- weights: Float
<sub>Go to [top](#class-Spline)</sub>

- sort_index: Integer
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

### Returns:

<sub>Go to [top](#class-Spline)</sub>

- tuple ('point_index', 'total')
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## resample

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def resample(self, count=None, length=None, mode='COUNT'):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html) )

<sub>Go to [top](#class-Spline)</sub>

### Args:
<sub>Go to [top](#class-Spline)</sub>

- count: Integer
<sub>Go to [top](#class-Spline)</sub>

- length: Float
<sub>Go to [top](#class-Spline)</sub>

- mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

### Returns:

<sub>Go to [top](#class-Spline)</sub>

- node with sockets ['curve']
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## resample_count

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def resample_count(self, count=None):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html) )

<sub>Go to [top](#class-Spline)</sub>

### Args:
<sub>Go to [top](#class-Spline)</sub>

- count: Integer
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

### Returns:

<sub>Go to [top](#class-Spline)</sub>

- node with sockets ['curve']
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## resample_evaluated

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def resample_evaluated(self):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html) )

<sub>Go to [top](#class-Spline)</sub>

### Returns:

<sub>Go to [top](#class-Spline)</sub>

- node with sockets ['curve']
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## resample_length

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def resample_length(self, length=None):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html) )

<sub>Go to [top](#class-Spline)</sub>

### Args:
<sub>Go to [top](#class-Spline)</sub>

- length: Float
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

### Returns:

<sub>Go to [top](#class-Spline)</sub>

- node with sockets ['curve']
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## resolution <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def resolution(self):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_resolution.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineResolution.html) )

<sub>Go to [top](#class-Spline)</sub>

### Returns:

<sub>Go to [top](#class-Spline)</sub>

  socket 'resolution'<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## resolution <span style="color:blue">*etter*</span>

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def resolution(self, attr_value):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Set Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_resolution.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html) )

<sub>Go to [top](#class-Spline)</sub>

Node implemented as property setter.

<sub>Go to [top](#class-Spline)</sub>

        ###Args:<sub>Go to [top](#class-Spline)</sub>

- attr_value: resolution
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## set_cyclic

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def set_cyclic(self, cyclic=None):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Set Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_cyclic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html) )

<sub>Go to [top](#class-Spline)</sub>

### Args:
<sub>Go to [top](#class-Spline)</sub>

- cyclic: Boolean
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

### Returns:

<sub>Go to [top](#class-Spline)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## set_material

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def set_material(self, material=None):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html) )

<sub>Go to [top](#class-Spline)</sub>

### Args:
<sub>Go to [top](#class-Spline)</sub>

- material: Material
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

### Returns:

<sub>Go to [top](#class-Spline)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## set_normal

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def set_normal(self, mode='MINIMUM_TWIST'):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Set Curve Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_normal.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveNormal.html) )

<sub>Go to [top](#class-Spline)</sub>

### Args:
<sub>Go to [top](#class-Spline)</sub>

- mode (str): 'MINIMUM_TWIST' in [MINIMUM_TWIST, Z_UP]
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

### Returns:

<sub>Go to [top](#class-Spline)</sub>

- node with sockets ['curve']
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## set_resolution

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def set_resolution(self, resolution=None):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Set Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_resolution.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html) )

<sub>Go to [top](#class-Spline)</sub>

### Args:
<sub>Go to [top](#class-Spline)</sub>

- resolution: Integer
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

### Returns:

<sub>Go to [top](#class-Spline)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## set_type

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def set_type(self, spline_type='POLY'):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Set Spline Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html) )

<sub>Go to [top](#class-Spline)</sub>

### Args:
<sub>Go to [top](#class-Spline)</sub>

- spline_type (str): 'POLY' in [CATMULL_ROM, POLY, BEZIER, NURBS]
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

### Returns:

<sub>Go to [top](#class-Spline)</sub>

- node with sockets ['curve']
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## type <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def type(self):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Set Spline Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html) )

<sub>Go to [top](#class-Spline)</sub>

'type' is a write only property.
Raise an exception if attempt to read.

<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

## type <span style="color:blue">*etter*</span>

<sub>Go to [top](#class-Spline)</sub>

```python
<sub>Go to [top](#class-Spline)</sub>

def type(self, attr_value):

<sub>Go to [top](#class-Spline)</sub>

```
<sub>Go to [top](#class-Spline)</sub>

Node [Set Spline Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html) )

<sub>Go to [top](#class-Spline)</sub>

Node implemented as property setter.

<sub>Go to [top](#class-Spline)</sub>

        ###Args:<sub>Go to [top](#class-Spline)</sub>

- attr_value: spline_type
<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>


<sub>Go to [top](#class-Spline)</sub>

