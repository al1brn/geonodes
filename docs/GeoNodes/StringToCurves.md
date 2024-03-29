# Node StringToCurves

- Node name : 'String to Curves'
- bl_idname : [GeometryNodeStringToCurves](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringToCurves.html)


``` python
StringToCurves(string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', font=None, overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- string : None
- size : None
- character_spacing : None
- word_spacing : None
- line_spacing : None
- text_box_width : None
- text_box_height : None
- align_x : 'LEFT'
- align_y : 'TOP_BASELINE'
- font : None
- overflow : 'OVERFLOW'
- pivot_mode : 'BOTTOM_LEFT'

## Implementation

- [STRING](/docs/GeoNodes/socket_STRING.md) : [string_to_curves](/docs/GeoNodes/socket_STRING.md#string_to_curves)

## Init

``` python
def __init__(self, string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', font=None, overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeStringToCurves', node_label=node_label, node_color=node_color, **kwargs)

    self.align_x         = align_x
    self.align_y         = align_y
    self.font            = font
    self.overflow        = overflow
    self.pivot_mode      = pivot_mode
    self.string          = string
    self.size            = size
    self.character_spacing = character_spacing
    self.word_spacing    = word_spacing
    self.line_spacing    = line_spacing
    self.text_box_width  = text_box_width
    self.text_box_height = text_box_height
```
