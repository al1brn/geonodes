
# Data socket Image

> Inherits from dsock.Image
  
<sub>go to [index](/docs/index.md)</sub>



## Methods

- [switch](#switch) : output (Image)

## switch

> Node: [Switch](/docs/nodes/Switch.md)
  
<sub>go to: [top](#data-socket-image) [index](/docs/index.md)
blender ref [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
node ref [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) </sub>
                          
```python
v = image.switch(switch1, true, node_label = None, node_color = None)
```

### Arguments

## Sockets
- false : Image (self)
- switch1 : Boolean
- true : Image## Parameters
- node_label : None
- node_color : None## Fixed parameters
- input_type : 'IMAGE'

### Node creation

```python
from geondes import nodes
nodes.Switch(false=self, switch1=switch1, true=true, input_type='IMAGE', label=node_label, node_color=node_color)
```

### Returns

Image

