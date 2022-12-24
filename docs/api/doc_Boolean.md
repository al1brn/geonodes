# Class Boolean

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Content

**Properties**

***Inherited***



**Class and static methods**

[Boolean](#Boolean) | [Input](#Input)

***Inherited***

Boolean | Input

**Methods**

[b_and](#b_and) | [b_not](#b_not) | [b_or](#b_or) | [imply](#imply) | [nand](#nand) | [nimply](#nimply) | [nor](#nor) | [switch](#switch) | [xnor](#xnor) | [xor](#xor)

***Inherited***

b_and | b_not | b_or | imply | nand | nimply | nor | switch | xnor | xor

## Class and static methods

### Boolean

```python
@classmethod
def Boolean(cls, boolean=False)
```



## Boolean <sub>*classmethod*</sub>

```python
def Boolean(cls, boolean=False):

```
> Node: [Boolean](FunctionNodeInputBool.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/boolean.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputBool.html)

#### Args:
- boolean (bool): False

#### Returns:
- socket `boolean`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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
    
Returns:
    Boolean: The Boolean data socket




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### b_and

```python
def b_and(self, boolean1=None)
```



## b_and

```python
def b_and(self, boolean1=None):

```
> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### b_not

```python
def b_not(self)
```



## b_not

```python
def b_not(self):

```
> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Returns:
- socket `boolean`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### b_or

```python
def b_or(self, boolean1=None)
```



## b_or

```python
def b_or(self, boolean1=None):

```
> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### imply

```python
def imply(self, boolean1=None)
```



## imply

```python
def imply(self, boolean1=None):

```
> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### nand

```python
def nand(self, boolean1=None)
```



## nand

```python
def nand(self, boolean1=None):

```
> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### nimply

```python
def nimply(self, boolean1=None)
```



## nimply

```python
def nimply(self, boolean1=None):

```
> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### nor

```python
def nor(self, boolean1=None)
```



## nor

```python
def nor(self, boolean1=None):

```
> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean1: Boolean

#### Returns:
- socket `boolean`






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
- true: Boolean

#### Returns:
- socket `output`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### xnor

```python
def xnor(self, boolean1=None)
```



## xnor

```python
def xnor(self, boolean1=None):

```
> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### xor

```python
def xor(self, boolean1=None)
```



## xor

```python
def xor(self, boolean1=None):

```
> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

