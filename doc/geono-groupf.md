# GroupF

``` python
GroupF(prefix=None)
```

Utility class exposing Groups as python functions.

This class provides an alternative to 'Group' to call groups. The snake case version of the group name is
used as method name of an instance of GroupF: ``` Group("Group Name") ``` is replaced by
``` GroupF().group_name() ```.

If the group is uses a prefix, the prefix is passed as init argument in GroupF : ``` GroupF(prefix).group_name() ```.

The arguments can be passed either using the socket names in a dict or as kwargs arguments.

``` python
# Prefix used to identifiy utility groups
UTIL = "UTIL"

# Create a group utility
with GeoNodes("Subtract two values", is_group=True):

    a = Float(0, "a")
    b = Float(0, "b")

    (a + b).out("Diff")


# Create a prefixed group utility
with GeoNodes("Add two values", prefix=UTIL, is_group=True):

    a = Float(0, "a")
    b = Float(0, "b")

    (a + b).out("Sum")

with GeoNodes("Gourp function call"):

    Geometry().out()

    a = Float(10, "a")
    b = Float(20, "b")

    # Call the the utility
    c = GroupF().subtract_two_values({'a': a}, b=b)._out

    # Call the the prefixed utility
    d = GroupF(UTIL).add_two_values(a=a, b=b)._out

    c.out("c")
    d.out("d")
```

#### Arguments:
- **prefix** ( = None)