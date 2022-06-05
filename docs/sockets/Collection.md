
# Class Collection

> Inherits from: ***dsock.Collection***

## Methods



- info : geometry (Geometry)
- switch : output (Collection)



## Methods


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



#### Returns

    Collection
