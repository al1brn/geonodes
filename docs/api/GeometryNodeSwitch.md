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

#### class [Float](Float.md)

 - [switch](Float.md#switch)
#### class [Integer](Integer.md)

 - [switch](Integer.md#switch)
#### class [Boolean](Boolean.md)

 - [switch](Boolean.md#switch)
#### class [String](String.md)

 - [switch](String.md#switch)
#### class [Vector](Vector.md)

 - [switch](Vector.md#switch)
#### class [Color](Color.md)

 - [switch](Color.md#switch)
#### class [Collection](Collection.md)

 - [switch](Collection.md#switch)
#### class [Object](Object.md)

 - [switch](Object.md#switch)
#### class [Image](Image.md)

 - [switch](Image.md#switch)
#### class [Texture](Texture.md)

 - [switch](Texture.md#switch)
#### class [Material](Material.md)

 - [switch](Material.md#switch)
#### class [Geometry](Geometry.md)

 - [switch](Geometry.md#switch)
#### Global functions

 - [switch](function.md#switch)
 - [switch_float](function.md#switch_float)
 - [switch_integer](function.md#switch_integer)
 - [switch_boolean](function.md#switch_boolean)
 - [switch_vector](function.md#switch_vector)
 - [switch_string](function.md#switch_string)
 - [switch_color](function.md#switch_color)
 - [switch_object](function.md#switch_object)
 - [switch_image](function.md#switch_image)
 - [switch_geometry](function.md#switch_geometry)
 - [switch_collection](function.md#switch_collection)
 - [switch_texture](function.md#switch_texture)
 - [switch_material](function.md#switch_material)
