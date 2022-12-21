# Node 'Float to Integer'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)
- geonodes name: `FloatToInteger`
- bl_idname: `FunctionNodeFloatToInt`

```python
from geonodes import nodes

node = nodes.FloatToInteger(float=None, rounding_mode='ROUND')
```

[Blender Image](self.node_image_ref)

### Args:

#### Input socket arguments:

- **float**: [Float](Float.md)

#### Node parameter arguments:

- **rounding_mode** (str): default = 'ROUND' in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')

### Output sockets:

- **integer** : [Integer](Integer.md)

## Implementation

### [Float](Float.md)

| Name | Definition |
|------|------------|
 | [to_integer](Float.md#to_integer) | `def to_integer(self, rounding_mode='ROUND'):` |
 | [round](Float.md#round) | `def round(self):` |
 | [floor](Float.md#floor) | `def floor(self):` |
 | [ceiling](Float.md#ceiling) | `def ceiling(self):` |
 | [truncate](Float.md#truncate) | `def truncate(self):` |

<sub>Go to [top](#node-Float-to-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

