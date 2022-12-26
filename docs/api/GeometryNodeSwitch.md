# Node *Switch*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
- geonodes name: `Switch`
- bl_idname: `GeometryNodeSwitch`

```python
from geonodes import nodes

node = nodes.Switch(switch=None, false=None, true=None, input_type='GEOMETRY')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSwitch.webp)

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

| Class or method name | Definition |
|----------------------|------------|
| **[Boolean](Boolean.md)** |
| [switch](Boolean.md#switch) | `def switch(self, switch=None, true=None):` |
| **[Collection](Collection.md)** |
| [switch](Collection.md#switch) | `def switch(self, switch=None, true=None):` |
| **[Color](Color.md)** |
| [switch](Color.md#switch) | `def switch(self, switch=None, true=None):` |
| **[Float](Float.md)** |
| [switch](Float.md#switch) | `def switch(self, switch=None, true=None):` |
| **[Geometry](Geometry.md)** |
| [switch](Geometry.md#switch) | `def switch(self, switch=None, true=None):` |
| **[Image](Image.md)** |
| [switch](Image.md#switch) | `def switch(self, switch=None, true=None):` |
| **[Integer](Integer.md)** |
| [switch](Integer.md#switch) | `def switch(self, switch=None, true=None):` |
| **[Material](Material.md)** |
| [switch](Material.md#switch) | `def switch(self, switch=None, true=None):` |
| **[Object](Object.md)** |
| [switch](Object.md#switch) | `def switch(self, switch=None, true=None):` |
| **[String](String.md)** |
| [switch](String.md#switch) | `def switch(self, switch=None, true=None):` |
| **[Texture](Texture.md)** |
| [switch](Texture.md#switch) | `def switch(self, switch=None, true=None):` |
| **[Vector](Vector.md)** |
| [switch](Vector.md#switch) | `def switch(self, switch=None, true=None):` |
| Global functions |
| [switch](functions.md#switch) | `def switch(switch=None, false=None, true=None, input_type='GEOMETRY'):` |
| [switch_float](functions.md#switch_float) | `def switch_float(switch=None, false=None, true=None):` |
| [switch_integer](functions.md#switch_integer) | `def switch_integer(switch=None, false=None, true=None):` |
| [switch_boolean](functions.md#switch_boolean) | `def switch_boolean(switch=None, false=None, true=None):` |
| [switch_vector](functions.md#switch_vector) | `def switch_vector(switch=None, false=None, true=None):` |
| [switch_string](functions.md#switch_string) | `def switch_string(switch=None, false=None, true=None):` |
| [switch_color](functions.md#switch_color) | `def switch_color(switch=None, false=None, true=None):` |
| [switch_object](functions.md#switch_object) | `def switch_object(switch=None, false=None, true=None):` |
| [switch_image](functions.md#switch_image) | `def switch_image(switch=None, false=None, true=None):` |
| [switch_geometry](functions.md#switch_geometry) | `def switch_geometry(switch=None, false=None, true=None):` |
| [switch_collection](functions.md#switch_collection) | `def switch_collection(switch=None, false=None, true=None):` |
| [switch_texture](functions.md#switch_texture) | `def switch_texture(switch=None, false=None, true=None):` |
| [switch_material](functions.md#switch_material) | `def switch_material(switch=None, false=None, true=None):` |

<sub>Go to [top](#node-Switch) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

