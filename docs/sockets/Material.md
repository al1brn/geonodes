
# Class Material

> Inherits from: ***dsock.Material***

## Methods



- [selection](#selection) : selection (Boolean)
- [switch](#switch) : output (Material)



## Methods


### selection

> Node: [MaterialSelection](../nodes/{self.node_name}.md)

```python
v = material.selection()
```


#### Arguments


##### Sockets arguments



- material : Material (self)



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



#### Returns

    Material
