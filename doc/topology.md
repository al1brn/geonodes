# topology

[Source Code](../demos/topology.py)

This demo provides two modifiers:
- Topology Indices :
  The modifier allows to select a domain in 'Vertices', 'Edges', ...
  It displays the index of each element iof the selected domain
- Mesh Topology :
  The modifier selects a domain in 'Vertices', 'Edges',... and a index which
  must be valid in the selected domain.
  The modifiers displays the linked domain elements, for instance the edges, faces and corners
  linked to a selected vertex.

> [!NOTE]
> Modifiers:
> - Topology Indices
> - Mesh Topology

``` python
from geonodes.demos import topology

topology.demo()
```