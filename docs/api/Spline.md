# class Spline

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

**Spline** is one of the two [Domains](Domain.md) of [Curve](Curve.md).
It is implemented as property `splines`

The other [Domain](Domain.md) is [ControlPoint](ControlPoint.md).
## Properties

- [count](#count-property)
- [cyclic](#cyclic-property)
- [length](#length-property)
- [material](#material-property)
- [normal](#normal-property)
- [resolution](#resolution-property)
- [type](#type-property)



## Methods

- [delete](#delete)
- [duplicate](#duplicate)
- [points](#points)
- [resample](#resample)
- [resample_count](#resample_count)
- [resample_evaluated](#resample_evaluated)
- [resample_length](#resample_length)
- [separate](#separate)
- [set_cyclic](#set_cyclic)
- [set_material](#set_material)
- [set_normal](#set_normal)
- [set_resolution](#set_resolution)
- [set_type](#set_type)

## count <sub>*property*</sub>

```python
def count(self, geometry=None):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `spline_count`

<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## cyclic <sub>*property*</sub>

```python
def cyclic(self):

```
> Node: [Is Spline Cyclic](GeometryNodeInputSplineCyclic.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/is_spline_cyclic.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineCyclic.html)

#### Returns:
- socket `cyclic`

<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## cyclic <sub>*etter*</sub>

```python
def cyclic(self, attr_value):

```
> Node: [Set Spline Cyclic](GeometryNodeSetSplineCyclic.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_cyclic.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html)

Node implemented as property setter.

#### Args:
- attr_value: cyclic


<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## delete

```python
def delete(self, mode='ALL'):

```
> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

#### Returns:
- self

<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## duplicate

```python
def duplicate(self, amount=None):

```
> Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

#### Args:
- amount: Integer

#### Returns:
- socket `duplicate_index`

<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## length <sub>*property*</sub>

```python
def length(self):

```
> Node: [Spline Length](GeometryNodeSplineLength.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_length.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineLength.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSplineLength.webp)

#### Returns:
- tuple ('`length`', '`point_count`')

<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## material <sub>*property*</sub>

```python
def material(self):

```
> Node: [Set Material](GeometryNodeSetMaterial.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

'material' is a write only property.
Raise an exception if attempt to read.


<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## material <sub>*etter*</sub>

```python
def material(self, attr_value):

```
> Node: [Set Material](GeometryNodeSetMaterial.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

Node implemented as property setter.

#### Args:
- attr_value: material


<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## normal <sub>*property*</sub>

```python
def normal(self):

```
> Node: [Normal](GeometryNodeInputNormal.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)

#### Returns:
- socket `normal`

<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## normal <sub>*etter*</sub>

```python
def normal(self, attr_value):

```
> Node: [Set Curve Normal](GeometryNodeSetCurveNormal.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_normal.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveNormal.html)

Node implemented as property setter.

#### Args:
- attr_value: mode


<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## points

```python
def points(self, weights=None, sort_index=None):

```
> Node: [Points of Curve](GeometryNodePointsOfCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/points_of_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsOfCurve.html)

#### Args:
- weights: Float
- sort_index: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePointsOfCurve.webp)

#### Returns:
- tuple ('`point_index`', '`total`')

<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## resample

```python
def resample(self, count=None, length=None, mode='COUNT'):

```
> Node: [Resample Curve](GeometryNodeResampleCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

#### Args:
- count: Integer
- length: Float
- mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]

#### Returns:
- self

<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## resample_count

```python
def resample_count(self, count=None):

```
> Node: [Resample Curve](GeometryNodeResampleCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

#### Args:
- count: Integer

#### Returns:
- self

<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## resample_evaluated

```python
def resample_evaluated(self):

```
> Node: [Resample Curve](GeometryNodeResampleCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

#### Returns:
- self

<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## resample_length

```python
def resample_length(self, length=None):

```
> Node: [Resample Curve](GeometryNodeResampleCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

#### Args:
- length: Float

#### Returns:
- self

<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## resolution <sub>*property*</sub>

```python
def resolution(self):

```
> Node: [Spline Resolution](GeometryNodeInputSplineResolution.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_resolution.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineResolution.html)

#### Returns:
- socket `resolution`

<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## resolution <sub>*etter*</sub>

```python
def resolution(self, attr_value):

```
> Node: [Set Spline Resolution](GeometryNodeSetSplineResolution.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_resolution.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html)

Node implemented as property setter.

#### Args:
- attr_value: resolution


<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## separate

```python
def separate(self, geometry=None):

```
> Node: [Separate Geometry](GeometryNodeSeparateGeometry.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

#### Args:
- geometry: Geometry

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

#### Returns:
- tuple ('`selection`', '`inverted`')

<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_cyclic

```python
def set_cyclic(self, cyclic=None):

```
> Node: [Set Spline Cyclic](GeometryNodeSetSplineCyclic.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_cyclic.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html)

#### Args:
- cyclic: Boolean

#### Returns:
- self

<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_material

```python
def set_material(self, material=None):

```
> Node: [Set Material](GeometryNodeSetMaterial.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

#### Args:
- material: Material

#### Returns:
- self

<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_normal

```python
def set_normal(self, mode='MINIMUM_TWIST'):

```
> Node: [Set Curve Normal](GeometryNodeSetCurveNormal.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_normal.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveNormal.html)

#### Args:
- mode (str): 'MINIMUM_TWIST' in [MINIMUM_TWIST, Z_UP]

#### Returns:
- self

<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_resolution

```python
def set_resolution(self, resolution=None):

```
> Node: [Set Spline Resolution](GeometryNodeSetSplineResolution.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_resolution.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html)

#### Args:
- resolution: Integer

#### Returns:
- self

<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_type

```python
def set_type(self, spline_type='POLY'):

```
> Node: [Set Spline Type](GeometryNodeCurveSplineType.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)

#### Args:
- spline_type (str): 'POLY' in [CATMULL_ROM, POLY, BEZIER, NURBS]

#### Returns:
- self

<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## type <sub>*property*</sub>

```python
def type(self):

```
> Node: [Set Spline Type](GeometryNodeCurveSplineType.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)

'type' is a write only property.
Raise an exception if attempt to read.


<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## type <sub>*etter*</sub>

```python
def type(self, attr_value):

```
> Node: [Set Spline Type](GeometryNodeCurveSplineType.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)

Node implemented as property setter.

#### Args:
- attr_value: spline_type


<sub>Go to [top](#class-Spline) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

