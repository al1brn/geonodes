# class Material

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)


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

#### Args:
- value: Blender Material or name of an existing Blender Material
- name: Input socket name. Avoid homonyms!
- description: user help

#### Returns:
- Material

<sub>Go to [top](#class-Material) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Material <sub>*classmethod*</sub>

```python
def Material(cls):

```
> Node: [Material](GeometryNodeInputMaterial.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/material.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterial.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMaterial.webp)

#### Returns:
- socket `material`

<sub>Go to [top](#class-Material) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## switch

```python
def switch(self, switch=None, true=None):

```
> Node: [Switch](GeometryNodeSwitch.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Material

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSwitch.webp)

#### Returns:
- socket `output`

<sub>Go to [top](#class-Material) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

