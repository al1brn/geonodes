from geonodes import *

def demo():

    with GeoNodes("Gizmo demo"):

        geo = Geometry()

        with Layout("Cube size"):

            x, y, z = Float(1, "X"), Float(1, "Y"), Float(1, "Z")

            scale = Float(1, "Scale")

            size = Vector((x, y, z))*scale

        with Layout("Size gizmos"):

            val1, val2, val3 = Float(1), Float(2), Float(3)
            gizmo = Gizmo.linear(val1, val1, val3)

            xg = x.linear_gizmo(position=(x/2*scale, 0, 0), direction=(1, 0, 0), color_id='X')
            x.pin_gizmo = True

            yg = y.linear_gizmo(position=(0, y/2*scale, 0), direction=(0, 1, 0), color_id='Y')
            y.pin_gizmo = True

            zg = z.linear_gizmo(position=(0, 0, z/2*scale), direction=(0, 0, 1), color_id='Z')
            z.pin_gizmo = True

            sg = scale.linear_gizmo(position=size/2, direction=(1, 1, 1))
            scale.pin_gizmo=True

        with Layout("Cube"):
            cube = Mesh.Cube(size=size) + (xg, yg, zg, sg)

        with Layout("Transformation Gizmo"):

            matrix = Matrix(None, name="Transformation")
            matrix = Matrix() #None, name="Transformation")
            matrix.transform_gizmo(use_translation_x=False, use_translation_y=False, use_translation_z=False, use_scale_x=False, use_scale_y=False, use_scale_z=False)
            matrix.pin_gizmo = True

            cube.transform(transform=matrix)

        cube.out()
