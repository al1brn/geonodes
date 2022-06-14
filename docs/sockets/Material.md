
# Data socket Material

> Inherits from dsock.Material
  
<sub>go to [index](/docs/index.md)</sub>



## Methods

- [selection](#selection) : selection (Boolean)
- [switch](#switch) : output (Material)

## switch

> Node: [Switch](/docs/nodes/Switch.md)
  
<sub>go to: [top](#data-socket-material) [index](/docs/index.md)
blender ref [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
node ref [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) </sub>
                          
```python
v = material.switch(switch1, true, node_label = None, node_color = None)
```

### Arguments

## Sockets
- false : Material (self)
- switch1 : Boolean
- true : Material## Parameters
- node_label : None
- node_color : None## Fixed parameters
- input_type : 'MATERIAL'

### Node creation

```python
from geondes import nodes
nodes.Switch(false=self, switch1=switch1, true=true, input_type='MATERIAL', label=node_label, node_color=node_color)
```

### Returns

Material


## selection

> Node: [MaterialSelection](/docs/nodes/MaterialSelection.md)
  
<sub>go to: [top](#data-socket-material) [index](/docs/index.md)
blender ref [GeometryNodeMaterialSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)
node ref [Material Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html) </sub>
                          
```python
v = material.selection(node_label = None, node_color = None)
```

### Arguments

## Sockets
- material : Material (self)## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.MaterialSelection(material=self, label=node_label, node_color=node_color)
```

### Returns

Boolean

