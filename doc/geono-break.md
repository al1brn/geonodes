# Break

``` python
Break(/, *args, **kwargs)
```

Exception used to exit a With context block.

``` python
with GeoNodes("Break Demo"):
    Geometry().out()
    raise Break()

    # Not executed
    Float(10).out()
```

#### Arguments:
- **args**
- **kwargs**

### Inherited