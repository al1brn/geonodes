
# Class MaterialSelection

> Geometry node name: _'Material Selection'_<br>Blender type:  **GeometryNodeMaterialSelection**
[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.MaterialSelection(material=None, label=None)
```


### Arguments


#### Input sockets



- **material** : _Material_



#### Node label



- **label** : Geometry node label



## Output sockets



- **selection** : _Boolean_



## Data sockets

> Data socket classes implementing this node


- [Material](../sockets/Material.md) [selection](../sockets/Material.md#selection) : Method
- [Mesh](../sockets/Mesh.md) [capture_material_selection](../sockets/Mesh.md#capture_material_selection) : Capture attribute
- [Mesh](../sockets/Mesh.md) [material_selection](../sockets/Mesh.md#material_selection) : Attribute


