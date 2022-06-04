
# Class StringToCurves

> Geometry node name: _'String to Curves'_<br>Blender type:  **GeometryNodeStringToCurves**

## Initialization


```python
from geonodes import nodes
node = nodes.StringToCurves(string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT', label=None)
```


### Arguments


#### Input sockets



- **string** : _String_
- **size** : _Float_
- **character_spacing** : _Float_
- **word_spacing** : _Float_
- **line_spacing** : _Float_
- **text_box_width** : _Float_
- **text_box_height** : _Float_



#### Parameters



- **align_x** : _'LEFT'_ in ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH')
- **align_y** : _'TOP_BASELINE'_ in ('TOP_BASELINE', 'TOP', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM')
- **overflow** : _'OVERFLOW'_ in ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE')
- **pivot_mode** : _'BOTTOM_LEFT'_ in ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT')



#### Node label



- **label** : Geometry node label



## Output sockets



- **curve_instances** : _Geometry_
- **remainder** : _String_
- **line** : _Integer_
- **pivot_point** : _Vector_



## Data sockets

> Data socket classes implementing this node


- [String](aaa). [to_curves](bbb) : Method


