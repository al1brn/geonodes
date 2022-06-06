
# Class Object

> Inherits from: ***dsock.Object***


[Index](/docs/index.md)

## Properties



- [**geometry**](#geometry) : [ObjectInfo](../nodes/ObjectInfo.md) geometry (Geometry) = info.geometry
- [**info**](#info) : [ObjectInfo](../nodes/ObjectInfo.md) Sockets      [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
- [**location**](#location) : [ObjectInfo](../nodes/ObjectInfo.md) location (Vector) = info.location
- [**rotation**](#rotation) : [ObjectInfo](../nodes/ObjectInfo.md) rotation (Vector) = info.rotation
- [**scale**](#scale) : [ObjectInfo](../nodes/ObjectInfo.md) scale (Vector) = info.scale



## Methods



- [**switch**](#switch) : [Switch](../nodes/Switch.md) output (Object)



## Methods reference


### geometry

> Node: [ObjectInfo](../nodes/{self.node_name}.md)


[Top](#class-object) [Index](/docs/index.md)

```python
v = object.geometry
```


#### Arguments


##### Sockets arguments



- object : Object (self)
- as_instance : Boolean



##### Parameters arguments



- transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]



##### Fixed parameters



- label:f"{self.node_chain_label}.geometry"



#### Node creation


```python
node = nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.geometry")
```


#### Returns

    Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]

### info

> Node: [ObjectInfo](../nodes/{self.node_name}.md)


[Top](#class-object) [Index](/docs/index.md)

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

### location

> Node: [ObjectInfo](../nodes/{self.node_name}.md)


[Top](#class-object) [Index](/docs/index.md)

```python
v = object.location
```


#### Arguments


##### Sockets arguments



- object : Object (self)
- as_instance : Boolean



##### Parameters arguments



- transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]



##### Fixed parameters



- label:f"{self.node_chain_label}.location"



#### Node creation


```python
node = nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.location")
```


#### Returns

    Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]

### rotation

> Node: [ObjectInfo](../nodes/{self.node_name}.md)


[Top](#class-object) [Index](/docs/index.md)

```python
v = object.rotation
```


#### Arguments


##### Sockets arguments



- object : Object (self)
- as_instance : Boolean



##### Parameters arguments



- transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]



##### Fixed parameters



- label:f"{self.node_chain_label}.rotation"



#### Node creation


```python
node = nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.rotation")
```


#### Returns

    Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]

### scale

> Node: [ObjectInfo](../nodes/{self.node_name}.md)


[Top](#class-object) [Index](/docs/index.md)

```python
v = object.scale
```


#### Arguments


##### Sockets arguments



- object : Object (self)
- as_instance : Boolean



##### Parameters arguments



- transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]



##### Fixed parameters



- label:f"{self.node_chain_label}.scale"



#### Node creation


```python
node = nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.scale")
```


#### Returns

    Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]

### switch

> Node: [Switch](../nodes/{self.node_name}.md)


[Top](#class-object) [Index](/docs/index.md)

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
