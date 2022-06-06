
# Class Image

> Inherits from: ***dsock.Image***


[Index](/docs/index.md)

## Methods



- [**switch**](#switch) : [Switch](../nodes/Switch.md) output (Image)



## Methods reference


### switch

> Node: [Switch](../nodes/{self.node_name}.md)


[Top](#image) [Index](/docs/index.md)

```python
v = image.switch(switch1, true)
```


#### Arguments


##### Sockets arguments



- false : Image (self)
- switch1 : Boolean
- true : Image



##### Fixed parameters



- input_type : 'IMAGE'



#### Node creation


```python
node = nodes.Switch(false=self, switch1=switch1, true=true, input_type='IMAGE')
```


#### Returns

    Image
