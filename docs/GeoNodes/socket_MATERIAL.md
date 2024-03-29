# Socket MATERIAL


### Methods

- [index_switch](#index_switch)
- [material_selection](#material_selection)
- [switch](#switch)

## Methods

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
    node = self.tree.IndexSwitch(self, *args, index=index, data_type='MATERIAL', node_label=node_label, node_color=node_color, **kwargs)
    return node.output
```
### material_selection


- node : [MaterialSelection](/docs/GeoNodes/MaterialSelection.md)
- self
- jump : No
- return : selection

##### Arguments

- material : None
- node_label : None
- node_color : None

#### Source code

``` python
def material_selection(self, material=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.MaterialSelection(material=material, node_label=node_label, node_color=node_color, **kwargs)
    return node.selection
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
    node = self.tree.Switch(switch=switch, false=self, true=true, input_type='MATERIAL', node_label=node_label, node_color=node_color, **kwargs)
    return node.output
```
