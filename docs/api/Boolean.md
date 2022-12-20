# class Boolean


## Class methods

- [Boolean](#Boolean-classmethod)
- [Input](#Input-classmethod)


## Methods

- [b_and](#b_and)
- [b_not](#b_not)
- [b_or](#b_or)
- [imply](#imply)
- [nand](#nand)
- [nimply](#nimply)
- [nor](#nor)
- [switch](#switch)
- [xnor](#xnor)
- [xor](#xor)

## Boolean <sub>*classmethod*</sub>

```python
def Boolean(cls, boolean=False):

```
Node [Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/boolean.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputBool.html) )

### Args:
- boolean (bool): False

### Returns:
- socket `boolean`

<sub>Go to [top](#class-Boolean) [data structure](../structure.md)</sub>

## Input <sub>*classmethod*</sub>

```python
def Input(cls, value=None, name="CLASS_METHOD", min_value=None, max_value=None, description=""):

```
Used to create an input socket in the Group Input node.
Even if homonyms are accepted, it is recommended to avoid to create to input sockets with the same name.

### Args:
- value: Initial value. Not changed if the group input socket already exists
- name: Input socket name. Avoid homonyms!
- min_value: minimum value
- max_value: maxium value
- description: user help

### Returns:
- Boolean

<sub>Go to [top](#class-Boolean) [data structure](../structure.md)</sub>

## b_and

```python
def b_and(self, boolean1=None):

```
Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html) )

### Args:
- boolean1: Boolean

### Returns:
- socket `boolean`

<sub>Go to [top](#class-Boolean) [data structure](../structure.md)</sub>

## b_not

```python
def b_not(self):

```
Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html) )

### Returns:
- socket `boolean`

<sub>Go to [top](#class-Boolean) [data structure](../structure.md)</sub>

## b_or

```python
def b_or(self, boolean1=None):

```
Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html) )

### Args:
- boolean1: Boolean

### Returns:
- socket `boolean`

<sub>Go to [top](#class-Boolean) [data structure](../structure.md)</sub>

## imply

```python
def imply(self, boolean1=None):

```
Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html) )

### Args:
- boolean1: Boolean

### Returns:
- socket `boolean`

<sub>Go to [top](#class-Boolean) [data structure](../structure.md)</sub>

## nand

```python
def nand(self, boolean1=None):

```
Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html) )

### Args:
- boolean1: Boolean

### Returns:
- socket `boolean`

<sub>Go to [top](#class-Boolean) [data structure](../structure.md)</sub>

## nimply

```python
def nimply(self, boolean1=None):

```
Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html) )

### Args:
- boolean1: Boolean

### Returns:
- socket `boolean`

<sub>Go to [top](#class-Boolean) [data structure](../structure.md)</sub>

## nor

```python
def nor(self, boolean1=None):

```
Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html) )

### Args:
- boolean1: Boolean

### Returns:
- socket `boolean`

<sub>Go to [top](#class-Boolean) [data structure](../structure.md)</sub>

## switch

```python
def switch(self, switch=None, true=None):

```
Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

### Args:
- switch: Boolean
- true: Boolean

### Returns:
- socket `output`

<sub>Go to [top](#class-Boolean) [data structure](../structure.md)</sub>

## xnor

```python
def xnor(self, boolean1=None):

```
Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html) )

### Args:
- boolean1: Boolean

### Returns:
- socket `boolean`

<sub>Go to [top](#class-Boolean) [data structure](../structure.md)</sub>

## xor

```python
def xor(self, boolean1=None):

```
Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html) )

### Args:
- boolean1: Boolean

### Returns:
- socket `boolean`

<sub>Go to [top](#class-Boolean) [data structure](../structure.md)</sub>

