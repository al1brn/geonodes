# Class Object

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

 Object DataSocket




### Constructor

```python
Object(self, obj=None)
```

## Content

**Properties**

[bobject](#bobject)

***Inherited***

[bl_idname](DataSocket.md#bl_idname) | [bnode](DataSocket.md#bnode) | [is_multi_input](DataSocket.md#is_multi_input) | [is_output](DataSocket.md#is_output) | [is_plugged](DataSocket.md#is_plugged) | [links](DataSocket.md#links) | [name](DataSocket.md#name) | [node_chain_label](DataSocket.md#node_chain_label) | [socket_index](DataSocket.md#socket_index)

**Class and static methods**

[Input](#Input) | [Self](#Self)

***Inherited***

[get_bl_idname](DataSocket.md#get_bl_idname) | [get_class_name](DataSocket.md#get_class_name) | [gives_bsocket](DataSocket.md#gives_bsocket) | [is_socket](DataSocket.md#is_socket) | [is_vector](DataSocket.md#is_vector) | [python_type_to_socket](DataSocket.md#python_type_to_socket) | [value_data_type](DataSocket.md#value_data_type)

**Methods**

[geometry](#geometry) | [info](#info) | [location](#location) | [rotation](#rotation) | [scale](#scale) | [switch](#switch)

***Inherited***

[connected_sockets](DataSocket.md#connected_sockets) | [get_blender_socket](DataSocket.md#get_blender_socket) | [init_domains](DataSocket.md#init_domains) | [init_socket](DataSocket.md#init_socket) | [plug](DataSocket.md#plug) | [reroute](DataSocket.md#reroute) | [reset_properties](DataSocket.md#reset_properties) | [stack](DataSocket.md#stack) | [to_output](DataSocket.md#to_output)

## Properties

### bobject

 Returns the blender of object.

A [DataSocket](DataSocket.md) **Object** has the particularity to be initialized without any socket.
This allow to call the node *'Object Info'* alone.

bobject returns the blender object for this node.

#### Returns:
- Blender Object or self if bsocket if not None



<sub>Go to [top](#class-Object) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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
    
#### Returns:
- Object: The Object data socket




<sub>Go to [top](#class-Object) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Self

```python
@classmethod
def Self(cls)
```



> Node: [Self Object](GeometryNodeSelfObject.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/self_object.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSelfObject.html)

#### Returns:
- socket `self_object`






<sub>Go to [top](#class-Object) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### geometry

```python
def geometry(self, as_instance=None, transform_space='ORIGINAL')
```



> Node: [Object Info](GeometryNodeObjectInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)

#### Args:
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- socket `geometry`






<sub>Go to [top](#class-Object) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### info

```python
def info(self, as_instance=None, transform_space='ORIGINAL')
```



> Node: [Object Info](GeometryNodeObjectInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)

#### Args:
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- node with sockets ['location', 'rotation', 'scale', 'geometry']






<sub>Go to [top](#class-Object) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### location

```python
def location(self, as_instance=None, transform_space='ORIGINAL')
```



> Node: [Object Info](GeometryNodeObjectInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)

#### Args:
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- socket `location`






<sub>Go to [top](#class-Object) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### rotation

```python
def rotation(self, as_instance=None, transform_space='ORIGINAL')
```



> Node: [Object Info](GeometryNodeObjectInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)

#### Args:
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- socket `rotation`






<sub>Go to [top](#class-Object) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### scale

```python
def scale(self, as_instance=None, transform_space='ORIGINAL')
```



> Node: [Object Info](GeometryNodeObjectInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)

#### Args:
- as_instance: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- socket `scale`






<sub>Go to [top](#class-Object) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch

```python
def switch(self, switch=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Object

#### Returns:
- socket `output`






<sub>Go to [top](#class-Object) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

