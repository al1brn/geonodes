
# Node ScaleElements

> Geometry node name: [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html)<br>
  Blender type: [Scale Elements](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.ScaleElements(geometry=None, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM', label=None, node_color=None)
```



## Arguments


### Input sockets

- geometry : Geometry
- selection : Boolean
- scale : Float
- center : Vector
- axis : Vector

### Parameters

- domain : str (default = 'FACE') in ('FACE', 'EDGE')
- scale_mode : str (default = 'UNIFORM') in ('UNIFORM', 'SINGLE_AXIS')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- geometry : Geometry
