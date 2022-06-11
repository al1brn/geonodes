
# Data socket Object

> Inherits from dsock.Object
  
<sub>go to [index](/docs/index.md)</sub>



## Properties

- [geometry](#geometry) : geometry (Geometry) = info.geometry
- [info](#info) : Sockets      [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]
- [location](#location) : location (Vector) = info.location
- [rotation](#rotation) : rotation (Vector) = info.rotation
- [scale](#scale) : scale (Vector) = info.scale

## Methods

- [switch](#switch) : output (Object)

## info

> Node: [ObjectInfo](/docs/nodes/ObjectInfo.md)
  
<sub>go to: [top](#data-socket-object) [index](/docs/index.md)
blender ref [GeometryNodeObjectInfo](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)
node ref [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) </sub>

```python
v = object.info
```

### Arguments


#### Sockets

- object : Object (self)
- as_instance : Boolean

#### Parameters

- transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Fixed parameters

- label:f"{self.node_chain_label}.info"

### Node creation

```python
from geondes import nodes
nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.info")
```

### Returns

Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]


## location

> Node: [ObjectInfo](/docs/nodes/ObjectInfo.md)
  
<sub>go to: [top](#data-socket-object) [index](/docs/index.md)
blender ref [GeometryNodeObjectInfo](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)
node ref [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) </sub>

```python
v = object.location
```

### Arguments


#### Sockets

- object : Object (self)
- as_instance : Boolean

#### Parameters

- transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Fixed parameters

- label:f"{self.node_chain_label}.location"

### Node creation

```python
from geondes import nodes
nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.location")
```

### Returns

Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]


## rotation

> Node: [ObjectInfo](/docs/nodes/ObjectInfo.md)
  
<sub>go to: [top](#data-socket-object) [index](/docs/index.md)
blender ref [GeometryNodeObjectInfo](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)
node ref [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) </sub>

```python
v = object.rotation
```

### Arguments


#### Sockets

- object : Object (self)
- as_instance : Boolean

#### Parameters

- transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Fixed parameters

- label:f"{self.node_chain_label}.rotation"

### Node creation

```python
from geondes import nodes
nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.rotation")
```

### Returns

Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]


## scale

> Node: [ObjectInfo](/docs/nodes/ObjectInfo.md)
  
<sub>go to: [top](#data-socket-object) [index](/docs/index.md)
blender ref [GeometryNodeObjectInfo](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)
node ref [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) </sub>

```python
v = object.scale
```

### Arguments


#### Sockets

- object : Object (self)
- as_instance : Boolean

#### Parameters

- transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Fixed parameters

- label:f"{self.node_chain_label}.scale"

### Node creation

```python
from geondes import nodes
nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.scale")
```

### Returns

Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]


## geometry

> Node: [ObjectInfo](/docs/nodes/ObjectInfo.md)
  
<sub>go to: [top](#data-socket-object) [index](/docs/index.md)
blender ref [GeometryNodeObjectInfo](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)
node ref [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) </sub>

```python
v = object.geometry
```

### Arguments


#### Sockets

- object : Object (self)
- as_instance : Boolean

#### Parameters

- transform_space : 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Fixed parameters

- label:f"{self.node_chain_label}.geometry"

### Node creation

```python
from geondes import nodes
nodes.ObjectInfo(object=self, as_instance=as_instance, transform_space=transform_space, label=f"{self.node_chain_label}.geometry")
```

### Returns

Sockets [location (Vector), rotation (Vector), scale (Vector), geometry (Geometry)]


## switch

> Node: [Switch](/docs/nodes/Switch.md)
  
<sub>go to: [top](#data-socket-object) [index](/docs/index.md)
blender ref [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
node ref [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) </sub>

```python
v = object.switch(switch1, true)
```

### Arguments


#### Sockets

- false : Object (self)
- switch1 : Boolean
- true : Object

#### Fixed parameters

- input_type : 'OBJECT'

### Node creation

```python
from geondes import nodes
nodes.Switch(false=self, switch1=switch1, true=true, input_type='OBJECT')
```

### Returns

Object

