
# Data socket Geometry

> Inherits from dsock.Geometry
  
<sub>go to [index](/docs/index.md)</sub>



## Static methods

- [is_viewport](#is_viewport) : is_viewport (Boolean)

## Properties

- [bound_box](#bound_box) : Sockets      [bounding_box (Geometry), min (Vector), max (Vector)]
- [box](#box) : bounding_box (Geometry) = bound_box.bounding_box
- [box_max](#box_max) : max (Vector) = bound_box.max
- [box_min](#box_min) : min (Vector) = bound_box.min
- [components](#components) : Sockets      [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]
- [curve_component](#curve_component) : curve (Curve) = components.curve
- [instances_component](#instances_component) : instances (Instances) = components.instances
- [mesh_component](#mesh_component) : mesh (Mesh) = components.mesh
- [points_component](#points_component) : point_cloud (Geometry) = components.point_cloud
- [volume_component](#volume_component) : volume (Volume) = components.volume

## Attribute capture

- [capture_ID](#capture_id) : ID (Integer)
- [capture_index](#capture_index) : index (Integer)
- [capture_named_attribute](#capture_named_attribute) : attribute (data_type dependant)
- [capture_named_boolean](#capture_named_boolean) : attribute (Float)
- [capture_named_boolean](#capture_named_boolean) : attribute (Boolean)
- [capture_named_color](#capture_named_color) : attribute (Color)
- [capture_named_integer](#capture_named_integer) : attribute (Integer)
- [capture_named_vector](#capture_named_vector) : attribute (Vector)
- [capture_normal](#capture_normal) : normal (Vector)
- [capture_position](#capture_position) : position (Vector)
- [capture_radius](#capture_radius) : radius (Float)

## Attributes

- [ID](#id) : Integer = capture_ID(domain='POINT')
- [index](#index) : Integer = capture_index(domain='POINT')
- [normal](#normal) : Vector = capture_normal(domain='FACE')
- [position](#position) : Vector = capture_position(domain='POINT')
- [radius](#radius) : Float = capture_radius(domain='POINT')

## Methods

- [attribute_domain_size](#attribute_domain_size) : Sockets      [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer), spline_count (Integer), instance_count (Integer)]
- [capture_attribute](#capture_attribute) : attribute (data_type dependant)
- [components](#components) : Sockets      [selection (Geometry), inverted (Geometry)]
- [convex_hull](#convex_hull) : convex_hull (Geometry)
- [delete_geometry](#delete_geometry) : geometry (Geometry)
- [duplicate_elements](#duplicate_elements) : Sockets      [geometry (Geometry), duplicate_index (Integer)]
- [duplicate_points](#duplicate_points) : Sockets      [geometry (Geometry), duplicate_index (Integer)]
- [join](#join) : geometry (Geometry)
- [merge_by_distance](#merge_by_distance) : geometry (Geometry)
- [proximity](#proximity) : Sockets      [position (Vector), distance (Float)]
- [remove_named_attribute](#remove_named_attribute) : geometry (Geometry)
- [replace_material](#replace_material) : geometry (Geometry)
- [scale_elements](#scale_elements) : geometry (Geometry)
- [set_ID](#set_id) : geometry (Geometry)
- [set_material](#set_material) : geometry (Geometry)
- [set_material_index](#set_material_index) : geometry (Geometry)
- [set_position](#set_position) : geometry (Geometry)
- [set_shade_smooth](#set_shade_smooth) : geometry (Geometry)
- [store_named_attribute](#store_named_attribute) : geometry (Geometry)
- [store_named_boolean](#store_named_boolean) : geometry (Geometry)
- [store_named_byte_color](#store_named_byte_color) : geometry (Geometry)
- [store_named_color](#store_named_color) : geometry (Geometry)
- [store_named_float](#store_named_float) : geometry (Geometry)
- [store_named_integer](#store_named_integer) : geometry (Geometry)
- [store_named_vector](#store_named_vector) : geometry (Geometry)
- [switch](#switch) : output (Geometry)
- [to_instance](#to_instance) : instances (Instances)
- [transfer_boolean](#transfer_boolean) : attribute (Boolean)
- [transfer_color](#transfer_color) : attribute (Color)
- [transfer_float](#transfer_float) : attribute (Float)
- [transfer_integer](#transfer_integer) : attribute (Integer)
- [transfer_vector](#transfer_vector) : attribute (Vector)
- [transform](#transform) : geometry (Geometry)

## is_viewport

> Node: [IsViewport](/docs/nodes/IsViewport.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeIsViewport](https://docs.blender.org/api/current/bpy.types.GeometryNodeIsViewport.html)
node ref [Is Viewport](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/is_viewport.html) </sub>
                          
```python
v = Geometry.is_viewport(node_label = None, node_color = None)
```

### Arguments

## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.IsViewport(label=node_label, node_color=node_color)
```

### Returns

Boolean


## bound_box

> Node: [BoundingBox](/docs/nodes/BoundingBox.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeBoundBox](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)
node ref [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) </sub>
                          
```python
v = geometry.bound_box
```

### Arguments

## Sockets
- geometry : Geometry (self)## Fixed parameters
- label:f"{self.node_chain_label}.bound_box"

### Node creation

```python
from geondes import nodes
nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.bound_box")
```

### Returns

Sockets [bounding_box (Geometry), min (Vector), max (Vector)]


## box

> Node: [BoundingBox](/docs/nodes/BoundingBox.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeBoundBox](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)
node ref [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) </sub>
                          
```python
v = geometry.box
```

### Arguments

## Sockets
- geometry : Geometry (self)## Fixed parameters
- label:f"{self.node_chain_label}.box"

### Node creation

```python
from geondes import nodes
nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.box")
```

### Returns

Sockets [bounding_box (Geometry), min (Vector), max (Vector)]


## box_min

> Node: [BoundingBox](/docs/nodes/BoundingBox.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeBoundBox](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)
node ref [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) </sub>
                          
```python
v = geometry.box_min
```

### Arguments

## Sockets
- geometry : Geometry (self)## Fixed parameters
- label:f"{self.node_chain_label}.box_min"

### Node creation

```python
from geondes import nodes
nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.box_min")
```

### Returns

Sockets [bounding_box (Geometry), min (Vector), max (Vector)]


## box_max

> Node: [BoundingBox](/docs/nodes/BoundingBox.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeBoundBox](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)
node ref [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) </sub>
                          
```python
v = geometry.box_max
```

### Arguments

## Sockets
- geometry : Geometry (self)## Fixed parameters
- label:f"{self.node_chain_label}.box_max"

### Node creation

```python
from geondes import nodes
nodes.BoundingBox(geometry=self, label=f"{self.node_chain_label}.box_max")
```

### Returns

Sockets [bounding_box (Geometry), min (Vector), max (Vector)]


## components

> Node: [SeparateComponents](/docs/nodes/SeparateComponents.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeSeparateComponents](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)
node ref [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) </sub>
                          
```python
v = geometry.components
```

### Arguments

## Sockets
- geometry : Geometry (self)## Fixed parameters
- label:f"{self.node_chain_label}.components"

### Node creation

```python
from geondes import nodes
nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.components")
```

### Returns

Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]


## mesh_component

> Node: [SeparateComponents](/docs/nodes/SeparateComponents.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeSeparateComponents](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)
node ref [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) </sub>
                          
```python
v = geometry.mesh_component
```

### Arguments

## Sockets
- geometry : Geometry (self)## Fixed parameters
- label:f"{self.node_chain_label}.mesh_component"

### Node creation

```python
from geondes import nodes
nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.mesh_component")
```

### Returns

Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]


## points_component

> Node: [SeparateComponents](/docs/nodes/SeparateComponents.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeSeparateComponents](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)
node ref [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) </sub>
                          
```python
v = geometry.points_component
```

### Arguments

## Sockets
- geometry : Geometry (self)## Fixed parameters
- label:f"{self.node_chain_label}.points_component"

### Node creation

```python
from geondes import nodes
nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.points_component")
```

### Returns

Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]


## curve_component

> Node: [SeparateComponents](/docs/nodes/SeparateComponents.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeSeparateComponents](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)
node ref [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) </sub>
                          
```python
v = geometry.curve_component
```

### Arguments

## Sockets
- geometry : Geometry (self)## Fixed parameters
- label:f"{self.node_chain_label}.curve_component"

### Node creation

```python
from geondes import nodes
nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.curve_component")
```

### Returns

Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]


## volume_component

> Node: [SeparateComponents](/docs/nodes/SeparateComponents.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeSeparateComponents](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)
node ref [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) </sub>
                          
```python
v = geometry.volume_component
```

### Arguments

## Sockets
- geometry : Geometry (self)## Fixed parameters
- label:f"{self.node_chain_label}.volume_component"

### Node creation

```python
from geondes import nodes
nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.volume_component")
```

### Returns

Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]


## instances_component

> Node: [SeparateComponents](/docs/nodes/SeparateComponents.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeSeparateComponents](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)
node ref [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) </sub>
                          
```python
v = geometry.instances_component
```

### Arguments

## Sockets
- geometry : Geometry (self)## Fixed parameters
- label:f"{self.node_chain_label}.instances_component"

### Node creation

```python
from geondes import nodes
nodes.SeparateComponents(geometry=self, label=f"{self.node_chain_label}.instances_component")
```

### Returns

Sockets [mesh (Mesh), point_cloud (Geometry), curve (Curve), volume (Volume), instances (Instances)]


## capture_ID

> Node: [ID](/docs/nodes/ID.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeInputID](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)
node ref [ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html) </sub>
                          
```python
v = geometry.capture_ID(self, domain='POINT', node_label = None, node_color = None)
```

### Arguments

## Parameters
- self
- domain:'POINT'
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.ID(label=node_label, node_color=node_color)
```

### Returns

Integer


## capture_index

> Node: [Index](/docs/nodes/Index.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeInputIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)
node ref [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) </sub>
                          
```python
v = geometry.capture_index(self, domain='POINT', node_label = None, node_color = None)
```

### Arguments

## Parameters
- self
- domain:'POINT'
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.Index(label=node_label, node_color=node_color)
```

### Returns

Integer


## capture_normal

> Node: [Normal](/docs/nodes/Normal.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeInputNormal](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)
node ref [Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html) </sub>
                          
```python
v = geometry.capture_normal(self, domain='FACE', node_label = None, node_color = None)
```

### Arguments

## Parameters
- self
- domain:'FACE'
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.Normal(label=node_label, node_color=node_color)
```

### Returns

Vector


## capture_position

> Node: [Position](/docs/nodes/Position.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeInputPosition](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)
node ref [Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html) </sub>
                          
```python
v = geometry.capture_position(self, domain='POINT', node_label = None, node_color = None)
```

### Arguments

## Parameters
- self
- domain:'POINT'
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.Position(label=node_label, node_color=node_color)
```

### Returns

Vector


## capture_radius

> Node: [Radius](/docs/nodes/Radius.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeInputRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)
node ref [Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html) </sub>
                          
```python
v = geometry.capture_radius(self, domain='POINT', node_label = None, node_color = None)
```

### Arguments

## Parameters
- self
- domain:'POINT'
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.Radius(label=node_label, node_color=node_color)
```

### Returns

Float


## capture_named_attribute

> Node: [NamedAttribute](/docs/nodes/NamedAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)
node ref [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) </sub>
                          
```python
v = geometry.capture_named_attribute(self, name, data_type, domain='POINT', node_label = None, node_color = None)
```

### Arguments

## Sockets
- name : String## Parameters
- self
- data_type : 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
- domain:'POINT'
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.NamedAttribute(name=name, data_type=data_type, label=node_label, node_color=node_color)
```

### Returns

data_type dependant


## capture_named_boolean

> Node: [NamedAttribute](/docs/nodes/NamedAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)
node ref [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) </sub>
                          
```python
v = geometry.capture_named_boolean(self, name, domain='POINT', node_label = None, node_color = None)
```

### Arguments

## Sockets
- name : String## Parameters
- self
- domain:'POINT'
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT'

### Node creation

```python
from geondes import nodes
nodes.NamedAttribute(name=name, data_type='FLOAT', label=node_label, node_color=node_color)
```

### Returns

Float


## capture_named_integer

> Node: [NamedAttribute](/docs/nodes/NamedAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)
node ref [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) </sub>
                          
```python
v = geometry.capture_named_integer(self, name, domain='POINT', node_label = None, node_color = None)
```

### Arguments

## Sockets
- name : String## Parameters
- self
- domain:'POINT'
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'INT'

### Node creation

```python
from geondes import nodes
nodes.NamedAttribute(name=name, data_type='INT', label=node_label, node_color=node_color)
```

### Returns

Integer


## capture_named_vector

> Node: [NamedAttribute](/docs/nodes/NamedAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)
node ref [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) </sub>
                          
```python
v = geometry.capture_named_vector(self, name, domain='POINT', node_label = None, node_color = None)
```

### Arguments

## Sockets
- name : String## Parameters
- self
- domain:'POINT'
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT_VECTOR'

### Node creation

```python
from geondes import nodes
nodes.NamedAttribute(name=name, data_type='FLOAT_VECTOR', label=node_label, node_color=node_color)
```

### Returns

Vector


## capture_named_color

> Node: [NamedAttribute](/docs/nodes/NamedAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)
node ref [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) </sub>
                          
```python
v = geometry.capture_named_color(self, name, domain='POINT', node_label = None, node_color = None)
```

### Arguments

## Sockets
- name : String## Parameters
- self
- domain:'POINT'
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT_COLOR'

### Node creation

```python
from geondes import nodes
nodes.NamedAttribute(name=name, data_type='FLOAT_COLOR', label=node_label, node_color=node_color)
```

### Returns

Color


## capture_named_boolean

> Node: [NamedAttribute](/docs/nodes/NamedAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)
node ref [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) </sub>
                          
```python
v = geometry.capture_named_boolean(self, name, domain='POINT', node_label = None, node_color = None)
```

### Arguments

## Sockets
- name : String## Parameters
- self
- domain:'POINT'
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'BOOLEAN'

### Node creation

```python
from geondes import nodes
nodes.NamedAttribute(name=name, data_type='BOOLEAN', label=node_label, node_color=node_color)
```

### Returns

Boolean


## ID

> Node: [ID](/docs/nodes/ID.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeInputID](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)
node ref [ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html) </sub>
                          
```python
v = geometry.ID(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.ID()
```

### Returns

Integer


## index

> Node: [Index](/docs/nodes/Index.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeInputIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)
node ref [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) </sub>
                          
```python
v = geometry.index(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.Index()
```

### Returns

Integer


## normal

> Node: [Normal](/docs/nodes/Normal.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeInputNormal](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)
node ref [Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html) </sub>
                          
```python
v = geometry.normal(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.Normal()
```

### Returns

Vector


## position

> Node: [Position](/docs/nodes/Position.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeInputPosition](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)
node ref [Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html) </sub>
                          
```python
v = geometry.position(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.Position()
```

### Returns

Vector


## radius

> Node: [Radius](/docs/nodes/Radius.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeInputRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)
node ref [Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html) </sub>
                          
```python
v = geometry.radius(self)
```

### Arguments

## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.Radius()
```

### Returns

Float


## switch

> Node: [Switch](/docs/nodes/Switch.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
node ref [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) </sub>
                          
```python
v = geometry.switch(switch1, true, node_label = None, node_color = None)
```

### Arguments

## Sockets
- false : Geometry (self)
- switch1 : Boolean
- true : Geometry## Parameters
- node_label : None
- node_color : None## Fixed parameters
- input_type : 'GEOMETRY'

### Node creation

```python
from geondes import nodes
nodes.Switch(false=self, switch1=switch1, true=true, input_type='GEOMETRY', label=node_label, node_color=node_color)
```

### Returns

Geometry


## capture_attribute

> Node: [CaptureAttribute](/docs/nodes/CaptureAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeCaptureAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
node ref [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) </sub>
                          
```python
v = geometry.capture_attribute(value, data_type, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- value : Float## Parameters
- data_type : 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.CaptureAttribute(geometry=self, value=value, data_type=data_type, domain=domain, label=node_label, node_color=node_color)
```

### Returns

Sockets [geometry (Geometry), attribute (data_type dependant)]


## transfer_boolean

> Node: [TransferAttribute](/docs/nodes/TransferAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeAttributeTransfer](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeTransfer.html)
node ref [Transfer Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/transfer_attribute.html) </sub>
                          
```python
v = geometry.transfer_boolean(attribute, source_position, index, domain, mapping, node_label = None, node_color = None)
```

### Arguments

## Sockets
- source : Geometry (self)
- attribute : Boolean
- source_position : Vector
- index : Integer## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'BOOLEAN'

### Node creation

```python
from geondes import nodes
nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
```

### Returns

Boolean


## transfer_integer

> Node: [TransferAttribute](/docs/nodes/TransferAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeAttributeTransfer](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeTransfer.html)
node ref [Transfer Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/transfer_attribute.html) </sub>
                          
```python
v = geometry.transfer_integer(attribute, source_position, index, domain, mapping, node_label = None, node_color = None)
```

### Arguments

## Sockets
- source : Geometry (self)
- attribute : Integer
- source_position : Vector
- index : Integer## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'INT'

### Node creation

```python
from geondes import nodes
nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='INT', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
```

### Returns

Integer


## transfer_float

> Node: [TransferAttribute](/docs/nodes/TransferAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeAttributeTransfer](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeTransfer.html)
node ref [Transfer Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/transfer_attribute.html) </sub>
                          
```python
v = geometry.transfer_float(attribute, source_position, index, domain, mapping, node_label = None, node_color = None)
```

### Arguments

## Sockets
- source : Geometry (self)
- attribute : Float
- source_position : Vector
- index : Integer## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT'

### Node creation

```python
from geondes import nodes
nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
```

### Returns

Float


## transfer_vector

> Node: [TransferAttribute](/docs/nodes/TransferAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeAttributeTransfer](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeTransfer.html)
node ref [Transfer Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/transfer_attribute.html) </sub>
                          
```python
v = geometry.transfer_vector(attribute, source_position, index, domain, mapping, node_label = None, node_color = None)
```

### Arguments

## Sockets
- source : Geometry (self)
- attribute : Vector
- source_position : Vector
- index : Integer## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT_VECTOR'

### Node creation

```python
from geondes import nodes
nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_VECTOR', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
```

### Returns

Vector


## transfer_color

> Node: [TransferAttribute](/docs/nodes/TransferAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeAttributeTransfer](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeTransfer.html)
node ref [Transfer Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/transfer_attribute.html) </sub>
                          
```python
v = geometry.transfer_color(attribute, source_position, index, domain, mapping, node_label = None, node_color = None)
```

### Arguments

## Sockets
- source : Geometry (self)
- attribute : Color
- source_position : Vector
- index : Integer## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT_COLOR'

### Node creation

```python
from geondes import nodes
nodes.TransferAttribute(source=self, attribute=attribute, source_position=source_position, index=index, data_type='FLOAT_COLOR', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
```

### Returns

Color


## duplicate_elements

> Node: [DuplicateElements](/docs/nodes/DuplicateElements.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeDuplicateElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)
node ref [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) </sub>
                          
```python
v = geometry.duplicate_elements(selection, amount, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- selection : Boolean
- amount : Integer## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, SPLINE, INSTANCE]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain=domain, label=node_label, node_color=node_color)
```

### Returns

Sockets [geometry (Geometry), duplicate_index (Integer)]


## duplicate_points

> Node: [DuplicateElements](/docs/nodes/DuplicateElements.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeDuplicateElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)
node ref [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) </sub>
                          
```python
v = geometry.duplicate_points(selection, amount, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- selection : Boolean
- amount : Integer## Parameters
- node_label : None
- node_color : None## Fixed parameters
- domain : 'POINT'

### Node creation

```python
from geondes import nodes
nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='POINT', label=node_label, node_color=node_color)
```

### Returns

Sockets [geometry (Geometry), duplicate_index (Integer)]


## delete_geometry

> Node: [DeleteGeometry](/docs/nodes/DeleteGeometry.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)
node ref [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) </sub>
                          
```python
v = geometry.delete_geometry(selection, domain, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- selection : Boolean## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
- mode : 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode=mode, label=node_label, node_color=node_color)
```

### Returns

Geometry


## merge_by_distance

> Node: [MergeByDistance](/docs/nodes/MergeByDistance.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeMergeByDistance](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)
node ref [Merge by Distance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html) </sub>
                          
```python
v = geometry.merge_by_distance(selection, distance, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- selection : Boolean
- distance : Float## Parameters
- mode : 'ALL' in [ALL, CONNECTED]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.MergeByDistance(geometry=self, selection=selection, distance=distance, mode=mode, label=node_label, node_color=node_color)
```

### Returns

Geometry


## replace_material

> Node: [ReplaceMaterial](/docs/nodes/ReplaceMaterial.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeReplaceMaterial](https://docs.blender.org/api/current/bpy.types.GeometryNodeReplaceMaterial.html)
node ref [Replace Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html) </sub>
                          
```python
v = geometry.replace_material(old, new, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- old : Material
- new : Material## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.ReplaceMaterial(geometry=self, old=old, new=new, label=node_label, node_color=node_color)
```

### Returns

Geometry


## scale_elements

> Node: [ScaleElements](/docs/nodes/ScaleElements.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeScaleElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)
node ref [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) </sub>
                          
```python
v = geometry.scale_elements(selection, scale, center, axis, domain, scale_mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- selection : Boolean
- scale : Float
- center : Vector
- axis : Vector## Parameters
- domain : 'FACE' in [FACE, EDGE]
- scale_mode : 'UNIFORM' in [UNIFORM, SINGLE_AXIS]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.ScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=axis, domain=domain, scale_mode=scale_mode, label=node_label, node_color=node_color)
```

### Returns

Geometry


## set_ID

> Node: [SetID](/docs/nodes/SetID.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeSetID](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)
node ref [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) </sub>
                          
```python
v = geometry.set_ID(selection, ID, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- selection : Boolean
- ID : Integer## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.SetID(geometry=self, selection=selection, ID=ID, label=node_label, node_color=node_color)
```

### Returns

Geometry


## set_material

> Node: [SetMaterial](/docs/nodes/SetMaterial.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeSetMaterial](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)
node ref [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) </sub>
                          
```python
v = geometry.set_material(selection, material, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- selection : Boolean
- material : Material## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.SetMaterial(geometry=self, selection=selection, material=material, label=node_label, node_color=node_color)
```

### Returns

Geometry


## set_material_index

> Node: [SetMaterialIndex](/docs/nodes/SetMaterialIndex.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeSetMaterialIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)
node ref [Set Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html) </sub>
                          
```python
v = geometry.set_material_index(selection, material_index, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- selection : Boolean
- material_index : Integer## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.SetMaterialIndex(geometry=self, selection=selection, material_index=material_index, label=node_label, node_color=node_color)
```

### Returns

Geometry


## set_position

> Node: [SetPosition](/docs/nodes/SetPosition.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeSetPosition](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)
node ref [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) </sub>
                          
```python
v = geometry.set_position(selection, position, offset, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- selection : Boolean
- position : Vector
- offset : Vector## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.SetPosition(geometry=self, selection=selection, position=position, offset=offset, label=node_label, node_color=node_color)
```

### Returns

Geometry


## set_shade_smooth

> Node: [SetShadeSmooth](/docs/nodes/SetShadeSmooth.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeSetShadeSmooth](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html)
node ref [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html) </sub>
                          
```python
v = geometry.set_shade_smooth(selection, shade_smooth, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- selection : Boolean
- shade_smooth : Boolean## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.SetShadeSmooth(geometry=self, selection=selection, shade_smooth=shade_smooth, label=node_label, node_color=node_color)
```

### Returns

Geometry


## transform

> Node: [Transform](/docs/nodes/Transform.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeTransform](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html)
node ref [Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/transform.html) </sub>
                          
```python
v = geometry.transform(translation, rotation, scale, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- translation : Vector
- rotation : Vector
- scale : Vector## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.Transform(geometry=self, translation=translation, rotation=rotation, scale=scale, label=node_label, node_color=node_color)
```

### Returns

Geometry


## store_named_attribute

> Node: [StoreNamedAttribute](/docs/nodes/StoreNamedAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)
node ref [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) </sub>
                          
```python
v = geometry.store_named_attribute(name, value, data_type, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- name : String
- value : Float## Parameters
- data_type : 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BYTE_COLOR, BOOLEAN]
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type=data_type, domain=domain, label=node_label, node_color=node_color)
```

### Returns

Geometry


## store_named_float

> Node: [StoreNamedAttribute](/docs/nodes/StoreNamedAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)
node ref [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) </sub>
                          
```python
v = geometry.store_named_float(name, value, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- name : String
- value : Float## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT'

### Node creation

```python
from geondes import nodes
nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT', domain=domain, label=node_label, node_color=node_color)
```

### Returns

Geometry


## store_named_integer

> Node: [StoreNamedAttribute](/docs/nodes/StoreNamedAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)
node ref [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) </sub>
                          
```python
v = geometry.store_named_integer(name, value, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- name : String
- value : Integer## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'INT'

### Node creation

```python
from geondes import nodes
nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='INT', domain=domain, label=node_label, node_color=node_color)
```

### Returns

Geometry


## store_named_vector

> Node: [StoreNamedAttribute](/docs/nodes/StoreNamedAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)
node ref [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) </sub>
                          
```python
v = geometry.store_named_vector(name, value, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- name : String
- value : Vector## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT_VECTOR'

### Node creation

```python
from geondes import nodes
nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)
```

### Returns

Geometry


## store_named_color

> Node: [StoreNamedAttribute](/docs/nodes/StoreNamedAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)
node ref [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) </sub>
                          
```python
v = geometry.store_named_color(name, value, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- name : String
- value : Color## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT_COLOR'

### Node creation

```python
from geondes import nodes
nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT_COLOR', domain=domain, label=node_label, node_color=node_color)
```

### Returns

Geometry


## store_named_byte_color

> Node: [StoreNamedAttribute](/docs/nodes/StoreNamedAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)
node ref [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) </sub>
                          
```python
v = geometry.store_named_byte_color(name, value, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- name : String
- value : Color## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'BYTE_COLOR'

### Node creation

```python
from geondes import nodes
nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='BYTE_COLOR', domain=domain, label=node_label, node_color=node_color)
```

### Returns

Geometry


## store_named_boolean

> Node: [StoreNamedAttribute](/docs/nodes/StoreNamedAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)
node ref [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) </sub>
                          
```python
v = geometry.store_named_boolean(name, value, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- name : String
- value : Boolean## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'BOOLEAN'

### Node creation

```python
from geondes import nodes
nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='BOOLEAN', domain=domain, label=node_label, node_color=node_color)
```

### Returns

Geometry


## attribute_domain_size

> Node: [DomainSize](/docs/nodes/DomainSize.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeAttributeDomainSize](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)
node ref [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) </sub>
                          
```python
v = geometry.attribute_domain_size(component, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)## Parameters
- component : 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.DomainSize(geometry=self, component=component, label=node_label, node_color=node_color)
```

### Returns

Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer), spline_count (Integer), instance_count (Integer)]


## remove_named_attribute

> Node: [RemoveNamedAttribute](/docs/nodes/RemoveNamedAttribute.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeRemoveAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)
node ref [Remove Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html) </sub>
                          
```python
v = geometry.remove_named_attribute(name, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- name : String## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.RemoveNamedAttribute(geometry=self, name=name, label=node_label, node_color=node_color)
```

### Returns

Geometry


## components

> Node: [SeparateGeometry](/docs/nodes/SeparateGeometry.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeSeparateGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
node ref [Separate Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) </sub>
                          
```python
v = geometry.components(selection, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- selection : Boolean## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.SeparateGeometry(geometry=self, selection=selection, domain=domain, label=node_label, node_color=node_color)
```

### Returns

Sockets [selection (Geometry), inverted (Geometry)]


## convex_hull

> Node: [ConvexHull](/docs/nodes/ConvexHull.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeConvexHull](https://docs.blender.org/api/current/bpy.types.GeometryNodeConvexHull.html)
node ref [Convex Hull](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/convex_hull.html) </sub>
                          
```python
v = geometry.convex_hull(node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.ConvexHull(geometry=self, label=node_label, node_color=node_color)
```

### Returns

Geometry


## to_instance

> Node: [GeometryToInstance](/docs/nodes/GeometryToInstance.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeGeometryToInstance](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)
node ref [Geometry to Instance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html) </sub>
                          
```python
v = geometry.to_instance(geometry_1, geometry_2, geometry_3, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : *Geometry (self)## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.GeometryToInstance(self, *geometry, label=node_label, node_color=node_color)
```

### Returns

Instances


## join

> Node: [JoinGeometry](/docs/nodes/JoinGeometry.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeJoinGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)
node ref [Join Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html) </sub>
                          
```python
v = geometry.join(geometry_1, geometry_2, geometry_3, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : *Geometry (self)## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.JoinGeometry(self, *geometry, label=node_label, node_color=node_color)
```

### Returns

Geometry


## proximity

> Node: [GeometryProximity](/docs/nodes/GeometryProximity.md)
  
<sub>go to: [top](#data-socket-geometry) [index](/docs/index.md)
blender ref [GeometryNodeProximity](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)
node ref [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) </sub>
                          
```python
v = geometry.proximity(source_position, target_element, node_label = None, node_color = None)
```

### Arguments

## Sockets
- target : Geometry (self)
- source_position : Vector## Parameters
- target_element : 'FACES' in [POINTS, EDGES, FACES]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.GeometryProximity(target=self, source_position=source_position, target_element=target_element, label=node_label, node_color=node_color)
```

### Returns

Sockets [position (Vector), distance (Float)]

