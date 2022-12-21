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

 - [switch](A.md#switch) ```python nodes.Switch(switch=switch, false=false, true=true, input_type=input_type````
 - [switch_float](A.md#switch_float) ```python nodes.Switch(switch=switch, false=false, true=true, input_type='FLOAT'````
 - [switch_integer](A.md#switch_integer) ```python nodes.Switch(switch=switch, false=false, true=true, input_type='INT'````
 - [switch_boolean](A.md#switch_boolean) ```python nodes.Switch(switch=switch, false=false, true=true, input_type='BOOLEAN'````
 - [switch_vector](A.md#switch_vector) ```python nodes.Switch(switch=switch, false=false, true=true, input_type='VECTOR'````
 - [switch_string](A.md#switch_string) ```python nodes.Switch(switch=switch, false=false, true=true, input_type='STRING'````
 - [switch_color](A.md#switch_color) ```python nodes.Switch(switch=switch, false=false, true=true, input_type='RGBA'````
 - [switch_object](A.md#switch_object) ```python nodes.Switch(switch=switch, false=false, true=true, input_type='OBJECT'````
 - [switch_image](A.md#switch_image) ```python nodes.Switch(switch=switch, false=false, true=true, input_type='IMAGE'````
 - [switch_geometry](A.md#switch_geometry) ```python nodes.Switch(switch=switch, false=false, true=true, input_type='GEOMETRY'````
 - [switch_collection](A.md#switch_collection) ```python nodes.Switch(switch=switch, false=false, true=true, input_type='COLLECTION'````
 - [switch_texture](A.md#switch_texture) ```python nodes.Switch(switch=switch, false=false, true=true, input_type='TEXTURE'````
 - [switch_material](A.md#switch_material) ```python nodes.Switch(switch=switch, false=false, true=true, input_type='MATERIAL'````
#### [Boolean](Boolean.md)

 - [switch](Boolean.md#switch) ```python nodes.Switch(switch=switch, false=self, true=true, input_type='BOOLEAN'````
#### [Collection](Collection.md)

 - [switch](Collection.md#switch) ```python nodes.Switch(switch=switch, false=self, true=true, input_type='COLLECTION'````
#### [Color](Color.md)

 - [switch](Color.md#switch) ```python nodes.Switch(switch=switch, false=self, true=true, input_type='RGBA'````
#### [Float](Float.md)

 - [switch](Float.md#switch) ```python nodes.Switch(switch=switch, false=self, true=true, input_type='FLOAT'````
#### [Geometry](Geometry.md)

 - [switch](Geometry.md#switch) ```python nodes.Switch(switch=switch, false=self, true=true, input_type='GEOMETRY'````
#### [Image](Image.md)

 - [switch](Image.md#switch) ```python nodes.Switch(switch=switch, false=self, true=true, input_type='IMAGE'````
#### [Integer](Integer.md)

 - [switch](Integer.md#switch) ```python nodes.Switch(switch=switch, false=self, true=true, input_type='INT'````
#### [Material](Material.md)

 - [switch](Material.md#switch) ```python nodes.Switch(switch=switch, false=self, true=true, input_type='MATERIAL'````
#### [Object](Object.md)

 - [switch](Object.md#switch) ```python nodes.Switch(switch=switch, false=self, true=true, input_type='OBJECT'````
#### [String](String.md)

 - [switch](String.md#switch) ```python nodes.Switch(switch=switch, false=self, true=true, input_type='STRING'````
#### [Texture](Texture.md)

 - [switch](Texture.md#switch) ```python nodes.Switch(switch=switch, false=self, true=true, input_type='TEXTURE'````
#### [Vector](Vector.md)

 - [switch](Vector.md#switch) ```python nodes.Switch(switch=switch, false=self, true=true, input_type='VECTOR'````
