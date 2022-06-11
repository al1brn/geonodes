
# Data socket Collection

> Inherits from dsock.Collection
  
<sub>go to [index](/docs/index.md)</sub>



## Methods

- [info](#info) : [CollectionInfo](/docs/nodes/CollectionInfo.md), geometry (Geometry)
- [switch](#switch) : [Switch](/docs/nodes/Switch.md), output (Collection)

## switch

> Node: [Switch](/docs/nodes/Switch.md)
  
<sub>go to: [top](#data-socket-collection) [index](/docs/index.md)
blender ref [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
node ref [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/switch.html) </sub>

```python
v = collection.switch(switch1, true)
```

### Arguments


#### Sockets

- false : Collection (self)
- switch1 : Boolean
- true : Collection

#### Fixed parameters

- input_type : 'COLLECTION'

### Node creation

```python
nodes.Switch(false=self, switch1=switch1, true=true, input_type='COLLECTION')
```

### Returns

Collection


## info

> Node: [CollectionInfo](/docs/nodes/CollectionInfo.md)
  
<sub>go to: [top](#data-socket-collection) [index](/docs/index.md)
blender ref [GeometryNodeCollectionInfo](https://docs.blender.org/api/current/bpy.types.GeometryNodeCollectionInfo.html)
node ref [Collection Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/collection_info.html) </sub>

```python
v = collection.info(separate_children, reset_children, transform_space)
```

### Arguments


#### Sockets

- collection : Collection (self)
- separate_children : Boolean
- reset_children : Boolean

#### Parameters

- transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]

### Node creation

```python
nodes.CollectionInfo(collection=self, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space)
```

### Returns

Geometry

