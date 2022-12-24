# Class Object

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Content



**Class and static methods**

[Input](#Input) | [Self](#Self)

**Methods**

[geometry](#geometry) | [info](#info) | [location](#location) | [rotation](#rotation) | [scale](#scale) | [switch](#switch)

## Class and static methods

### Input

```python
@classmethod
def Input(cls, value=None, name="Object", description="")
```

 Create an Object input socket in the Group Input Node

#### Args:
- name: The socket name
- description: User tip
    
Returns:
    Object: The Object data socket




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Self

```python
@classmethod
def Self(cls)
```



## Self <sub>*classmethod*</sub>

```python
def Self(cls):

```
> Node: [Self Object](GeometryNodeSelfObject.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/self_object.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSelfObject.html)

#### Returns:
- socket `self_object`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### geometry

```python
def geometry(self, object=None, as_instance=None, transform_space='ORIGINAL')
```



## geometry

```python
def geometry(self, object=None, as_instance=None, transform_space='ORIGINAL'):

```
> Node: [Object Info](GeometryNodeObjectInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)

#### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- socket `geometry`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### info

```python
def info(self, object=None, as_instance=None, transform_space='ORIGINAL')
```



## info

```python
def info(self, object=None, as_instance=None, transform_space='ORIGINAL'):

```
> Node: [Object Info](GeometryNodeObjectInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)

#### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- node with sockets ['location', 'rotation', 'scale', 'geometry']






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### location

```python
def location(self, object=None, as_instance=None, transform_space='ORIGINAL')
```



## location

```python
def location(self, object=None, as_instance=None, transform_space='ORIGINAL'):

```
> Node: [Object Info](GeometryNodeObjectInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)

#### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- socket `location`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### rotation

```python
def rotation(self, object=None, as_instance=None, transform_space='ORIGINAL')
```



## rotation

```python
def rotation(self, object=None, as_instance=None, transform_space='ORIGINAL'):

```
> Node: [Object Info](GeometryNodeObjectInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)

#### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- socket `rotation`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### scale

```python
def scale(self, object=None, as_instance=None, transform_space='ORIGINAL')
```



## scale

```python
def scale(self, object=None, as_instance=None, transform_space='ORIGINAL'):

```
> Node: [Object Info](GeometryNodeObjectInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)

#### Args:
- object: Object
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- socket `scale`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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
- true: Object

#### Returns:
- socket `output`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

