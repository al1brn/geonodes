
# Node CollectionInfo

> Geometry node name: [Collection Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/collection_info.html)<br>
  Blender type: [Collection Info](https://docs.blender.org/api/current/bpy.types.GeometryNodeCollectionInfo.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.CollectionInfo(collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL', label=None, node_color=None)
```



## Arguments


### Input sockets

- collection : Collection
- separate_children : Boolean
- reset_children : Boolean

### Parameters

- transform_space : str (default = 'ORIGINAL') in ('ORIGINAL', 'RELATIVE')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- geometry : Geometry
