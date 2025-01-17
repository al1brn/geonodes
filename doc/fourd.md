# fourd

[Source Code](../demos/fourd.py)

The 4D Engine provides modifiers to create 4D geometries, transform them and project
them into 3D space.

> [!NOTE]
> The 4D light is still work in progress

> [!IMPORTANT]
> - The engine needs an object named "4D Parameters" with the modifier "4D Parameters":
>   this is where you control the 4D paramaters.
> - The last modifier must be "4D Projection" to project the 4D geometry into a 3D space.

For instance, to visualize an Hypersphere, you have to stack two modifiers:
- 4D Hyper Sphere
- 4D Projection

### Creating 4D Geometry

You can use modifiers creating 4D geometry:
- 4D Hyper Sphere
- 4D Hyper Cube
- 4D Hyper Cone
- 4D 5 Cell Polytope
- 4D Torus
- 4-Curve Circle
- 4-Curve Line

You can also create your own geometry with modifiers and groups
- 4D Plunge into 4D
- 4-Math xxx
- 4-Vector xxx
- 4-Matrix xxx

You can then transform your geometry with:
- 4D Rotation
- 4D Translation
- 4D Scale
- 4D Roll Axes
- 4D Swap Axes



> [!NOTE]
> Modifiers:
> - 4D Parameters
> - 4D Projection
> - 4D Hyper Sphere
> - 4D Hyper Cube
> - 4D Hyper Cone
> - 4D 5 Cell Polytope
> - 4D Torus
> - 4-Curve Circle
> - 4-Curve Line
> - 4D Plunge into 4D
> - 4D Rotation
> - 4D Translation
> - 4D Scale
> - 4D Roll Axes
> - 4D Swap Axes
> - 4-Math xxx (Group)
> - 4-Vector xxx (Group)
> - 4-Matrix xxx (Group)


``` python
from geonodes.demos import fourd

fourd.demo()
```