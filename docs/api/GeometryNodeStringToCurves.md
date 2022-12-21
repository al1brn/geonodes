# Node String to Curves

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_to_curves.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringToCurves.html)
- geonodes name: `StringToCurves`
- bl_idname: `GeometryNodeStringToCurves`

```python
from geonodes import nodes

node = nodes.StringToCurves(string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT')
```

### Args:

#### Input socket arguments:

- **string**: [String](String.md)
- **size**: [Float](Float.md)
- **character_spacing**: [Float](Float.md)
- **word_spacing**: [Float](Float.md)
- **line_spacing**: [Float](Float.md)
- **text_box_width**: [Float](Float.md)
- **text_box_height**: [Float](Float.md)

#### Node parameter arguments:

- **align_x** (str): default = 'LEFT' in ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH')
- **align_y** (str): default = 'TOP_BASELINE' in ('TOP_BASELINE', 'TOP', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM')
- **overflow** (str): default = 'OVERFLOW' in ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE')
- **pivot_mode** (str): default = 'BOTTOM_LEFT' in ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT')

### Output sockets:

- **curve_instances** : [Geometry](Geometry.md)
- **remainder** : [String](String.md)
- **line** : [Integer](Integer.md)
- **pivot_point** : [Vector](Vector.md)

## Implementation

#### class [String](String.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x168102950>>](String.md#to_curves)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x168102980>>](function.md#string_to_curves)
