# Node *Simulation Output*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/i.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSimulationOutput.html)
- geonodes name: `SimulationOutput`
- bl_idname: `GeometryNodeSimulationOutput`

```python
from geonodes import nodes

node = nodes.SimulationOutput(geometry=None, active_index=0)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSimulationOutput.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)

#### Node parameter arguments:

- **active_index** (int): default = 0

### Output sockets:

- **geometry** : [Geometry](Geometry.md)


<sub>Go to [top](#node-Simulation-Output) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

