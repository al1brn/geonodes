
# Node StringToCurves

> Geometry node name: [String to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_to_curves.html)<br>
  Blender type: [String to Curves](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringToCurves.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.StringToCurves(string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT', label=None, node_color=None)
```



## Arguments


### Input sockets

- string : String
- size : Float
- character_spacing : Float
- word_spacing : Float
- line_spacing : Float
- text_box_width : Float
- text_box_height : Float

### Parameters

- align_x : str (default = 'LEFT') in ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH')
- align_y : str (default = 'TOP_BASELINE') in ('TOP_BASELINE', 'TOP', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM')
- overflow : str (default = 'OVERFLOW') in ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE')
- pivot_mode : str (default = 'BOTTOM_LEFT') in ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- curve_instances : Geometry
- remainder : String
- line : Integer
- pivot_point : Vector
