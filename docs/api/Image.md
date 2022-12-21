# class Image

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)


## Class methods

- [Input](#Input-classmethod)


## Methods

- [switch](#switch)
- [texture](#texture)

## Input <sub>*classmethod*</sub>

```python
def Input(cls, value=None, name="CLASS_METHOD", description=""):

```
Used to create an input socket in the Group Input node.
Even if homonyms are accepted, it is recommended to avoid to create to input sockets with the same name.
The initial value can be either a valid Blender Image or the name of an existing Blender Image.

### Args:
- value: Blender Image or name of an existing Blender Image
- name: Input socket name. Avoid homonyms!
- description: user help

### Returns:
- Image

<sub>Go to [top](#class-Image) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## switch

```python
def switch(self, switch=None, true=None):

```
Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

### Args:
- switch: Boolean
- true: Image

### Returns:
- socket `output`

<sub>Go to [top](#class-Image) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## texture

```python
def texture(self, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):

```
Node [Image Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageTexture.html) )

### Args:
- vector: Vector
- frame: Integer
- extension (str): 'REPEAT' in [REPEAT, EXTEND, CLIP]
- interpolation (str): 'Linear' in [Linear, Closest, Cubic]

### Returns:
- tuple ('`color`', '`alpha`')

<sub>Go to [top](#class-Image) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

