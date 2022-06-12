
# Node RotateInstances

> Geometry node name: [Rotate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html)<br>
  Blender type: [Rotate Instances](https://docs.blender.org/api/current/bpy.types.GeometryNodeRotateInstances.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
        from geonodes import nodes
        node = nodes.RotateInstances(instances=None, selection=None, rotation=None, pivot_point=None, local_space=None, label=None)
        ```



## Arguments


### Input sockets

- instances : Instances
- selection : Boolean
- rotation : Vector
- pivot_point : Vector
- local_space : Boolean

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- instances : Instances

## Data sockets

> Data socket classes implementing this node.
  
  
- [Instances](/docs/sockets/Instances.md).[rotate](/docs/sockets/Instances.md#rotate) : Method
  
