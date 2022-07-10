
# Class CloudPoint

Cloud point : the point domain of cloud of points


## delete

Delete points.

Node :class:`~geonodes.nodes.nodes.DeleteGeometry`        

Returns:
  self
  
.. code-block:: python

  cloud.points(...).delete()
  
  

## merge

Merge points by distance.

Node :class:`~geonodes.nodes.nodes.MergeByDistance`

Args:
  distance : Float
  
Returns:
  self
  
.. code-block:: python

  cloud.points().merge()
  
  
  

## to_vertices

Convert points to vertices.

Node :class:`~geonodes.nodes.nodes.PointsToVertices`

Returns:
  Points
  
.. code-block:: python

  verts = cloud.points.to_vertices()
  
  

## to_volume

Convert points to volume.

Node :class:`~geonodes.nodes.nodes.PointsToVolume`

Args:
  density : Float
  voxel_size : Float
  voxel_amount : Float
  radius : Float
  resolution_mode (str): (default = 'VOXEL_AMOUNT') in ('VOXEL_AMOUNT', 'VOXEL_SIZE')
  
Returns:
  Volume
  
.. code-block:: python

  volume = cloud.points.to_volume()
  
  