# Node IndexSwitch

- Node name : 'Index Switch'
- bl_idname : [GeometryNodeIndexSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeIndexSwitch.html)

> 
``` python
IndexSwitch(*args, index=None, data_type=None, node_label=None, node_color=None, **kwargs)
```

## Arguments
- args (Sockets) : the sockets to pick into
- index (integer Socket) : selection index
- data_type (str=None) : type of value sockets. If None, data_type is deduced from kwargs data types
- kwargs : socket name -> socket to select from

> [!NOTE]
> The total number of sockets is the sum of the number of items in args and in kwargs

> [!CAUTION]
> Keys of kwargs dict must be a socket number : '**_0**', '**_1**', '**_2**', ... 

## Example

In the following example, the node is initialized with a list of 3 geometries passed as non keyed arguments
and one addtional geometry passed as keyed argument.

``` python
with GeoNodes("Test") as tree:
    
    node = tree.IndexSwitch(
        tree.ico_sphere(), tree.cube(), tree.cone(),
        index = tree.integer_input("Shape", 0),
        _1 = tree.ig)
        
    tree.og = node.output
```


## Implementation

- [BOOLEAN](/docs/GeoNodes/socket_BOOLEAN.md) : [index_switch](/docs/GeoNodes/socket_BOOLEAN.md#index_switch)
- [COLLECTION](/docs/GeoNodes/socket_COLLECTION.md) : [index_switch](/docs/GeoNodes/socket_COLLECTION.md#index_switch)
- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [index_switch](/docs/GeoNodes/socket_GEOMETRY.md#index_switch)
- [IMAGE](/docs/GeoNodes/socket_IMAGE.md) : [index_switch](/docs/GeoNodes/socket_IMAGE.md#index_switch)
- [INT](/docs/GeoNodes/socket_INT.md) : [index_switch](/docs/GeoNodes/socket_INT.md#index_switch)
- [MATERIAL](/docs/GeoNodes/socket_MATERIAL.md) : [index_switch](/docs/GeoNodes/socket_MATERIAL.md#index_switch)
- [OBJECT](/docs/GeoNodes/socket_OBJECT.md) : [index_switch](/docs/GeoNodes/socket_OBJECT.md#index_switch)
- [RGBA](/docs/GeoNodes/socket_RGBA.md) : [index_switch](/docs/GeoNodes/socket_RGBA.md#index_switch)
- [ROTATION](/docs/GeoNodes/socket_ROTATION.md) : [index_switch](/docs/GeoNodes/socket_ROTATION.md#index_switch)
- [STRING](/docs/GeoNodes/socket_STRING.md) : [index_switch](/docs/GeoNodes/socket_STRING.md#index_switch)
- [VALUE](/docs/GeoNodes/socket_VALUE.md) : [index_switch](/docs/GeoNodes/socket_VALUE.md#index_switch)
- [VECTOR](/docs/GeoNodes/socket_VECTOR.md) : [index_switch](/docs/GeoNodes/socket_VECTOR.md#index_switch)

