from ..geonodes import *

def demo():

    with GeoNodes("Frise"):

        with Layout("Frise"):

            count       = Integer(10, "Patterns Count", 1)
            use_circle  = Boolean(True, "Circular Shape")
            rot_handles = Boolean(True, "Rotate handles")

            resol = 2

            frise = Curve.Line(0, (count, 0, 0)).resample(count*resol + 1)
            frise.splines.type = 'BEZIER'
            frise.splines.resolution = 32

            frise.points[(nd.index % resol).equal(1)].offset = (-.6, 0, .5)

            frise.points[(nd.index % resol).equal(0)].set_handle_type(left=True, right=True, handle_type='ALIGN')
            frise.points[(nd.index % resol).equal(1)].set_handle_type(left=True, right=True, handle_type='FREE')

            frise.points[(nd.index % resol).equal(0)].left_handle_offset = (-.1, 0, 0)
            frise.points[(nd.index % resol).equal(0)].right_handle_offset = (.3, 0, 0)

            frise.points[(nd.index % resol).equal(1)].left_handle_offset = (0.5, 0, .5)
            frise.points[(nd.index % resol).equal(1)].right_handle_offset = (.2, 0, .9)

            radius = count/tau
            theta = nd.position.x/radius

            frise.points.store("Left",  frise.points.left_handle_position  - nd.position)
            frise.points.store("Right", frise.points.right_handle_position - nd.position)
            frise.points.store("Theta", theta)

            straight = Curve(frise)

        with Layout("Circle"):

            frise.points.position = radius*gnmath.cos(theta), radius*gnmath.sin(theta), nd.position.z

            unrotated = Curve(frise)

            theta = Float.Named("Theta") + pi/2

            p = Vector.Named("Left")
            frise.points.left_handle_position = nd.position + (p.x*gnmath.cos(theta), p.x*gnmath.sin(theta), p.z)

            p = Vector.Named("Right")
            frise.points.right_handle_position = nd.position + (p.x*gnmath.cos(theta), p.x*gnmath.sin(theta), p.z)

            frise = unrotated.switch(rot_handles, frise)

        straight.switch(use_circle, frise).out()

    with GeoNodes("Abs"):

        count = Integer(10, "Resolution")
        x_loc = 0


        with Layout("A"):
            A = Curve.Line(0, (.8, 0, 0)).resample(3)

            A.points[1].position = (.4, 0, 1)

            A += Curve.Line((.2, 0, .5), (.6, 0, .5))


        A.points.offset = (x_loc, 0, 0)
        x_loc += 1

        alphabet = A

        with Layout("B"):

            B = Curve.Line(0, (1, 0, 0)).resample(4)
            B.splines.type = 'BEZIER'

            B.points[1].position = (0, 0, 1)
            B.points[2].position = (0, 0, .6)
            B.points[3].position = (0, 0, 0)

            B.points[1].right_handle_position = (.5, 0, 1)

            B.points[2].left_handle_position = (.5, 0, .6)
            B.points[2].right_handle_position = (.7, 0, .6)


            B.points[3].left_handle_position = (.7, 0, 0)

        B.points.offset = (x_loc, 0, 0)
        x_loc += 1

        alphabet += B

        with Layout("S"):
            S = Curve.Line(end = (0, 0, 1)).resample(3)
            S.splines.type = 'BEZIER'
            #S.splines.resolution = 30

            delta = .4

            S.points[0].offset = (-.2, 0, .1)
            S.points[2].offset = (.2, 0, -.1)


            S.points[0].right_handle_position = (.3, 0, -.3)
            S.points[2].left_handle_position  = (-.3, 0, 1.3)

            S.points[1].left_handle_position = (.6, 0, .5)
            S.points[1].right_handle_position = S.points[1].left_handle_position * (-1, 1, 1)


        S.points.offset = (x_loc, 0, 0)
        x_loc += 1

        alphabet += S
        alphabet.splines.resolution = 24


        alphabet.out()
