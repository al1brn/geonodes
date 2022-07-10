
# Data socket Volume

> Inherits from gn.Geometry
  
<sub>go to [index](/docs/index.md)</sub>



## Methods

- [to_mesh](#to_mesh) : mesh (Mesh)

## to_mesh

Geometry node [*Volume to Mesh*].


  Args:
    voxel_size: Float
    voxel_amount: Float
    threshold: Float
    adaptivity: Float
    resolution_mode (str): 'GRID' in [GRID, VOXEL_AMOUNT, VOXEL_SIZE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Mesh
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.VolumeToMesh`
  
  
  .. blid:: GeometryNodeVolumeToMesh
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.VolumeToMesh(volume=self, voxel_size=voxel_size, voxel_amount=voxel_amount, threshold=threshold, adaptivity=adaptivity, resolution_mode=resolution_mode, label=node_label, node_color=node_color)
    
