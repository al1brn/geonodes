# topology demo

This page describes a demonstration scene. For current tree declarations and
build calls, see [Modifiers, groups and tools](../getting_started/modifiers_groups.md)
and [Packages](../getting_started/packages.md). Older module-level `demo(...)`
entry points are specific to each demo and do not define the builder API.


![render](images/topology_render_01.png)

Display the indices of mesh domain elements with their peer elements :
vertex indices of an edge, edge indices of face... 


## Modifiers

- **Topology Indices** : The modifier allows to select a domain in 'Vertices', 'Edges', ...
  It displays the index of each element of the selected domain
- **Mesh Topology** : The modifier selects a domain in 'Vertices', 'Edges',...
  and a index which must be valid in the selected domain.
  The modifiers displays the linked domain elements, for instance the edges, faces and corners
  linked to a selected vertex.

## What to learn

- dealing with element indices
- element of elements

![node](images/topology_node.png)












