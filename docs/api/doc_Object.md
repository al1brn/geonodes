# Class Object

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Content



**Class and static methods**

[Input](#Input) | [Self](#Self)

**Methods**

[geometry](#geometry) | [info](#info) | [location](#location) | [rotation](#rotation) | [scale](#scale) | [switch](#switch)

## Inheritance

**Properties**

[[DataSocket](DataSocket.md#bl_idname](#[DataSocket](DataSocket.md#bl_idname) | [[DataSocket](DataSocket.md#bnode](#[DataSocket](DataSocket.md#bnode) | [[DataSocket](DataSocket.md#is_multi_input](#[DataSocket](DataSocket.md#is_multi_input) | [[DataSocket](DataSocket.md#is_output](#[DataSocket](DataSocket.md#is_output) | [[DataSocket](DataSocket.md#is_plugged](#[DataSocket](DataSocket.md#is_plugged) | [[DataSocket](DataSocket.md#links](#[DataSocket](DataSocket.md#links) | [[DataSocket](DataSocket.md#name](#[DataSocket](DataSocket.md#name) | [[DataSocket](DataSocket.md#node_chain_label](#[DataSocket](DataSocket.md#node_chain_label) | [[DataSocket](DataSocket.md#socket_index](#[DataSocket](DataSocket.md#socket_index)**Class and static methods**

[[DataSocket](DataSocket.md#get_bl_idname](#[DataSocket](DataSocket.md#get_bl_idname) | [[DataSocket](DataSocket.md#get_class_name](#[DataSocket](DataSocket.md#get_class_name) | [[DataSocket](DataSocket.md#gives_bsocket](#[DataSocket](DataSocket.md#gives_bsocket) | [[DataSocket](DataSocket.md#is_socket](#[DataSocket](DataSocket.md#is_socket) | [[DataSocket](DataSocket.md#is_vector](#[DataSocket](DataSocket.md#is_vector) | [[DataSocket](DataSocket.md#value_data_type](#[DataSocket](DataSocket.md#value_data_type)**Methods**

[[DataSocket](DataSocket.md#connected_sockets](#[DataSocket](DataSocket.md#connected_sockets) | [[DataSocket](DataSocket.md#convert_python_type](#[DataSocket](DataSocket.md#convert_python_type) | [[DataSocket](DataSocket.md#get_blender_socket](#[DataSocket](DataSocket.md#get_blender_socket) | [[DataSocket](DataSocket.md#init_domains](#[DataSocket](DataSocket.md#init_domains) | [[DataSocket](DataSocket.md#init_socket](#[DataSocket](DataSocket.md#init_socket) | [[DataSocket](DataSocket.md#plug](#[DataSocket](DataSocket.md#plug) | [[DataSocket](DataSocket.md#reroute](#[DataSocket](DataSocket.md#reroute) | [[DataSocket](DataSocket.md#reset_properties](#[DataSocket](DataSocket.md#reset_properties) | [[DataSocket](DataSocket.md#stack](#[DataSocket](DataSocket.md#stack) | [[DataSocket](DataSocket.md#to_output](#[DataSocket](DataSocket.md#to_output)

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

