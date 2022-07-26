# Building an arrow

> Tutorial on how to build a full parametrized arrow.

## Objective

We need arrows of different resolution, appearance, size which can take various orientations.
We want to control these parameters with the modifier, including the material on shaft and arrowhead.

The image below shows what we want to build:

<img src="images/arrow_1.png" width="600" class="center">


## Parameters

The parameters to create are the following:

| Name             | Type           | Description                                                      |
| ---------------- | -------------- | ---------------------------------------------------------------- |
| Length           | Float          | Total length of the arrow, including the arrowhead               |
| Radius           | Float          | Radius shaft                                                     |
| Head size        | Float          | Size of the arrow head, expressed as a factor applied to radius  |
| Head angle       | Float (Angle)  | Angle of the arrowhead peak                                      |
| Recess           | Float          | How "deep" the shaft penetrates in the arrowhead (0: flat, 1: max) |
| Vertices         | Integer        | Circular resolution expressed inf number of vertices             |

We will add complementatry parameters later on but for the moment, these parameters allow to build the arrow.
The good practice is to start by declaring the parameters at the begining of the tree.

``` python
import numpy as np
import geonodes as gn

  with gn.Tree("Arrow") as tree:

      length    = gn.Float.Input(1, "Length", min_value=0)
      r         = gn.Float.Input(0.1, "Radius", min_value=0.001)
      s         = gn.Float.Input(2, "Head size", min_value=1.001)
      angle     = gn.Float.Angle(np.radians(20), "Angle", min_value=np.radians(10), max_value=0.999*gn.pi/2)
      k         = gn.Float.Input(0.5, "Recess", min_value=0., max_value=0.99)
      vertices  = gn.Integer.Input(12, "Vertices", min_value=3)

```

## Some maths

We will build the arrow by extruding a base disk up along the z axis and then enlarging the cylinder to build the arrowhead.
Some maths are required to build the arrow according the parameters.

<img src="images/Arrow_comp.png" width="600" class="center">





