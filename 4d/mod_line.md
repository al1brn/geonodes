# Line (Modifier)

> Build a 4D line curve. Can by used as curve 4D in [Build along curve](mod_build_along_curve.md).

**Note:** Input geometry is unsued.

## Sockets & attributes

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Mesh        | Modifier input geometry (unused)                                      |
| xyz 0       | Vector      | Vector part starting point                                            |
| w 0         | Float       | Float part of starting point                                          |
| xyz 1       | Vector      | Vector part of ending point                                           |
| w 1         | Float       | Float part of endinf point                                            |
| Count       | Integer     | Number of point in the line                                           |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Geometry    | Mesh        | Modifier output geometry                                              |

### Named attributes

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| w           | Float       | The fourth dimension                                                  |
| Txyz        | Vector      | Vector part of the tangents                                           |
| Tw          | Float       | Float part of the tangents                                           |


## Code

``` python

with gn.Tree(modifiers.name("Line")) as tree:

   v0 = gn.Vector.Input( 0, "xyz 0")
   w0 = gn.Float.Input(-1, "w 0")
   v1 = gn.Vector.Input( 0, "xyz 1")
   w1 = gn.Float.Input( 1, "w 1")
   count = gn.Integer.Input(10, "Count", min_value=2)

   line = gn.Curve.Line(start=v0, end=v1).resample(count=count)

   line.points.set_named_float("w", gn.Float(line.points.index).map_range(from_min=0, from_max=count-1, to_min=w0, to_max=w1))

   # ----- Tangents

   tv = v1 - v0
   tw = w1 - v0
   node = maths.normalize(xyz=tv, w=tw)

   tv = node.xyz
   tw = node.w

   # ----- Store the named attributes

   line.points.set_named_float("w", gn.Float(line.points.index).map_range(from_min=0, from_max=count-1, to_min=w0, to_max=w1))

   line.points.set_named_vector("Txyz", tv)
   line.points.set_named_float("Tw", tw)

   tree.og = line

```

