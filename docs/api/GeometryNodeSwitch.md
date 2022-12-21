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

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3df5b0>>](Float.md#switch)
#### class [Integer](Integer.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3df6d0>>](Integer.md#switch)
#### class [Boolean](Boolean.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dda50>>](Boolean.md#switch)
#### class [String](String.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3df010>>](String.md#switch)
#### class [Vector](Vector.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dd510>>](Vector.md#switch)
#### class [Color](Color.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3df1c0>>](Color.md#switch)
#### class [Collection](Collection.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3df160>>](Collection.md#switch)
#### class [Object](Object.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3df940>>](Object.md#switch)
#### class [Image](Image.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3df2b0>>](Image.md#switch)
#### class [Texture](Texture.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3de440>>](Texture.md#switch)
#### class [Material](Material.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3dd6f0>>](Material.md#switch)
#### class [Geometry](Geometry.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16e3deef0>>](Geometry.md#switch)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e3dd7e0>>](function.md#switch)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e3df850>>](function.md#switch_float)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e3df250>>](function.md#switch_integer)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e3dcdc0>>](function.md#switch_boolean)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e3df610>>](function.md#switch_vector)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e3dd810>>](function.md#switch_string)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e3dc6a0>>](function.md#switch_color)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e3dc5e0>>](function.md#switch_object)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e3dd060>>](function.md#switch_image)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e3dd180>>](function.md#switch_geometry)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e3dd690>>](function.md#switch_collection)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e3dcee0>>](function.md#switch_texture)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16e3dcf70>>](function.md#switch_material)
