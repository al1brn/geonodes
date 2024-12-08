# G

``` python
G(/, *args, **kwargs)
```

Group funcitonal call

This weird class is empty but two static methods aimed at building dynamic static functions.

For each built Tree, a function is created in class G (for Groups).
To call the created group, the function syntax can be used rather than instantiating the Group Node.

Let's suppose we have the following group.

``` python
with GeoNodes("Translate Geometry"):
    v = Vector(0, "Translation")
    factor = Float.Factor(1, "Factor")

    Geometry().transform(translation=v*factor).out()
```

The created group can be called in another tree following the two possible syntax:

```
with GeoNodes("Calling a Group"):

    geo = Geometry()

    # ----- Instantiate a node Group by its name

    geo = Group("Translate Geometry", geometry=geo).geometry

    # Or with parameters

    geo = Group("Translate Geometry", geometry=geo, translation=(1, 0, 0), factor=.5).geometry


    # ----- Function call

    geo = G.translate_geometry(geo)

    # Or with parameters
    # be sure of the sockets order if you don't use keyword argument syntax

    geo = G.translate_geometry(geo, (1, 0, 0), .5)
```

#### Arguments:
- **args**
- **kwargs**