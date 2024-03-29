# Socket COLLECTION


### Methods

- [collection_info](#collection_info)
- [index_switch](#index_switch)
- [switch](#switch)

## Methods

### collection_info


- node : [CollectionInfo](/docs/GeoNodes/CollectionInfo.md)
- self : collection
- jump : No
- return : instances

##### Arguments

- separate_children : None
- reset_children : None
- transform_space : 'ORIGINAL' in ('ORIGINAL', 'RELATIVE')
- node_label : None
- node_color : None

#### Source code

``` python
def collection_info(self, separate_children=None, reset_children=None, transform_space='ORIGINAL', node_label=None, node_color=None, **kwargs):
    node = self.tree.CollectionInfo(collection=self, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space, node_label=node_label, node_color=node_color, **kwargs)
    return node.instances
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
    node = self.tree.IndexSwitch(self, *args, index=index, data_type='COLLECTION', node_label=node_label, node_color=node_color, **kwargs)
    return node.output
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
    node = self.tree.Switch(switch=switch, false=self, true=true, input_type='COLLECTION', node_label=node_label, node_color=node_color, **kwargs)
    return node.output
```
