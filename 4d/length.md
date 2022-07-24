# Length (maths)

> Compute the length of a 4-vector.

## Sockets

### Input sockets

- **xyz** (Vector): vector part
- **w** (Float): float part

### Output sockets

- **Length** (Float): vector norm
- **Null** (Boolean): True of norm is null (less than 0.001)

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
