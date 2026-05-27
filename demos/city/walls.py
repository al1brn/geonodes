# WORK IN PROGRESS

from geonodes import *
from .constants import *

# ====================================================================================================
# Preview wall
# ====================================================================================================

def demo():

    def wall_dims():

        return (
            Float.Distance(2.0, "Length", MIN_HEIGHT),
            Float.Distance(2.3, "Height", MIN_HEIGHT),
            Float.Distance(0.5, "Depth", MIN_SIZE),
            )

    # ----------------------------------------------------------------------------------------------------
    # Preview
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("WALL Preview", is_group=IS_GROUP):

        length, height, depth = wall_dims()

        #preview, lod, seed = render_input()

        cube = Mesh.Cube(size=(depth, length, height))
        cube.position += (depth/2, length/2, height/2)

        cube.out()

    # ----------------------------------------------------------------------------------------------------
    # Wall Corner Preview
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("WALL Corner Preview", is_group=IS_GROUP):

        height = Float.Distance(2.4, "Height", MIN_HEIGHT)
        width  = Float.Distance(0.3, "Width", MIN_SIZE)
        depth  = Float.Distance(0.5, "Depth", MIN_SIZE)

        cube = Mesh.Cube((width, width, height))

        cube.out()

    # ----------------------------------------------------------------------------------------------------
    # Stone wall
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("WALL Stones", is_group=IS_GROUP):

        length, height, depth = wall_dims()

        preview, lod, seed = render_input()

        wall_preview = Mesh(G("WALL").preview(length, height, depth))
        wall = Mesh(wall_preview).subdivide(7)

        tex = Texture.Voronoi(
            scale       = 3.0,
            detail      = 0.3,
            roughness   = 0.4,
            lacunarity  = 1.6,
            )
        ofs = tex.map_range(from_min=0.4, from_max=1.0, to_min=0, to_max=-0.05)
        wall.offset = (ofs, 0, 0)


        wall.switch(preview, wall_preview)

        wall.out()

    # ----------------------------------------------------------------------------------------------------
    # Corner
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("WALL Corner", is_group=IS_GROUP):

        wall = G("WALL").corner_preview().link_inputs()
        wall.out()

    # ----------------------------------------------------------------------------------------------------
    # Wall Door
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("WALL Door", is_group=IS_GROUP):

        pos    = Vector.Translation(0, "Position")
        width  = Float.Distance(0.8, "Width", 0.3)
        height = Float.Distance(1.80, "Height", .7)
        depth  = Float.Distance(0.5, "Depth", MIN_SIZE)

        j_depth = depth + .05
        left_jamb = Mesh.Cube(size=(depth, j_depth, height)).transform(translation=(-width/2 - depth/2, 0, height/2))
        right_jamb = Mesh.Cube(size=(depth, j_depth, height)).transform(translation=(width/2 + depth/2, 0, height/2))
        lintel = Mesh.Cube(size=(width + 2*depth, j_depth, depth/2)).transform(translation=(0, 0, height + depth/4))

        menel = left_jamb + right_jamb + lintel
        menel.out()

    # ----------------------------------------------------------------------------------------------------
    # Wall Door
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("WALL Door", is_group=IS_GROUP):

        width  = Float.Distance(0.8, "Width", 0.3)
        height = Float.Distance(1.80, "Height", .7)
        depth  = Float.Distance(0.5, "Depth", MIN_SIZE)

        j_depth = depth + .05
        left_jamb = Mesh.Cube(size=(depth, j_depth, height)).transform(translation=(-width/2 - depth/2, 0, height/2))
        right_jamb = Mesh.Cube(size=(depth, j_depth, height)).transform(translation=(width/2 + depth/2, 0, height/2))
        lintel = Mesh.Cube(size=(width + 2*depth, j_depth, depth/2)).transform(translation=(0, 0, height + depth/4))

        menel = left_jamb + right_jamb + lintel
        menel.out()

    # ----------------------------------------------------------------------------------------------------
    # Wall Window
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("WALL Window", is_group=IS_GROUP):

        width  = Float.Distance(1.2, "Width", 0.3)
        height = Float.Distance(0.9, "Height", .4)
        base   = Float.Distance(.9, "Base", 0)
        depth  = Float.Distance(0.5, "Depth", MIN_SIZE)

        j_depth = depth + .05
        left_jamb = Mesh.Cube(size=(depth, j_depth, height)).transform(translation=(-width/2 - depth/2, 0, height/2))
        right_jamb = Mesh.Cube(size=(depth, j_depth, height)).transform(translation=(width/2 + depth/2, 0, height/2))
        lintel = Mesh.Cube(size=(width + 2*depth, j_depth, depth/2)).transform(translation=(0, 0, height + depth/4))

        menel = left_jamb + right_jamb + lintel
        menel.out()









        
        

        








