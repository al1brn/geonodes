# Node Geometry Proximity

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)
- geonodes name: `GeometryProximity`
- bl_idname: `GeometryNodeProximity`

```python
from geonodes import nodes

node = nodes.GeometryProximity(target=None, source_position=None, target_element='FACES')
```

### Args:

#### Input socket arguments:

- **target**: [Geometry](Geometry.md)
- **source_position**: [Vector](Vector.md)

#### Node parameter arguments:

- **target_element** (str): default = 'FACES' in ('POINTS', 'EDGES', 'FACES')

### Output sockets:

- **position** : [Vector](Vector.md)
- **distance** : [Float](Float.md)

## Implementation

#### [Geometry](Geometry.md)

 - [proximity](Geometry.md#proximity)
  ```python
  def proximity(self, target=None, source_position=None, target_element='FACES')
  ```

 - [proximity_points](Geometry.md#proximity_points)
  ```python
  def proximity_points(self, target=None, source_position=None)
  ```

 - [proximity_edges](Geometry.md#proximity_edges)
  ```python
  def proximity_edges(self, target=None, source_position=None)
  ```

 - [proximity_facess](Geometry.md#proximity_facess)
  ```python
  def proximity_facess(self, target=None, source_position=None)
  ```

