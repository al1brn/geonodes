
# Class Instance

Instance domain


## rotation

Rotation attribute

Returns:
  Vector
  
- getter: :class:`~geonodes.nodes.nodes.InstanceRotation`
- setter: Read only
  
  
  

## scale

Scale attribute

Returns:
  Vector
  
- getter: :class:`~geonodes.nodes.nodes.InstanceScale`
- setter: Read only
  
  
  

## delete

Delete instances.

Node :class:`~geonodes.nodes.nodes.DeleteGeometry`

Returns:
  self
  
.. code-block:: python

  instances.insts(...).delete()
  
  

## rotate

Rotate instances.

Node :class:`~geonodes.nodes.nodes.RotateInstances`

Args:
  rotation : Vector
  pivot_point : Vector
  local_space : Boolean
  
Returns:
  self
  
.. code-block:: python

  instances.insts(...).rotate(...)
  
  

## set_scale

Scale instances.

Node :class:`~geonodes.nodes.nodes.ScaleInstances`

Args:
  scale : Vector
  center : Vector
  local_space : Boolean
  
Returns:
  self
  
.. code-block:: python

  instances.insts(...).scale(...)
  
  

## translate

> Translate instances.
  
Node :class:`~geonodes.nodes.nodes.TranslateInstances`

Args:
- translation : Vector
- local_space : Boolean
  
Returns:
  self
  
.. code-block:: python

  instances.insts(...).translate(...)
  
  