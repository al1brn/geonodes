# Class Material

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

 Material DataSocket




### Constructor

```python
Material(self, value=None, label=None)
```

## Content

**Properties**

***Inherited***

[bl_idname](DataSocket.md#bl_idname) | [bnode](DataSocket.md#bnode) | [is_multi_input](DataSocket.md#is_multi_input) | [is_output](DataSocket.md#is_output) | [is_plugged](DataSocket.md#is_plugged) | [links](DataSocket.md#links) | [name](DataSocket.md#name) | [node_chain_label](DataSocket.md#node_chain_label) | [socket_index](DataSocket.md#socket_index)

**Class and static methods**

[Input](#Input) | [Material](#Material)

***Inherited***

[get_bl_idname](DataSocket.md#get_bl_idname) | [get_class_name](DataSocket.md#get_class_name) | [gives_bsocket](DataSocket.md#gives_bsocket) | [is_socket](DataSocket.md#is_socket) | [is_vector](DataSocket.md#is_vector) | [python_type_to_socket](DataSocket.md#python_type_to_socket) | [value_data_type](DataSocket.md#value_data_type)

**Methods**

[switch](#switch)

***Inherited***

[connected_sockets](DataSocket.md#connected_sockets) | [get_blender_socket](DataSocket.md#get_blender_socket) | [init_domains](DataSocket.md#init_domains) | [init_socket](DataSocket.md#init_socket) | [plug](DataSocket.md#plug) | [reroute](DataSocket.md#reroute) | [reset_properties](DataSocket.md#reset_properties) | [stack](DataSocket.md#stack) | [to_output](DataSocket.md#to_output)

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
    
#### Returns:
- Material: The Material data socket




<sub>Go to [top](#class-Material) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Material

```python
@classmethod
def Material(cls)
```



> Node: [Material](GeometryNodeInputMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterial.html)

#### Returns:
- socket `material`






<sub>Go to [top](#class-Material) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### switch

```python
def switch(self, switch=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Material

#### Returns:
- socket `output`






<sub>Go to [top](#class-Material) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

