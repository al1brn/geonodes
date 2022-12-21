# class Object

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)


## Class methods

- [Input](#Input-classmethod)
- [Self](#Self-classmethod)


## Methods

- [geometry](#geometry)
- [info](#info)
- [location](#location)
- [rotation](#rotation)
- [scale](#scale)
- [switch](#switch)

## Input <sub>*classmethod*</sub>

```python
def Input(cls, value=None, name="CLASS_METHOD", description=""):

```
Used to create an input socket in the Group Input node.
Even if homonyms are accepted, it is recommended to avoid to create to input sockets with the same name.
The initial value can be either a valid Blender Object or the name of an existing Blender Object.

#### Args:
- value: Blender Object or name of an existing Blender Object
- name: Input socket name. Avoid homonyms!
- description: user help

#### Returns:
- Object

<sub>Go to [top](#class-Object) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Self <sub>*classmethod*</sub>

```python
def Self(cls):

```
Node [Self Object](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/self_object.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSelfObject.html) )

#### Returns:
- socket `self_object`

<sub>Go to [top](#class-Object) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## geometry

```python
def geometry(self, object=None, as_instance=None, transform_space='ORIGINAL'):

```
Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

#### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- socket `geometry`

<sub>Go to [top](#class-Object) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## info

```python
def info(self, object=None, as_instance=None, transform_space='ORIGINAL'):

```
Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

#### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- node with sockets ['location', 'rotation', 'scale', 'geometry']

<sub>Go to [top](#class-Object) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## location

```python
def location(self, object=None, as_instance=None, transform_space='ORIGINAL'):

```
Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

#### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- socket `location`

<sub>Go to [top](#class-Object) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## rotation

```python
def rotation(self, object=None, as_instance=None, transform_space='ORIGINAL'):

```
Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

#### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- socket `rotation`

<sub>Go to [top](#class-Object) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## scale

```python
def scale(self, object=None, as_instance=None, transform_space='ORIGINAL'):

```
Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html) )

#### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- socket `scale`

<sub>Go to [top](#class-Object) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## switch

```python
def switch(self, switch=None, true=None):

```
Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

#### Args:
- switch: Boolean
- true: Object

#### Returns:
- socket `output`

<sub>Go to [top](#class-Object) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

