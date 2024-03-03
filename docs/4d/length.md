# Length (maths)

> Compute the length of a 4-vector.

## Sockets

### Input sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| xyz         | Vector      | Vector part of the 4-vector                                           |
| w           | Float       | Float part of the 4-vector                                            |

### Output sockets

| Name        | Type        | Description                                                           |
| ----------- | ----------- | --------------------------------------------------------------------- |
| Length      | Float       | Vector Length                                                         |
| Null        | Boolean     | True if length is null (less than 0.001)                              |

## Code

``` python

with gn.Tree(maths.name("Length"), group=True) as tree:

    v = gn.Vector.Input(0, "xyz")
    w = gn.Float.Input( 1, "w")

    length = (v.dot(v) + w*w).sqrt()
    null   = gn.Boolean(length.less_than(zero))

    length.to_output("Length")
    null.to_output("Null")

```
