# Node 'Switch'

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

### Global functions

| Name | Definition |
|------|------------|
 | [switch](A.md#switch) | `def switch(switch=None, false=None, true=None, input_type='GEOMETRY'):` |
 | [switch_float](A.md#switch_float) | `def switch_float(switch=None, false=None, true=None):` |
 | [switch_integer](A.md#switch_integer) | `def switch_integer(switch=None, false=None, true=None):` |
 | [switch_boolean](A.md#switch_boolean) | `def switch_boolean(switch=None, false=None, true=None):` |
 | [switch_vector](A.md#switch_vector) | `def switch_vector(switch=None, false=None, true=None):` |
 | [switch_string](A.md#switch_string) | `def switch_string(switch=None, false=None, true=None):` |
 | [switch_color](A.md#switch_color) | `def switch_color(switch=None, false=None, true=None):` |
 | [switch_object](A.md#switch_object) | `def switch_object(switch=None, false=None, true=None):` |
 | [switch_image](A.md#switch_image) | `def switch_image(switch=None, false=None, true=None):` |
 | [switch_geometry](A.md#switch_geometry) | `def switch_geometry(switch=None, false=None, true=None):` |
 | [switch_collection](A.md#switch_collection) | `def switch_collection(switch=None, false=None, true=None):` |
 | [switch_texture](A.md#switch_texture) | `def switch_texture(switch=None, false=None, true=None):` |
 | [switch_material](A.md#switch_material) | `def switch_material(switch=None, false=None, true=None):` |

### [Boolean](Boolean.md)

| Name | Definition |
|------|------------|
 | [switch](Boolean.md#switch) | `def switch(self, switch=None, true=None):` |

### [Collection](Collection.md)

| Name | Definition |
|------|------------|
 | [switch](Collection.md#switch) | `def switch(self, switch=None, true=None):` |

### [Color](Color.md)

| Name | Definition |
|------|------------|
 | [switch](Color.md#switch) | `def switch(self, switch=None, true=None):` |

### [Float](Float.md)

| Name | Definition |
|------|------------|
 | [switch](Float.md#switch) | `def switch(self, switch=None, true=None):` |

### [Geometry](Geometry.md)

| Name | Definition |
|------|------------|
 | [switch](Geometry.md#switch) | `def switch(self, switch=None, true=None):` |

### [Image](Image.md)

| Name | Definition |
|------|------------|
 | [switch](Image.md#switch) | `def switch(self, switch=None, true=None):` |

### [Integer](Integer.md)

| Name | Definition |
|------|------------|
 | [switch](Integer.md#switch) | `def switch(self, switch=None, true=None):` |

### [Material](Material.md)

| Name | Definition |
|------|------------|
 | [switch](Material.md#switch) | `def switch(self, switch=None, true=None):` |

### [Object](Object.md)

| Name | Definition |
|------|------------|
 | [switch](Object.md#switch) | `def switch(self, switch=None, true=None):` |

### [String](String.md)

| Name | Definition |
|------|------------|
 | [switch](String.md#switch) | `def switch(self, switch=None, true=None):` |

### [Texture](Texture.md)

| Name | Definition |
|------|------------|
 | [switch](Texture.md#switch) | `def switch(self, switch=None, true=None):` |

### [Vector](Vector.md)

| Name | Definition |
|------|------------|
 | [switch](Vector.md#switch) | `def switch(self, switch=None, true=None):` |

<sub>Go to [top](#node-{wnode.bnode.name}) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

