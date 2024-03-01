# Socket Mat


### Methods

- [material_selection](#material_selection)
- [switch](#switch)

## Methods

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
def material_selection(self, material=None, node_label=None, node_color=None):
    node = self.tree.MaterialSelection(material=material, node_label=node_label, node_color=node_color)
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
def switch(self, switch=None, true=None, node_label=None, node_color=None):
    node = self.tree.Switch(switch=switch, false=self, true=true, input_type='MATERIAL', node_label=node_label, node_color=node_color)
    return node.output
```
