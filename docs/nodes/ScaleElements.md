
# Node ScaleElements

> Geometry node name: [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/scale_elements.html)<br>
  Blender type: [Scale Elements](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.ScaleElements(geometry=None, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM', label=None)
```



## Arguments


### Input sockets

geometry : Geometry
- selection : Boolean
- scale : Float
- center : Vector
- axis : Vector

### Parameters

domain : str (default = 'FACE') in ('FACE', 'EDGE')
- scale_mode : str (default = 'UNIFORM') in ('UNIFORM', 'SINGLE_AXIS')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

geometry : Geometry

## Data sockets

> Data socket classes implementing this node.
  
[Geometry](/docs/sockets/Geometry.md).[scale_elements](/docs/sockets/Geometry.md#scale_elements) : Method

