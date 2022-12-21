# Node Switch

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
- geonodes name: `Switch`
- bl_idname: `GeometryNodeSwitch`

```python
from geonodes import nodes

node = nodes.Switch(switch=None, false=None, true=None, input_type='GEOMETRY')
```

### Args:

#### Input socket arguments:

- **switch**: **input_type** dependant
- **false**: **input_type** dependant
- **true**: **input_type** dependant

#### Node parameter arguments:

- **input_type** (str): default = 'GEOMETRY' in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL')

### Output sockets:

- **output** : ``input_type`` dependant

#### Shared sockets:

- Driving parameter : ``input_type`` in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL')
- Input sockets  : ['switch', 'false', 'true']
- Output sockets : ['output']
## Implementation

#### Global functions

 - [switch](A.md#switch)
 - [switch_float](A.md#switch_float)
 - [switch_integer](A.md#switch_integer)
 - [switch_boolean](A.md#switch_boolean)
 - [switch_vector](A.md#switch_vector)
 - [switch_string](A.md#switch_string)
 - [switch_color](A.md#switch_color)
 - [switch_object](A.md#switch_object)
 - [switch_image](A.md#switch_image)
 - [switch_geometry](A.md#switch_geometry)
 - [switch_collection](A.md#switch_collection)
 - [switch_texture](A.md#switch_texture)
 - [switch_material](A.md#switch_material)
#### class [Boolean](Boolean.md)

 - [switch](Boolean.md#switch)
#### class [Collection](Collection.md)

 - [switch](Collection.md#switch)
#### class [Color](Color.md)

 - [switch](Color.md#switch)
#### class [Float](Float.md)

 - [switch](Float.md#switch)
#### class [Geometry](Geometry.md)

 - [switch](Geometry.md#switch)
#### class [Image](Image.md)

 - [switch](Image.md#switch)
#### class [Integer](Integer.md)

 - [switch](Integer.md#switch)
#### class [Material](Material.md)

 - [switch](Material.md#switch)
#### class [Object](Object.md)

 - [switch](Object.md#switch)
#### class [String](String.md)

 - [switch](String.md#switch)
#### class [Texture](Texture.md)

 - [switch](Texture.md#switch)
#### class [Vector](Vector.md)

 - [switch](Vector.md#switch)
