# Class Material

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Content



**Class and static methods**

[Input](#Input) | [Material](#Material)

**Methods**

[switch](#switch)

## Inheritance

**Properties**

[DataSocket](DataSocket.md#bl_idname) | [DataSocket](DataSocket.md#bnode) | [DataSocket](DataSocket.md#is_multi_input) | [DataSocket](DataSocket.md#is_output) | [DataSocket](DataSocket.md#is_plugged) | [DataSocket](DataSocket.md#links) | [DataSocket](DataSocket.md#name) | [DataSocket](DataSocket.md#node_chain_label) | [DataSocket](DataSocket.md#socket_index)**Class and static methods**

[DataSocket](DataSocket.md#get_bl_idname) | [DataSocket](DataSocket.md#get_class_name) | [DataSocket](DataSocket.md#gives_bsocket) | [DataSocket](DataSocket.md#is_socket) | [DataSocket](DataSocket.md#is_vector) | [DataSocket](DataSocket.md#value_data_type)**Methods**

[DataSocket](DataSocket.md#connected_sockets) | [DataSocket](DataSocket.md#convert_python_type) | [DataSocket](DataSocket.md#get_blender_socket) | [DataSocket](DataSocket.md#init_domains) | [DataSocket](DataSocket.md#init_socket) | [DataSocket](DataSocket.md#plug) | [DataSocket](DataSocket.md#reroute) | [DataSocket](DataSocket.md#reset_properties) | [DataSocket](DataSocket.md#stack) | [DataSocket](DataSocket.md#to_output)

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

