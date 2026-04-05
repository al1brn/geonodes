# Math

Maths are performed as in pure python. Use `gnmath` module rather than standard `math`

``` python
    # Let's initialize two geonodes Float
    x = Float(1)
    y = Float(2)

    distance = gnmath.sqrt(x**2 + y**2)
```

## Operators

Python operators can be used to operate on data, as shown below:

``` python
# Float operators
a = Float(10)
c = a*pi # Math node, operation 'MULTIPLY'
c += 1 # Math node, operation 'ADD'
ok = a <= c # Compare node, operation 'LESS_EQUAL'

# Integer operators
a = Integer(10)
c = a*42 # Operation between two Integers : Integer Math node is used
c += 1 # Integer Math node, operation 'ADD'
d = -c # Integer Math node, operation 'NEGATE'

# Bitwise operators
a = Integer(1) << 3
a |= Integer(7) & 1

# Vector operators
u = Vector((1, 2, 3))
v = u + (7, 8, 9) # Vector Math node, operation 'ADD'
w = u*3 # Vector Math node, operation 'SCALE'

# Boolean operators
b = Boolean(True)
c = b | False # Boolean Math node, operation 'OR'

# String operators
s = String("A string")
s += ": this is something added. "
s += String(" ") * ("This", "is", "a", String("sentence."))

# Join Geometry
geo = Geometry() # Input geometry
geo += Mesh.Cube(), Curve.Spiral() # Join with two other geometries

# Mesh boolean
cube = Mesh.Cube()
ico  = Mesh.IcoSphere(radius=.8)

mesh = cube - ico # Difference
mesh = cube * ico # Union
mesh = cube / ico # Intersect
```

!!! warning

    Python boolean operators `or`, `and` and `not` **can not** be used with **Boolean** class, use their binary
    equivalent instead : |, & and -.

## 'gnmath' module

**gnmath** provides the mathematical functions, basically the operations performed by **Math** nodes
(_Math_, _Integer Math_, _Vector Math_, _Boolean Math_,...)

Math functions are named after their standard name in python **math** module.

> **Vector** functions having the same name as their **Float** equivalent are prefixed with the letter *v*
> **Integer** functions having the same name as their **Float** equivalent are prefixed with the letter *i*
> All bitwise **Integer** operations are prefixed with *bw_*

``` python
    with GeoNodes("gnmath"):
        a = Float(1)
        b = gnmath.sin(a)
        
        # Add between two Floats
        c = gnmath.add(b, 7.5)

        i = Integer(123)
        # Greater Common Divisor exists only for Integers
        j = gnmath.gcd(i, 17) 
        
        # Add exists also for Floats
        k = gnmath.iadd(j, 7)
        
        u = Vector((1, 2, 3))
        # Cross product exists only for vectors
        v = gnmath.cross(u, (7, 8, 9))
        # Add axists also for Floats
        w = gnmath.vadd(v, (5, 6,7))

        # Bitwise functions
        j = gnmath.bw_and(i, 7)        
```

> Similarly **Boolean** functions _and_, _or_ and _not_ are prefixed by the letter *b*

``` python
    a = Boolean(True)
    b = gnmath.xor(a, False)
    c = gnmath.band(b, False)
    d = gnmath.band(b, False)
```

> Math functions are also available as methods and some of them as operators.

The following example gives the same result as the two previous ones:

``` python
    a = Float(1)
    b = a.sin()
    c = b + 7.5

    i = Integer(123)
    j = i.gcd(17) 
    k = j + 7
    
    u = Vector((1, 2, 3))
    v = u.cross((7, 8, 9))
    w = v + (5, 6,7)
    
    
    a = Boolean(True)
    b = a.xor(False)
    # and operator is implemented with & 
    c = b & False
    # or operator is implemented with |
    d = b | False
```

