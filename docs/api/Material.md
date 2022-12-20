# class Material


## Class methods

- [Input](#Input-classmethod)
- [Material](#Material-classmethod)


## Methods

- [switch](#switch)

## Input <sub>*classmethod*</sub>

```python
def Input(cls, value=None, name="CLASS_METHOD", description=""):

```
Used to create an input socket in the Group Input node.
Even if homonyms are accepted, it is recommended to avoid to create to input sockets with the same name.
The initial value can be either a valid Blender Material or the name of an existing Blender Material.

### Args:
- value: Blender Material or name of an existing Blender Material
- name: Input socket name. Avoid homonyms!
- description: user help

### Returns:
- Material

<sub>Go to [top](#class-Material) [data structure](../structure.md)</sub>

## Material <sub>*classmethod*</sub>

```python
def Material(cls):

```
Node [Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterial.html) )

### Returns:
- socket `material`

<sub>Go to [top](#class-Material) [data structure](../structure.md)</sub>

## switch

```python
def switch(self, switch=None, true=None):

```
Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

### Args:
- switch: Boolean
- true: Material

### Returns:
- socket `output`

<sub>Go to [top](#class-Material) [data structure](../structure.md)</sub>

