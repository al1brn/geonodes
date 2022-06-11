
# Node TranslateInstances

> Geometry node name: [Translate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html)<br>
  Blender type: [Translate Instances](https://docs.blender.org/api/current/bpy.types.GeometryNodeTranslateInstances.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.TranslateInstances(instances=None, selection=None, translation=None, local_space=None, label=None)
```



## Arguments


### Input sockets

- instances : Instances
- selection : Boolean
- translation : Vector
- local_space : Boolean

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- instances : Instances

## Data sockets

> Data socket classes implementing this node.
  
  
- [Instances](/docs/sockets/Instances.md).[translate](/docs/sockets/Instances.md#translate) : Method
  
