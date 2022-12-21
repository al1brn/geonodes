# class Rotation

> [main](./structure.md) - [nodes](ndes.md) - [nodes menu](.nodes_menus.md)


## Class methods

- [AxisAngle](#AxisAngle-classmethod)
- [Euler](#Euler-classmethod)


## Methods

- [align_to_vector](#align_to_vector)
- [rotate_axis_angle](#rotate_axis_angle)
- [rotate_euler](#rotate_euler)

## AxisAngle <sub>*classmethod*</sub>

```python
def AxisAngle(cls, rotation=None, axis=None, angle=None, space='OBJECT'):

```
Node [Rotate Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotate_euler.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html) )

### Args:
- rotation: Vector
- axis: Vector
- angle: Float
- space (str): 'OBJECT' in [OBJECT, LOCAL]

### Returns:
- socket `rotation`

<sub>Go to [top](#class-Rotation) - [main](./structure.md) - [nodes](ndes.md) - [nodes menu](.nodes_menus.md)</sub>

## Euler <sub>*classmethod*</sub>

```python
def Euler(cls, rotation=None, rotate_by=None, space='OBJECT'):

```
Node [Rotate Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotate_euler.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html) )

### Args:
- rotation: Vector
- rotate_by: Vector
- space (str): 'OBJECT' in [OBJECT, LOCAL]

### Returns:
- socket `rotation`

<sub>Go to [top](#class-Rotation) - [main](./structure.md) - [nodes](ndes.md) - [nodes menu](.nodes_menus.md)</sub>

## align_to_vector

```python
def align_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO'):

```
Node [Align Euler to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/align_euler_to_vector.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html) )

### Args:
- factor: Float
- vector: Vector
- axis (str): 'X' in [X, Y, Z]
- pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]

### Returns:
- self

<sub>Go to [top](#class-Rotation) - [main](./structure.md) - [nodes](ndes.md) - [nodes menu](.nodes_menus.md)</sub>

## rotate_axis_angle

```python
def rotate_axis_angle(self, axis=None, angle=None, space='OBJECT'):

```
Node [Rotate Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotate_euler.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html) )

### Args:
- axis: Vector
- angle: Float
- space (str): 'OBJECT' in [OBJECT, LOCAL]

### Returns:
- socket `rotation`

<sub>Go to [top](#class-Rotation) - [main](./structure.md) - [nodes](ndes.md) - [nodes menu](.nodes_menus.md)</sub>

## rotate_euler

```python
def rotate_euler(self, rotate_by=None, space='OBJECT'):

```
Node [Rotate Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotate_euler.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html) )

### Args:
- rotate_by: Vector
- space (str): 'OBJECT' in [OBJECT, LOCAL]

### Returns:
- socket `rotation`

<sub>Go to [top](#class-Rotation) - [main](./structure.md) - [nodes](ndes.md) - [nodes menu](.nodes_menus.md)</sub>

