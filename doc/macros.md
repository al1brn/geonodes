# macros

Created on 2024/07/29

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : macros
---------------
- Some macros

classes
-------

functions
---------
- Solidify

updates
-------
- creation : 2024/07/29

## Content

- [double_integrals](macros.md#double_integrals)
- [impulsion](macros.md#impulsion)
- [integrals](macros.md#integrals)
- [solidify](macros.md#solidify)

## Functions



----------
### double_integrals()

> function

``` python
double_integrals(x0=0, x1=1, y0=0, y1=1, count_x=100, count_y=100, **values)
```

Compute double integrals of a function on the intervals [x0, x1], [y0, y1]

Plural version : several integrals are computed by the same macro
The values must be computed using:
- variable 1 : nd.position.x
- variable 2 : nd.position.y

For instance:
``` python
count = 100

x = nd.position.x
y = nd.position.y

# Integral of x*y
xy = nd.position.x * nd.position.y

# Integral of x*sine in interval [0, 10],[0, pi]
sin = (nd.position.x*10)*gnmath.sin(nd.position.y*pi)

integrals = macros.double_integrals(x0=0, x1=10, y0=-pi/2, y1=pi/2, count=count, xy=x*y, sin=x*gnmath.cos(y))

mesh = Mesh()
mesh.points.store("xy", integrals["xy"])
mesh.points.store("sin", integrals["sin"])

mesh.out()
```

#### Arguments:
- **x0** (_Float_ = 0) : Left bound of the x integration interval
- **x1** (_Float_ = 1) : Right bound of the x integration interval
- **y0** (_Float_ = 0) : Left bound of the y integration interval
- **y1** (_Float_ = 1) : Right bound of the y integration interval
- **count_x** (_Integer_ = 100) : number of intervals on x
- **count_y** (_Integer_ = 100) : number of intervals on y
- **values** (_keyword arguments_) : named argument



#### Returns:
- **dict** : the integrals

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [macros](macros.md#macros) :black_small_square: [Content](macros.md#content) :black_small_square: [Functions](macros.md#functions)</sub>

----------
### impulsion()

> function

``` python
impulsion(value, from_min=0, from_max=1, amplitude=1.0, increase=0.5, decrease=0.5, c=0, t=0, dist_falloff=0, time_falloff=0, smooth=True)
```

Create an impulse varying with time and distance.

The function returns a value in the interval [0, amplitude]
The increase interval is [from_min, from_min + increase]
The decrease interval is [to_max - decreare, to_max]

Motion is taken into account by moving the intervals with c*t
Falloff can take place with time and/or time. The fall is exp(-falloff * x^2))

#### Arguments:
- **value** (_Float_) : the input value
- **from_min** (_Float_ = 0) : value where the impulse starts
- **from_max** (_Float_ = 1) : value where the impulse ends
- **amplitude** (_Float_ = 1.0) : max returned value
- **increase** (_Float_ = 0.5) : increase length
- **decrease** (_Float_ = 0.5) : ecrease length
- **c** (_Float_ = 0) : impulse celerity
- **t** (_Float_ = 0) : time
- **dist_falloff** (_Float_ = 0) : distance falloff
- **time_falloff** (_Float_ = 0) : time falloff
- **smooth** (_Boolean_ = True) : use map_range smooth option

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [macros](macros.md#macros) :black_small_square: [Content](macros.md#content) :black_small_square: [Functions](macros.md#functions)</sub>

----------
### integrals()

> function

``` python
integrals(x0=0, x1=1, count=100, **values)
```

Compute integrals of a function on the interval [x0, x1]

Plural version : several integrals are computed by the same macro
Values are computed using nd.position.x

For instance:
``` python
count = 100

# Integral of x in interval [0, 1]
x = nd.position.x

# Integral of sine in interval [0, pi]
sin = gnmath.sin(x)

integrals = macros.integrals(0, pi, count, x=x, sin=sin)

mesh = Mesh()
mesh.points.store("x", integrals["x"])
mesh.points.store("sin", integrals["sin"])

mesh.out()
```

#### Arguments:
- **x0** (_Float_ = 0) : Left bound of the integration interval
- **x1** (_Float_ = 1) : Right bound of the integration interval
- **count** (_Integer_ = 100) : number of intervals
- **values** (_keyword arguments_) : named argument



#### Returns:
- **dict** : the integrals

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [macros](macros.md#macros) :black_small_square: [Content](macros.md#content) :black_small_square: [Functions](macros.md#functions)</sub>

----------
### solidify()

> function

``` python
solidify(mesh, thickness=0.01, individual=False, merge_distance=0.001)
```

Solidify a mesh

#### Arguments:
- **mesh**
- **thickness** (_Float_ = 0.01) : thickness
- **individual** (_Boolean_ = False) : extrude individual faces
- **merge_distance** (_Float_ = 0.001) : distance to use to merge intial faces and the extruded mesh



#### Returns:
- **Mesh** : the solidified mesh

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [macros](macros.md#macros) :black_small_square: [Content](macros.md#content) :black_small_square: [Functions](macros.md#functions)</sub>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [macros](macros.md#macros) :black_small_square: [Content](macros.md#content) :black_small_square: [macros](macros.md#macros)</sub>