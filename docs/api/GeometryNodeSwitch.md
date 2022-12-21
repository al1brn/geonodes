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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55690>>](Float.md#switch)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55660>>](Integer.md#switch)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55630>>](Boolean.md#switch)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee555d0>>](String.md#switch)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55600>>](Vector.md#switch)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee555a0>>](Color.md#switch)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee554e0>>](Collection.md#switch)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55570>>](Object.md#switch)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55540>>](Image.md#switch)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee554b0>>](Texture.md#switch)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55480>>](Material.md#switch)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55510>>](Geometry.md#switch)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16ee55900>>](function.md#switch)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16ee558d0>>](function.md#switch_float)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16ee558a0>>](function.md#switch_integer)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16ee55870>>](function.md#switch_boolean)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16ee55840>>](function.md#switch_vector)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16ee55810>>](function.md#switch_string)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16ee557e0>>](function.md#switch_color)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16ee557b0>>](function.md#switch_object)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16ee55780>>](function.md#switch_image)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16ee55750>>](function.md#switch_geometry)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16ee55720>>](function.md#switch_collection)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16ee556f0>>](function.md#switch_texture)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16ee556c0>>](function.md#switch_material)
