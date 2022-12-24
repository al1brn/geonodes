# Class Material

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Content

**Properties**

***Inherited***



**Class and static methods**

[Input](#Input) | [Material](#Material)

***Inherited***

Input | Material

**Methods**

[switch](#switch)

***Inherited***

switch

## Class and static methods

### Input

```python
@classmethod
def Input(cls, value=None, name="Material", description="")
```

 Create a Material input socket in the Group Input Node

#### Args:
- name: The socket name
- description: User tip
    
Returns:
    Material: The Material data socket




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Material

```python
@classmethod
def Material(cls)
```



## Material <sub>*classmethod*</sub>

```python
def Material(cls):

```
> Node: [Material](GeometryNodeInputMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterial.html)

#### Returns:
- socket `material`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### switch

```python
def switch(self, switch=None, true=None)
```



## switch

```python
def switch(self, switch=None, true=None):

```
> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Material

#### Returns:
- socket `output`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

