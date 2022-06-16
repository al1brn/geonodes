
# Data socket Collection

> Inherits from dsock.Collection
  
<sub>go to [index](/docs/index.md)</sub>



## Methods

- [info](#info) : geometry (Geometry)
- [switch](#switch) : output (Collection)

## switch

> Node: [Switch](/docs/nodes/Switch.md)
  
<sub>go to: [top](#data-socket-collection) [index](/docs/index.md)
blender ref [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
node ref [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) </sub>
                          
```python
v = collection.switch(switch, true, node_label = None, node_color = None)
```

### Arguments

## Sockets
- false : Collection (self)
- switch : Boolean
- true : Collection## Parameters
- node_label : None
- node_color : None## Fixed parameters
- input_type : 'COLLECTION'

### Node creation

```python
from geondes import nodes
nodes.Switch(false=self, switch=switch, true=true, input_type='COLLECTION', label=node_label, node_color=node_color)
```

### Returns

Collection


## info

> Node: [CollectionInfo](/docs/nodes/CollectionInfo.md)
  
<sub>go to: [top](#data-socket-collection) [index](/docs/index.md)
blender ref [GeometryNodeCollectionInfo](https://docs.blender.org/api/current/bpy.types.GeometryNodeCollectionInfo.html)
node ref [Collection Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/collection_info.html) </sub>
                          
```python
v = collection.info(separate_children, reset_children, transform_space, node_label = None, node_color = None)
```

### Arguments

## Sockets
- collection : Collection (self)
- separate_children : Boolean
- reset_children : Boolean## Parameters
- transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.CollectionInfo(collection=self, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space, label=node_label, node_color=node_color)
```

### Returns

Geometry

