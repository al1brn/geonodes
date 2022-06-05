
# Class Collection

> Inherits from: ***dsock.Collection***

## Methods



- [info](#info) : [CollectionInfo](../nodes/CollectionInfo.md) geometry (Geometry)
- [switch](#switch) : [Switch](../nodes/Switch.md) output (Collection)



## Methods reference


### info

> Node: [CollectionInfo](../nodes/{self.node_name}.md)

```python
v = collection.info(separate_children, reset_children, transform_space)
```


#### Arguments


##### Sockets arguments



- collection : Collection (self)
- separate_children : Boolean
- reset_children : Boolean



##### Parameters arguments



- transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]



#### Node creation


```python
node = nodes.CollectionInfo(collection=self, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space)
```


#### Returns

    Geometry

### switch

> Node: [Switch](../nodes/{self.node_name}.md)

```python
v = collection.switch(switch1, true)
```


#### Arguments


##### Sockets arguments



- false : Collection (self)
- switch1 : Boolean
- true : Collection



##### Fixed parameters



- input_type : 'COLLECTION'



#### Node creation


```python
node = nodes.Switch(false=self, switch1=switch1, true=true, input_type='COLLECTION')
```


#### Returns

    Collection
