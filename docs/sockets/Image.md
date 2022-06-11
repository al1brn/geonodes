
# Data socket Image

> Inherits from dsock.Image
  
<sub>go to [index](TBD)</sub>



## Methods

- [switch](#switch) : [Switch](section:nodes/Switch.md), output (Image)

## switch

> Node: [Switch](section:nodes/Switch)
<sub>go to: [top](#image) [index](TBD)
blender ref [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
node ref [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/switch.html) </sub>

```python
v = image.switch(switch1, true)
```

### Arguments


#### Sockets

- false : Image (self)
- switch1 : Boolean
- true : Image

#### Fixed parameters

- input_type : 'IMAGE'

### Node creation

```python
nodes.Switch(false=self, switch1=switch1, true=true, input_type='IMAGE')
```

### Returns

Image

