# Node Object Info

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)
- geonodes name: `ObjectInfo`
- bl_idname: `GeometryNodeObjectInfo`

```python
from geonodes import nodes

node = nodes.ObjectInfo(object=None, as_instance=None, transform_space='ORIGINAL')
```

### Args:

#### Input socket arguments:

- **object**: [Object](Object.md)
- **as_instance**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **transform_space** (str): default = 'ORIGINAL' in ('ORIGINAL', 'RELATIVE')

### Output sockets:

- **location** : [Vector](Vector.md)
- **rotation** : [Vector](Vector.md)
- **scale** : [Vector](Vector.md)
- **geometry** : [Geometry](Geometry.md)

## Implementation

#### [Object](Object.md)

 - [info](Object.md#info) ```python nodes.ObjectInfo(object=object, as_instance=as_instance, transform_space=transform_space````
 - [location](Object.md#location) ```python nodes.ObjectInfo(object=object, as_instance=as_instance, transform_space=transform_space````
 - [rotation](Object.md#rotation) ```python nodes.ObjectInfo(object=object, as_instance=as_instance, transform_space=transform_space````
 - [scale](Object.md#scale) ```python nodes.ObjectInfo(object=object, as_instance=as_instance, transform_space=transform_space````
 - [geometry](Object.md#geometry) ```python nodes.ObjectInfo(object=object, as_instance=as_instance, transform_space=transform_space````
