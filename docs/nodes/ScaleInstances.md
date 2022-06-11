
# Node ScaleInstances

> Geometry node name: [Scale Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/scale_instances.html)<br>
  Blender type: [Scale Instances](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleInstances.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.ScaleInstances(instances=None, selection=None, scale=None, center=None, local_space=None, label=None)
```



## Arguments


### Input sockets

- instances : Instances
- selection : Boolean
- scale : Vector
- center : Vector
- local_space : Boolean

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- instances : Instances

## Data sockets

> Data socket classes implementing this node.
  
  
- [Instances](/docs/sockets/Instances.md).[scale](/docs/sockets/Instances.md#scale) : Method
  
