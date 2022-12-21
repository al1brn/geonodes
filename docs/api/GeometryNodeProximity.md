# Node Geometry Proximity

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)
- geonodes name: `GeometryProximity`
- bl_idname: `GeometryNodeProximity`

```python
from geonodes import nodes

node = nodes.GeometryProximity(target=None, source_position=None, target_element='FACES')
```

### Args:

#### Input socket arguments:

- **target**: [Geometry](Geometry.md)
- **source_position**: [Vector](Vector.md)

#### Node parameter arguments:

- **target_element** (str): default = 'FACES' in ('POINTS', 'EDGES', 'FACES')

### Output sockets:

- **position** : [Vector](Vector.md)
- **distance** : [Float](Float.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x1683b27a0>>](Geometry.md#proximity)
 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x1683b3ac0>>](Geometry.md#proximity_points)
 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x1683b31f0>>](Geometry.md#proximity_edges)
 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x1683b0d30>>](Geometry.md#proximity_facess)
