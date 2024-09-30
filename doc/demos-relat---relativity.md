# relativity

Created on 2024/08/02

@author: alain

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : demos/relativity
-------------------------
Generates modifiers for special relativity

The space-time is (x, y, z=t) : space in 2D plus time dimension on z axis

Geometry Nodes
--------------
    - "Plane Line Intersection" (group) : intersection between a line and a plane
    - "Frame Change" (group) : Change position and direction to align X axis along the given direction
    - "Normalize Speed" (group) : Normalize speed
    - "Transformation" (group) : Lorentz or Galilean transformation
    - "Simulateneity Plane" (group): Compute the simultaneity plane of event + speed
    - "Simultaneity Intersection" (modifier) : Compute the intersection of the simultaneity plane with the provided curve
    - "Accelerated Transformation" (modifier) : transform a uniform motion into an accelerated frame defined a curve in (x, y, t=z) space time
    - "Rounded Triangle" (group) : function t -> (x, y) producing a triangle with a rounded summit

updates
-------
- creation : 2024/08/25
- update   : 2024/09/04