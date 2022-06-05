
# Class Object

> Inherits from: ***dsock.Object***

## Properties



- info : Sockets      [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]



## Methods



- switch : output (Object)



## Methods


### info

> Node: [ObjectInfo](../nodes/{self.node_name}.md)

```python
v = object.info
```


#### Arguments


##### Sockets arguments



- object : Object (self)
- as_instance : Boolean



##### Parameters arguments



- transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]



##### Fixed parameters



- label:f"{self.node_chain_label}.info"



#### Returns

    Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]

### switch

> Node: [Switch](../nodes/{self.node_name}.md)

```python
v = object.switch(switch1, true)
```


#### Arguments


##### Sockets arguments



- false : Object (self)
- switch1 : Boolean
- true : Object



##### Fixed parameters



- input_type : 'OBJECT'



#### Returns

    Object
