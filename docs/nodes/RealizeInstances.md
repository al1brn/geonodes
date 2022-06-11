
# Node RealizeInstances

> Geometry node name: [Realize Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/realize_instances.html)<br>
  Blender type: [Realize Instances](https://docs.blender.org/api/current/bpy.types.GeometryNodeRealizeInstances.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.RealizeInstances(geometry=None, legacy_behavior=False, label=None)
```



## Arguments


### Input sockets

- geometry : Geometry

### Parameters

- legacy_behavior : bool (default = False)

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- geometry : Geometry

## Data sockets

> Data socket classes implementing this node.
  
  
- [Geometry](/docs/sockets/Geometry.md).[realize_instances](/docs/sockets/Geometry.md#realize_instances) : Method
  
