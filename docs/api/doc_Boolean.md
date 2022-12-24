# Class Boolean

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Content

**Properties**

***Inherited***

[bl_idname](DataSocket.md#bl_idname) | [bnode](DataSocket.md#bnode) | [is_multi_input](DataSocket.md#is_multi_input) | [is_output](DataSocket.md#is_output) | [is_plugged](DataSocket.md#is_plugged) | [links](DataSocket.md#links) | [name](DataSocket.md#name) | [node_chain_label](DataSocket.md#node_chain_label) | [socket_index](DataSocket.md#socket_index)

**Class and static methods**

[Boolean](#Boolean) | [Input](#Input)

***Inherited***

[get_bl_idname](DataSocket.md#get_bl_idname) | [get_class_name](DataSocket.md#get_class_name) | [gives_bsocket](DataSocket.md#gives_bsocket) | [is_socket](DataSocket.md#is_socket) | [is_vector](DataSocket.md#is_vector) | [value_data_type](DataSocket.md#value_data_type)

**Methods**

[b_and](#b_and) | [b_not](#b_not) | [b_or](#b_or) | [imply](#imply) | [nand](#nand) | [nimply](#nimply) | [nor](#nor) | [switch](#switch) | [xnor](#xnor) | [xor](#xor)

***Inherited***

[connected_sockets](DataSocket.md#connected_sockets) | [convert_python_type](DataSocket.md#convert_python_type) | [get_blender_socket](DataSocket.md#get_blender_socket) | [init_domains](DataSocket.md#init_domains) | [init_socket](DataSocket.md#init_socket) | [plug](DataSocket.md#plug) | [reroute](DataSocket.md#reroute) | [reset_properties](DataSocket.md#reset_properties) | [stack](DataSocket.md#stack) | [to_output](DataSocket.md#to_output)

## Class and static methods

### Boolean

```python
@classmethod
def Boolean(cls, boolean=False)
```



```python
def Boolean(cls, boolean=False):

```
> Node: [Boolean](FunctionNodeInputBool.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/boolean.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputBool.html)

#### Args:
- boolean (bool): False

#### Returns:
- socket `boolean`






<sub>Go to [top](#class-Boolean) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Input

```python
@classmethod
def Input(cls, value = False, name = "Boolean", description = "")
```

 Create a Boolean input socket in the Group Input Node

#### Args:
- value: The default value
- name: The socket name
- description: User tip
    
#### Returns:
- Boolean: The Boolean data socket




<sub>Go to [top](#class-Boolean) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### b_and

```python
def b_and(self, boolean1=None)
```



```python
def b_and(self, boolean1=None):

```
> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#class-Boolean) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### b_not

```python
def b_not(self)
```



```python
def b_not(self):

```
> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Returns:
- socket `boolean`






<sub>Go to [top](#class-Boolean) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### b_or

```python
def b_or(self, boolean1=None)
```



```python
def b_or(self, boolean1=None):

```
> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#class-Boolean) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### imply

```python
def imply(self, boolean1=None)
```



```python
def imply(self, boolean1=None):

```
> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#class-Boolean) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### nand

```python
def nand(self, boolean1=None)
```



```python
def nand(self, boolean1=None):

```
> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#class-Boolean) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### nimply

```python
def nimply(self, boolean1=None)
```



```python
def nimply(self, boolean1=None):

```
> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#class-Boolean) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### nor

```python
def nor(self, boolean1=None)
```



```python
def nor(self, boolean1=None):

```
> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#class-Boolean) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch

```python
def switch(self, switch=None, true=None)
```



```python
def switch(self, switch=None, true=None):

```
> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Boolean

#### Returns:
- socket `output`






<sub>Go to [top](#class-Boolean) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### xnor

```python
def xnor(self, boolean1=None)
```



```python
def xnor(self, boolean1=None):

```
> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#class-Boolean) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### xor

```python
def xor(self, boolean1=None)
```



```python
def xor(self, boolean1=None):

```
> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#class-Boolean) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>
