
# Class Object

> Inherits from: ***dsock.Object***

## Properties



- [info](#info) : [ObjectInfo](../nodes/ObjectInfo.md) Sockets      [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]



## Methods



- [switch](#switch) : [Switch](../nodes/Switch.md) output (Object)



## Methods reference


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



#### Node creation


```python
node = nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.info")
```


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



#### Node creation


```python
node = nodes.Switch(false=self, switch1=switch1, true=true, input_type='OBJECT')
```


#### Returns

    Object
