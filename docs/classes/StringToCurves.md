# class StringToCurves (Node)

<sub>go to [index](/docs/index.md)</sub>

## Node reference

Node
 - Class name : StringToCurves
 - bl_idname : GeometryNodeStringToCurves

Node parameters
 - align_x : 'LEFT'
 - align_y : 'TOP_BASELINE'
 - font
 - overflow : 'OVERFLOW'
 - pivot_mode : 'BOTTOM_LEFT'

Input sockets
 - string : Str
 - size : Float
 - character_spacing : Float
 - word_spacing : Float
 - line_spacing : Float
 - text_box_width : Float
 - text_box_height : Float

Output sockets
 - curve_instances : Geometry
 - remainder : Str
 - line : Int
 - pivot_point : Vect

### Header

``` python
def StringToCurves(self, string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', font=None, overflow='OVERFLOW',
pivot_mode='BOTTOM_LEFT', node_label=None, node_color=None):
```

## Implementations


