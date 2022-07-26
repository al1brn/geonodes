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

The corresponding python code is given here after:

``` python

    with tree.layout("Maths stuff..."):

        # ----- Arrowhead radius from the shaft radius

        rh = r*s

        # ----- Arrowhead height from the angle

        tg = gn.tan(angle)
        hh = rh/tg
        z0 = length - hh

        # ----- Recess computation

        h  = r/tg
        d  = k*h*(s - 1)

        z1 = z0 + d
        z2 = z0 + k*h*s
```

## Building by extrusion

The starting point is a disk:

``` python
    arrow = gn.Mesh.Circle(vertices=vertices, radius=r, fill_type='NGON')
```

The shaft length was computed above, it is equal to `z1`. Hence, the shaft is built by extruding the disk edges up to z1:

``` python
    top, _ = arrow.edges.extrude(offset=(0, 0, 1), offset_scale=z1)
```

The extrude method returns the extrudes edges and the side faces. The faces are useless for now.
In the final version will set material to the faces and we will collect the faces.

The next extrusion step is to extrude the edges downwards and outwards.
It the schema above, we are a points `Q'` and want to extrude to point `Q''`.
The direction of extrusion is given by the vector `QQ'`.
The amount of extrusion is given by the maths.

**Note:** Points `Q'` and  `Q''` are multiple (points forming the top circle of the shaft) when the point `Q` is unique.

``` python
    top, _ = top.extrude(offset=top.position - (0, 0, z2), offset_scale=s - 1)
```

To finish the arrow, we simply extrude from the current position to the top of the arrow:

``` python
    top, _ = top.extrude(offset=(0, 0, length) - top.position)
```

## First version

The first version of our arrow is then the following:

``` python

import geonodes as gn

with gn.Tree("Arrow") as tree:

    length    = gn.Float.Input(1, "Length", min_value=0)
    r         = gn.Float.Input(0.1, "Radius", min_value=0.001)
    s         = gn.Float.Input(2, "Head size", min_value=1.001)
    angle     = gn.Float.Angle(np.radians(20), "Angle", min_value=np.radians(10), max_value=0.999*gn.pi/2)
    k         = gn.Float.Input(0.5, "Recess", min_value=0., max_value=0.99)
    vertices  = gn.Integer.Input(12, "Vertices", min_value=3)


    with tree.layout("Maths stuff..."):

        # ----- Arrowhead radius from the shaft radius

        rh = r*s

        # ----- Arrowhead height from the angle

        tg = gn.tan(angle)
        hh = rh/tg
        z0 = length - hh

        # ----- Recess computation

        h  = r/tg
        d  = k*h*(s - 1)

        z1 = z0 + d
        z2 = z0 + k*h*s

    # -----Extrusion

    arrow = gn.Mesh.Circle(vertices=vertices, radius=r, fill_type='NGON')
    
    top, _ = arrow.edges.extrude(offset=(0, 0, 1), offset_scale=z1)
    
    top, _ = top.extrude(offset=top.position - (0, 0, z2), offset_scale=s - 1)

    top, _ = top.extrude(offset=(0, 0, length) - top.position)

    # ----- Output the arrow
    
    tree.og = arrows

```











aaa





