# Normalize (Maths)

> Return the normalized 4-vector of a 4-vector.

## Sockets

### Input sockets

- **xyz** (Vector): vector part
- **w** (Float): float part

### Output sockets

- **xyz** (Vector): vector part
- **w** (Float): float part
- **Null** (Boolean): True if the input vector is null


## Code

``` python

with gn.Tree(maths.name("Normalize"), group=True) as tree:

    v = gn.Vector.Input(0, "xyz")
    w = gn.Float.Input( 1, "w")

    n = maths.length(xyz=v, w=w).length

    null = gn.Boolean(n.less_than(zero))

    rv = (v/n).switch(null, gn.Vector(0))
    rw = (w/n).switch(null, gn.Float(0))

    rv.to_output("xyz")
    rw.to_output("w")
    null.to_output("Null")


```


