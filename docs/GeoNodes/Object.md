# Socket Object


### Methods

- [object_info](#object_info)
- [switch](#switch)

## Methods

### object_info


- node : [ObjectInfo](/docs/GeoNodes/ObjectInfo.md)
- self : object
- jump : No
- return : node

##### Arguments

- as_instance : None
- transform_space : ORIGINAL in ('ORIGINAL', 'RELATIVE')
- node_label : None
- node_color : None

#### Source code

``` python
def object_info(self, as_instance=None, transform_space='ORIGINAL', node_label=None, node_color=None):
    node = self.tree.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, node_label=node_label, node_color=node_color)
    return node
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
    node = self.tree.Switch(switch=switch, false=self, true=true, input_type='OBJECT', node_label=node_label, node_color=node_color)
    return node.output
```
