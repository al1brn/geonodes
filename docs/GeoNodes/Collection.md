# Socket Collection

### Properties


### Methods

- [collection_info](#collection_info)
- [switch](#switch)

## Properties

## Methods

### collection_info


- node : [CollectionInfo](/docs/GeoNodes/CollectionInfo.md)
- self : collection
- jump : No
- return : instances

##### Arguments

- separate_children : None
- reset_children : None
- transform_space : ORIGINAL in ('ORIGINAL', 'RELATIVE')
- node_label : None
- node_color : None

#### Source code

``` python
def collection_info(self, separate_children=None, reset_children=None, transform_space='ORIGINAL', node_label=None, node_color=None):
    node = self.tree.CollectionInfo(collection=self, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space, node_label=node_label, node_color=node_color)
    return node.instances
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
    node = self.tree.Switch(switch=switch, false=self, true=true, input_type='COLLECTION', node_label=node_label, node_color=node_color)
    return node.output
```
