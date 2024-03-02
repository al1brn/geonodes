# Socket TEXTURE


### Methods

- [switch](#switch)

## Methods

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
    node = self.tree.Switch(switch=switch, false=self, true=true, input_type='TEXTURE', node_label=node_label, node_color=node_color)
    return node.output
```
