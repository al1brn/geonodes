# Socket BOOLEAN


### Methods

- [band](#band)
- [bnot](#bnot)
- [bor](#bor)
- [imply](#imply)
- [index_switch](#index_switch)
- [nand](#nand)
- [nimply](#nimply)
- [nor](#nor)
- [switch](#switch)
- [xnor](#xnor)
- [xor](#xor)

## Methods

### band


- node : [BooleanMath](/docs/GeoNodes/BooleanMath.md)
- self : boolean
- jump : No
- return : boolean

##### Arguments

- boolean : None
- node_label : None
- node_color : None

#### Source code

``` python
def band(self, boolean=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.BooleanMath(boolean=self, boolean_1=boolean, operation='AND', node_label=node_label, node_color=node_color, **kwargs)
    return node.boolean
```
### bnot


- node : [BooleanMath](/docs/GeoNodes/BooleanMath.md)
- self : boolean
- jump : No
- return : boolean

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def bnot(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.BooleanMath(boolean=self, operation='NOT', node_label=node_label, node_color=node_color, **kwargs)
    return node.boolean
```
### bor


- node : [BooleanMath](/docs/GeoNodes/BooleanMath.md)
- self : boolean
- jump : No
- return : boolean

##### Arguments

- boolean : None
- node_label : None
- node_color : None

#### Source code

``` python
def bor(self, boolean=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.BooleanMath(boolean=self, boolean_1=boolean, operation='OR', node_label=node_label, node_color=node_color, **kwargs)
    return node.boolean
```
### imply


- node : [BooleanMath](/docs/GeoNodes/BooleanMath.md)
- self : boolean
- jump : No
- return : boolean

##### Arguments

- boolean : None
- node_label : None
- node_color : None

#### Source code

``` python
def imply(self, boolean=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.BooleanMath(boolean=self, boolean_1=boolean, operation='IMPLY', node_label=node_label, node_color=node_color, **kwargs)
    return node.boolean
```
### index_switch


- node : [IndexSwitch](/docs/GeoNodes/IndexSwitch.md)
- self : ARG0
- jump : No
- return : output

##### Arguments

- *args : 'ARG_NO_VALUE'
- index : None
- node_label : None
- node_color : None

#### Source code

``` python
def index_switch(self, *args, index=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.IndexSwitch(self, *args, index=index, data_type='BOOLEAN', node_label=node_label, node_color=node_color, **kwargs)
    return node.output
```
### nand


- node : [BooleanMath](/docs/GeoNodes/BooleanMath.md)
- self : boolean
- jump : No
- return : boolean

##### Arguments

- boolean : None
- node_label : None
- node_color : None

#### Source code

``` python
def nand(self, boolean=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.BooleanMath(boolean=self, boolean_1=boolean, operation='NAND', node_label=node_label, node_color=node_color, **kwargs)
    return node.boolean
```
### nimply


- node : [BooleanMath](/docs/GeoNodes/BooleanMath.md)
- self : boolean
- jump : No
- return : boolean

##### Arguments

- boolean : None
- node_label : None
- node_color : None

#### Source code

``` python
def nimply(self, boolean=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.BooleanMath(boolean=self, boolean_1=boolean, operation='NIMPLY', node_label=node_label, node_color=node_color, **kwargs)
    return node.boolean
```
### nor


- node : [BooleanMath](/docs/GeoNodes/BooleanMath.md)
- self : boolean
- jump : No
- return : boolean

##### Arguments

- boolean : None
- node_label : None
- node_color : None

#### Source code

``` python
def nor(self, boolean=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.BooleanMath(boolean=self, boolean_1=boolean, operation='NOR', node_label=node_label, node_color=node_color, **kwargs)
    return node.boolean
```
### switch


- node : [Switch](/docs/GeoNodes/Switch.md)
- self : false
- jump : No
- return : output

##### Arguments

- switch : None
- true : None
- node_label : None
- node_color : None

#### Source code

``` python
def switch(self, switch=None, true=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.Switch(switch=switch, false=self, true=true, input_type='BOOLEAN', node_label=node_label, node_color=node_color, **kwargs)
    return node.output
```
### xnor


- node : [BooleanMath](/docs/GeoNodes/BooleanMath.md)
- self : boolean
- jump : No
- return : boolean

##### Arguments

- boolean : None
- node_label : None
- node_color : None

#### Source code

``` python
def xnor(self, boolean=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.BooleanMath(boolean=self, boolean_1=boolean, operation='XNOR', node_label=node_label, node_color=node_color, **kwargs)
    return node.boolean
```
### xor


- node : [BooleanMath](/docs/GeoNodes/BooleanMath.md)
- self : boolean
- jump : No
- return : boolean

##### Arguments

- boolean : None
- node_label : None
- node_color : None

#### Source code

``` python
def xor(self, boolean=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.BooleanMath(boolean=self, boolean_1=boolean, operation='XOR', node_label=node_label, node_color=node_color, **kwargs)
    return node.boolean
```
