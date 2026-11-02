"""Blender 5.3 feature checks, with one modifier per change.

Build a check from Blender with:

    from geonodes.generation import test_53
    test_53.combine_list.rebuild()

Build all checks with test_53.build(rebuild=True).

The length outputs should be 0, 1 and 3 for each tested type.
"""

from geonodes import (
    Boolean, Cloud, Color, Float, Geometry, Integer, Layout, Matrix,
    Rotation, String, Vector, Package, nd,
)


test_53 = Package("Test 5.3")


def build(rebuild=False):
    """Build all feature checks registered in the package."""
    test_53.build(rebuild=rebuild)


@test_53.geo_modifier("Test 5.3 - Combine List")
def combine_list():
    """Combine zero, one and three values into lists of different types."""

    Geometry().out()

    with Layout("Float"):
        empty = Float.CombineList()
        single = Float.CombineList(1)
        multiple = Float.CombineList(1, 2, 3)
        empty.list_length().out("Float 0")
        single.list_length().out("Float 1")
        multiple.list_length().out("Float 3")

    with Layout("Integer"):
        empty = Integer.CombineList()
        single = Integer.CombineList(1)
        multiple = Integer.CombineList(1, 2, 3)
        empty.list_length().out("Integer 0")
        single.list_length().out("Integer 1")
        multiple.list_length().out("Integer 3")

    with Layout("Boolean"):
        empty = Boolean.CombineList()
        single = Boolean.CombineList(True)
        multiple = Boolean.CombineList(True, False, True)
        empty.list_length().out("Boolean 0")
        single.list_length().out("Boolean 1")
        multiple.list_length().out("Boolean 3")

    with Layout("Vector"):
        empty = Vector.CombineList()
        single = Vector.CombineList((1, 0, 0))
        multiple = Vector.CombineList((1, 0, 0), (0, 1, 0), (0, 0, 1))
        empty.list_length().out("Vector 0")
        single.list_length().out("Vector 1")
        multiple.list_length().out("Vector 3")

    with Layout("Color"):
        red = Color((1, 0, 0, 1))
        green = Color((0, 1, 0, 1))
        blue = Color((0, 0, 1, 1))
        empty = Color.CombineList()
        single = Color.CombineList(red)
        multiple = Color.CombineList(red, green, blue)
        empty.list_length().out("Color 0")
        single.list_length().out("Color 1")
        multiple.list_length().out("Color 3")

    with Layout("Rotation"):
        a = Rotation((0, 0, 0))
        b = Rotation((0, 0, 1))
        c = Rotation((0, 1, 0))
        empty = Rotation.CombineList()
        single = Rotation.CombineList(a)
        multiple = Rotation.CombineList(a, b, c)
        empty.list_length().out("Rotation 0")
        single.list_length().out("Rotation 1")
        multiple.list_length().out("Rotation 3")

    with Layout("Matrix"):
        matrix = Matrix(name="Matrix")
        empty = Matrix.CombineList()
        single = Matrix.CombineList(matrix)
        multiple = Matrix.CombineList(matrix, matrix, matrix)
        empty.list_length().out("Matrix 0")
        single.list_length().out("Matrix 1")
        multiple.list_length().out("Matrix 3")

    with Layout("String"):
        empty = String.CombineList()
        single = String.CombineList("A")
        multiple = String.CombineList("A", "B", "C")
        empty.list_length().out("String 0")
        single.list_length().out("String 1")
        multiple.list_length().out("String 3")


@test_53.geo_modifier("Test 5.3 - Rasterize Points")
def rasterize_points():
    """Rasterize named float/vector fields and read the resulting grids."""

    points = Cloud.Points(count=5, position=(nd.index * 0.3, 0, 0))

    with Layout("Named sockets dictionary"):
        grids = points.rasterize_points(
            {"Density": Float(1)},
            voxel_size=0.1,
        )
        grids.density.grid_to_points().out("Dictionary Density")

    with Layout("Named sockets keywords"):
        grids = points.rasterize_points(
            voxel_size=0.1,
            density=Float(1),
            coordinates=nd.position,
        )
        grids.density.grid_to_points().out("Keyword Density")
        grids.coordinates.grid_to_points().out("Keyword Coordinates")
