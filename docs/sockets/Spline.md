
# Data socket Spline

> Inherits from gn.Geometry
  
<sub>go to [index](/docs/index.md)</sub>



## Methods

- [duplicate_splines](#duplicate_splines) : Sockets      [geometry (Geometry), duplicate_index (Integer)]
- [set_cyclic](#set_cyclic) : geometry (Geometry)
- [set_resolution](#set_resolution) : geometry (Geometry)

## set_cyclic

> Node: [SetSplineCyclic](/docs/nodes/SetSplineCyclic.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeSetSplineCyclic](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html)
node ref [Set Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_cyclic.html) </sub>
                          
```python
v = spline.set_cyclic(selection, cyclic, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- selection : Boolean
- cyclic : Boolean## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.SetSplineCyclic(geometry=self, selection=selection, cyclic=cyclic, label=node_label, node_color=node_color)
```

### Returns

Geometry


## set_resolution

> Node: [SetSplineResolution](/docs/nodes/SetSplineResolution.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeSetSplineResolution](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html)
node ref [Set Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_resolution.html) </sub>
                          
```python
v = spline.set_resolution(selection, resolution, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- selection : Boolean
- resolution : Integer## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.SetSplineResolution(geometry=self, selection=selection, resolution=resolution, label=node_label, node_color=node_color)
```

### Returns

Geometry


## duplicate_splines

> Node: [DuplicateElements](/docs/nodes/DuplicateElements.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeDuplicateElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)
node ref [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) </sub>
                          
```python
v = spline.duplicate_splines(selection, amount, node_label = None, node_color = None)
```

### Arguments

## Sockets
- geometry : Geometry (self)
- selection : Boolean
- amount : Integer## Parameters
- node_label : None
- node_color : None## Fixed parameters
- domain : 'SPLINE'

### Node creation

```python
from geondes import nodes
nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='SPLINE', label=node_label, node_color=node_color)
```

### Returns

Sockets [geometry (Geometry), duplicate_index (Integer)]

