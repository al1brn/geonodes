# Modifiers and Groups

## Creating a Group

When creating a new tree, the argument **is_group** is used to specify to create a **group of nodes** rather
than a **modifier**:

``` python
with GeoNodes("A Function", is_group=True):

    a = Float(name="Value 1")
    b = Float(name="Value 2")

    (a + b).out("Sum")
```

This creates the following group:

<img src="doc/images/group_sample.png" width="300" class="center">

## Calling a Group

Calling a group is made by instantiating a **Group** class.
The first parameter of the **Group** instantiation is the name of the _Group_ to call.
The sockets to plug th the input sockets of the group can be passed in two ways:
- as a dict
- as keyword arguments using their _snake_case_ name

The output sockets of the group are read as properties of the **Group** instance,
using their _snake_case_ name.


``` python
from geonodes import *

with GeoNodes("A Function", is_group=True):
    (Float(0, "Value 1") + Float(0, "Value 2")).out("Sum")

with GeoNodes("A Function is called"):

    a, b = 1, 2

    # ---------------------------------------------------------------------------
    # Standard method
    # ---------------------------------------------------------------------------

    # dict syntax

    val1 = Group("A Function", {'Value 1': a, 'Value 2': b}).sum

    # snake_case syntax

    val2 = Group("A Function", value_1=a, value_2=b).sum

    # ---------------------------------------------------------------------------
    # Alternative method
    # ---------------------------------------------------------------------------
    
    # For big projects, one can prefer the python syntax
    # Class G makes it possible

    val3 = G().a_function(val1, val2)
    
    geo = Geometry()
    geo.offset = (val1, val2, val3)
    geo.out()        
```

