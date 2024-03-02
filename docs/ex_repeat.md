# Repeat

> Example of repeat zone

**Repeat** zone is created with `tree.repeat` method following the same principles as a **simulation** zone. See [Simulation zone](ex_simulation.md) for details.

## Sample code

In this demo:
- Create a material using an attribute created by the geometry node modifier
- Create a repeat loop creating one line per loop

![Result](images/ex_repeat.png)

``` python
from geonodes import GeoNodes, Shader

# ----- Material for the lines
# The Geometry Nodes modifier with set a color attribute named "col"

with Shader("Line Material") as tree:
    col = tree.Attribute("col").color
    tree.output_surface = tree.PrincipledBSDF(base_color=col).bsdf

# ----- Create random lines

with GeoNodes("Demo Repeat") as tree:
    
    # Input parameter
    
    count = tree.int_input("Count", 1, min_value=1, max_value=1000)
    
    # Create one random line per loop
    
    with tree.repeat(iterations=count, geometry=None, seed=0) as repeat:
        
        # Build a random line
        
        curve = tree.CurveLine(end=(0, 0, 10)).curve.resample_curve(count=30)
        curve.set_position(offset=tree.random_vector(-.2, .2, seed=repeat.seed+1))
        
        tree.RandomValue.print_doc()
        print(tree.integer(1))
        
        
        curve.transform_geometry(rotation=tree.random_vector(-1, 1, ID=tree.integer(1), seed=repeat.seed+2))
        
        repeat.geometry = repeat.geometry + curve
        
        repeat.seed += 2
        
    # A different color per line
    lines = repeat.geometry
    lines.CURVE.store_named_float_color("col", tree.random_vector(.2, .8, seed=1000))
    
    # To mes
        
    mesh = lines.curve_to_mesh(profile_curve=tree.curve_circle(radius=.02))
        
    tree.og = mesh.set_material("Line Material")
```
        
    
