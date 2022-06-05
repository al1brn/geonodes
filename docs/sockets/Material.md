
# Class Material

> Inherits from: ***dsock.Material***

## Methods



- [**self.meth_name**](#selection) : [MaterialSelection](../nodes/MaterialSelection.md) selection (Boolean)
- [**self.meth_name**](#switch) : [Switch](../nodes/Switch.md) output (Material)



## Methods reference


### selection

> Node: [MaterialSelection](../nodes/{self.node_name}.md)

```python
v = material.selection()
```


#### Arguments


##### Sockets arguments



- material : Material (self)



#### Node creation


```python
node = nodes.MaterialSelection(material=self)
```


#### Returns

    Boolean

### switch

> Node: [Switch](../nodes/{self.node_name}.md)

```python
v = material.switch(switch1, true)
```


#### Arguments


##### Sockets arguments



- false : Material (self)
- switch1 : Boolean
- true : Material



##### Fixed parameters



- input_type : 'MATERIAL'



#### Node creation


```python
node = nodes.Switch(false=self, switch1=switch1, true=true, input_type='MATERIAL')
```


#### Returns

    Material
